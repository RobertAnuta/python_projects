# Structure quiz logic

class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question['text']} (True/False): ").lower()
        self.check_answer(user_answer, current_question)

    def check_answer(self, user_answer, current_q):
        if user_answer == current_q["answer"].lower():
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_q['answer']}")
            print(f"Your score is: {self.score}/{self.question_no}")
            print("\n")
        else:
            print("That's wrong!")
            print(f"The correct answer was: {current_q['answer']}")
            print(f"Your score is: {self.score}/{self.question_no}")
            print("\n")
