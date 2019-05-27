#!/usr/bin/python3
import socket
import sys

def main():
   HOST = sys.argv[1]      # Endereco IP do Servidor.
   PORT = int(sys.argv[2]) # Porta que o Servidor esta.
   tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   dest = (HOST, PORT)
   tcp.connect(dest)
   msg = "list"
   tcp.sendto(msg.encode(), ('192.168.0.110', 33000))
   con, servidor = tcp.accept()
   print(con, servidor)

   tcp.close()

if __name__ == '__main__':
   main()