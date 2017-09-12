 -*- coding: utf-8 -*-
import telebot
import const
import smtplib
import time
import codecs, sys
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


outf = codecs.getwriter('utf-8')(sys.stdout)
print(outf, u'Привет!')

bot = telebot.TeleBot(const.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
 answer = "Здравствуйте, я - автоматизированный бот.Я помогу вам с получением документов, необходимых для зачисления ребёнка в детский садик Катюша в городе Сковродино. Вот мои команды:"
 bot.send_message(message.from_user.id, "Здравствуйте, я - автоматизированный бот.Я помогу вам с получением документов, необходимых для зачисления ребёнка в детский садик Катюша в городе Сковродино. Вот мои команды:")
 from telebot import types
 markup = types.ReplyKeyboardMarkup(True,False)
 markup.row('привет','список')
 #markup.row('привет', 'выход')
 markup.row('документы', 'документы на почту')
 bot.send_message(message.from_user.id, "документы - документы для поступления в формате PDF \n список - список, необходимых для поступления в детский садик документов \n отправка документов - отправка документов, для поступления в детский садик на указанную Вами почту в формате PDF \n", reply_markup=markup)
 pass


@bot.message_handler(content_types=["text"])

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
 if message.text=="документы на почту":
  send = bot.send_message(message.chat.id, 'На какой email отправить письмо?')
  bot.register_next_step_handler(send, otpt)
  #bot.send_message(message.chat.id,message.text)

 elif message.text == "привет" or message.text == "ghbdtn":
  bot.send_message(message.from_user.id, ("Здравствуйте, " + message.from_user.last_name))
  bot.send_message(message.from_user.id,"Здравствуйте,а я Katdetbot- автоматизированный бот.\n Я помогу вам с получением документов, необходимых для зачисления ребёнка в детский садик Катюша в городе Сковородино.")
 elif message.text == "документы":
  bot.send_message(message.from_user.id, "https://drive.google.com/open?id=0B_ih07bPpTxqMGpMV2JmTEpOM1U")
 elif message.text == "список":
  bot.send_message(message.from_user.id,
                 "1.Паспорт-2 шт \n 2.Свидетельво о рождении-2 шт \n 3.Справка о составе семьи \n 4.Резвизиты банковской карты, для возврата средств \n 4.Заполненое заявления о приеме ребенка в садик \n 5. Заполненое заявление о компенсации \n 6.Заполненый договор на оказание образовательных услуг \n \n Документы для заполения(последние три пункта) есть в разделе документы ")
pass

def otpt(message):
  otpto=str(message.text)
  otpfr=const.postlogi
#  bot.send_message(message.chat.id,otpto)
  mesfrto="Hello!"
  msg = MIMEText('Документы доступны по ссылке: \n https://drive.google.com/open?id=0B_ih07bPpTxqMGpMV2JmTEpOM1U'.encode('utf-8'), _charset='utf-8')
  msg['Subject'] = 'Документы для поступления в десткий садик Катюша'
  #help(smtplib)
  smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpObj.starttls()
  smtpObj.login(const.postlogi,const.postpsw)
  #help(smtpObj)
  smtpObj.sendmail(otpfr,otpto, msg.as_string())
  bot.send_message(message.chat.id,"Письмо отправлено, посмотрите Ваш электронный почтовый ящик")
  smtpObj.quit()
  pass


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    time.sleep(.25)


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)