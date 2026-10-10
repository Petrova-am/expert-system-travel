import json


def load_rules(rules_file):
    with open(rules_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_rules(rules_file, data):
    with open(rules_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_rule(rules_file, new_rule):
    data = load_rules(rules_file)
    data["rules"].append(new_rule)
    save_rules(rules_file, data)
    print(f"Правило {new_rule['id']} добавлено.")


def delete_rule(rules_file, rule_id):
    data = load_rules(rules_file)
    data["rules"] = [r for r in data["rules"] if r["id"] != rule_id]
    save_rules(rules_file, data)
    print(f"Правило {rule_id} удалено.")