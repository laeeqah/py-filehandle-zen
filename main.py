#Longest Word
words = open("zen-python.txt","r")
s = words.read()
first = s.split()

print(max(first, key = len))
words.close()

#Number of words
count = len(open("zen-python.txt","r").readlines())
print(count)
