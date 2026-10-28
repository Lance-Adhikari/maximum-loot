# Initial attempt: choosing weight and value separately loses item pairings.
# See the completed solutions for the correct fractional knapsack approach.
weights = [5, 4, 3]
values = [30, 28, 24]

def best_item(weights, values):

    ratios = []
    kg = 0
    dollar = 0

    for i in range(len(weights)):
        kg = max(weights) # Find max kg
        dollar = max(values) # Find max dollar
        ratio = (dollar // kg)
        ratios.append(ratio)
        values.remove(dollar)
        weights.remove(kg)
        i = i + 1

    max_number = max(ratios)
    best_index = ratios.index(max_number)

    print(max_number, best_index)

best_item(weights, values)
