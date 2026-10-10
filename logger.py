import json
from datetime import datetime


def log_session(fact_base, filename="session.log"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n--- Сеанс {datetime.now()} ---\n")
        f.write(f"Факты: {json.dumps(fact_base.facts, ensure_ascii=False)}\n")
        f.write(f"Цепочка: {json.dumps(fact_base.get_trace(), ensure_ascii=False)}\n")
    print(f"Сеанс записан в {filename}")