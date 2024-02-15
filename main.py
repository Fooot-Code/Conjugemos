import time
import cv2
import mss
import numpy
import keyboard
import pytesseract
import pyautogui
from pynput.mouse import Controller






# Define the screen region to capture
mon = {'top': 275, 'left': 700, 'width': 600, 'height': 100}

dictENGtoESP = {
    "avenue": "La avenida",
    "truck": "El camión",
    "highway": "La carretera",
    "driver/conductor": "El conductor",
    "intersection": "El cruce de calles",
    "block": "La cuadra",
    "corner": "La esquina",
    "statue": "La estatua",
    "fountain": "La fuente",
    "pedestrian": "El peatón",
    "driver's license": "El permiso de manejar",
    "plaza": "La plaza",
    "police": "El policía",
    "To give a ticket": "Poner una multa",
    "bridge": "El puente",
    "stoplight": "El semáforo",
    "stop sign": "La señal de parada",
    "Traffic": "El tráfico",
    "wide": "ancho",
    "Enough!": "¡Basta!",
    "Agree": "De acuerdo.",
    "To leave": "Dejar",
    "Leave me alone": "Déjame en paz",
    "Slowly": "Despacio",
    "To wait": "Esperar",
    "To be sure": "Estar seguro",
    "tight": "estrecho",
    "You are making me nervous": "Me estás poniendo nervioso",
    "dangerous": "peligroso",
    "To remove": "Quitar",
    "To be careful": "Tener cuidado",
    "already": "ya",
    "Approximately": "Aproximadamente",
    "How do you get to...?": "¿Cómo se va…?",
    "complicated": "complicado",
    "To cross": "Cruzar",
    "Straight": "Derecho",
    "since": "Desde",
    "To turn": "Doblar",
    "In the middle of": "En medio de",
    "Until": "Hasta",
    "To drive": "manejar",
    "metro": "El metro",
    "To stop": "Parar",
    "To pass": "Pasar",
    "Through/by": "Por",
    "To stay": "Quedar",
    "To follow": "Seguir",
    "To be in a hurry": "Tener prisa"
}

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        cv2.imshow('Image', im)

        # Create a mouse controller
        # mouse = Controller()

        # Get the mouse position
        # x, y = mouse.position
        # print(f"Mouse position: X = {x}, Y = {y}")
        
        # Get the mouse position
        # Get the desired coordinates (replace with your own)
        target_x1, target_y2 = 964, 452

        # Move the mouse to the desired location
        pyautogui.moveTo(target_x1, target_y2, duration=0.5)

        # Perform a left mouse click
        pyautogui.click()

        for keys in dictENGtoESP:
            if keys.lower() == text.rstrip().lower():
                print(dictENGtoESP[keys])
                keyboard.write(dictENGtoESP[keys])

        target_x3, target_y4 = 1154, 607

        # Move the mouse to the desired location
        pyautogui.moveTo(target_x3, target_y4, duration=0.5)

        # Perform a left mouse click
        pyautogui.click()

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        time.sleep(5)  # Capture one screenshot per second
