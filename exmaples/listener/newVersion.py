from QiRub import ClientMessenger as CM, QiUpdater

AUTH = ""
KEY = ""

bot = CM(AUTH, KEY)

@bot.onPlusMessage()
def App(message: QiUpdater):
  print(message)
  #...

bot.polling()
