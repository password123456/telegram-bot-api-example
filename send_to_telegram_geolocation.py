__author__ = 'https://github.com/password123456/'

import sys
import requests


class Bcolors:
    Black = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Magenta = '\033[35m'
    Cyan = '\033[36m'
    White = '\033[37m'
    Endc = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    
    
    
def send_to_telegram_location(latitude, longitude, horizontal_accuracy, chat_id):
    token = '$your_bot_token_id$'
    url = 'https://api.telegram.org/bot%s/sendLocation' % token

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/49.0.2623.112 Safari/537.36'}

    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'horizontal_accuracy': horizontal_accuracy,
    }

    try:
        r = requests.get(url, headers=header, data=params, verify=True)
        print('%s- ok::%s%s' % (Bcolors.Green, r.text, Bcolors.Endc))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, send_to_telegram_location.__name__, e, Bcolors.Endc))
    else:
        r.close()


def main():
    # horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
    
    latitude = float(37.258038)
    longitude = float(127.116693)
    horizontal_accuracy = float(600)
    chat_id = 1212123121212     # chat_room_number

    
    send_to_telegram_location(latitude, longitude, horizontal_accuracy, chat_id)
        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, __name__.__name__, e, Bcolors.Endc))
