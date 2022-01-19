"""4.	Write a program to perform the following on List
 a. Enter a List of Numbers and sort the value in Largest-to-smallest order.
 b. Do the same thing, but for strings and in reverse alphabetical order.
 c. Create a list with elements as "apple", “banana",”cherry", "kiwi", “melon", "mango".
     Display each with its position
 d. Insert “Orange”, then Copy list into another list
 e. Remove “cherry” from first list and display both the strings
f. Display the third, fourth, and fifth item of first list.
g. Check if "apple" is present in the list display message as present.
h. And then print all items in the list, one by one
 i. To delete element at third index and perform pop()."""
List1 = []
count=0
limit = int(input("Enter the number of elements of the list"))
while count<limit:
    item=int(input("Enter the numbers to be added in list"))
    List1.append(item)
    count=count+1
print(List1)
print(List1.sort())

List2 = []
count=0
limit = int(input("Enter the number of alphabets of the list"))
while count<limit:
    item=(input("Enter the alphabets to be added in list"))
    List2.append(item)
    count=count+1
print(List2)
List2.sort()
print(List2)
fruit=["apple","banana","cherry","kiwi","mango","lemon"]
for i in range (len(fruit)):
    print("current fruit:",i,fruit[i])
fruit.append("orange")
print(fruit)
new_fruit=fruit
print(new_fruit)
fruit.remove("cherry")
print(fruit)
print(new_fruit)
for i in range (2,5):
    print("Fruit at index:  ",i,fruit[i])
fruit=["apple","banana","cherry","kiwi","mango","lemon"]
if "apple" in fruit:
    print("PRESENT")
else:
    print("NOT PRESENT")
fruit=["apple","banana","cherry","kiwi","mango","lemon"]
for i in range(0,len(fruit),1):
    print(fruit[i])
fruit = ["apple", "banana", "cherry", "kiwi", "mango", "lemon"]
fruit.pop(2)
print(fruit)

