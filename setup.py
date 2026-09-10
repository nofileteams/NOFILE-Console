from pathlib import Path
import os

Path("main.txt").open("w", encoding="UTF-8").write(os.getcwd())
log = input("install library? y/n")
if log != "n":
	if Path("requirement.txt").exists() == True:
		os.system("pip3 install -r requirement.txt")
	else:
		print("You've got bad luck. (Lmao) It's all about your daily conduct.")
