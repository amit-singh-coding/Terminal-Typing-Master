import os
import json
import time
import random

class color_the_line:
    bg_WHITE = '\033[48;5;15m'
    bg_GREEN = '\033[48;5;32m'
    bg_RED = '\033[48;5;196m'
    bg_GG = '\033[48;5;46m'
    bg_SKY_BLUE = '\033[48;5;39m'
    END = '\033[0m'  # Reset background color to default

    li_WHITE = '\033[38;5;15m'  
    li_GREEN = '\033[38;5;32m'   
    li_light_g = '\033[38;5;46m'     
    li_SKY_BLUE = '\033[38;5;39m'  
    li_RED = '\033[38;5;196m'   
    li_YELLOW = '\033[38;5;226m'  
    END = '\033[0m'  # Reset color to default


def create_directory():
    if not os.path.exists("typing_master"):
        os.makedirs("typing_master")

def create_username():
    text1 = f"{color_the_line.li_GREEN} {'Enter your username:'} {color_the_line.END}"
    username = input(text1)
    return username

def validate_user(username): #True if the file exists and False otherwise.
    leaderboard_file_path = "typing_master/leaderboard.json"
    if os.path.exists(leaderboard_file_path) and os.path.getsize(leaderboard_file_path) > 0:
        with open(leaderboard_file_path, "r") as leaderboard_file:
            leaderboard = json.load(leaderboard_file)
            for user, data in sorted(leaderboard.items(), key=lambda x: x[1]["WPM"], reverse=True):
                if user == username:
                    return True
    return False            
                

def update_leaderboard(username, wpm):
    leaderboard_file_path = "typing_master/leaderboard.json"
    leaderboard = {}

    if os.path.exists(leaderboard_file_path) and os.path.getsize(leaderboard_file_path) > 0:
        with open(leaderboard_file_path, "r") as leaderboard_file:
            leaderboard = json.load(leaderboard_file)

    leaderboard[username] = {"WPM": wpm, "Timestamp": time.time()}

    with open(leaderboard_file_path, "w") as leaderboard_file:
        json.dump(leaderboard, leaderboard_file, indent=2)

def show_leaderboard():
    leaderboard_file_path = "typing_master/leaderboard.json"

    if os.path.exists(leaderboard_file_path) and os.path.getsize(leaderboard_file_path) > 0:
        with open(leaderboard_file_path, "r") as leaderboard_file:
            leaderboard = json.load(leaderboard_file)

            t4 = f"{color_the_line.bg_RED} {'Leaderboard:'} {color_the_line.END}"
            print(t4)
            count=0
            for user, data in sorted(leaderboard.items(), key=lambda x: x[1]["WPM"], reverse=True):
                count+=1
                user_data = f'''---------------------------------------------------------------
{count} {user}: {data['WPM']} WPM'''
                t4 = f"{color_the_line.li_light_g} {user_data} {color_the_line.END}"
                print(t4)
            print()  
            print()  
    else:
        t14 = f"{color_the_line.li_RED} {'Leaderboard is empty.'} {color_the_line.END}"
        print(t14)
def generate_random_sentence():
    sentence_length = random.randint(5, 15)
    words = ["apple", "banana", "cherry", "dog", "elephant", "fox", "grape", "house", "igloo", "jazz", "kangaroo", "lemon", "monkey", "notebook", "orange", "penguin", "quilt", "rainbow", "sunshine", "turtle", "umbrella", "violin", "waterfall", "xylophone", "zebra"]
    random_sentence = " ".join(random.sample(words, sentence_length))
    return random_sentence.capitalize() + "."

def start_typing_test():
    random_sentence = generate_random_sentence()
    t5 = f"{color_the_line.li_YELLOW} {'Type the following sentence:👇👇'} {color_the_line.END}"
    print(t5)
    t11 = f"{color_the_line.bg_GREEN} {random_sentence} {color_the_line.END}"
    print(t11)

    t13 = f"{color_the_line.li_RED} {'Press Enter when you are ready...'} {color_the_line.END}"
    input(t13)
    print()

    start_time = time.time()

    t12 = f"{color_the_line.bg_RED} {'Start typing->'} {color_the_line.END}"
    user_input = input(t12)

    end_time = time.time()

    words_typed = user_input.split()
    randem_words = random_sentence.split()
    wpm = measure_wpm(start_time, end_time, words_typed, randem_words)
    def user_score_in_colour(datax1, datax2, datax3):
        x1 = f"{color_the_line.li_light_g} {datax1} {color_the_line.END}"
        data2 = f"{datax2} {datax3}"
        x2 = f"{color_the_line.li_RED} {data2} {color_the_line.END}"
        print(x1,x2)

    user_score_in_colour('Your typing speed:', wpm[0],'WPM')
    user_score_in_colour('total time taken:', wpm[1],'Minutes')
    user_score_in_colour('Total currect words:', wpm[2],'..')
    user_score_in_colour('Total wrong words: ', wpm[3],'..')
    return wpm   

def measure_wpm(start_time, end_time, words_typed, randem_words):
    c_w=0
    w_w=0
    for words in words_typed:
        if words in randem_words:
            c_w+=1
        else:
            w_w+=1    
    minutes_elapsed = (end_time - start_time) / 60
    wpm = c_w / minutes_elapsed
    lis = [round(wpm, 2), round(minutes_elapsed, 2),round(c_w, 2),round(w_w, 2)]
    return lis

def main():
    create_directory()
    title = """
 ===============================================================
||               ⌨   Welcome to Typing Master  ⌨               ||
 ==============================================================="""
    t2 = f"{color_the_line.li_RED} {title} {color_the_line.END}"
    print(t2)
    while True:
        options = '''_________________________
        | Options:                  |
        | 1. Start Typing Test      |
        | 2. Create Username        |
        | 3. Show Leaderboard       |
        | 4. Exit                   |
        | Enter option (1/2/3/4):--> '''
        t3 = f"{color_the_line.li_YELLOW} {options} {color_the_line.END}"
        option = input(t3)
        print()
        if option == "1": #Start Typing Test----------------------++++++++|
            if not os.path.exists("typing_master/leaderboard.json"):
                open("typing_master/leaderboard.json", "w").close()

            username = create_username()

            if validate_user(username):
                welcome = f"   Welcome back ->"
                to_user = f"  {username}🧒"
                t6 = f"{color_the_line.bg_RED} {welcome} {color_the_line.END}"
                t7 = f"{color_the_line.li_light_g} {to_user} {color_the_line.END}"
                print(t6,t7)

            else:
                welcome = f"New user ->"
                to_user = f"{username}🧒"
                t6 = f"{color_the_line.bg_RED} {welcome} {color_the_line.END}"
                t7 = f"{color_the_line.li_light_g} {to_user} {color_the_line.END}"
                print(t6,t7)

            wpm = start_typing_test()
            update_leaderboard(username, wpm[0])

        elif option == "2": #create_username-----------------------++++++|
            username = create_username()
            result = validate_user(username)
            if result == False:
                update_leaderboard(username, 00)
                new_user=f"Username '{username}' created successfully!🧑"
                t10 = f"{color_the_line.li_light_g} {new_user} {color_the_line.END}"
                print(t10)
            else:
                new_user=f"Username '{username}' Already exist in our database!🧑"
                t10 = f"{color_the_line.li_light_g} {new_user} {color_the_line.END}"
                print(t10)    

        elif option == "3": #show_leaderboard-----------------------+++++|
            show_leaderboard()

        elif option == "4":
            t6 = f"{color_the_line.bg_WHITE} {'Exiting program. Goodbye!👋'} {color_the_line.END}"
            print(t6)
            break

        else:
            data2="Invalid option. Please choose 1, 2, 3, or 4.🥴"
            t7 = f"{color_the_line.bg_RED} {data2} {color_the_line.END}"
            print(t7)            

if __name__ == "__main__":
    main()
