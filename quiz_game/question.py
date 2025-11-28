class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer: str) -> bool:
        return user_answer.strip().lower() == self.answer.strip().lower()
