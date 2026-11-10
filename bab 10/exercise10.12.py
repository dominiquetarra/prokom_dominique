from pathlib import Path
import json

path = Path('exercise10_12.json')
if path.exists() :
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number, its {number}!")

else :
    number = int(input("What's your favorite number? "))
    contents = json.dumps(number)
    path.write_text(contents)
    print("Okay, I'll remember that.")