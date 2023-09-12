
print("Welcome to the Quiz Game!")
print("Rules:")
print("1. Answer each question with the corresponding number.")
print("2. Each correct answer earns you 1 point.")
print("3. Let's begin!")

score = 0
name = input("Enter your full name to play this game : ")
user = input(f"{name}DO YOU WANT TPLAY QUIZ GAME ??:")
if (user== 'YES'):
    print(f"WELCOME {user}\nLET'S PLAY !!")
    print("1. What is the capital of India ?\n")
    ans = input*("""Choose your Answer:
            1. Delhi
            2. Kanpur
            3. Mumbai
            4. Jaipur              """)
    if ans == 'Delhi':
        print("Delhi is a Correct Answer   !")
        score = score+1
    else:
        print("You choise Incorrect! Answer, The correct answer is Delhi ! ")

    print("1.What is the largest mammal in the world?\n")
    ans = input*("""Choose your Answer:
            1.  Elephant
            2.  Giraffe
            3.  Blue Whale
            4.  Polar Bear            """)
    if ans == 'Blue whale':
        print("Blue Whale is a Correct Answer   !")
        score = score+1
    else:
        print("You choise Incorrect! Answer, The correct answer is Blue Whale ! ") 

    print("1.Which planet is known as the Red Planet?\n")
    ans = input*("""Choose your Answer:
            1.  Venus
            2.  Jupiter
            3.   Mars
            4.  Saturn           """)
    if ans == 'Mars':
        print("Marsis a Correct Answer   !")
        score = score+1
    else:
        print("You choise Incorrect! Answer, The correct answer is Mars! ")  
        print(f"Quiz completed! Your score is: {score}")
    if score == 3:
        print("Congratulations! You got a perfect score!")
    elif score >=  2:
        print("Well done! You did a good job.")
    else:
     print("Keep practicing. You can do better next time.")   

else:
    print("Thanks you Vist again")

    
