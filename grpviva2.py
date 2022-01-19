string1 = input("enter a string")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
for i in range(len(string1)):
    if string1[i] in alpha:
        count = count + 1
print(count)