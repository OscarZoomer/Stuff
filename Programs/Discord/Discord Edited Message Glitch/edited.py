import sys
import clipboard

def encode_txt(m, pos):
    res = " ".join(m[:pos] + [b'\xe2\x80\xab'.decode()] + m[pos:]) + b" \xe2\x80\xab".decode()
    return res

if len(sys.argv) <= 1:
    print("\nYou must enter some text to proceed the 'edited' symbol!\nTry again, but with text next time\nEnter any key to exit ... ", end = "")
else:
    res = encode_txt(sys.argv[1:], 0)
    try:
        clipboard.copy(res)
        print("\nSuccessfully Copied Text to Clipboard!\nEnter any key to exit ... ", end = "")
    except:
        print("\nSomething's gone wrong :(\nI was unable to copy the text to your Clipboard\nEnter any key to exit ... ", end = "")

input()
print()