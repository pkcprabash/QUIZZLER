from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_STYLE = ("Arial",20,"italic")

class QuizBoard():

    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)

        self.score = Label(text = "Score:0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions = self.canvas.create_text(150,125,text="Hello", font=FONT_STYLE, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        wrong = PhotoImage(file="images/false.png")
        right = PhotoImage(file="images/true.png")
        self.wrong_button = Button(image=wrong, highlightthickness=0, command=self.wrong_question)
        self.wrong_button.grid(row=2,column=0)
        self.right_button = Button(image=right, highlightthickness=0, command=self.right_question)
        self.right_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()


    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text=ques)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.questions, text=f"Score: {self.quiz.score}")
            self.wrong_button.config(state="disable")
            self.right_button.config(state="disable")



    def right_question(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)


    def wrong_question(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)


    def give_feedback(self,answer):
        if answer==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)


