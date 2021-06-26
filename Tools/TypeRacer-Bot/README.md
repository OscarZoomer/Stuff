# TypeRacer-Bot
Automatically types for you on typeracer.com — without Selenium.

## Information
This tool was developed to demonstrate how straightforward it is to automate/cheat on a service like TypeRacer. This uses image recognition and not Selenium unlike my old TypeRacer script. Usage of this tool increases chances to win; especially by selecting the "Pro" or "Hacker" speed. It is 100% accurate and does not mistype. Please refrain from using this bot as it was developed for educational purposes only. Nevertheless, if you use this, you are doing it at your own risk — it is against TypeRacer's Terms of Service. You have been warned.

It works in public, as well as private matches with friends.<br/>
Tutorial: https://www.youtube.com/watch?v=FqjH89JRGCY

## Preview
![](https://i.imgur.com/xG8J3yM.gif)<br/>
![](https://i.imgur.com/y4iW9hu.png)

## Usage
- Python 3.6 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.
- If you do not already have the **PyAutoGUI** library installed, run setup.py — make sure PIP is added to PATH.

Public matches:
1. Run main.py.
2. Select the desired speed.
3. Visit [play.typeracer.com](https://play.typeracer.com).
4. Launch any HTTP debugger — built-in browser debuggers work. In this example, I am going to use Chrome's built-in debugger.
5. Head over to the [Network tab](https://i.imgur.com/UAzJL0R.png).
6. Click "Enter a typing race" on the website.
7. Click on [this request](https://i.imgur.com/3gdyVdm.png) for further details.
8. Under the [Preview tab](https://i.imgur.com/oKbygth.png), scroll down until you see an [arrow](https://i.imgur.com/hBj61ou.png) — keep in mind that the numbers could vary. Click on it.
9. Copy [the text](https://i.imgur.com/P7Lrl73.png), and paste it in the program.
10. Go back to the match, and make sure the txtInput field is visible.
11. Lay back and watch!

Private matches:
1. Run main.py.
2. Select the desired speed.
3. Visit [play.typeracer.com](https://play.typeracer.com).
4. Launch **DevTools**. If you use Chrome, CTRL + SHIFT + I or F12.
5. Click "Race your friends", then "join race" on the website.
6. CTRL + SHIFT + C or click [this arrow](https://i.imgur.com/zvxm2Aw.png).
7. Select [the text](https://i.imgur.com/3D5SacJ.png).
8. Right click on the selected element in **DevTools**, and click "Edit as HTML".
9. Copy [the text](https://i.imgur.com/cN83wmr.png) and paste it in the program. Note: the first word may sometimes be excluded, requiring manual input.
10. Go back to the match, and make sure the txtInput field is visible.
11. Lay back and watch!

## Legal Notice
This is against TypeRacer's Terms of Service. I am not accountable for any of your actions; this was merely a speedrun to demonstrate how automation/cheating works. Please do not misuse this tool.
