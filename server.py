#! /usr/bin/python3
import sys
import os
import ftplib
import socket

# Listando arquivos no diretório atual
def listaDiretorio():
    localFiles = os.listdir(os.getcwd())
    files = ""
    for file in localFiles:
        file += file + '\t'
    return file

def main():
    HOST = socket.gethostbyname(socket.gethostname())      # Endereco IP do Servidor
    PORT = int(sys.argv[1]) # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        print ('Concetado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            elif msg == b'list': print(listaDiretorio())
            print (cliente, msg)
        print ('Finalizando conexao do cliente', cliente)
        con.close()


if __name__ == "__main__":
    main()


