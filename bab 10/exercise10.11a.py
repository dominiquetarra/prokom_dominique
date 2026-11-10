from pathlib import Path
import json

number = int(input("What's your favorite number? "))

path = Path('exercise10_11.json')
contents = json.dumps(number)
path.write_text(contents)
