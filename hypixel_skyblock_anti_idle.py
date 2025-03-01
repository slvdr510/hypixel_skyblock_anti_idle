import random
import sys
import pyautogui
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# FUNCTIONS

def logoutFromServer():
    pyautogui.hotkey('escape')
    time.sleep(0.1)
    pyautogui.leftClick(958,506)
    time.sleep(1)

def loginToServer():
    pyautogui.leftClick(701,127)
    pyautogui.leftClick(701,127)
    time.sleep(5)

def playSkyblock():
    #pyautogui.hotkey('escape')
    pyautogui.hotkey('t')
    pyautogui.hotkey('shift', '7')
    pyautogui.hotkey('p','l','a','y','space','s','b')
    pyautogui.hotkey('enter')
    time.sleep(5)

def warpHome():
    pyautogui.hotkey('t')
    pyautogui.hotkey('shift', '7')
    pyautogui.hotkey('w','a','r','p','space','h','o','m','e')
    pyautogui.hotkey('enter')
    time.sleep(5)

def moveMouse():
    current_x, current_y = pyautogui.position()
    random_pixels_x = random.randint(10, 300)
    random_pixels_y = random.randint(10, 200)
    random_movement_duration_time = random.uniform(0.2,0.5)
    pyautogui.moveTo(
        (current_x + (random_pixels_x * arrayValorPositivoNegativo[random.randint(0,1)]) ),
        (current_y + (random_pixels_y * arrayValorPositivoNegativo[random.randint(0,1)]) ),
        duration=random_movement_duration_time)

def takeScreenshot(screenRegion):
    regionScreenshot = pyautogui.screenshot(region=screenRegion)
    return regionScreenshot

def imageToString(screenshot):
    screenshotText = pytesseract.image_to_string(screenshot, lang='eng')
    return screenshotText

def regionToString(region):
    resultString = imageToString(takeScreenshot(region))
    return resultString

# FLAGS
currentZoneScreenshotRegionNormal=(1735,486,124,17)
currentZoneScreenshotRegionEvent=(1637,463,238,20)
cooldown_duration = 5  # 5 seconds cooldown
arrayValorPositivoNegativo = [1,-1]
reloadTimesCounter=0
errorScanCounter=0
goodScanCounter=0

sys.stdout.write("\n")
sys.stdout.write("\r | GOOD SCANS | ERROR SCANS | TOTAL RELOADS |\n")
sys.stdout.write("\r |------------|-------------|---------------|\n")
sys.stdout.write("\r | {:10.0f} | {:11.0f} | {:13.0f} |".format(goodScanCounter, errorScanCounter, reloadTimesCounter))
sys.stdout.flush()

time.sleep(2)
while True:

    sys.stdout.write("\r | {:10.0f} | {:11.0f} | {:13.0f} |".format(goodScanCounter, errorScanCounter, reloadTimesCounter))
    sys.stdout.flush()
    
    time.sleep(random.uniform(2.0,4.0)) 

    currentZoneNormalText = regionToString(currentZoneScreenshotRegionNormal)
    currentZoneEventText = regionToString(currentZoneScreenshotRegionEvent)

    if "and" in currentZoneNormalText:
        moveMouse()
        errorScanCounter = 0
        goodScanCounter += 1

    elif "and" in currentZoneEventText:
        moveMouse()
        errorScanCounter = 0
        goodScanCounter += 1

    elif errorScanCounter == 5:
        errorScanCounter = 0
        reloadTimesCounter += 1
        logoutFromServer()
        loginToServer()
        playSkyblock()
        if "and" in currentZoneNormalText:
            goodScanCounter += 0
        elif "and" in currentZoneEventText:
            goodScanCounter += 0
        else:
            warpHome()
            errorScanCounter=0

    else:
        moveMouse()
        errorScanCounter += 1