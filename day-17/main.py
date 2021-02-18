from question_model import Question
from question_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_q = Question(question_text,question_answer)
    question_bank.append(new_q)

start_quiz = QuizBrain(question_bank)

while start_quiz.still_questions():
    answer = start_quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {start_quiz.final_score()}")