class Dialog:
    def __init__(self):
        self.questions = {
            "season": ("В какое время года планируете поездку?",
                       ["весна", "лето", "осень", "зима"]),
            "duration": ("Сколько дней планируете отдыхать?",
             ["3-5", "7-10", "11-14"]),
            "interest_beach": ("Вам интересен пляжный отдых?",
                               ["да", "нет", "неизвестно"]),
            "interest_culture": ("Вам интересна культура и история?",
                                 ["да", "нет", "неизвестно"]),
            "interest_nature": ("Вам интересна природа?",
                                ["да", "нет", "неизвестно"]),
            "interest_exotic": ("Вам интересна экзотика?",
                                ["да", "нет", "неизвестно"]),
            "visa_free": ("Вам нужен безвизовый въезд?",
                          ["да", "нет", "неизвестно"]),
            "direct_flight": ("Вам важен прямой рейс?",
                              ["да", "нет", "неизвестно"]),
            "budget": ("Какой у вас бюджет?",
                       ["низкий", "средний", "высокий"]),
        }

    def ask(self, key, fact_base):
        """Задаёт вопрос и проверяет ответ."""
        question, allowed = self.questions[key]
        print(f"\n{question}")
        print(f"Допустимые ответы: {', '.join(allowed)}")

        while True:
            answer = input("> ").strip().lower()
            if answer in allowed:
                fact_base.set(key, answer)
                return answer
            print(f"Некорректный ответ. Введите одно из: {', '.join(allowed)}")

    def collect_facts(self, fact_base, inference):
        """Собирает факты, пока есть неизвестные."""
        asked = set()
        while True:
            missing = inference.get_missing_facts(fact_base)
            to_ask = [k for k in missing if k not in asked]
            if not to_ask:
                break
            self.ask(to_ask[0], fact_base)
            asked.add(to_ask[0])