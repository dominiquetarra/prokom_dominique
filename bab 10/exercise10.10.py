from pathlib import Path

filename = 'exercise10_10_story.txt'

try:
    with open(filename, encoding='utf-8') as f :
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    total_the = contents.lower().count('the')
    print(f"'the' appears in {filename} about {total_the} times.")
