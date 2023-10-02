def find_items(backpack_capacity, items):
    sorted_items = sorted(items.items(), key=lambda x: x[1])
    current_weight = 0
    selected_items = []

    for item, weight in sorted_items:
        if current_weight + weight <= backpack_capacity:
            selected_items.append((item, weight))
            current_weight += weight

    return selected_items

# Example usage
backpack_capacity = 10
items = {
    'Тент': 3,
    'Спальник': 2,
    'Котелок': 1,
    'Фонарик': 1,
    'Палатка': 4
}

result = find_items(backpack_capacity, items)
print(result)