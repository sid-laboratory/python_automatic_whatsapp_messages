import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller 
import datetime
import requests

keyboard = Controller()

def send_whatsapp_message(msg: str):
    while True:
        try:
            category = 'happiness'
            now = datetime.datetime.now()
            api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
            response = requests.get(api_url, headers={'X-Api-Key': 'cXUC+qdzNSj20vmC9usDYg==LCRiOXYagcWJxTgb'})
            message = f"{msg} Current time is {now.strftime('%Y-%m-%d %H:%M:%S')}. Quote of the day: {response.text}"
            pywhatkit.sendwhatmsg_to_group_instantly(
                "SMS",
                message=message,
                tab_close=False 
            )
            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(18) 
            print("Message sent!")
            time.sleep(18) 
            pyautogui.hotkey('ctrl', 'w')  
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    send_whatsapp_message(msg="Hello !!!! ")
