import socket
import sys 
import os


host = ''
port = 9000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host,port))
except socket.error as msg:
	sys.exit()



def conexion():
	s.listen(10)
	conn, addr = s.accept()
	os.system('say "hey"')
	equipo = socket.gethostname()
	ip = socket.gethostbyname(equipo)

	print("ip : " + ip)
	print("nombre : " + equipo)
	print('>>> User: ' +addr[0] + ' --> ' + str(addr[1]) + ' 🙋‍♂️ ')
	print("\n")

	while True:
		s.listen(10)
		conn, addr = s.accept()
		os.system('say "hey"')
		print('>>> User: ' +addr[0] + ' --> ' + str(addr[1]) + ' 🙋‍♂️ ')
		print("\n")


conexion()









	