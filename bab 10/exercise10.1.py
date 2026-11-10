from pathlib import Path
path = Path('exercise10_1.txt')

#entire file
contents = path.read_text()
print(contents)

#loop
for line in contents.splitlines() :
    print(line)

#storing lines
lines = contents.splitlines()
for line in lines :
    print(line)