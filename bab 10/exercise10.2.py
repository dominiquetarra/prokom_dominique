from pathlib import Path
path = Path('exercise10_1.txt')
contents = path.read_text()

#looping modified lines
for line in contents.splitlines() :
    modified_line = line.replace('Python' , 'C')
    print(modified_line)