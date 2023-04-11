import pyautogui
import time

# Set the key to use for bunnyhopping (in this case, space bar)
key = 'space'

# Set the delay between jumps (in seconds)
jump_delay = 0.05

# Set the duration of the script (in seconds)
duration = 1000

# Set the starting time
start_time = time.time()

# Loop until the duration is reached
while time.time() - start_time < duration:
    # Press the key
    pyautogui.keyDown(key)

    # Wait for a short period
    time.sleep(jump_delay)

    # Release the key
    pyautogui.keyUp(key)