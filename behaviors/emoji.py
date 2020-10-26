import discord

class Emoji:
    emojis = [{'name': 'repicy', 'code': 'a:repicy:644999601270685707', 'response': 'rEpIcY!'},
        {'name': 'cringe', 'code': 'kershrek:768886281773383762', 'response': 'cringe bro'},
        {'name': 'smh', 'code': 'smhmyhead:651848089224609793', 'response': 'my head'},
        {'name': 'nate', 'code': 'yetinate:520637149566205964', 'response': 'schweeeee'},
        {'name': 'fuck yeah', 'code': ':thicc:438569502637293568', 'response': 'hnnnnn'},
        {'name': 'bill', 'code': ':bill:378712561832689674', 'response': '#1 Power-Bottom in TX'},
        {'name': 'michael', 'code': ':mike:768901680787488810', 'response': 'michael'},
        {'name': 'goose', 'code': ':goosechamp:551145779834781737', 'response': 'honk'},
        {'name': 'kyle', 'code': 'SexyKyle:388117155176120320', 'response': 'kyle'},]

    def get_emoji(self, message):
        emojiData = next((x for x in self.emojis if x['name'] == message), None)
        return emojiData

    async def send_emoji(self, message):
        emoji = self.get_emoji(message)
        if emoji:
            await message.channel.send(emoji['response'])
            await message.add_reaction(emoji['code'])
