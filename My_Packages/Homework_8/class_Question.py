class Question:
    text_question = None
    complexity = 0
    correct_answer = None

    is_ask = False
    user_answer = None
    points_awarded = 0

    def build_question(self, num: int) -> str:
        return (f"Вопрос {num}: {self.text_question}\n"
                f"Сложность: {self.complexity}/10")

    def is_correct(self) -> bool:
        return self.user_answer.lower() == self.correct_answer.lower()

    def get_points(self) -> int:
        return self.complexity * 10

    def build_feedback(self, right: bool) -> str:
        if right:
            return f"Ответ верный, получено {self.points_awarded} баллов"

        return f"Ответ неверный. Верный ответ – {self.correct_answer}"
