from random import randint

def header():
	print('\033[38;5;'+str(randint(80,100))+'m        ____       _____            __  ______    ______')
	print('\033[38;5;'+str(randint(80,120))+'m  _____/ __ \____ /__  /  __  __   / /_/ ____/  _/_  __/ ')
	print('\033[38;5;'+str(randint(80,120))+'m / ___/ /_/ / __ `/ / /  / / / /  / __/ __/ | |/_// /    ')
	print('\033[38;5;'+str(randint(80,120))+'m/ /__/ _, _/ /_/ / / /__/ /_/ /  / /_/ /____>  < / /     ')
	print('\033[38;5;'+str(randint(80,120))+'m\___/_/ |_|\__,_/ /____/\__, /   \__/_____/_/|_|/_/      ')
	print('\033[38;5;'+str(randint(80,120))+'m                       /____/                            ')
	print('\033[38;5;'+str(randint(80,120))+'m'+'-'*80)
	print('\033[38;5;'+str(randint(80,120))+'mText scroller using simple recursion')
	print('\033[38;5;'+str(randint(80,120))+'m'+'-'*80+'\n\n')
