import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

#Set the variables for Q+A
question = trivia["question"]
correct = trivia["correct_answer"]
incorrect = trivia["incorrect_answers"]


#combine answers
answers = incorrect + correct

#display Q+A
print(f"Question: {question}")
for idx, answer in enumerate(answers, start=1):
    print(f"{idx}. {answer}")

#get the input
userinput = input("Your answer (enter the number): ")


# check the answer




