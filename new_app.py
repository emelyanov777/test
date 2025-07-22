purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
def generate_report(purchases, min_price):

    def total_revenue(purchases : list) -> float:
        revenue = 0
        for i in purchases:
            revenue += i["price"] * i["quantity"]
        return revenue

    def items_by_category(purchases: list) -> dict:
        d = dict()
        for i in purchases:
            cat = i["category"]
            item = i["item"]
            if cat not in d.keys():
                d[cat] = []
            if item not in d[cat]:
                d[cat].append(item)
        return d

    def expensive_purchases(purchases: list, min_price: float) -> list:
        lst = []
        for i in purchases:
            if i["price"] >= min_price:
                lst.append(i)
        return lst

    def average_price_by_category(purchases: list) -> dict:
         d = dict()
         for i in purchases:
            cat = i["category"]
            if cat not in d.keys():
                d[cat] = [i["price"]]
            else:
                d[cat].append(i["price"])
         for cat in d:
             d[cat] = sum(d[cat]) / len(d[cat])
         return d

    def most_frequent_category(purchases: list) -> str:
        d = dict()
        for i in purchases:
            cat = i["category"]
            if cat not in d.keys():
                d[cat] = [i["quantity"]]
            else:
                d[cat].append(i["quantity"])
        for cat in d:
            d[cat] = sum(d[cat])
        return max(d, key=d.get)

    print('Общая выручка:', total_revenue(purchases))
    print('Товары по категориям:', items_by_category(purchases))
    print(f'Покупки дороже {min_price}:', expensive_purchases(purchases, min_price))
    print('Средняя цена по категориям:', average_price_by_category(purchases))
    print('Категория с наибольшим количеством проданных товаров:', most_frequent_category(purchases))

generate_report(purchases, 1.0)
