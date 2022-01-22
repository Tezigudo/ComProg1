class Question:
    def __init__(self, question, correct_answer, incorrect_0, incorrect_1, incorrect_2):
        self.question = question
        self.answer = correct_answer
        self.incorrect_0 = incorrect_0
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2

    @classmethod
    def make_ques(cls, ques_dct):
        return cls(ques_dct['question'], ques_dct['correct_answer'], ques_dct['incorrect_answers/0'],
                   ques_dct['incorrect_answers/1'], ques_dct['incorrect_answers/2'])

    def all_choice(self):
        return [self.answer, self.incorrect_0, self.incorrect_1, self.incorrect_2]
