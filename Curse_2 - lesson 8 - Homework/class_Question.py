class Question:
    """
    Класс, содержащий в себе свойства и методы вопросов для игры
    """
    POINTS_PER_ANSWER = 10

    text_question = None
    complexity = 0
    correct_answer = None

    is_ask = False
    user_answer = None
    points_awarded = 0

    def __str__(self):
        return f"Вопрос: {self.text_question}\n" \
               f"Правильный ответ: {self.correct_answer}\n" \
               f"Сложность: {self.complexity}"

    def __repr__(self):
        return f"Question("\
               f"'text_question'='{self.text_question}'," \
               f"'complexity'='{self.complexity}'," \
               f"'correct_answer'='{self.correct_answer}'," \
               f"'is_ask'='{self.is_ask}'," \
               f"'user_answer'='{self.user_answer}'," \
               f"'points_awarded'='{self.points_awarded})'"

    def build_question(self, num: int) -> str:
        """
        Возвращает строку с текстом вопроса и его сложностью

        :param num: порядковый номер вопроса в сессии

        :return: строка с текстом вопроса и его сложностью
        """
        return (f"Вопрос {num}: {self.text_question}\n"
                f"Сложность: {self.complexity}/10")

    def is_correct(self) -> bool:
        """Определяет является ли ответ игрока верным"""
        return self.user_answer.lower() == self.correct_answer.lower()

    def get_points(self) -> int:
        """
        Возвращает количество баллов за правильный ответ
        в зависимости от сложности вопроса
        """
        return self.complexity * self.POINTS_PER_ANSWER

    def build_feedback(self) -> str:
        """
        Возвращает строку с текстом для игрока
        в зависимости от правильности ответа
        """
        if self.points_awarded:
            return f"Ответ верный, получено {self.points_awarded} баллов"
        return f"Ответ неверный. Верный ответ – {self.correct_answer}"
