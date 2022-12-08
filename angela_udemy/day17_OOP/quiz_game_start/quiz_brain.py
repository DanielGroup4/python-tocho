# TODO asking the questions
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list) # total de numero de preguntas, devuelve True o False


# TODO cheking if the answer was correct
    def next_question(self):
        current_question = self.question_list[self.question_number] # valor iniciado en 0
        self.question_number += 1
        user_answer = input(f"Question. {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That´s wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your correct score is: {self.score}/{self.question_number}")
        print("\n")

# TODO cheking if we´re the end of the quiz
