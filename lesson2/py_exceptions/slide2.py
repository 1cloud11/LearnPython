def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = int(max_discount)
    except (ValueError, TypeError):
        return 'Убедись, что указал числа!'
    
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

print(discounted(100, 20, 'asd'))