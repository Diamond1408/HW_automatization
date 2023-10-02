def get_duplicates(lst):
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

# Example usage
input_list = [1, 2, 3, 1, 2]
result = get_duplicates(input_list)
print(result)