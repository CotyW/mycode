import random

#Answers variables for winning
correct_answers = 0
win_threshold = 9
response_streak = 0

#Random responses
responses = [
        "\nNice shot!  Ball in the hoop. \n",
        "\nBuckets! Good answer.\n",
        ]
responses_fire = "He's on fire!\n"
        

#List of HOFers
hall_of_famers = [
    {"name": "Michael Jordan", "induction_year": 2009},
    {"name": "Magic Johnson", "induction_year": 2002},
    {"name": "Larry Bird", "induction_year": 1998},
    {"name": "Kareem Abdul-Jabbar", "induction_year": 1995},
    {"name": "Bill Russell", "induction_year": 1975},
    {"name": "Wilt Chamberlain", "induction_year": 1979},
    {"name": "Shaquille O'Neal", "induction_year": 2016},
    {"name": "Hakeem Olajuwon", "induction_year": 2008},
    {"name": "Scottie Pippen", "induction_year": 2010},
    {"name": "Charles Barkley", "induction_year": 2006}
]

#Quiz Time
def quiz(hall_of_famers):
    questions = []
    for player in hall_of_famers:
        question = {
            "question": f"In which year was {player['name']} inducted into the NBA Hall of Fame?",
            "answer": player['induction_year']
        }
        questions.append(question)
        if len(questions) >= 10:
            break
    return questions

# Generate the questions
questions = quiz(hall_of_famers)

# Display the quiz
for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    
    attempts = 0
    while attempts < 3:
        user_answer = input("Your answer (type the year): ").strip()
        try:
            if int(user_answer) == q['answer']:
                print(random.choice(responses))
                correct_answers += 1
                response_streak +=1
                if response_streak >=3:
                    print(responses_fire)
                break
            else:
                attempts += 1
                correct_streak = 0
                if attempts < 3:
                    print(f"Tough luck on that one. You missed the shot and rebound.  You have {3 - attempts} attempt(s) left.")
                else:
                    correct_streak = 0
                    print(f"Wrong. The correct answer is {q['answer']}.\n")
        except ValueError:
            print("Please enter a valid year.")
            attempts += 1
            if attempts < 3:
                print(f"You have {3 - attempts} attempt(s) left.")
#Win condition

if correct_answers >= win_threshold:
    print(f"Congratulations!  You've won a GOLD medal! You had a total of {correct_answers} correct answers!")
else:
    print(f"Sorry, you failed to make enough shots. You only answered {correct_answers} questions correctly")


