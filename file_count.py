line_count =0
sen_count=0
word_count=0
lower_count=0
upper_count=0
spl_count=0

spl_char ="!@#$%^&*()_+=-{}][]:|\"';<>?/.,"

file=open("file.txt","r")
content = file.read()

line_count = content.count("\n")+1
sen_count = content.count(".")+content.count("!")+content.count("?")

words =content.split()
word_count = len(words)

for char in content:  # Scan entire content once
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
    elif char in spl_char:  # Use predefined special chars
        spl_count += 1

print("line count is :",line_count)
print("sentence count is :",sen_count)
print("word count is :",word_count)
print("lowercase count is :",lower_count)
print("uppercase count is :",upper_count)

