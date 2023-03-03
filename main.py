# Quiz Time generates a quiz for the user and keeps track of correct and incorrect answers

# Display title and game rules

print(r"""
                                                                    ,----,                                   ,---,  
                                                                  ,/   .`|                                ,`--.' |  
    ,----..                                                     ,`   .'  :                  ____          |   :  :  
   /   /   \                    ,--,                          ;    ;     / ,--,           ,'  , `.        '   '  ;  
  /   .     :            ,--, ,--.'|          ,----,        .'___,/    ,',--.'|        ,-+-,.' _ |        |   |  |  
 .   /   ;.  \         ,'_ /| |  |,         .'   .`|        |    :     | |  |,      ,-+-. ;   , ||        '   :  ;  
.   ;   /  ` ;    .--. |  | : `--'_      .'   .'  .'        ;    |.';  ; `--'_     ,--.'|'   |  || ,---.  |   |  '  
;   |  ; \ ; |  ,'_ /| :  . | ,' ,'|   ,---, '   ./         `----'  |  | ,' ,'|   |   |  ,', |  |,/     \ '   :  |  
|   :  | ; | '  |  ' | |  . . '  | |   ;   | .'  /              '   :  ; '  | |   |   | /  | |--'/    /  |;   |  ;  
.   |  ' ' ' :  |  | ' |  | | |  | :   `---' /  ;--,            |   |  ' |  | :   |   : |  | ,  .    ' / |`---'. |  
'   ;  \; /  |  :  | : ;  ; | '  : |__   /  /  / .`|            '   :  | '  : |__ |   : |  |/   '   ;   /| `--..`;  
 \   \  ',  . \ '  :  `--'   \|  | '.'|./__;     .'             ;   |.'  |  | '.'||   | |`-'    '   |  / |.--,_     
  ;   :      ; |:  ,      .-./;  :    ;;   |  .'                '---'    ;  :    ;|   ;/        |   :    ||    |`.  
   \   \ .'`--"  `--`----'    |  ,   / `---'                             |  ,   / '---'          \   \  / `-- -`, ; 
    `---`                      ---`-'                                     ---`-'                  `----'    '---`"  
                       

""")

print("Welcome to Quiz Time! You will answer several True or False questions. Please ONLY enter the letter T or F when it's your turn to answer. Have fun!")

# Create tuples for questions and answers
questions = ("Q1. There are only 40 states in USA", "Q2. The White House is located in Columbia, Maryland", "Q3. The golden gate bridge in California is made of real gold", "Q4. We have only had 30 US presidents", "Q5. Post high-school education is free for everyone is USA")
answers = ('F', 'F', 'F', 'F', 'F')

# Create variable for number of correct answers
correct = 0

# Set variable for length of questions tuple
numOfQuestions = len(questions)

# Display questions
for index in range(numOfQuestions):
  print(questions[index])

# Display prompt for user's answer
  answer = input("Please enter 'T' for True or 'F' for False: ")

# Increment counter if answer is correct
  if (answer == answers[index]):
    correct += 1
    
# Display final message to state how many questions were answered correctly
print(f"You got {correct} out of {numOfQuestions} correct! Thanks for playing!")