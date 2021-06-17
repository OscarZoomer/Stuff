# Zoom-Code-Scraper
Finds Zoom Codes for you.

## Information
This tool specifically searches for Zoom Meeting Codes/URLs posted recently by users on Twitter. It filters possible results.

I got the idea from verdict, he made a similar tool a few months ago but using TweetDeck. Mine uses Twitter's official API.<br/>
His Discord username: verdict#0200

## Preview
![](https://i.imgur.com/8mfXao4.png)<br/>
![](https://i.imgur.com/hRONic6.png)

## Usage
- Python 3.8 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.
- If you do not already have the **requests** library installed, run setup.py — make sure PIP is added to PATH.
1. Launch any HTTP debugger — built-in browser debuggers work. In this example, I am going to use Chrome's built-in debugger.
2. Head over to the [Network tab](https://i.imgur.com/UAzJL0R.png).
3. Visit [this URL](https://twitter.com/search?q=zoom%20code&src=typed_query&f=live) — in the same tab.
4. Click on [this request](https://i.imgur.com/Pxc4gGh.png) for further details.
5. Under the "Request Headers" tab, copy the [authorization header's value](https://i.imgur.com/38aPHHV.png). Replace **BEARER TOKEN** with **the authorization header** in Config.json.
6. Below the authorization header, copy the [cookie's value](https://i.imgur.com/OphifTK.png). Replace **COOKIE** with **the cookie header** in Config.json. Take notice how the cookie includes 2 double quotation marks. Put a backslash before personalization_id's double quotation marks like this: ```personalization_id=\"...\";```
7. Save Config.json, obviously.
8. Run main.py!
