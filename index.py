#You really managed to dig that up, didn't you? But if you have time for that sort of thing, you ought to be finding a partner, getting a job, and earning money instead.
import argparse
import json
import locale
import getpass
from colorama import init, Fore, Back, ansi
import platform
import os
import seedir as sd
import sys
from playsound3 import playsound
import random
import readchar
from pathlib import Path

log = 1
#main = os.path.dirname(os.path.abspath(sys.argv[0]))
main = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))

move = "none"

fore = Fore.WHITE
back = Back.BLACK

if os.path.exists(main) == False:
	print("\033[31mAn unexpected error has occurred.\033[0m")
	sys.exit()

lang = locale.getlocale()[0][:2].lower()
if Path(f"{main}/lang/{lang}.json").exists() == True:
	with open(f"{main}/lang/{lang}.json", "r", encoding="UTF-8") as lang_file:
		file_lang = lang_file.read()
	with open(f"{main}/config.json", "w", encoding="UTF-8") as lang_file:
		lang_file.write(file_lang)

with open(f"{main}/config.json", "r", encoding="UTF-8") as json_file:
	data = json.loads(json_file.read())
with open(f"{main}/cmd/os.json", "r", encoding="UTF-8") as os_file:
	os_data = json.loads(os_file.read())

move_data = json.loads("{}")

if os.name == "nt":
	data["logo"] = os_data["win"]
else:
	if platform.system().lower() == "darwin":
		data["logo"] = os_data["mac"]
	else:
		data["logo"] = os_data["linux"]

#os.chdir("/")

angry_mater = 0

sound_mode = False

data["username"] = getpass.getuser()
if Path(f"{main}/cmd/sub.name").read_text(encoding="UTF-8") != "":
	data["username"] = Path(f"{main}/cmd/sub.name").read_text(encoding="UTF-8")

parser = argparse.ArgumentParser()
parser.add_argument("-f", default="none", help=data["help"]["file"])
parser.add_argument("-c", default="none", help=data["help"]["command"])
args = parser.parse_args()

sys.stdout.write(f"\x1b]2;{data["title"]}\x07")
sys.stdout.flush()

if args.c != "none" or args.f != "none":
	terminal_mode = False
else:
	terminal_mode = True

exits = False
os_name = f"{platform.system()}{platform.release()}"


with open(f"{main}/cmd/bashrc.sh", "r", encoding="UTF-8") as bashrc_file:
	bashrc = bashrc_file.read().lstrip()



#prompt = f"┌──({data["username"]}{data["logo"]}{os_name})-[{os.getcwd().replace("C:", "").replace("\\", "/")}]\n└─$"
prompt_load = Path(f"{main}/cmd/zsh.rc")

prompt = prompt_load.read_text(encoding="UTF-8").replace("$path$", f"{os.getcwd().replace("C:", "").replace("\\", "/")}").replace("$user$", f"{data["username"]}{data["logo"]}{os_name}")

def command(cmd: str):
	global load_cmd
	global exits
	global back
	global fore
	global counts
	global dirs
	global ascii_liner
	global log
	global commands
	global ascii_text
	global arg2
	global sound
	global sound2
	global sound_mode
	global move
	commands = False
	load_cmd = cmd
	#custom
	if load_cmd.split()[0] == "none" or load_cmd.split()[0] == "cls" or load_cmd.split()[0] == "clear" or load_cmd.split()[0] == "exit" or load_cmd.split()[0] == "ls" or load_cmd.split()[0] == "dir" or load_cmd.split()[0] == "cd" or load_cmd.split()[0] == "chdir" or load_cmd.split()[0] == "bash" or load_cmd.split()[0] == "title" or load_cmd.split()[0] == "pause" or load_cmd.split()[0] == "help" or load_cmd.startswith("./") == True or load_cmd.startswith(":") == True or load_cmd.split()[0] == "secret" or load_cmd.split()[0] == "grep" or load_cmd.split()[0] == "tree" or load_cmd.split()[0] == "echo" or load_cmd.split()[0] == "what" or load_cmd.split()[0] == "color" or load_cmd.split()[0] == "pwd" or load_cmd.split()[0] == "lang" or load_cmd.split()[0] == "playsound" or load_cmd.split()[0] == "stopsound" or load_cmd.split()[0] == "playsound2" or load_cmd.split()[0] == "goto":
		if load_cmd.split()[0] == "cls" or load_cmd.split()[0] == "clear":
			if os.name == "nt":
				log = os.system("cls")
			else:
				log = os.system("clear")
		
		if load_cmd.split()[0] == "exit":
			exits = True
			sys.exit()
		
		
		if load_cmd.startswith(":") == True:
			arg = load_cmd.replace(":", "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				move = arg.split()[0]
		

		if load_cmd.split()[0] == "pwd":
			print(os.getcwd())
		
		if load_cmd.split()[0] == "playsound":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				if Path(arg).exists() == True:
					if Path(arg).suffix != ".ogg":
						if Path(arg).suffix == ".wav" or Path(arg).suffix == ".mp3":
							sound = playsound(arg, block=False)
							sound_mode = True
						else:
							print(data["message"]["wrong_file"])
					else:
						print(data["message"]["wrong_file"])
				else:
					print(f"{arg}{data["message"]["sound_error"]}")
			else:
				print(data["message"]["sound_help"])
		
		if load_cmd.split()[0] == "playsound2":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				if Path(arg).exists() == True:
					if Path(arg).suffix != ".ogg":
						if Path(arg).suffix == ".wav" or Path(arg).suffix == ".mp3":
							sound2 = playsound(arg, block=True)
						else:
							print(data["message"]["wrong_file"])
					else:
						print(data["message"]["wrong_file"])
				else:
					print(f"{arg}{data["message"]["sound_error"]}")
			else:
				print(data["message"]["sound_help2"])

		if load_cmd.split()[0] == "stopsound":
			if sound_mode == True:
				sound.stop()

		if load_cmd.split()[0] == "lang":
			print(data["message"]["lang"])
			print(Path(f"{main}/lang/list.txt").read_text(encoding="UTF-8"))
		
		if load_cmd.split()[0] == "what":
			print(data["message"]["what"])
		
		if load_cmd.split()[0] == "color":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).lower().lstrip().strip()
			if arg != "":
				if len(arg) == 1:
					count = 0
					fore = "error"
					for _ in range(1):
						if arg == "0":
							fore = Fore.BLACK
						if arg == "1":
							fore = Fore.BLUE
						if arg == "2" or arg == "a":
							fore = Fore.GREEN
						if arg == "3" or arg == "b":
							fore = Fore.CYAN
						if arg == "4" or arg == "c":
							fore = Fore.RED
						if arg == "5" or arg == "d":
							fore = Fore.MAGENTA
						if arg == "6" or arg == "e":
							fore = Fore.YELLOW
						if arg == "7" or arg == "f":
							fore = Fore.WHITE
						if arg == "8":
							fore = Fore.LIGHTBLACK_EX
							
						count = count + 1
					if fore != "error":
						sys.stdout.write(back + fore)
					else:
						print(data["message"]["color1"])
						print("")
						print(data["message"]["color2"])
						print("")
						print(data["message"]["color3"])
						print("")
						print(data["message"]["color4"])
						print(data["message"]["color5"])
						print(data["message"]["color6"])
						print("")
						print(data["message"]["color7"])
						print(data["message"]["color8"])
						print(data["message"]["color9"])
						print(data["message"]["color10"])
						print(data["message"]["color11"])
						print(data["message"]["color12"])
						print(data["message"]["color13"])
						print(data["message"]["color14"])
						print("")
						print(data["message"]["color15"])
						print(data["message"]["color16"])
						print(data["message"]["color17"])
						print("")
						print(data["message"]["color18"])
						print(data["message"]["color19"])
						print("")
						print(data["message"]["color20"])
				else:
					if len(arg) >= 3:
						print("error")
					else:
						count = 0
						fore = "error"
						back = "error"
						for _ in range(2):
							if count == 1:
								if arg[1] == "0":
									fore = Fore.BLACK
								if arg[1] == "1":
									fore = Fore.BLUE
								if arg[1] == "2" or arg[1] == "a":
									fore = Fore.GREEN
								if arg[1] == "3" or arg[1] == "b":
									fore = Fore.CYAN
								if arg[1] == "4" or arg[1] == "c":
									fore = Fore.RED
								if arg[1] == "5" or arg[1] == "d":
									fore = Fore.MAGENTA
								if arg[1] == "6" or arg[1] == "e":
									fore = Fore.YELLOW
								if arg[1] == "7" or arg[1] == "f":
									fore = Fore.WHITE
								if arg[1] == "8":
									fore = Fore.LIGHTBLACK_EX
							if count == 0:
								if arg[0] == "0":
									back = Back.BLACK
								if arg[0] == "1":
									back = Back.BLUE
								if arg[0] == "2" or arg[0] == "a":
									back = Back.GREEN
								if arg[0] == "3" or arg[0] == "b":
									back = Back.CYAN
								if arg[0] == "4" or arg[0] == "c":
									back = Back.RED
								if arg[0] == "5" or arg[0] == "d":
									back = Back.MAGENTA
								if arg[0] == "6" or arg[0] == "e":
									back = Back.YELLOW
								if arg[0] == "7" or arg[0] == "f":
									back = Back.WHITE
								if arg[0] == "8":
									back = Back.LIGHTBLACK_EX
							
							count = count + 1
						if fore != "error" or back != "error":
							sys.stdout.write(back + fore)
						else:
							print(data["message"]["color1"])
							print("")
							print(data["message"]["color2"])
							print("")
							print(data["message"]["color3"])
							print("")
							print(data["message"]["color4"])
							print(data["message"]["color5"])
							print(data["message"]["color6"])
							print("")
							print(data["message"]["color7"])
							print(data["message"]["color8"])
							print(data["message"]["color9"])
							print(data["message"]["color10"])
							print(data["message"]["color11"])
							print(data["message"]["color12"])
							print(data["message"]["color13"])
							print(data["message"]["color14"])
							print("")
							print(data["message"]["color15"])
							print(data["message"]["color16"])
							print(data["message"]["color17"])
							print("")
							print(data["message"]["color18"])
							print(data["message"]["color19"])
							print("")
							print(data["message"]["color20"])
		
		if load_cmd.split()[0] == "echo":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip().replace("%RANDOM%", str(random.randint(1000, 9999))).replace("%ERRORLEVEL%", str(log)).replace("%PROMPT%", f"\033[31m{data["message"]["error"]}\033[0m")
			print(arg)
			
		if load_cmd.split()[0] == "secret":
			print(data["message"]["secret2"])
		
		if load_cmd.split()[0] == "grep":
			print(data["message"]["grep"])
			
		if load_cmd.split()[0] == "tree":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			counts = 0
			if arg != "":
				if os.path.exists(arg) == True:
					print(data["message"]["tree"])
					sd.seedir(arg)
				else:
					print(f"{arg}{data["message"]["ls_error"]}")
			else:
				print(data["message"]["tree"])
				sd.seedir()
		
			
		if load_cmd.split()[0] == "help":
			print(Path(f"{main}/cmd/help.txt").read_text(encoding="UTF-8"))
		
		if load_cmd.split()[0] == "pause":
			print(data["message"]["pause"])
			log = readchar.readchar()
			
		if load_cmd.startswith("./") == True:
			arg = load_cmd.replace("./", "", 1).lstrip().strip()
			if arg != "":
				if os.name == "nt":
					log = os.system(arg)
				else:
					log = os.system(f"./{arg}")
			
		
		if load_cmd.split()[0] == "title":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			sys.stdout.write(f"\x1b]2;{arg}\x07")
			sys.stdout.flush()
			
		
		if load_cmd.split()[0] == "bash":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				if Path(arg).suffix == ".sh":
					if Path(arg).exists() == True:
						with open(arg, "r", encoding="UTF-8") as file_load:
							load_file = file_load.read()
						file_lines = load_file.splitlines()
						file_count = 0
						while True:
							arg2 = file_lines[file_count]
							if arg2.split()[0] == "goto":
								if arg2.split()[1] in move_data:
									file_count = data[arg2.split()[1]]
							cmd_load(file_lines[file_count])
							if move != "none":
								data[move] = file_count
								move = "none"
							file_count = file_count + 1
							if file_count == len(file_lines):
								break
					else:
						print(f"{arg}{data["message"]["wrong_file2"]}")
				else:
					print(data["message"]["wrong_file"])
		
		if load_cmd.split()[0] == "cd" or load_cmd.split()[0] == "chdir":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				if os.path.exists(arg) == True:
					os.chdir(arg)
				else:
					print(f"{arg}{data["message"]["cd_error"]}")
			else:
				os.chdir("/")
		
		
		if load_cmd.split()[0] == "ls" or load_cmd.split()[0] == "dir":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			counts = 0
			if arg != "":
				if os.path.exists(arg) == True:
					dirs = os.listdir(arg)
					for _ in range(len(dirs)):
						print(dirs[counts])
						counts = counts + 1
				else:
					print(f"{arg}{data["message"]["ls_error"]}")
			else:
				dirs = os.listdir()
				for _ in range(len(dirs)):
					print(dirs[counts])
					counts = counts + 1
				
				
	else:
		if Path(f"{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]}").exists() == True:
			if commands == False:
				commands = True
				arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
				if os.name == "nt":
					log = os.system(f"{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]} {arg}")
				else:
					log = os.system(f"./{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]} {arg}")
		if Path(f"{main}/cmd/{load_cmd.split()[0]}/index.py").exists() == True:
			if commands == False:
				commands = True
				arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
				log = os.system(f"{data["execution"]} {main}/cmd/{load_cmd.split()[0]}/index.py {arg}")
				if log == 1:
					print(f"\033[31m{data["message"]["python_error"]}\033[0m")
		
		if Path(load_cmd.split()[0]).suffix != "":
			if Path(load_cmd.split()[0]).exists() == True:
				if commands == False:
					commands = True
					arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip().strip()
					if os.name == "nt":
						log = os.system(f"{load_cmd.split()[0]} {arg}")
					else:
						log = os.system(f"./{load_cmd.split()[0]} {arg}")
		
		if commands == False:
			commands = True
			log = os.system(cmd)


def cmd_load(loader: str):
	global cmd
	global cmd_count
	global cmds
	global prompt
	cmd_count = 0
	cmds = loader.lstrip()
	for _ in range(len(cmds.split("&&"))):
		command(cmds.split("&&")[cmd_count])
		prompt = prompt_load.read_text(encoding="UTF-8").replace("$path$", f"{os.getcwd().replace("C:", "").replace("\\", "/")}").replace("$user$", f"{data["username"]}{data["logo"]}{os_name}")
		cmd_count = cmd_count + 1
	

if bashrc != "":
	file_lines = bashrc.splitlines()
	file_count = 0
	for _ in range(len(file_lines)):
		cmd_load(file_lines[file_count])
		file_count = file_count + 1


if terminal_mode == True:
	print("")
	while True:
		try:
			cmd = input(prompt)
			if cmd != "":
				cmd_load(cmd)
			if exits == True:
				break
			print("")
		except (KeyboardInterrupt, EOFError):
			if os.name == "nt":
				print("\033[31m^C\033[0m")
			angry_mater = angry_mater + 1
			if angry_mater >= 87:
				print(data["message"]["secret"])
			if os.name == "nt":
				print("")
			else:
				print("\n")
else:
	if args.c != "none" and args.f != "none":
		print(data["message"]["wrong_arg"])
	else:
		if args.c != "none":
			cmd_load(args.c)
		if args.f != "none":
			if Path(args.f).suffix == ".sh":
				if Path(args.f).exists() == True:
					with open(args.f, "r", encoding="UTF-8") as file_load:
						load_file = file_load.read()
					file_lines = load_file.splitlines()
					file_count = 0
					while True:
						arg2 = file_lines[file_count]
						if arg2.split()[0] == "goto":
							if arg2.split()[1] in move_data:
								file_count = data[arg2.split()[1]]
						cmd_load(file_lines[file_count])
						if move != "none":
							data[move] = file_count
							move = "none"
						file_count = file_count + 1
						if file_count == len(file_lines):
							break
				else:
					print(f"{args.f}{data["message"]["wrong_file2"]}")
			else:
				print(data["message"]["wrong_file"])
