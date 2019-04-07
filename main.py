from telegram.ext import Updater, CommandHandler
import random

updater = Updater(token='TOKEN', use_context=True)

def start(update, context):
	if update.message.from_user.language_code == "ru":
		context.bot.send_message(chat_id=update.message.chat_id, text="Отправь мне /cookie name1 name2 name3\nИ я скажу кто пойдёт за печеньем))0)")
	else:
		context.bot.send_message(chat_id=update.message.chat_id, text="Send me /cookie name1 name2 name3\nAnd I will tell you who will go for cookies))0)")

def cookie(update, context):
	res = random.choice(context.args)
	if update.message.from_user.language_code == "ru":
		variations = ("бежит за печенюхами", "ковыляет за печеньем", "стремительно мчится за кукисами", "в слоумо уносится за печенбками")
		res += " " + random.choice(variations)
	else:
		variations = ("running for cookies", "goes in slow motion for cookies")
		res += " " + random.choice(variations)
	context.bot.send_message(chat_id=update.message.chat_id, text=res)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cookie', cookie))
updater.start_polling()
updater.idle()
