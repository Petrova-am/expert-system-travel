from facts import FactBase
from inference import InferenceEngine
from dialog import Dialog
from explanation import Explainer
from logger import log_session


def main():

    print("Система задаст несколько вопросов и порекомендует страну.")

    # Инициализация компонентов
    fact_base = FactBase()
    inference = InferenceEngine("rules.json")
    dialog = Dialog()
    explainer = Explainer()

    # Собираем факты от пользователя
    dialog.collect_facts(fact_base, inference)

    # Запускаем прямой вывод
    fact_base = inference.forward_chain(fact_base)

    # Показываем результат
    country = fact_base.get("country")
    if country:
        print(f"Рекомендация: {country}")
    else:
        print("Рекомендация: недостаточно данных")
        missing = inference.get_missing_facts(fact_base)
        if missing:
            print(f"Не хватает данных: {', '.join(missing)}")

    # Объяснение решения
    explainer.explain(fact_base)

    # Журнал сеанса
    log_session(fact_base)


if __name__ == "__main__":
    main()