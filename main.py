from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4
import random

updater = Updater(token='TOKEN', use_context=True)

variationsRU = ("бежит за печенюхами", "ковыляет за печеньем", "стремительно мчится за кукисами", "в слоумо уносится за печенбками")
variationsEN = ("running for cookies", "goes in slow motion for cookies")

def start(update, context):
	if update.message.from_user.language_code == "ru":
		context.bot.send_message(chat_id=update.message.chat_id, text="Отправь мне имена кандидатов на поход за печеньками через пробел.\nИ я скажу кто пойдёт за печеньем))0)")
	else:
		context.bot.send_message(chat_id=update.message.chat_id, text="Send me the names of the candidates for the campaign for cookies through the space.\nAnd I will tell you who will go for cookies))0)")

def cookie(update, context):
	res = random.choice(update.message.text.split())
	if update.message.from_user.language_code == "ru":
		res += " " + random.choice(variationsRU)
	else:
		res += " " + random.choice(variationsEN)
	context.bot.send_message(chat_id=update.message.chat_id, text=res)

def inlinequery(update, context):
	if update.inline_query.query != "":
		query = update.inline_query.query.split()
		res = random.choice(query)
		if update.inline_query.from_user.language_code == "ru":
			res += " " + random.choice(variationsRU)
		else:
			res += " " + random.choice(variationsEN)
		update.inline_query.answer([InlineQueryResultArticle(id=uuid4(), title="Choose your fighter🍪", input_message_content=InputTextMessageContent(res))], cache_time=1)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, cookie))
updater.dispatcher.add_handler(InlineQueryHandler(inlinequery))
updater.start_polling()
updater.idle()
