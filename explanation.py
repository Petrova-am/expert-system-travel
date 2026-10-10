# explanation.py
# Объяснение по реально сработавшим правилам


class Explainer:
    def explain(self, fact_base):
        trace = fact_base.get_trace()
        if not trace:
            print("\nРешение не было принято: недостаточно данных.")
            return

        print("Объяснения решения")
        print("\nСистема применила следующие правила:")

        for i, entry in enumerate(trace, 1):
            print(f"{i}. Правило {entry['rule']}")
            print(f"   если: {entry['condition']}")
            print(f"   то: {entry['conclusion']}")
            print()

        print("Цепочка вывода:")
        for entry in trace:
            for key, value in entry["conclusion"].items():
                print(f"  {entry['rule']} → {key} = {value}")

    def why(self, fact_base, fact_key):
        trace = fact_base.get_trace()
        for entry in trace:
            if fact_key in entry["conclusion"]:
                print(f"\nПочему {fact_key} = {entry['conclusion'][fact_key]}?")
                print(f"Потому что сработало правило {entry['rule']}:")
                print(f"  если: {entry['condition']}")
                print(f"  то: {entry['conclusion']}")
                return
        print(f"\nНет правила, которое вывело {fact_key}.")