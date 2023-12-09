# Задача 1
# import random

# def qwerty(list, file_path):

#     random_language = random.choice(list)

#     with open(file_path, 'w') as file:
#         file.write(random_language)

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# file_path = "random_language.txt"

# qwerty(language, file_path)
# Задача 2
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum."""

with open("text.txt", "w") as file:
    file.write(text)

# Доп задача
with open("text.txt", "r") as source_file:
        text = source_file.read()
with open("wikipedia.txt", "w") as file:
    file.write(text)


