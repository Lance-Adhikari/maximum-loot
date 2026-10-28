def best_item(weights, values):
    max_ratio = 0
    best_index = -1

    for i in range(len(weights)):
        if weights[i] > 0:
            ratio = values[i] / weights[i]

            if ratio > max_ratio:
                max_ratio = ratio
                best_index = i

    return best_index


def knapsack(capacity, weights, values):
    # Work on a copy so the original weights stay unchanged.
    weights = weights.copy()

    amounts = [0] * len(weights)
    total_value = 0

    for _ in range(len(weights)):
        if capacity == 0:
            break

        # Choose the remaining item with the highest value per unit of weight.
        i = best_item(weights, values)

        if i == -1:
            break

        # Take the whole item or just enough to fill the remaining capacity.
        amount = min(weights[i], capacity)

        total_value = total_value + amount * (values[i] / weights[i])

        weights[i] = weights[i] - amount
        amounts[i] = amounts[i] + amount
        capacity = capacity - amount

    return total_value, amounts


# Sample item weights and values.
weights = [5, 4, 3]
values = [30, 28, 24]

total, amounts = knapsack(9, weights, values)

print("Maximum value:", total)
print("Amounts taken:", amounts)
