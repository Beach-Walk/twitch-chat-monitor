from selenium import webdriver;
from selenium.webdriver.chrome.options import Options
import time;
import re;
import sys;
from bs4 import BeautifulSoup;
class messageClass():
    def __init__(self,uName,message,inPrinted):
        self.name=uName
        self.message=message
        self.printed=inPrinted

menu=True
try:

    while menu is True:
        chrome_path =r"drivers\chrome\chromedriver.exe" #driver needs to be the same version as your chrome version
        options = Options()
        options.headless=True
        driver = webdriver.Chrome(chrome_path,chrome_options=options)
        chatLink = input("Enter a Twitch Popout url...\n")
        #chatLink = r"https://www.twitch.tv/popout/xqcow/chat?popout="#input("Enter a Twitch Chat url...\n")
        driver.get(chatLink)
        print("Opening: ",chatLink," ...")

        chatSearch = True
        messageClasses = []
        matchedClasses = []
        keyWordsNotSriped= []#"song\?","song name","music"
        keyWords = []
        print("Reading 'keywords.txt'...")
        f = open("keywords.txt", "r")
        keyWordsNotSriped= f.readlines()

        for list in keyWordsNotSriped:#remove \n from the list
            keyWords.append(list.rstrip('\n'))
        print("Done!")
        print("Searching chat, press CTRL+C ONCE at any time to exit...")

        while chatSearch is True:
            time.sleep(1)
            if(len(messageClasses)>=5000):
                print("******FLUSH******")
                messageClasses.clear()

            htmlSource = driver.page_source  # get html code from selenium loaded site

            soup = BeautifulSoup(htmlSource, "html.parser")  # input html code from selenium to beautiful soup

            parsedMessages = soup.find_all("div", class_="chat-line__message")

            parsedUsernames = soup.find_all("div", class_="chat-line__message")

            for messages in parsedMessages:

                if  messages.find("span", class_="chat-author__display-name") is not None:
                    username = messages.find("span", class_="chat-author__display-name").text
                    if messages.find("span", class_="text-fragment") is not None:
                        message = messages.find("span", class_="text-fragment").text
                        m = messageClass(username,message,False)
                        skip=False
                        for dupCheck in messageClasses:
                            if(dupCheck.name==m.name and dupCheck.message==m.message):
                                skip=True
                        if skip==False:
                            messageClasses.append(m)

            for classes in messageClasses:#filter chat
                for keyW in keyWords:
                    result = re.search(keyW, classes.message, re.IGNORECASE)
                    #print(result)
                    if(result is not None):
                        matchedClasses.append(classes)

            for matched in matchedClasses:
                if matched.printed == False:
                    print(matched.name+": " + matched.message)
                    matched.printed = True

except KeyboardInterrupt:
    print("Cleaning up, please wait...")
    driver.quit()
    sys.exit()
