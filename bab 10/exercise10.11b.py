from pathlib import Path
import json

path = Path("exercise10_11.json")
contents = path.read_text()
number = json.loads(contents)

print(f"I know your favorite number, its {number}!")
