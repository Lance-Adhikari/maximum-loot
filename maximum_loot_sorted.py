def knapsack_fast(capacity, weights, values):

    items = []

    for i in range(len(weights)):
        if weights[i] > 0:
            ratio = values[i] / weights[i]
            items.append((ratio, i))

    # Sort by highest value per kg first
    items.sort(reverse=True)

    amounts = [0] * len(weights)
    total_value = 0

    for ratio, i in items:
        if capacity == 0:
            break

        # Take the whole item or just enough to fill the remaining capacity.
        amount = min(weights[i], capacity)

        total_value = total_value + amount * ratio
        amounts[i] = amounts[i] + amount
        capacity = capacity - amount

    return total_value, amounts


weights = [5, 4, 3]
values = [30, 28, 24]

total, amounts = knapsack_fast(9, weights, values)

print("Maximum value:", total)
print("Amounts taken:", amounts)
