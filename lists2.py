lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

friends.append("Creed") # Adds an element to a list
print(friends)

friends.insert(1, "Kelly") # Inserts an element at a position in a list
print(friends)

friends.remove("Jim") # Removes an element from a list (just first one?)
print(friends)

friends.clear() # Empties a list
print(friends)

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop() # Removes from end of the list.
print(friends)

print("Karen is at index ", friends.index("Karen")) # element at 1

friends = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Toby"]
print("Number of Jims in list = ", friends.count("Jim")) # Count of Jims in list

friends.sort()
print("Sorted friends list = ", friends)

lucky_numbers.reverse()
print("reversed lucky numbers = ", lucky_numbers)

friends2 = friends.copy()
print("friends2 = ", friends2)


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers) # Adds a list to another list
print(friends)
