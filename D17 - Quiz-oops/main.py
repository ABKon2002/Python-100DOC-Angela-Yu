from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    currQn = Question(question['text'], question['answer'])
    question_bank.append(currQn)

qBrain = QuizBrain(question_bank)

score = 0
while qBrain.still_got_questions():
    print('\n-----------------------------------------------------------\n')
    print(f"Current Score: {score}")
    print()
    score += qBrain.next_question()
    print('\n-----------------------------------------------------------\n')

print(f"You got {score} questions right. Thank you for playing :)")
