# Quiz in Quiz

In this task, you are to implement the program that read the csv file, then make the quiz program. The `questions.csv` file has information as below:

|category|type|difficulty|question|correct_answer|incorrect_answers/0|incorrect_answers/1|incorrect_answers/2|
|---|---|---|---|---|---|---|---|
|Science: Computers|multiple|easy|What does CPU stand for?|Central Processing Unit|Central Process Unit|Computer Personal Unit|Central Processor Unit|
|Science: Computers|multiple|medium|Whistler was the codename of this Microsoft Operating System.|Windows XP|Windows 2000|Windows 7|Windows 95|
|Science: Computers|multiple|easy|HTML is what type of language?|Markup Language|Macro Language|Programming Language|Scripting Language|
|Science: Computers|multiple|easy|What amount of bits commonly equals one byte?|8|1|2|64|
|...|...|...|...|...|...|...|...|

Your tasks are about to implement the program that works as follows:
1. The user inputs the difficulty level with 3 levels (easy, medium, hard).
   * There are 8, 9, and 3 questions for `easy`, `medium`, and `hard`, respectively.
         <u>*Hint*</u>: If the user chooses `hard`, append-only 3 question objects into question_list.
2. The question order is ordered as in `questions.csv`.
3. The choices for each question must be shuffled.
4. Next, user inputs an answer.
   * If an answer is correct, count the score.
   * If an answer is incorrect, show the correct one.

---
## Example 1

Select difficulty (easy, medium, hard): `hard`<br>
Question: Which RAID array type is associated with data mirroring?<br>
Choice 1: RAID 10<br>
Choice 2: RAID 0<br>
Choice 3: RAID 1<br>
Choice 4: RAID 5<br>
Answer: `3`<br>
That's correct.<br>
Your score is: 1/3

Question: What major programming language does Unreal Engine 4 use?<br>
Choice 1: C++<br>
Choice 2: ECMAScript<br>
Choice 3: Assembly<br>
Choice 4: C#<br>
Answer: `3`<br>
That's wrong.<br>
The correct answer is C++<br>
Your score is: 1/3

Question: What was the name of the first Bulgarian personal computer?<br>
Choice 1: IZOT 1030<br>
Choice 2: Pravetz 82<br>
Choice 3: IMKO-1<br>
Choice 4: Pravetz 8D<br>
Answer: `3`<br>
That's correct.<br>
Your score is: 2/3

---

## Example 2

Select difficulty (easy, medium, hard): `hard`<br>
Question: Which RAID array type is associated with data mirroring?<br>
Choice 1: RAID 5<br>
Choice 2: RAID 10<br>
Choice 3: RAID 0<br>
Choice 4: RAID 1<br>
Answer: `4`<br>
That's correct.<br>
Your score is: 1/3

Question: What major programming language does Unreal Engine 4 use?<br>
Choice 1: Assembly<br>
Choice 2: ECMAScript<br>
Choice 3: C++<br>
Choice 4: C#<br>
Answer: `3`<br>
That's correct.<br>
Your score is: 2/3

Question: What was the name of the first Bulgarian personal computer?<br>
Choice 1: IZOT 1030<br>
Choice 2: Pravetz 82<br>
Choice 3: Pravetz 8D<br>
Choice 4: IMKO-1<br>
Answer: `3`<br>
That's wrong.<br>
The correct answer is IMKO-1<br>
Your score is: 2/3

---
## NOTE:
As you can see in Example 1 and Example 2:
1. The order of questions must be ordered as in `question.csv` (Don't need to shuffle the questions).
2. The choices must be shuffled for each question. (Hint: `random.shuffle(list)`)
---

## Example 3

Select difficulty (easy, medium, hard): `easy`<br>
Question: What does CPU stand for?<br>
Choice 1: Computer Personal Unit<br>
Choice 2: Central Process Unit<br>
Choice 3: Central Processing Unit<br>
Choice 4: Central Processor Unit<br>
Answer: `3`<br>
That's correct.<br>
Your score is: 1/8

Question: HTML is what type of language?<br>
Choice 1: Markup Language<br>
Choice 2: Macro Language<br>
Choice 3: Scripting Language<br>
Choice 4: Programming Language<br>
Answer: `1`<br>
That's correct.<br>
Your score is: 2/8

Question: What amount of bits commonly equals one byte?<br>
Choice 1: 64<br>
Choice 2: 2<br>
Choice 3: 8<br>
Choice 4: 1<br>
Answer: `3`<br>
That's correct.<br>
Your score is: 3/8

Question: Which computer hardware device provides an interface for all other connected devices to communicate?<br>
Choice 1: Central Processing Unit<br>
Choice 2: Hard Disk Drive<br>
Choice 3: Motherboard<br>
Choice 4: Random Access Memory<br>
Answer: `1`<br>
That's wrong.<br>
The correct answer is Motherboard<br>
Your score is: 3/8


.<br>
.<br>
.<br>

---

## Running Tests

There are no tests in this task.

## Your Task


1. Complete the implementations of the `main.py` and `quiz_control.py`.
2. Please do not change file `question_model.py`.


**Notes:**  __If you don't want to use OOP in this task,
you can do so. But the score will be limited to 70%.__


## Submission

1. Check that everything is working as expected.
2. Commit your code with all related files.
3. Push the commit to GitHub.

## Grading Criteria

1. **Program output (70%):** Your program must work, as shown in the examples.
   * Read `questions.csv` file (10%)
   * Classify easy medium, or hard questions (10%)
   * Display questions (20%)
   * Shuffle choices (10%)
   * Suggest correct answer (10%)
   * Display correct score (10%)
2. **OOP (30%):** Your program must follow the given OOP template.
