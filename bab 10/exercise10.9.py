from pathlib import Path

filenames = ['exercise10_8_cat.txt', 'exercise10_8_dog.txt']

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)