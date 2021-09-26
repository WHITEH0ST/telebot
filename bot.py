import time, urllib3
from requests.api import get
import telebot
from telebot import types


TOKEN = "1742334431:AAGBbN1icZohPy6nhXhx3P17qYmHYE9n3B0"

bot = telebot.TeleBot(TOKEN)

is_running = False
unfinished = False

stil = ("1","2","3","4","5","6","7")

@bot.message_handler(commands=["start"])
def start_command(message):
    global unfinished
    unfinished = True
    bot.send_message(
        message.chat.id,
        'Greetings {}!\n'.format(str(message.chat.first_name)) +
        'I am here to assist you in getting tools from @TheHubProgram SHOP.\n'+
        'To get list of available items, press /avaliable.\n' +
        'To get help press /help.'
    )
    global is_running
    is_running = True
    unfinished = False

@bot.message_handler(commands=['help'])
def help_command(message):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                "Message my creator", url='telegram.me/thecodeisinvalid'
            )
        )
        bot.send_message(
            message.chat.id,
            '1) To get list of available items, press /avaliable.\n' +
            '2) If you need help with anything, Just use /support.\n' +
            '3) Make a request, (Custom Scam Pages/Custom Hacking Tools/Custom Spam tools.\n' +
            '4) Click “Update” to receive the current information regarding the request. ' +
            'The bot will also show the difference between the previous and the current exchange rates.\n',
        #   +'5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
            reply_markup=keyboard
        )
        unfinished = False

@bot.message_handler(commands=['avaliable'])
def exchange_command(message):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('BANK LOGS', callback_data='get-BANKLOGS'),
            telebot.types.InlineKeyboardButton('SCRIPTS', callback_data='get-SCRIPTS'),
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('FRAUD TOOLS', callback_data='get-FRAUDTOOLS'),
            telebot.types.InlineKeyboardButton('WIPEDOWN', url="https://bit.ly/wipedown"),
            telebot.types.InlineKeyboardButton('OTP BOT', callback_data='get-OTP')
        )
        # img = open("matrix.jpg", "rb")
        # img= urllib3.('C:/Users/BlackAdministrator/Downloads/matrix.jpg').read()
        msg = bot.send_message(message.chat.id, "Items for Sale in the shop", reply_markup=keyboard)
        unfinished = False


# @bot.message_handler(func=lambda message: True)
# def message_manner(message):
#     print (message)
#     if message.text == "OTP BOT":
#         bot.reply_to(message, "Hello")


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        if call.data == "get-OTP":
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.answer_callback_query(callback_query_id=call.id, text='Initializing OTP Service')
            msg = bot.send_message(call.message.chat.id, "To use OTP Bot u need to have a Auth Token, Put that here: ")
            bot.register_next_step_handler(msg, otp_bot_service)
            # otp_bot_service(call.message)
        elif call.data == "get-FRAUDTOOLS":
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.answer_callback_query(callback_query_id=call.id, text='Opening FraudTools Menu')
            msg = bot.send_message(call.message.chat.id,
                "TOOLS IN THE SHOP:\n" +
                "1. LEADSFINDER\n"+
                "2. LEADENERATOR\n"
                "(leads generator *40 percent accurate, MAD algorithm*)\n"+
                "3. Validator by @thehubprogram\n\n"
                "Reply with 1, 2 or 3...."
            )
            bot.register_next_step_handler(msg, get_fraud_tools)
        elif call.data == "get-SCRIPTS":
            bot.send_chat_action(call.message.chat.id, "typing")
            bot.answer_callback_query(callback_query_id=call.id, text='Fetching Available Scripts')
            msg = bot.send_message(call.message.chat.id, 
                "`SCRIPTS FOR SALE`: \n\n\n" +
                "1. LEADS FINDER SCRIPT, $1,500\n"+
                "*OFFICIAL PUBLIC RECORDS LEADS SEARCH SCRIPT*\n\n"+
                "2. LEADS GENERATOR SCRIPT, $100\n"+
                "*NEW ALGORITHMS ON NUMBER SYNTAX*\n\n"+
                "3. VALIDATOR SCRIPT WITH FREE API, $200\n"+
                "*VALIDATE YOUR LEADS INSTANTLY WITH THE SOURCE CODE*",
            parse_mode= 'Markdown')
            bot.register_next_step_handler(msg, buy_scripts)
        
        elif call.data == "get-BANKLOGS":
            bot.send_chat_action(call.message.chat.id, "typing")
            bot.answer_callback_query(callback_query_id=call.id, text='Retrieving Bank Logs')
            msg = bot.send_message(call.message.chat.id, "Logs")
        unfinished = False

my_tokens = ["awesomeGod", "thanks", "Jehovah"]

def otp_bot_service(message):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        if message.text in my_tokens:
            bot.send_message(message.chat.id, "Starting OTP bot, Prepare for takeoff")
            time.sleep(5)
            msg = bot.send_message(message.chat.id, "Authentication Token: ")
            text = message.text
            print (text)
            bot.send_message(message.chat.id, "Welcome to OTP BOT Service by @thecodeisinvalid\n" + "Select the bank you want to call....\n1. WELLS FARGO\n2. CHASE\n3. BANK OF AMERICA\n4. CITI\n\n\n\nReply with 1, 2, 3, or 4")
        
        else:
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.row(
                telebot.types.InlineKeyboardButton('Get Auth Token', url="https://t.me/thecodeisinvalid")
            )
            bot.send_message(message.chat.id, "Invalid Authentication Token, Please contact my master to get Authenticator Token now", reply_markup=keyboard)
        unfinished = False
        pass


@bot.message_handler(func=lambda message: True)
def get_fraud_tools(message):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        if message.text == "1":
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Coming Soon!")
        elif message.text == "2":
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Coming soon!")
        unfinished = False
        pass




def buy_scripts(message):
    global unfinished
    if is_running and unfinished == False:
        unfinished = True
        if message.text == "1":
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Coming Soon!")
        elif message.text == "2":
            bot.send_chat_action(message.chat.id, 'typing')
            bot.send_message(message.chat.id, "Coming soon!")
        unfinished = False
        pass










bot.enable_save_next_step_handlers(delay=2)
bot.polling()