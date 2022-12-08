from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]  # esto toma el texto de la pregunta
    question_answer = question["answer"]  # toma el texto de la respuesta
    new_question = Question(q_text= question_text, q_answer= question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer) # return True value

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # if quiz still has questions remaining
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
