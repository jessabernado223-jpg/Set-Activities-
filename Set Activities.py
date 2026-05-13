numbers = [1, 2, 2, 3, 4, 4, 5]

print(set(numbers))

fruits = {"apple", "banana"}

fruits.add("orange")
fruits.remove("banana")

print(fruits)

A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)
print("Intersection:", A & B)

classA = {"Jessa", "Francis", "Isaytey"}
classB = {"Francis", "Isaytey", "Liza"}

print("Both:", classA & classB)
print("All:", classA | classB)
