# Task 1: Count the frequency of each word using a dictionary.

text = input("Enter a paragraph: ")
text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word Frequency:")
for word in word_count:
    print(word, ":", word_count[word])


# Task 2: Read student grades from a file and calculate the average score.

file = open("grades.txt", "w")
file.write("Ali,85\n")
file.write("Sana,70\n")
file.write("fatima,65\n")
file.write("Ayesha,75\n")
file.write("Zainab,80\n")
file.close()

try:
    file = open("grades.txt", "r")
    total = 0
    count = 0
    for line in file:
        data = line.strip().split(",")
        name = data[0]
        marks = int(data[1])
        total = total + marks
        count = count + 1
    average = total / count
    print("Average Score:", average)
    file.close()
except FileNotFoundError:
    print("File not found.")


# Task 3: Filter numbers using list comprehension.

numbers = [12, 45, 2, 18, 9, 33, 70, 5, 21, 6]
filtered_numbers = [num for num in numbers if num > 15 and num % 3 == 0]
print("Original List:", numbers)
print("Filtered List:", filtered_numbers)
