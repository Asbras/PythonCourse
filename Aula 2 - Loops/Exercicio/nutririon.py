def main():
    frutas = [
            {"nome": "Apple", "caloria": "130"},
            {"nome": "Avocado", "caloria": "50"},
            {"nome": "Banana", "caloria": "110"},
            {"nome": "Canteloupe", "caloria": "50"},
            {"nome": "Grapefruit", "caloria": "60"},
            {"nome": "Grapes", "caloria": "90"},
            {"nome": "Honeydew Melon", "caloria": "50"},
            {"nome": "Kiwifruit", "caloria": "90"},
            {"nome": "Lemon", "caloria": "15"},
            {"nome": "Lime", "caloria": "20"},
            {"nome": "Nectarine", "caloria": "60"},
            {"nome": "Orange", "caloria": "80"},
            {"nome": "Peach", "caloria": "60"},
            {"nome": "Pear", "caloria": "100"},
            {"nome": "Pineapple", "caloria": "50"},
            {"nome": "Plums", "caloria": "70"},
            {"nome": "Strawberries", "caloria": "50"},
            {"nome": "Sweet Cherries", "caloria": "100"},
            {"nome": "Tangerine", "caloria": "50"},
            {"nome": "Watermelon", "caloria": "80"},
        ]
    fruta = input("Item: ")
    for item in frutas:
        if item["nome"].lower() == fruta.lower():
            print(f"Calories: {item['caloria']}")


main()
