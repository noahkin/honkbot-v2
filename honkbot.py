import discord
from discord.utils import get
import goose_cli
from datetime import datetime
import time
from auth import token


### Birthday Stuff
# Needs support for duplicate bdays
data = [{'Name': 'Nate', 'Bday': '04-01'},{'Name': 'Bobby G', 'Bday': '08-14'},{'Name': 'Kelly', 'Bday': '02-18'},
        {'Name': 'Jake Medina', 'Bday': '12-12'},{'Name': 'Kaleb', 'Bday': '12-24'},{'Name': 'Jenni', 'Bday': '05-05'},
        {'Name': 'Kyle', 'Bday': '05-01'},{'Name': 'Dan', 'Bday': '08-12'}, {'Name': 'Noah', 'Bday': '11-13'},{'Name': 'Bill', 'Bday': '05-07'},{'Name': 'Zack and John', 'Bday': '01-01'}]
dateDict = []
for i in range(len(data)):
     dateDict.append(data[i]['Bday'])
     dateDict.sort()
def birthday_knower(data):
     today = datetime.today()
     today = today.strftime('%m-%d')
     for i in range(len(data)):
          for y in dateDict:
               if y > today:
                    nextBday = y
                    break
          bdayDate = data[i]['Bday']
          bdayPerson = data[i]['Name']
          if bdayDate == today:
               bdayPerson = bdayPerson
          elif bdayDate != today:
               bdayPerson = 'nobody'
          if nextBday == data[i]['Bday']:
               nextPerson = data[i]['Name']
          
     return bdayPerson, nextBday, nextPerson
bdayPerson, nextBday, nextPerson = birthday_knower(data)


class Client(discord.Client):
    # Runs when bot has finished initializing
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await goose_cli.run_cli(client) # Run any relevant CLI args passed to honkbot
    
    # Runs for each message in the server
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        ## Various bot commands below:
        if message.author != self.user: # Needs to check dev instance as well
            if 'kyle' in message.content.lower(): # prob kill this at some point?
                emoji = 'SexyKyle:388117155176120320'
                await message.channel.send('kyle')
                await message.add_reaction(emoji)
            if message.content.lower() == 'bday' and bdayPerson == 'nobody':
                response = ('it aint nobodys bday bitch')
                await message.channel.send(response)
            elif message.content.lower() == 'bday' and bdayPerson != 'nobody':
                response = ('HAPPY BDAY TO ' + bdayPerson + '!!!!!!!!  buy them shit')
                await message.channel.send(response)
            if message.content.lower() == 'next bday':
                response = ('The next goose bday is ' + nextPerson + '\'s on ' + nextBday + '!!!!!!!!!!!!!!!!!!  Get hype bout it')
                await message.channel.send(response)
            if message.content.lower() == 'hey honkbot':
                response = ('hey')
                await message.channel.send(response)
                time.sleep(3) # delay before honk
            if 'honk' in message.content.lower():
                await message.channel.send('honk')
     #####emoji reactions lmaooooooo
            if 'repicy' in message.content.lower():
                emoji = 'a:repicy:644999601270685707'
                await message.channel.send('rEpIcY!')
                await message.add_reaction(emoji)
            if 'cringe' in message.content.lower():
                emoji = 'kershrek:768886281773383762'
                await message.add_reaction(emoji)
            if 'smh' in message.content.lower() or 'smdh' in message.content.lower():
                emoji = 'smhmyhead:651848089224609793'
                await message.add_reaction(emoji)
            if 'nate' in message.content.lower():
                emoji = 'yetinate:520637149566205964'
                await message.add_reaction(emoji)
            if 'fuck yeah' in message.content.lower():
                emoji = ':thicc:438569502637293568'
                await message.add_reaction(emoji)


# Launch bot
client = Client()
client.run(token)
