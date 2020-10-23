import discord
import goose_cli
from auth import token

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await goose_cli.run_cli(client)
    ### adding birthday list and bday functionality below -klb
    data = [{'Name': 'Nate', 'Bday': '04-01'},{'Name': 'Bobby G', 'Bday': '08-14'},{'Name': 'Kelly', 'Bday': '02-18'},
        {'Name': 'Jake Medina', 'Bday': '12-12'},{'Name': 'Kaleb', 'Bday': '12-24'},{'Name': 'Jenni', 'Bday': '05-05'},
        {'Name': 'Kyle', 'Bday': '05-01'},{'Name': 'Dan', 'Bday': '08-12'}, {'Name': 'Noah', 'Bday': '11-13'},{'Name': 'Bill', 'Bday': '05-07'}]
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
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # honk
        if message.author != self.user:
            if 'honk' in message.content:
                await message.channel.send('honk')
            if 'kyle' in message.content:
                await message.channel.send('kyle')
            if message.content == 'BDAY' and bdayPerson == 'nobody':
                response = ('it aint nobodys bday bitch')
                await message.channel.send(response)
            elif message.content == 'BDAY' and bdayPerson != 'nobody':
                response = ('HAPPY BDAY TO ' + bdayPerson + '!!!!!!!!  buy them shit')
                await message.channel.send(response)
            if message.content == 'NEXT BDAY':
                response = ('The next goose bday is ' + nextPerson + '\'s on ' + nextBday + '!!!!!!!!!!!!!!!!!!  Get hype bout it')
                await message.channel.send(response)
            if message.content == 'hey hypebot'or message.content == 'HEY HYPEBOT':
                response = ('hey')
                await message.channel.send(response)
client = Client()
client.run(token)
