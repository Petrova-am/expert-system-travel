class FactBase:
    def __init__(self):
        self.facts = {}
        self.trace = []

    def set(self, key, value):

        self.facts[key] = value

    def get(self, key):

        return self.facts.get(key, None)

    def has(self, key):

        return key in self.facts

    def add_trace(self, rule_id, condition, conclusion):

        self.trace.append({
            "rule": rule_id,
            "condition": condition,
            "conclusion": conclusion
        })

    def get_trace(self):

        return self.trace