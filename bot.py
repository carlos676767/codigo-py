import time
import pyautogui
import datetime
import pyperclip  

def getDate():
    data_atual = datetime.datetime.now().strftime('%d/%m/%Y')
    pyperclip.copy(data_atual)

class AutomationBot:
    count = 0

    @staticmethod
    def startAutomation(vezes, id):
        AutomationBot.pressKey(7, id, "enter")
        
        while AutomationBot.count < vezes:
            AutomationBot.pressKey(7, "8", "enter")
            AutomationBot.pressKey(7, "1", "enter")
            AutomationBot.pressKey(7, "14", "enter")
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "5", "enter")
            AutomationBot.pressKey(7, "3", "enter")
            
            AutomationBot.pasteDate()
            AutomationBot.pressKey(7, '1', 'enter')
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "1", "enter")
            AutomationBot.pressKey(7, "14", "enter")
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "5", "enter")
            AutomationBot.pressKey(7, "3", "enter")
            
           
            AutomationBot.pasteDate()
            AutomationBot.pressKey(7, '1', 'enter')
            AutomationBot.pressKey(7, "2", "enter")
            AutomationBot.pressKey(7, "1", "enter")
            
  
            AutomationBot.count += 1
            
            
            
            if AutomationBot.count == 3:
                return print("Automation completed.")
            
            

    @staticmethod
    def pressKey(delay: int, text: str, key: str):
        time.sleep(delay)
        pyautogui.write(text)
        pyautogui.press(key)

    @staticmethod
    def pasteDate():
        getDate()
        time.sleep(7) 
        pyautogui.hotkey('ctrl', 'v') 
        pyautogui.press('enter') 
        




