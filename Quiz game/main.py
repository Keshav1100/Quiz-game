import question
import random
print("--------------WELCOME TO THE QUIZ MASTERS-----------\n-------------------------------------------------------\nRules:\n1.You will be asked to choose a category from which you would be asked questions.\n2.+1 score for every right answer and 0 for every wrong answer.\n3.Kindly enter the your option choices in correct manner. Any invalid option will be considered wrong.\n🎮🎯Enjoy the game🎯🎮")
print("--------------------------------------------------")
category = ""
score = 0
def user_playChoice():
#to ask user if it wants to play after playing in any category
    user_play = input("Enter Y to play more and N to exit: ")
    if user_play.lower() == "y":
        choice()
    else:
        score_show()
        print("Thanks for playing. Have a nice day.")
        n = input("press any key to exit.")
def choice():
# to ask user which category he wants to play in 
    global category
    user_choice = int(input("Please select your questions category\n1.Technology\n2.Current Affairs\n3.Economics/Finance\n4.Entertainment\n5.Sports\n->"))
    if user_choice == 1:
        category = "Tech"
        print("--------------------------------")
        game(category)
    elif user_choice == 2:
        category = "CurrentAffairs"
        print("--------------------------------")
        game(category)
    elif user_choice == 3:
        category = "EcoFin"
        print("--------------------------------")
        game(category)
    elif user_choice == 4:
        category = "Entertainment"
        print("--------------------------------")
        game(category)
    elif user_choice == 5:
        category = "Sports"
        print("--------------------------------")
        game(category)
    else:
        print("PLEASE ENTER CORRECT CHOICE")
        choice()

def game(ques_category):
# to start the game after getting the desired category from the user
    global score
    q_category = question.dic[ques_category]
    ques_no_list = []
    for i in range(1,len(q_category["questions"])+1):
        ques_no_list.append(i)
    random.shuffle(ques_no_list)   
    for x in ques_no_list:
        ques = q_category["questions"][f"{x}"]
        options = q_category["options"][f"{x}"]
        ans = q_category["ans"][f"{x}"]
        print(f"Q. {ques}")
        print(f"{options}")
        choice = input("Enter your choice (A,B,C,D): ")
        if choice.lower() == ans:
            print("Correct")
            score+=1
        else:
            print("Incorrect")
            print(f"Correct answer: option {ans.upper()}")
        print("------------------------------------------")
    user_playChoice()
# choice()
def score_show():
# to show the score to the user in the end
    global score
    print(f"Your total score : {score}")
    with open("highScore.txt","r") as f:
        data = f.read()
        if data < str(score):
            print("Congratulations! You broke the last record.")
            print(f"Last high score : {data}")
            with open("highScore.txt","w") as f:
                f.write(f"{score}")
            
        elif data > str(score):
            print("Sorry! you couldn't break the last record.")
            print(f"Last high score : {data}")
        else:
            print(f"Last high score : {data}")
choice()