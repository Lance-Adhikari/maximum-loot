# Maximum Loot

Python solutions to the fractional knapsack problem: fill a bag with the highest possible value while staying within its weight capacity. Fractions of items can be taken.

- [maximum_loot_simple.py](maximum_loot_simple.py): Repeatedly finds the remaining item with the highest value per unit of weight.
- [maximum_loot_sorted.py](maximum_loot_sorted.py): Sorts items by value per unit of weight once, then fills the bag in that order.
- [initial_attempt.py](initial_attempt.py): An early exercise, not a correct knapsack solution. It selects weights and values separately, losing their original pairings, and uses integer division for ratios.

With weights `[5, 4, 3]`, values `[30, 28, 24]`, and capacity `9`, both completed solutions return a maximum value of **64**, taking amounts `[2, 4, 3]`.
