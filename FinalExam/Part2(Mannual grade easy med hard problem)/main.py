import csv
import random

from question_model import Question
from quiz_control import QuizControl

questions = []
all_question = []


def exact_diff(diff):
    now_ques = 0
    if diff == 'easy':
        for each_quesion in all_question:
            if each_quesion['difficulty'] == 'easy':
                now_ques += 1
                questions.append(Question.make_ques(each_quesion))
            if now_ques == 8:
                break

    elif diff == 'medium':
        for each_quesion in all_question:
            if each_quesion['difficulty'] == 'medium':
                now_ques += 1
                questions.append(Question.make_ques(each_quesion))

            if now_ques == 9:
                break

    elif diff == 'hard':
        for each_quesion in all_question:
            if each_quesion['difficulty'] == 'hard':
                now_ques += 1
                questions.append(Question.make_ques(each_quesion))

            if now_ques == 3:
                break


with open('questions.csv', 'r') as data:
    all_ques = csv.DictReader(data)
    for each_quesion in all_ques:
        all_question.append(each_quesion)

random.shuffle(all_question)
diff = input('Select difficulty (easy, medium, hard):')

exact_diff(diff)

quiz = QuizControl(questions)
score = 0
while quiz.has_question():
    now_quez = quiz.now_ques
    now_choice = now_quez.all_choice()
    random.shuffle(now_choice)
    print(now_quez.question)

    for i, choice in enumerate(now_choice):
        print(f'Choice {i + 1}: {choice}')
        if choice == now_quez.answer:
            correct_ans, correct_choice = str(i + 1), choice

    ans = input('Answer: ')
    if ans == correct_ans:
        score += 1
        print("That's correct.")

    else:
        print("That's wrong.")
        print(f'The correct answer is {correct_choice}')
    print(f'Your score is: {score}/{quiz.num_ques}\n')

    quiz.next()
