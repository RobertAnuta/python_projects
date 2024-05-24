from quiz_brain import QuizBrain
from data import question_data

question = QuizBrain(question_data)

while question.still_has_questions():
    question.next_question()
    if question.still_has_questions() == False:
        print(f'Greate job you scored {question.score} out of {len(question_data)}')