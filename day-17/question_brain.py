class QuizBrain:
    
    def __init__(self, q_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = q_bank

    def still_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1} {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(answer,current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right! ")
        else:
            print("You are wrong! ")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        return f"{self.score}/{self.question_number}"
