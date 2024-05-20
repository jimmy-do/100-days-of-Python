from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item["question"]
    answer = item["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# if quiz still has questions remaining:

while quiz.still_has_questions:
    if not quiz.still_has_questions():
        print('You\'ve completed the quiz')
        print(f'Your final score was {quiz.score}/{quiz.question_number})')
        break
    quiz.question()
