import time
import keyboard
import pyttsx3 as pt
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

path = os.getcwd()
driver_path = path + '/chromedriver.exe'


def scrap(n):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
        driver.get("https://www.tradingview.com/markets/cryptocurrencies/prices-" + n + "/")
        driver.maximize_window()
        t1 = driver.find_element(By.XPATH, "//header/div/div[3]/div/div/div/div/div").text
        t2 = t1.replace('\n', '').split('USD')
        pt.init()
        pt.speak(t2[0])
        driver.close()
        driver.quit()
        return True
    except:
        pt.init()
        pt.speak("Sorry Not recognized the Coin")
        return False


def scrapper():
    n = input("Enter the currency name:")
    tme = int(input("Enter Time duration in seconds:"))
    chck = scrap(n)
    pre = time.time()
    if chck:
        while True:
            time.sleep(0.01)
            if int(time.time() - pre) >= tme:
                scrap(n)
                pre = time.time()
            if keyboard.is_pressed('p'):
                print('Exit program')
                break
    else:
        exit()
        print("Sorry wrong Coin Name")


if __name__ == "__main__":
    scrapper()
