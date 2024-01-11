from time import *
import keyboard
import random

def leaderboard(user_error, time1, time2, user_sen):
    time_diff = time2 - time1
    round_of_time = round(time_diff, 2) 
    time_taken = len(user_sen) / round_of_time
    #x=time_taken * 0.0166667--> for  wpm
    final_time = round(time_taken, 2)
    print("W.P.S->", final_time)
    print("User Error->", user_error)

def final_result(rendom_sen):
    print("<-------------Type this sentence----------->")
    print(rendom_sen)
    time1 = time()
    user_sen = input("""
                     Type here : """)
    time2 = time()
    user_error = 0
    for i in range(len(rendom_sen)):
        try:
            if rendom_sen[i] != user_sen[i]:
                user_error += 1                       
        except:            
            user_error += 1 
    return leaderboard(user_error, time1, time2, user_sen) 

while True:
    if keyboard.is_pressed('ctrl+q'):
        print("Thank you for using T.T.M. Exiting...")
        break

    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python programming language is widely used for web development.",
        "A journey of a thousand miles begins with a single step.",
        "The sunsets in the west, painting the sky with vibrant hues.",
        "Innovation distinguishes between a leader and a follower.",
        "Coding is the language of the future; embrace it and excel.",
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "The universe is under no obligation to make sense to you.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Every problem is an opportunity in disguise."
    ]

    print("<-------------Terminal Typing Master----------------->")
    user_input = int(input("""
    1. Start the typing test
    2. Exit T.T.M : """))

    random_sentence = random.choice(sentences)

    if user_input == 1:
        final_result(random_sentence)
    else:
        print("Thank you for using T.T.M. Exiting...")
        break
