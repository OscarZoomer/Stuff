#include <array>

namespace random {
	constexpr auto m_time = __TIME__;
	constexpr auto m_seed = static_cast<unsigned>(m_time[7]) + static_cast<unsigned>(m_time[6]) * 10 + static_cast<unsigned>(m_time[4]) * 60 + static_cast<unsigned>(m_time[3]) * 600 + static_cast<unsigned>(m_time[1]) * 3600 + static_cast<unsigned>(m_time[0]) * 36000;

	template <int A>
	struct gen_t {
	private:
		static constexpr unsigned m_a = 16807;
		static constexpr unsigned m_b = 2147483647;

		static constexpr unsigned m_s = gen_t<A - 1>::m_value;
		static constexpr unsigned m_lo = m_a * (m_s & 0xFFFFu);
		static constexpr unsigned m_hi = m_a * (m_s >> 16u);
		static constexpr unsigned m_lo2 = m_lo + ((m_hi & 0x7FFFu) << 16u);
		static constexpr unsigned m_hi2 = m_hi >> 15u;
		static constexpr unsigned m_lo3 = m_lo2 + m_hi;
	public:
		static constexpr unsigned m_max = m_b;
		static constexpr unsigned m_value = m_lo3 > m_b ? m_lo3 - m_b : m_lo3;
	};

	template <>
	struct gen_t<0> {
		static constexpr unsigned m_value = m_seed;
	};

	template <int A, int B>
	struct int_t {
		static constexpr auto m_value = gen_t<A + 1>::m_value % B;
	};

	template <int A>
	struct char_t {
		static const char m_value = static_cast<char>(1 + int_t<A, 0x7F - 1>::m_value);
	};
}

template <int A, char B>
struct xor_str_t {
private:
	static constexpr char enc(const char c) { return c ^ B; }
public:
	template <int... C>
	constexpr __forceinline xor_str_t(const char* str, std::index_sequence<C...>) { encrypted = { enc(str[C])... }; }

	__forceinline std::string dec() {
		std::string dec;

		dec.resize(A);

		for (int i = 0; i < A; i++) {
			dec.at(i) = enc(encrypted.at(i));
		}

		return dec;
	}

	__forceinline std::string ot(bool decrypt = true) {
		std::string dec;

		dec.resize(A);

		for (int i = 0; i < A; i++) {
			dec.at(i) = decrypt ? enc(encrypted.at(i)) : encrypted.at(i);

			encrypted.at(i) = '\0';
		}

		return dec;
	}

	std::array<char, A> encrypted = {};
};

#define _(s) xor_str_t<sizeof(s), random::char_t<__COUNTER__>::m_value>(s, std::make_index_sequence<sizeof(s)>()).dec().c_str()
#define _ot(s) xor_str_t<sizeof(s), random::char_t<__COUNTER__>::m_value>(s, std::make_index_sequence<sizeof(s)>()).ot().c_str()
#define __(s) []() -> std::pair<std::string, char> { \
	constexpr auto key = random::char_t<__COUNTER__>::m_value; \
	return std::make_pair(xor_str_t<sizeof(s), key>(s, std::make_index_sequence<sizeof(s)>()).ot(false), key); \
}()
#define _rt(n, s) auto (n) = reinterpret_cast<char*>(alloca(((s).first.size() + 1) * sizeof(char))); \
	for (int i = 0; i < (s).first.size(); i++) \
        (n)[i] = (s).first[i] ^ (s).second; \
    (n)[(s).first.size()] = '\0'