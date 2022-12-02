#!/usr/bin/env python3

# Day 1

# retrieve minimum 50 stars by Dec 25
# Grab any fruit, not just special star fruit
# counting calories each elf is carrying (puzzle input)

# elves take turns writing down number of calories, one item per line
# blank line = separate elf

f = open('input.txt', 'r')
lines = f.readlines()

foodCounts = []
calories = []

currentCount = 0
currentCals = 0
counter = 0
for line in lines:
    counter = counter + 1
    if line.isspace():
        foodCounts.append(int(currentCount))
        calories.append(int(currentCals))
        currentCount = 0
        currentCals = 0
    else:
        currentCount = currentCount + 1
        currentCals = currentCals + int(line)

print("Max food count: " + str(max(foodCounts)) + ", index: " + str(foodCounts.index(max(foodCounts))))
print("Max cals: " + str(max(calories)) + ", index: " + str(calories.index(max(calories))))

sortedCalories = sorted(calories)
print("Highest 3 caloriest sum last: " + str(sortedCalories[-1] + sortedCalories[-2] + sortedCalories[-3]))
