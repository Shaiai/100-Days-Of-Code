from data import question_data
from quiz_brain import QuizBrain
from question_model import Question

#Create our library/list of questions.
question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#Create our quiz using our quizbrain class model.
quiz = QuizBrain(question_bank)

#loop using our check method to see if there are any remaining questions
while quiz.still_has_questions():
    quiz.next_question()


print(f"You've completed the Quiz, congratulations!\nYour final score was {quiz.score}/{len(question_bank)}")