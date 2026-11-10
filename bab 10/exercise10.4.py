from pathlib import Path

name = input("Please enter your name : ")

path = Path("exercise10_4.txt")
path.write_text(name)