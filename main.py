import time
import cv2
import mss
import numpy
import pytesseract

# Define the screen region to capture
mon = {'top': 275, 'left': 700, 'width': 600, 'height': 100}

dictENGtoESP = {
    "The avenue": "La avenida",
    "truck": "El camión",
    "The highway": "La carretera",
    "The driver (male/female)": "El conductor/la conductora",
    "The street crossing": "El cruce de calles",
    "The block": "La cuadra",
    "The corner": "La esquina",
    "The statue": "La estatua",
    "The fountain": "La fuente",
    "The pedestrian/pedestrians": "El peatón/los peatones",
    "driver's license": "El permiso de manejar",
    "The square": "La plaza",
    "The police officer (male/female)": "El policía, la policía",
    "To give a fine": "Poner una multa",
    "The bridge": "El puente",
    "The traffic light": "El semáforo",
    "The stop sign": "La señal de parada",
    "Traffic": "El tráfico",
    "wide": "ancho/a",
    "Enough!": "¡Basta!",
    "Agree": "De acuerdo.",
    "To leave": "Dejar",
    "Leave me alone": "Déjame en paz",
    "Slowly": "Despacio",
    "To wait": "Esperar",
    "To be sure": "Estar seguro/a",
    "narrow": "estrecho/a",
    "You are making me nervous": "Me estás poniendo nervioso/a",
    "dangerous": "peligroso/a",
    "To remove": "Quitar",
    "To be careful": "Tener cuidado",
    "already": "ya",
    "Approximately": "Aproximadamente",
    "How do you get to...?": "¿Cómo se va…?",
    "complicated": "complicado/a",
    "To cross": "Cruzar",
    "Straight": "Derecho",
    "From": "Desde",
    "To turn": "Doblar",
    "In the middle of": "En medio de",
    "Until": "Hasta",
    "To drive": "manejar",
    "The subway": "El metro",
    "To stop": "Parar",
    "To pass": "Pasar",
    "Through/by/for": "Por",
    "To stay": "Quedar",
    "To follow": "Seguir (e→i)",
    "To be in a hurry": "Tener prisa"
}

with mss.mss() as sct:
    while True:
        im = numpy.asarray(sct.grab(mon))
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(im)
        cv2.imshow('Image', im)

        for keys in dictENGtoESP:
            if keys.lower() == text.rstrip().lower():
                print(dictENGtoESP[keys])

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        time.sleep(1)  # Capture one screenshot per second
