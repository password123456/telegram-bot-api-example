__author__ = 'https://github.com/password123456/'

import requests
import time


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
    
    
def send_to_telegram_text(message, chat_id):
    token = '$your_bot_token_id$'
    url = 'https://api.telegram.org/bot%s/sendMessage' % token

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/49.0.2623.112 Safari/537.36'}

    params = {
        'chat_id': chat_id,
        'text': message,
    }

    try:
        r = requests.get(url, headers=header, data=params, verify=True)
        print('%s- ok::%s%s' % (Bcolors.Green, r.text, Bcolors.Endc))
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, send_to_telegram_text.__name__, e, Bcolors.Endc))
    else:
        r.close()


def check_msg_size(text, chat_id):
    if len(text) <= 4096:
        send_to_telegram_text(text, chat_id)
    else:
        parts = []
        while len(text) > 0:
            if len(text) > 4080:
                part = text[:4080]
                first_lnbr = part.rfind('\n')
                if first_lnbr != -1:
                    parts.append(part[:first_lnbr])
                    text = text[first_lnbr:]
                else:
                    parts.append(part)
                    text = text[4080:]
            else:
                parts.append(text)
                break
        for idx, part in enumerate(parts):
            if idx == 0:
                send_to_telegram_text(part, chat_id)
            else:
                part = '(Continue...)\n%s' % part
                send_to_telegram_text(part, chat_id)
            time.sleep(2)
       

def main():
    message = '$messages to send a telegram$'
    chat_id = 12121212     # chat_room_number 
    
    # Telegram limits on sending messages up to 4,096 characters
    check_msg_size(message, chat_id)
        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print('%s- [%s] Exception::%s%s' % (Bcolors.Yellow, __name__.__name__, e, Bcolors.Endc))
