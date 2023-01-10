from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data = "https://opentdb.com/api.php?amount=20&category=18&difficulty=easy&type=boolean"
print(data)

question_bank = []
for qus in question_data:
    question_text = qus['text']
    question_answer = qus['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the quiz")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}")