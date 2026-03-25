# String Operations in Python

# 1. Creating Strings
name = "joan"
age = 19
city = "New York"

# 2. String Concatenation
full_info = name + " is " + str(age) + " years old"
print(f"Concatenation: {full_info}")

# 3. String Formatting
formatted = f"{name} lives in {city}"
print(f"F-string: {formatted}")

# 4. String Methods
text = "hello world python"
print(f"Upper: {text.upper()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title: {text.title()}")

# 5. String Slicing
word = "Programming"
print(f"First 4 chars: {word[:4]}")
print(f"Last 3 chars: {word[-3:]}")

# 6. String Search
email = "warugurujoan"
print(f"Contains @: {'@' in email}")
print(f"Index of @: {email.find('@')}")

# 7. String Splitting
sentence = "Python is awesome"
words = sentence.split()
print(f"Words: {words}")

# 8. String Replacement
message = "I like cats"
new_message = message.replace("cats", "dogs")
print(f"Replaced: {new_message}")

# 9. String Stripping
padded = "  hello world  "
print(f"Stripped: '{padded.strip()}'")

# 10. String Repetition
symbol = "*"
print(f"Repetition: {symbol * 10}")

# 11. String Joining
items = ["apple", "banana", "orange"]
fruit_list = ", ".join(items)
print(f"Joined: {fruit_list}")

# 12. Check String Type
print(f"Is digit? {'123'.isdigit()}")
print(f"Is alpha? {'abc'.isalpha()}")
