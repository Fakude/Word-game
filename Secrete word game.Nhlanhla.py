
Hiddeneword = "speed"
lives = 5

Template = "_"*5
print("Let's start you have 5 lives.")

while lives > 0:
    playerinput = input("Guess: ")
    print("-"*25)
    
    if len(playerinput) != 5:
        print("Only five word letters are allowed")
        continue
    
    playeranswer = ""

    for i in range(5):
        if playerinput[i] == Hiddeneword[i]:
            playeranswer += playerinput[i]
        else:
            playeranswer += Template[i]
    lives -= 1
    print("Words that match the secrete word:",playeranswer)
    
    if playeranswer == Hiddeneword:
        print(playeranswer,"Is correct answer!!")
        print("Nice job you got the word ;)")
        break 
    
    if lives ==1:
     print("only 1 life remains")

if playeranswer != Hiddeneword:
    print("My secrete word is ",Hiddeneword,"\nYour lives are finished  :( .... better luck next time.)")
