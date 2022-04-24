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
    

def send_to_telegram_document(file_name, file_caption, chat_id):
    token = '$your_bot_token_id$'
    url = 'https://api.telegram.org/bot%s/sendDocument' % token

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/49.0.2623.112 Safari/537.36'}

    params = {
        'chat_id': chat_id,
        'caption': file_caption,
    }

    readfile = open(file_name, 'rb')
    sendfile = {'document': readfile}

    try:
        r = requests.post(url, headers=header, data=params, files=sendfile, verify=True)
        print('%s- ok::%s%s' % (Bcolors.Green, r.text, Bcolors.Endc))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, send_to_telegram_document.__name__, e, Bcolors.Endc))
    else:
        r.close()
        

def main():
    file_name = '$/data/program/docs/telegram.pdf$'
    file_caption = '$your document description$'
    chat_id = 12121212     # chat_room_number 
    
    send_to_telegram_document(file_name, file_caption, chat_id)

        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, __name__.__name__, e, Bcolors.Endc))
