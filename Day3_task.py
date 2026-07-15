# Task 1 :Take a sentence from the user, find unique characters using a set, and count them.

sentence = str(input("Enter a sentence : "))
unique_chars = set(sentence)
print(unique_chars)
count = len(unique_chars)
print("Total unique characters :", count)

# Task 2: Clean a messy string, convert it to lowercase, and count each word frequency using a dictionary.



string =  "Python is amazing! It helps us solve problems, learn coding. Data is important."
string = string.replace(",","")
string = string.replace("!","")
string = string.replace(".","")
string = string.replace("?","")
string = string.lower()
string=string.split()
word_count = {}
for word in string:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(word, ":", count)


 #  Task 3: Create a function to check whether a word is a palindrome or not.

n = input()
rev = ''
for char in n:
    rev = char + rev
if n == rev:
    print("palindrome")
else:
    print("not a palindrome")
