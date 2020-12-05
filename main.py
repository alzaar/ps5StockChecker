from checker import get_availablity
from notifier import notify_user
from playsound import playsound
import time

url = 'https://INSERT_URL.com'
url = 'https://www.nowinstock.net/ca/videogaming/consoles/sonyps5/'


if __name__ == "__main__":
  counter = 1
  while True:
    print(f'Round: {counter}')
    stock_availble = get_availablity(url)
    
    if len(stock_availble) > 0:
      playsound('found.mp3')
      notify_user(stock_availble)
    
    time.sleep(5)
    counter += 1