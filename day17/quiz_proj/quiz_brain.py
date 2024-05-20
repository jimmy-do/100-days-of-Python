class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number - len(self.question_list)

    def question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}:{current_question.text} (True or False)?: ').title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print('Correct!')
        else:
            print('Incorrect')
        print(f'The correct answer was: {correct_ans}')
        print(f'Your score is {self.score}/{self.question_number}')

