
class QuizBrain:
    def __init__(self, question_list) -> None:
        self.qNo = 0
        self.qList = question_list
        self.score = 0
    
    def still_got_questions(self):
        return self.qNo < len(self.qList)

    def next_question(self):
        self.qNo += 1
        qNo = self.qNo
        question = self.qList[qNo - 1]
        usr_input = input(f"Q{qNo}. {question.question} (True[T] or False[F])?: ").capitalize()
        if usr_input == 'T':
            usr_input = 'True'
        elif usr_input == 'F':
            usr_input = 'False'
        
        if usr_input == question.answer:
            self.score += 1
            return 1
        print("You got it wrong.")
        return 0