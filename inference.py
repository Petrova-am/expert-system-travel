# inference.py
# Механизм вывода: прямой вывод с поддержкой AND/OR

import json


class InferenceEngine:
    def __init__(self, rules_file):
        with open(rules_file, "r", encoding="utf-8") as f:
            self.rules = json.load(f)["rules"]
        self.max_iterations = 100  # защита от циклов

    def forward_chain(self, fact_base):
        """Прямой вывод: от фактов к выводам."""
        iteration = 0
        while iteration < self.max_iterations:
            iteration += 1
            applicable = []


            for rule in self.rules:
                if self._conditions_met(rule["if"], fact_base):
                    applicable.append(rule)


            if not applicable:
                break


            applicable.sort(key=lambda r: r["priority"], reverse=True)
            best = applicable[0]


            if self._already_applied(best, fact_base):
                break


            for key, value in best["then"].items():
                fact_base.set(key, value)
            fact_base.add_trace(best["id"], best["if"], best["then"])

        return fact_base

    def _conditions_met(self, conditions, fact_base):
        """Рекурсивная проверка условий с поддержкой AND и OR."""
        if "AND" in conditions:
            return all(self._conditions_met(c, fact_base) for c in conditions["AND"])
        if "OR" in conditions:
            return any(self._conditions_met(c, fact_base) for c in conditions["OR"])
        # Простое условие
        for key, value in conditions.items():
            if fact_base.get(key) != value:
                return False
        return True

    def _already_applied(self, rule, fact_base):
        """Проверяет, не сработало ли правило уже."""
        for entry in fact_base.get_trace():
            if entry["rule"] == rule["id"]:
                return True
        return False

    def get_missing_facts(self, fact_base):
        """Возвращает, каких фактов не хватает для срабатывания правил."""
        missing = set()
        for rule in self.rules:
            self._collect_missing(rule["if"], fact_base, missing)
        return list(missing)

    def _collect_missing(self, conditions, fact_base, missing):
        """Рекурсивно собирает отсутствующие факты."""
        if "AND" in conditions:
            for c in conditions["AND"]:
                self._collect_missing(c, fact_base, missing)
        elif "OR" in conditions:
            known = any(self._conditions_met(c, fact_base) for c in conditions["OR"])
            if not known:
                for c in conditions["OR"]:
                    self._collect_missing(c, fact_base, missing)
        else:
            for key in conditions:
                if not fact_base.has(key):
                    missing.add(key)