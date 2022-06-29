# Twitch Chat Monitor
Twitch Chat Monitor. Monitors Twitch chat and outputs matching regex using Selenium & BeautifulSoup. Written in Python3.

## Limitations
- Only press ctrl+c ***ONCE*** to exit. Pressing it multiple times could leave the browser driver to run in the background even though program is closed.
- Currently only works with popout chats
- Only tested on Windows. May need modification for other OSs.

## Requirements
- Chrome Browser
- Chrome Driver
- Python 3 & pip (or some variant)
- Dependencies in requirements.txt

## How It Works
- It scans through Twitch Chat and looks for matches of regex in "keywords.txt"
 - Add regex to this file and seperate with new lines
- Once a match is found it will output the username and the message that matched.
- Messages stored in array will flush at around 5000~ messages to reduce ram usage.

## To Build & Run (assuming you have py3)
1. Download ZIP or clone repository 

2. Install dependencies
    - pip install -r requirements.txt
3. Download chrome driver
    - https://chromedriver.chromium.org/
     - Be sure your downloaded driver is the same version as the regular chrome browser you have installed.
      you can check chrome version by going to help>about chrome
    - Unzip and place .exe in the folder: drivers/chrome
4. Open CMD in program directory and run:
    - python run.py
  ## To Do
  - Executable?
  - Add more driver support
  - Clean up code / user input

