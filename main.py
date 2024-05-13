from pynput import keyboard
import logging

logging.basicConfig(
  level=logging.INFO,
  format='[%(asctime)s] %(levelname)s [%(name)s] %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
)
logger = logging.getLogger(__name__)

def on_press(key):
  try:
    logger.info(f'Key pressed {key.char!r}')
  except AttributeError:
    logger.info(f'Key pressed {key!r}')

def on_release(key):
  logger.info(f'Key {key} released')
  if key == keyboard.Key.esc:
    # Stop listener
    return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
  on_press=on_press,
  on_release=on_release
) 
listener.start()
