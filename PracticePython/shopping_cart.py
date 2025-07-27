shopping_cart = {
    '사과': {'quantity': 2, 'price': 1000},
    '바나나': {'quantity': 3, 'price': 800},
    '오렌지': {'quantity': 1, 'price': 1500}
}
total_price = 0
print("쇼핑 카트:")
for fruit, details in shopping_cart.items():
    quantity = details['quantity']
    price_per_item = details['price']
    item_total = quantity * price_per_item
    total_price += item_total
    print(f"{fruit}: {quantity}개 (개당 {price_per_item}원) = {item_total}원")
print(f"총 가격: {total_price}원")