# Automatisierter Bot für Googles Trex Spiel:
# www.trex-game.skipser.com

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Koordinaten():
    # Lokaliesieren des Replay Buttons
    replayBtn = (350, 400)
    # Lokaliesieren der Spielfigur
    dinosaurier = (171, 440)

# Automatischer Restart des Spiels
def restartGame():
    pyautogui.click(Koordinaten.replayBtn)

    # Automatisches ducken um spätere Vögel zu dodgen
    pyautogui.keyDown('down')

# Methode um zu Springen
def pressSpace():
    pyautogui.keyUp('down')

    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    time.sleep(0.2)
    pyautogui.keyUp('space')
    # Nach dem Hüpfen direkt wieder in den geduckten Modus
    pyautogui.keyDown('down')

# Methode um zu erkennen ob sich ein Gegenstand vor dem Spieler befindet
def ImageGrab():
    box = (Koordinaten.dinosaurier[0] + 60, Koordinaten.dinosaurier[1], Koordinaten.dinosaurier[0] + 150, Koordinaten.dinosaurier[1] + 5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    img = array(grayImage.getcolors())
    print(img.sum(  ))
    return img.sum()



def if __name__ == "__main__":
    restartGame()
    
    # Wenn ein Gegenstand vor dem Spieler erkannt wurde, wird die Methode pressSpace() aufgerufen
    While True:
        if (ImageGrab() != 697):
            pressSpace()
            time.sleep(0.1)


