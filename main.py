import pyautogui as pt
from time import sleep
import pyperclip
import random
# import mouseinfo

sleep(4)

position1 = pt.locateOnScreen("Whatsapp\smiley_paperclip.PNG" , confidence = .6) # recongnizable as the picture with 60% chance
# x = position1[0]
# y = position1[1]

# function that gets message
def get_message():
    global x, y


    pyperclip.copy('')
    postion = pt.locateOnScreen("Whatsapp\smiley_paperclip.PNG" , confidence = .6) # recongnizable as 60% chance
    # x = postion[0]
    # y = postion[1]
    pt.moveTo( postion[0] , postion[1] , duration= 0.5)
    pt.moveTo( postion[0] + 90 , postion[1] - 40, duration= 0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12 , 15)
    pt.click()
    # just trying to copy the message from Whatsapp
    # pyperclip.copy()
    whatsapp_message = pyperclip.paste()
    message = pyperclip.copy('')

    # pasting from clipboard 
    pt.click()

    print("Message received: " + whatsapp_message)

    return whatsapp_message

    


def post_response(message):
    global x, y

    postion = pt.locateOnScreen("Whatsapp\smiley_paperclip.PNG" , confidence = .6) # recongnizable as 60% chance
    # x = postion[0]
    # y = postion[1]
    pt.moveTo( postion[0] + 250 , postion[1] + 30 , duration= 0.5) #it will drag the cursor from smiley-paperclip to "Type a message" box in Whatasapp
    pt.click()
    pt.typewrite(message , interval= .01) # typewrite will insert the message, letter interval 10%

    # pt.typewrite(" \n", interval= .01)  # "\n" pressing Enter, i.e sends the message



#processes response __
def process_response(message):
    random_no = random.randrange(6)

    # elif "Assalamualaikum" or "Assalamu Alaikum" in str(message).lower():
    #     return "Wa Alaikumus Salam Wa Rahmatullah."
    if "?" in str(message).lower():
    #    return "I can't answer that now. I will tell you later."
    elif "Okk" in str(message).lower():
         return "My pleasure."
    # elif "Thank you" or "Thanks" in str(message).lower():
    #     return "My pleasure. You're Welcome."
    
    else:
        if random_no == 0:
            return "That's allright. I hear you!"
        elif random_no == 1:
            return "Tell me more. What else do you know about it?"
        elif random_no == 2:
            return "Don't Tell me a word about this again! "    
        elif random_no == 3:
            return "Someone's at the door. Please hold on."
        elif random_no == 4:
            return "It's almost Prayer time, I gotta go. I will catch up on you later!"
        elif random_no == 5:
            return "I'm listening. And then?"
        else:
            return "I Understand."

    
        

# Check for new messages

def check_for_new_messages():
    pt.moveTo( 510 , 715 , duration= .5)

    while True: 
        try:
            position = pt.locateOnScreen("Whatsapp\Green_dot.PNG" , confidence = .8) # recongnizable as 80% chance
            
            if position == pt.pixelMatchesColor(482,248, (0,168,132), tolerance = 10) or pt.pixelMatchesColor(482,320, (0,168,132), tolerance = 10) or pt.pixelMatchesColor(505,392, (0,168,132), tolerance = 10): # If there is Green dot,
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)  # Now we are in the chat with the user with New message
            else:
                print("No New Messages Yet...")
                

        except(Exception):
            print("No other user with new message located")

        pt.moveTo( 476 , 647 , duration= .5)
        if pt.pixelMatchesColor(595 , 643, (32,44,51), tolerance = 10) or pt.pixelMatchesColor(595 , 643, (255,255,255) , tolerance = 10): # int(position1[0] + 90) , int(position1[1] - 22) which is white
            print("Is Dark Blue")
            # we got new message
            post_response(process_response(get_message()))

        else:
            print("No New Messages Yet...")

    
        

        
        
        
        
        
        sleep(7) # i.e the program will check for new messages every 7 sec

# post_response(process_response(get_message()))
# mouseinfo.MouseInfoWindow()
    # elif "?" in str(message).lower():
    #     return "I can't answer that now. I will tell you later."
    # elif "Congratulations" or "Congratulation" or "Congrats" or "Happy Birth Day" or "Jonomdin er shuveccha" or "Jonmodin er shuveccha" or "shuveccha" or "shuvecca" in str(message).lower():
    #     return "Thanks A Lot!"
    # elif "Allah Hafez" or "Allah Hafiz" or "Allah Hafij" or "Allah Hafej" or "Valo theko" or "Bye" or "dkha hbe" or "dekha hobe" in str(message).lower():
    #     return "Allah Hafez. Allah Sobaike nirapode rakhuK"
    # elif "Kemon acho" or "Achis kemn" or "Achis kemon" or "Shorir valo" or "Shorir kemon" in str(message).lower():
    #     return "ALhamdulillah. Ami toh valo achi. Tomar ki Obostha?"
    # elif "Basar sobai kemon" or "Uncle Aunty kemon" or "Tomar Abba Amma kemon" in str(message).lower():
    #     return "Abba Amma ache Valo,ALhamdulillah. Tomar ?"

check_for_new_messages()





