import json


def save_data():
    test_data = {"prizrak_id": 100, "bot_id": 80}

    with open("data.json", "w") as f:
        json.dump(test_data, f)
    print("Datas are in data.json")
