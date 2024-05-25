import time
import pyautogui

def auto_clicker(num_clicks, delay):
    for _ in range(num_clicks):
        pyautogui.click()
        time.sleep(delay)

# Example: Auto click 10 times with a delay of 1 second
auto_clicker(10, 1)
