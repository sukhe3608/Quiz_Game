class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0 

    def start(self):
        for idx , question in enumerate(self.questions):
            print(f"\nQuestion {idx + 1}: {question.question}")

            for i , option in enumerate(question.options):
                print(f"  {i + 1}. {option}")

            user_answer = input("Your answer (type the option number):")
            if question.is_correct(question.options[int(user_answer) - 1]):
                print("Correct!")
                self.score += 1

            else:
                print(f"Wrong! The correct answer was: {question.answer}")

        print(f"\nQuiz Over! Your final score is: {self.score}/{len(self.questions)}")