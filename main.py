import time
import cv2
import mss
import numpy
import keyboard
import pytesseract
import pyautogui
from pynput.mouse import Controller
from random import randint, choice





# Define the screen region to capture
mon = {'top': 275, 'left': 700, 'width': 600, 'height': 100}

dictENGtoESP = {
    "action figure": "el muñeco",
    "as achild": "de niño/a",
    "as a child or when | was little": "de pequeño/a",
    "blocks": "los bloques",
    "coin": "la moneda",
    "collection": "la colección",
    "daycare center": "la guardería infantil",
    "disobedient": "desobediente",
    "doll": "la muñeca",
    "electric train": "el tren eléctrico",
    "everyone": "todo el mundo",
    "fish": "el pez",
    "generous": "generoso/a",
    "in general": "por lo general",
    "naughty": "travieso/a",
    "neighbor": "el vecino/la vecina",
    "obedient": "obediente",
    "once in a while": "de vez en cuando",
    "playground": "el patio de recreo",
    "rope": "la cuerda",
    "spoiled": "consentido/a",
    "teddy bear": "el oso de peluche",
    "timid": "tímido/a",
    "to behave badly": "portarse mal",
    "to behave well": "portarse bien",
    "to bother": "molestar",
    "to collect": "coleccionar",
    "to fight": "pelearse",
    "to jump rope": "saltar a la cuerda",
    "to lie": "mentir",
    "to obey": "obedecer",
    "to offer": "ofrecer",
    "to permit": "permitir",
    "tricycle": "el triciclo",
    "truth": "la verdad",
    "turtle": "la tortuga",
    "well-behaved": "bien educado/a",
    "world": "el mundo"
}

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        #cv2.imshow('Image', im)
        # Create a mouse controller
        # mouse = Controller()

        # Get the mouse position
        # x, y = mouse.position
        # print(f"Mouse position: X = {x}, Y = {y}")
        
        # Get the mouse position
        # Get the desired coordinates (replace with your own)
        ansBoxX, ansBoxY = 964, 452
        submitButtonX, submitButtonY = 1154, 607

        # Move the mouse to the desired location
        pyautogui.moveTo(ansBoxX, ansBoxY, duration=0.5)

        # Perform a left mouse click
        pyautogui.click()

        print(text.rstrip().lower())
        for keys in dictENGtoESP:
            if keys.lower() == text.rstrip().lower():
                print(dictENGtoESP[keys])
                if randint(0, 100) < 86:
                    keyboard.write(dictENGtoESP[keys])

                    # Move the mouse to the desired location
                    pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)

                    # Perform a left mouse click
                    pyautogui.click()
                else:
                    dictList = list(dictENGtoESP.keys())
                    keyboard.write(dictENGtoESP[choice(dictList)])
                    pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)
                    pyautogui.click()
                    
                    pyautogui.moveTo(ansBoxX, ansBoxY, duration=0.5)
                    pyautogui.click()
                    keyboard.press_and_release("ctrl+a")
                    keyboard.write("\b")

                    keyboard.write(dictENGtoESP[keys])
                    pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)
                    pyautogui.click()

                    # Move the mouse to the desired location
                    

                    # Perform a left mouse click
                    

                    

        

        

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        time.sleep(15)  # Capture one screenshot per second
