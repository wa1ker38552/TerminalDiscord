import os
import time
import discord
import requests
from colors import *
from replit import db
from alive import keepAlive
from threading import Thread

#del db['messages'] #reset messages
if not 'messages' in db.keys(): db['messages'] = []

webhook = 'YOUR DISCORD WEBHOOK HERE'
client = discord.Client()

def chat_listener():
  while True:
    response = input()
    requests.post(webhook, json={'content': response})
    db['messages'].append(f'Bot: {response}')

def chat_updater():
  while True:
    os.system('clear')
    for message in db['messages']:
      if message.split()[0] == 'Bot:':
        print(f'{blue}{message}')
      else: print(f'{white}{message}')
    time.sleep(1)


if __name__ == '__main__':
  Thread(target=chat_listener).start()
  Thread(target=chat_updater).start()
  @client.event
  async def on_ready():
      print(client.user)
  @client.event
  async def on_message(message):
    if message.author != client.user:
      m = str(message.content)
      a = str(message.author)
      if not a == 'YOURUSERNAME#0000': #replace the id in your username with 0000
        db['messages'].append(f'{a}: {m}')

  keepAlive()
  client.run(os.environ['DISCORDBOTSECRET'])
