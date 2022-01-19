def letterFrequency(fileName, letter):
    file = open(fileName, "r")
    text = file.read()
    count = 0
    for char in text:
        if char == letter:
            count += 1
  
    
    return count
print(letterFrequency('ron.txt', 'd'))