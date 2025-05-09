from html import unescape

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = unescape(self.current_question.text)
        return f"Q.{self.question_number}: {self.current_question.text} (True(T)/False(F)): "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == 't': 
            user_answer = 'True'
        elif user_answer.lower() == 'f':
            user_answer = 'False'
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return True
        else:
            print("That's wrong.")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return False
