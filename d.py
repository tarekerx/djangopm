import pyautogui
import time

# Give yourself 5 seconds to switch to the WhatsApp chat window
time.sleep(5)

# Number of times to spam the message
spam_count = 100

# The message to spam
message = "sad"

# Optional: Set the typing interval to make it faster
pyautogui.PAUSE = 0.01  # Reduce the pause between actions

for _ in range(spam_count):
    pyautogui.write(message)  # Type the message
    pyautogui.press('enter')  # Press Enter to send
