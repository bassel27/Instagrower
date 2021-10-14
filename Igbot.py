from instabot import Bot
class Igbot:
    def __init__(self):
        self.bot = Bot()

    def login(self, valueInside):
        if valueInside == 'longlivebassel':
            self.bot.login(username = 'longlivebassel', password = '3nd13$$10v3', ask_for_code=True)
        elif valueInside == 'fake_account':
            self.bot.login(username = 'aksjdfkafjoi', password = '3nd13$$10v3')
            #self.bot.login(username = 'retro_codger', password = 'Bassel27', ask_for_code=True)

    def uploadPhoto (self, imgPath, captionText):
        self.bot.upload_photo(imgPath, caption = captionText)
        
        