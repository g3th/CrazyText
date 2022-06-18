import time
from header import header


while True:
	print('\x1bc')
	header()
	try:		
		crazy = input('Enter text: ')
		speed = float(input('\nEnter speed(1-10): ')); print("\x1bc")
		if speed < 1 or speed > 10:
			print("\x1bc"); pass
		else:
			speed = '{:.2f}'.format(speed/100)
			break
	except Exception:
		pass
	
def string(s):
	time.sleep(float(speed))
	print("\x1bc");header()
	print(s,end='',flush=True)
	if len(s) ==0:
		return ''
	print (string(s[:len(s)-1]),end='',flush=True)
	time.sleep(float(speed))
	if len(s) != len(crazy+' '):
		print("\x1bc");header()
	return s

string(crazy+' '); time.sleep(0.9);print("\n")
