from pathlib import Path

path = Path('exercise10_3.txt')

for line in path.read_text().splitlines() :
  print(line)