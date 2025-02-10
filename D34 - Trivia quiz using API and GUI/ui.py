from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, qBrain : QuizBrain):      # The variable qBrain can now only be a QuizBrain object as we declared it using ':'
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = qBrain

        self.score_label = Label(text="Score: 0", fg="black", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="D34 - Trivia quiz using API and GUI//images//true.png")
        wrong_image = PhotoImage(file="D34 - Trivia quiz using API and GUI//images//false.png")
        self.correct_button = Button(image=correct_image, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()  
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(3000, self.get_next_question)

        self.correct_button.config(state="normal")
        self.wrong_button.config(state="normal")

        self.score_label.config(text=f"Score: {self.quiz.score}")

        self.canvas.itemconfig(self.question_text, text=self.quiz.current_question.text)