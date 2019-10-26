from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
import random

updater = Updater(token='TOKEN', use_context=True)

variationsRU = ("{} бежит за печенюхами", "{} ковыляет за печеньем", "{} стремительно мчится за кукисами", "{} в слоумо уносится за печенбками", "Собирая своё снаряжение {} уходит в пустоши сражаться с крысами мутантами за крышки, на которые он купит печенье")
variationsEN = ("{} running for cookies", "{} goes in slow motion for cookies")

def start(update, context):
	if update.message.from_user.language_code == "ru":
		context.bot.send_message(chat_id=update.message.chat_id, text="Отправь мне имена кандидатов на поход за печеньками через пробел.\nИ я скажу кто пойдёт за печеньем))0)\nЛибо можешь добавить меня в группу и делать тоже самое добавляя в начале /cookie (пример - /cookie имя1 имя2). Или же использовать меня в inline режиме, для этого в любом чате набери @Who_will_go_for_cookies_bot и имена через пробел.")
	else:
		context.bot.send_message(chat_id=update.message.chat_id, text="Send me the names of the candidates for the campaign for cookies through the space.\nAnd I will tell you who will go for cookies))0)\nOr you can add me to the group and do the same thing adding at the beginning /cookie (example - /cooke name1 name2). Or use me in inline mode, for this in any chat type @Who_will_go_for_cookies_bot and the names are separated by a space.")

def cookie(update, context):
	if update.message.text == "/cookie":
		if update.message.from_user.language_code == "ru":
			context.bot.send_message(chat_id=update.message.chat_id, text="Так не пойдёт, мне нужно /cookie и имена через пробел (пример - /cookie имя1 имя2)")
		else:
			context.bot.send_message(chat_id=update.message.chat_id, text="So it will not work, I need /cookie and names separated by a space (example - /cooke name1 name2)")
		return
	if context.args is None:
		res = getResult(update.message.text.split(), update.message.from_user.language_code)
	else:
		res = getResult(context.args, update.message.from_user.language_code)
	context.bot.send_message(chat_id=update.message.chat_id, text=res)

def inlinequery(update, context):
	if update.inline_query.query != "":
		res = getResult(update.inline_query.query.split(), update.inline_query.from_user.language_code)
		update.inline_query.answer([InlineQueryResultArticle(id=uuid4(), title="🍪 Choose your fighter", input_message_content=InputTextMessageContent(res))], cache_time=1)

def getResult(names, language_code = "ru"):
	if language_code == "ru":
		res = random.choice(variationsRU).format(random.choice(names))
		candidates = "Кандидаты: "
	else:
		res = random.choice(variationsEN).format(random.choice(names))
		candidates = "Candidates: "
	for i, candidate in enumerate(names):
		if i != 0:
			candidates += ", "
		candidates += candidate
		if i == len(names) - 1:
			candidates += "."
	return candidates + "\n\n" + res

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cookie', cookie))
updater.dispatcher.add_handler(MessageHandler(Filters.text, cookie))
updater.dispatcher.add_handler(InlineQueryHandler(inlinequery))
updater.start_polling()
updater.idle()