# Hypixel Skyblock Anti-Idle

This tool automates certain actions in the game Hypixel Skyblock to prevent the player from being sent to the lobby. It uses `pyautogui` to control the mouse and keyboard, and `pytesseract` for optical character recognition (OCR).

## Requirements

- Python 3.x
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)

## Installation

1. Clone this repository or download the `hypixelSkyblockAntiLobby.py` file.
2. Install the necessary dependencies:
    ```sh
    pip install pyautogui pytesseract
    ```
3. Make sure you have Tesseract-OCR installed and configured correctly. You can download it [here](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Open Minecraft, enter your Hypixel Skyblock island, and position yourself where you want to stay AFK.
2. Type `/setspawn` in the Minecraft chat at that location to respawn there. (There should be no blocks above where you want to spawn).
3. Run the `hypixelSkyblockAntiLobby.py` script:
    ```sh
    python hypixelSkyblockAntiLobby.py
    ```
4. The script will start monitoring the screen and perform the necessary actions to prevent the player from being sent to the lobby. If the script detects that you have been sent to a public lobby, it will automatically return you to your personal island. Otherwise it will move the mouse.

## Functions

- `logoutFromServer()`: Logs out from the server.
- `loginToServer()`: Logs in to the server.
- `playSkyblock()`: Enters Skyblock mode.
- `warpHome()`: Teleports the player home.
- `moveMouse()`: Moves the mouse randomly to avoid inactivity.
- `takeScreenshot(screenRegion)`: Takes a screenshot of a specific region.
- `imageToString(screenshot)`: Converts a screenshot to text using OCR.
- `regionToString(region)`: Converts a region of the screen to text using OCR.
- `checkIfInPublicLobby()`: Checks if the player has been sent to a public lobby.

## Notes

- Make sure the path to `tesseract.exe` in the script is correct.
- This script is designed to be used on Windows.

## Contributions

Contributions are welcome. If you find any issues or have any suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.