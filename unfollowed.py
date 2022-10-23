from instabot import Bot

usernames = []

bot = Bot() 
bot.login(username="BURNER USERNAME",password="BURNER PASSWORD")

followers = bot.get_user_followers("YOUR USERNAME")
following = bot.get_user_following("YOUR USERNAME")

difference = [x for x in following if x not in followers]

for id in difference:
    usernames.append(bot.get_username_from_user_id(id))
    
print(usernames)
