import time
import cv2
import mss
import numpy
import keyboard
import pytesseract
import pyautogui
from pynput.mouse import Controller
from random import randint, choice
from deep_translator import GoogleTranslator




# Define the screen region to capture
mon = {'top': 275, 'left': 700, 'width': 600, 'height': 100}



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
        translation = GoogleTranslator(source='auto', target='en').translate(text.rstrip().lower())
        if randint(0, 100) < 86:
            keyboard.write(translation)

            # Move the mouse to the desired location
            pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)

            # Perform a left mouse click
            pyautogui.click()
        else:
            keyboard.write("iba")
            pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)
            pyautogui.click()
            
            pyautogui.moveTo(ansBoxX, ansBoxY, duration=0.5)
            pyautogui.click()
            keyboard.press_and_release("ctrl+a")
            keyboard.write("\b")

            keyboard.write(translation)
            pyautogui.moveTo(submitButtonX, submitButtonY, duration=0.5)
            pyautogui.click()

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        time.sleep(1)  # Capture one screenshot per second
