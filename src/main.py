import os
from os.path import join, dirname
from dotenv import load_dotenv
import telebot

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

todos = []

@bot.message_handler(commands=['greet'])
def greet(msg):
  bot.send_message(msg.chat.id, 'greetings!')


@bot.message_handler(commands=['list'])
def listTodos(msg):
  list_str = ""
  for todo in todos: 
    list_str += todo + "\n"
  bot.send_message(msg.chat.id, list_str)

@bot.message_handler(commands=['push'])
def addTodo(msg):
  print(msg.text)
  todos.append('Tood')
  bot.send_message(msg.chat.id, 'Added.')

@bot.message_handler(commands=['pop'])
def addTodo(msg):
  todos.pop();
  bot.send_message(msg.chat.id, 'First task deleted.')

@bot.message_handler(commands=['clear'])
def addTodo(msg):
  todos.clear();
  bot.send_message(msg.chat.id, 'Cleared.')

bot.polling()