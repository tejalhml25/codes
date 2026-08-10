# Initial list
numbers = [100, 50, 400, 500]

print("Initial List:", numbers)

numbers[1] = 200
print("After changing second element:", numbers)

numbers.append(600)
print("After appending 600:", numbers)


numbers.insert(2, 300)
print("After inserting 300 at index 2:", numbers)


numbers.remove(600)
print("After removing 600:", numbers)


numbers.pop(0)
print("After removing element at index 0:", numbers)