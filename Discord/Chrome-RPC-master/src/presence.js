module.exports = function pre (client, body) {




    if (body.action === "set") {



        if (body.details === "www.pornhub.com") {

            client.setActivity({





                state: body.state,
                details: body.details,
                startTimestamp: new Date(),
                largeImageKey: "pornhub-symbol",
                largeImageText: body.largeText || body.title,
                smallImageKey: 'chrome',
                smallImageText: body.smallText,
                instance: true

            }).then(console.log, console.error);
        }


        else


            if (body.details === "www.youtube.com") {


                client.setActivity({

                    state: body.state,
                    details: body.details,
                    startTimestamp: new Date(),
                    largeImageKey: "ytdark",
                    largeImageText: body.largeText || body.title,
                    smallImageKey: 'chrome',
                    smallImageText: body.smallText,
                    instance: true

                }).then(console.log, console.error);

            }

            else
            
            if (body.details === "github.com" ) {

                client.setActivity({

                    state: body.state,
                    details: body.details,
                    startTimestamp: new Date(),
                    largeImageKey: "github",
                    largeImageText: body.largeText || body.title,
                    smallImageKey: 'chrome',
                    smallImageText: body.smallText.includes("search") && body.smallText.length >= 128 ? body.title : body.smallText,
                    instance: true

                }).then(console.log, console.error);

            } else{
                client.setActivity({

                    state: body.state,
                    details: body.details,
                    startTimestamp: new Date(),
                    largeImageKey: "chrome",
                    largeImageText: body.largeText || body.title,
                    smallImageKey: 'chromeium',
                    smallImageText: body.smallText.includes("search") && body.smallText.length >= 128 ? body.title : body.smallText,
                    instance: true

                }).then(console.log, console.error);
            }




    } else if (body.action === "clear") {
        client.clearActivity();
    }

}