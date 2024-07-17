import random
import telebot
from telebot import types
import gtts
import qrcode
# from datetime import date,datetime
from khayyam import JalaliDatetime

bot = telebot.TeleBot("Your_Token!!")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+", you are welcome😊")

@bot.message_handler(commands=['game'])
def game(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+"Give me your guess number(0,100): ",reply_markup=game_menu_markup)
	computer_number = random.randint(0, 100)
	# Define a function to handle the user's guess
	def handle_guess(msg):
		try:
			if msg.text == "/newgame":
				new_game(msg)
				return
			user_guess = int(msg.text)
			if computer_number == user_guess:
				bot.reply_to(msg,user_name+" Congratulations! You guessed it! 👏🎉",reply_markup=main_menu_markup)
				return
			elif computer_number > user_guess:
				bot.reply_to(msg,"Go up ⬆️")
			elif computer_number < user_guess:
				bot.reply_to(msg,"Go down ⬇️")
			bot.send_message(msg.chat.id, "Give me your next guess:")
			bot.register_next_step_handler(msg, handle_guess)
		except ValueError:
			bot.send_message(msg.chat.id, "Please enter a valid number.")
	bot.register_next_step_handler(message, handle_guess)

@bot.message_handler(commands=['newgame'])
def new_game(message):
	bot.send_message(message.chat.id, "Starting a new game...",)
	game(message)

@bot.message_handler(commands=['age'])
def age(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+"please give me your age in Jalali Date!(1381,6,11)")
	bot.clear_step_handler_by_chat_id(message.chat.id)
	def handle_age(msg):
		try:
			birthday = msg.text
			year, month, day = map(int, birthday.split(","))
			birth_date = JalaliDatetime(year, month, day)
			today = JalaliDatetime.now()

			age = today - birth_date
			years = age.days // 365
			months = (age.days % 365) // 30
			days = (age.days % 365) % 30

			age_str=f"{years} years, {months} months, {days} days"
			bot.reply_to(msg, f"Now your age is: {age_str}")
		except ValueError:
			bot.send_message(msg.chat.id,"please send it in the correct form!!")
	bot.register_next_step_handler(message, handle_age)

@bot.message_handler(commands=['voice'])
def voice(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+" give me an English text✌️")
	# Clear any existing next step handlers
	bot.clear_step_handler_by_chat_id(message.chat.id)
	# Define a function to handle the user's text
	def handle_text(msg):
		try:
			output = msg.text
			text_to_voice=gtts.gTTS(output,lang="en",slow=False)
			text_to_voice.save("voic_of_text.mp3")
			audio=open("voic_of_text.mp3","rb")
			bot.send_audio(msg.chat.id,audio)
		except ValueError:
			bot.send_message(msg.chat.id, "Please give an English text!!")
	bot.register_next_step_handler(message, handle_text)

@bot.message_handler(commands=['max','argmax'])
def argmax(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+"give me an arrary like: 2,4,1,6,3,10,25")
	bot.clear_step_handler_by_chat_id(message.chat.id)
	def handel_array_index(msg):
		try:
			array = msg.text.split(",")
			array = list(map(lambda x:int(x),array))

			max_value = max(array)
			max_index = array.index(max_value)

			if message.text.startswith("/max"):
				bot.reply_to(msg,max_value)
			elif message.text.startswith("/argmax"):
				bot.reply_to(msg,max_index)
		except ValueError:
			bot.send_message(msg.chat.id,"please send it in the correct form!!")
	bot.register_next_step_handler(message,handel_array_index)

@bot.message_handler(commands=['qrcode'])
def qr_code(message):
	user_name = message.from_user.username
	bot.send_message(message.chat.id,user_name+"give me a text to make it a qrcode!🫡")
	# Clear any existing next step handlers
	bot.clear_step_handler_by_chat_id(message.chat.id)
	def handle_sentence(msg):
		try:
			sentence=msg.text
			qr_code=qrcode.make(sentence)
			qr_code.save(sentence+".png")
			photo=open(sentence+".png","rb")
			bot.send_photo(msg.chat.id,photo)
		except ValueError:
			bot.send_message(msg.chat.id,"I can not make a Qr code for this text!!")
	bot.register_next_step_handler(message,handle_sentence)

@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message,"😊کامند استارت با شما سلام و خوش امدگویی می کند")
	bot.reply_to(message,"✌️کامند بازی با انتخاب یک عدد رندوم بین 0 و 100 از شما می خواهد تا با حدس ان موفق شوید")
	bot.reply_to(message,"🤪کامند سن از شما تاریخ تولدتون رو به شمسی می پرسه و سنتون رو بهتون میگه")
	bot.reply_to(message,"🎶کامند صدا از شما یک جمله انگیلیسی می گیره و جمله را به صورت صوت برای شما می فرستد")
	bot.reply_to(message,"👀کامند بیشترین،بزرگترین عدد داخل آرایه را به شما میگوید")
	bot.reply_to(message,"👣کامند ارگومان بیشترین به شما میگوید کدام خانه از آرایه بیشترین مقدار را نگهداری می کند")
	bot.reply_to(message,"🫡کامند بارکد از شما یک جمله می گیرد و ان را تبدیل به بارکد می کند")
	bot.reply_to(message,"⚠️کامند کمک این توضیحات را به شما می دهد")
	bot.reply_to(message,"start = welcome command😊")
	bot.reply_to(message,"game = you should guess a number between 0-100 until you win✌️")
	bot.reply_to(message,"age = get your birthday in persian calender and give you your age🤪")
	bot.reply_to(message,"voice = get an English text and give you the pronunciation as a mp3 file🎶")
	bot.reply_to(message,"max = get an array and give you the greatest number in it👀")
	bot.reply_to(message,"argmax = get an array and give you the subscrip of the greatest number👣")
	bot.reply_to(message,"qrcode = get a text and make a qrcode and give it to you by an image in png format🫡")
	bot.reply_to(message,"help = give you this information⚠️")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.send_message(message.chat.id,"Menu:",reply_markup=main_menu_markup)

# Main Menu Markup
main_menu_markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/start')
itembtn2 = types.KeyboardButton('/game')
itembtn3 = types.KeyboardButton('/age')
itembtn4 = types.KeyboardButton('/voice')
itembtn5 = types.KeyboardButton('/max')
itembtn6 = types.KeyboardButton('/argmax')
itembtn7 = types.KeyboardButton('/qrcode')
itembtn8 = types.KeyboardButton('/help')
main_menu_markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

# Game Menu Markup
game_menu_markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn_new_game = types.KeyboardButton('/newgame')
game_menu_markup.add(itembtn_new_game)

bot.infinity_polling()
