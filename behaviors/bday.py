import discord
from datetime import datetime
import time
from operator import itemgetter

class Bday:
    bdays = [{'Name': 'Nate', 'Bday': '04-01'},
        {'Name': 'Bobby G', 'Bday': '08-14'},
        {'Name': 'Kelly', 'Bday': '02-18'},
        {'Name': 'Jake Medina', 'Bday': '12-12'},
        {'Name': 'Kaleb', 'Bday': '12-24'},
        {'Name': 'Jenni', 'Bday': '05-05'},
        {'Name': 'Kyle', 'Bday': '05-01'},
        {'Name': 'Dan', 'Bday': '08-12'},
        {'Name': 'Noah', 'Bday': '11-13'},
        {'Name': 'Bill', 'Bday': '05-07'},
        {'Name': 'Zack', 'Bday': '01-01'},
        {'Name': 'John', 'Bday': '01-01'},
        {'Name': 'Erin', 'Bday': '09-20'},]    

    def build_date_dict(self, bdays):
        dict = []
        for i in range(len(bdays)):
            dict.append(bdays[i]['Bday'])
        dict.sort()
        return dict

    def get_response(self, msgContent):
        today = datetime.today()
        today = today.strftime('%m-%d')
        if msgContent == '!bday':
            return self.get_current_bday_response(self.bdays, today)
        elif msgContent == '!bday next':
            return self.get_nxt_bday_response(self.bdays, today)
        else:
            return False
    
    def get_current_bday_response(self, data, today):
        currentBdayObj = next((x for x in self.bdays if x['Bday'] == today), None)
        bdayPerson = currentBdayObj['Name'] if currentBdayObj else 'nobody'
        return 'it aint nobodys bday bitch' if bdayPerson == 'nobody' else f'HAPPY BDAY TO {bdayPerson}!!!!!!!! buy them shit'

    def get_nxt_bday_response(self, data, today):
        dateDict = self.build_date_dict(self.bdays)
        nextBday = next((x for x in dateDict if x > today))
        nextPerson = itemgetter('Name')(next((x for x in self.bdays if x['Bday'] == nextBday)))
        return f'The next goose bday is {nextPerson}\'s on {nextBday}!!!!!!!!!!!!!!!!!! Get hype bout it'

    async def send_bday(self, message, msgContent):
        response = self.get_response(msgContent)
        if response:
            await message.channel.send(response)



