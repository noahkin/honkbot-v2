from freebible import read_web
import random

class Scripture:
    def get_verse(self, msgContent):
        if msgContent == '^preach':
            return self.get_random_verse()

    def get_random_verse(self):
        bible = read_web()
        book = random.choice(bible.books)
        bookLength = len(book)
        chapter = book[random.randint(1, bookLength)]
        chapterLength = len(chapter)
        verse = chapter[random.randint(1, chapterLength)]

        return verse

    async def send_verse(self, message, msgContent):
        response = self.get_verse(msgContent)
        if response:
            await message.channel.send(response)