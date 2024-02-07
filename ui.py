THEME_COLOR = "#375362"
from tkinter import *
# from quiz_brain import next_question

class Ui:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.score = 0


        self.window = Tk()

        self.window.title("Who wants to be a Millionaire")
        self.window.minsize(width=300, height=500)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f"Score: {self.score}", fg="white")
        self.score_text.config(bg=THEME_COLOR, font=("Montserrat", 12, "normal"))
        self.score_text.grid(column=1, row=0)
        self.canvas=Canvas(width = 300, height=250, bg="white")
        self.questions_text = self.canvas.create_text(150, 125, text="Questions", font=("Montserat", 12, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        self.f_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.f_img, command=self.false_click)
        self.false_button.grid(column=0, row = 3)

        self.t_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.t_img, command=self.right_click)
        self.true_button.grid(column=1, row = 3)
        self.next_quest()


        self.window.mainloop()

    def next_quest(self):
        self.canvas.config(bg="white")
        self.quiz.next_question()
        self.canvas.itemconfig(self.questions_text, text=self.quiz.next_question())

    def right_click(self):
        check = self.quiz.check_answer("True")
        self.give_feedback(check)
        # if self.quiz.question_number > 10:
        #     self.true_button.disable()




    def false_click(self):
        check = self.quiz.check_answer("False")
        self.give_feedback(check)


    def give_feedback(self, check):
        if check:
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_quest)


#
# class Ui():
#     def __init__(self, question):
#         super().__init__()
#         self.window = Tk()
#         self.window.minsize(width=400, height=500)
#         self.window.title("Who wants to be a Millionaire")
#         self.window.config(padx=20, pady=20)
#
#
#
#     def click_right(self):
#         canvas = Canvas()
#         canvas.pack()
#         Image = PhotoImage(file="./images/false.png")
#         canvas.config(bg="grey")
#         button = Button(image=self.Image, command=click_right)
#         button.pack()
#         self.canvas.create_text(200, 150, text=question, fill="white")
#         return False
#
#     def click_right(self):
#         return False
#
#
#
#
