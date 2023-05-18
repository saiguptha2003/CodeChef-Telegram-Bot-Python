import os
import telebot
import answers as a
BOT_TOKEN="6009001701:AAGAmuUmVeCMiHhIbxZsXcp8pPfJ8azsL1E"
bot=telebot.TeleBot(BOT_TOKEN) 
NotFoundMessage="Answer still not found wait for a while.........."
@bot.message_handler(commands=['start','hello','hi'])
def send_welcome(message):
    bot.reply_to(message,"hi chefs iam codechefresponse bot \n for any answers please send message like  /question1 or /solution1 or /1 or /2 etc")
    
    
@bot.message_handler(commands=['question1','solution1','1'])
def ques1(message):
    data=a.readfile("ques1.txt")
    if(os.path.getsize("ques1.txt") > 0):
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
        
@bot.message_handler(commands=['question2','solution2','2'])
def ques2(message):
    data=a.readfile("ques2.txt")
    if os.path.getsize("ques2.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
@bot.message_handler(commands=['question3','solution3','3'])
def ques3(message):
    data=a.readfile("ques3.txt")
    if os.path.getsize("ques3.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
@bot.message_handler(commands=['question4','solution4','4'])
def ques4(message):
    data=a.readfile("ques4.txt")
    if os.path.getsize("ques4.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)

@bot.message_handler(commands=['question5','solution5','5'])
def ques5(message):
    data=a.readfile("ques5.txt")
    if os.path.getsize("ques5.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
@bot.message_handler(commands=['question6','solution6','6'])
def ques6(message):
    data=a.readfile("ques6.txt")
    if os.path.getsize("ques6.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
@bot.message_handler(commands=['question7','solution7','7'])
def ques7(message):
    data=a.readfile("ques7.txt")
    if os.path.getsize("ques7.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
@bot.message_handler(commands=['question8','solution8','8'])
def ques8(message):
    data=a.readfile("ques8.txt")
    if os.path.getsize("ques8.txt") > 0:
        bot.reply_to(message,data)
    else:
        bot.reply_to(message,NotFoundMessage)
        
    
@bot.message_handler(func=lambda msg:True)
def echo_all(message):
    bot.reply_to(message,message.text)       
bot.infinity_polling()
