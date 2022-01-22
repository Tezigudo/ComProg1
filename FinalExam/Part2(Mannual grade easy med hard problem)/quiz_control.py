class QuizControl:
    def __init__(self, question_list):
        self.ques_lst = question_list
        self.now = 0

    def has_question(self):
        return self.now <= self.num_ques - 1

    def next(self):
        self.now += 1

    @property
    def now_ques(self):
        return self.ques_lst[self.now]

    @property
    def num_ques(self):
        return len(self.ques_lst)
