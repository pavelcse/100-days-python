class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, currect_answer):
        if user_answer.lower() == currect_answer.lower():
            self.score += 1
            print("Your got the right answer.")
        else:
            print("That's wrong!")

        print(f"The currect answer was : {currect_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
