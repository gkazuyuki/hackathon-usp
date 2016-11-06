#coding: utf-8
import urllib
import urllib2
import re
import telegram 
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, RegexHandler
import logging
logFile = "botlog.txt"
token = "256661264:AAElZlnuGuUBsK8zm9kBCFuP54T315QX7HE"
logging.basicConfig(filename = "botlog.txt", level = logging.INFO)
updater = Updater(token = token)
dispatcher = updater.dispatcher
userFile = "classifier.txt"

def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()
    # Welcome message
    msg = "Olá!\n"
    msg += "Eu sou o {0}\n".format(me.first_name)
    msg += "O que você gostaria de saber?\n\n"
    msg += "É só digitar algo e eu tentarei te ajudar\n"
    msg +="Minhas informações vêm do site linux.ime.usp.br/~kazuyuki\n\n"
    bot.sendMessage(chat_id = update.message.chat_id, text = msg)

def form(voto):
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    values = {'voto' : voto}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req) 
    the_page = response.read()


def query(bot, update):
    message = update.message.text.split(" ")
    #if message[0] = 
    bot.sendMessage(chat_id = update.message.chat_id, text = "Só um minuto, estou pensando em como posso te ajudar\n")
    url = 'https://linux.ime.usp.br/~kazuyuki/pages/sobreca.html'
    url2= 'https://linux.ime.usp.br/~kazuyuki/pages/index.html'
    resp = urllib.urlopen(url)
    resp2 = urllib.urlopen(url2)
    respData = resp.read()
    respData2 = resp2.read()
    querytext = re.findall(r'<!--query-->[^<>]*<!--query-->', respData)
    for i in range(0, len(message)):
        message[i]=message[i].lower()
    querytextaux=querytext[:]
    for i in range(0,len(querytext)):
        querytext[i]=str(querytext[i])[12:len(str(querytext[i]))-12]
        querytextaux[i]=querytext[i]
        querytextaux[i]=querytextaux[i].lower()
    for word in message:
        if word in querytextaux:
            i = querytextaux.index(word)
            string = '<!--query-->'+querytext[i]+'<!--query-->'
            index=respData.find(string)
            index+=len(string[i])
            parsetext=re.search(r'<!--parse-->[^<>]*<!--parse-->',respData[index:])
            parsetext=parsetext.group(0)
            bot.sendMessage(chat_id = update.message.chat_id, text = parsetext[12:len(parsetext)-12])
            return
    bot.send_message(chat_id=update.message.chat_id, text="Desculpe, mas não entendi o que você disse")
    




start_handler = CommandHandler('start', start)
query_handler = MessageHandler(Filters.text, query)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(query_handler)

updater.start_polling()
print("Up and running")
