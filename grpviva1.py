#Python program to count number of lowercase characters in a string ...
"""str=input("Enter the string:")
count=0
for i in str:
      if(i.islower()):
            count=count+1
print("Total number of lowercase characters are:")
print(count)"""


"""string1 = input("ENTER STRING:")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
for i in range(len(alpha)):
    for alpha[i] in string1:
        count = count + 1
print(count)"""
"""string1 = input("ENTER A STRING::")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
for i in range(len(alpha)):
    if alpha[i] in string1:
        count = count + 1
print(count)"""
"""str=input("Enter a string: ")
upper=0
lower=0
for i in range(len(str)):
      #to lower case letter
      if(str[i]>='a' and str[i]<='z'):
          lower+=1
          print('Lower case letters= ',lower)"""
string1 = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
for i in range(len(string1)):
    if string1[i] in alpha:
        count = count + 1
print(count)
