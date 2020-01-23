# Importing Required Packages
import time

# Defining the Response function
def bot_response(user_response):
    return "BOT: You said "+user_response

# Initiating the Chat
user_response = str()
print("Hi. This is a simple reflexive chat-bot")
while(user_response!="bye"):
    print()
    time.sleep(0.2)
    user_response = input("YOU: ")
    user_response = user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            time.sleep(0.2)
            print("BOT: You are welcome..")
        else:
            time.sleep(0.2)
            print(bot_response(user_response))
    else:
        time.sleep(0.2)
        print("BOT: Bye! take care..")
