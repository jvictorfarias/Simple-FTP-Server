#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import socket

# Listando arquivos no diret0rio atual
def listDirectory():
    localFiles = os.listdir(os.getcwd())
    files = ""
    for file in localFiles:
        files += file + '\t'
    return files


def getFile(fileName):
    f = open(os.getcwd() + '/{fileName}', 'rb')
    return f


def main():
    HOST = socket.gethostbyname(socket.gethostname())      # Endereco IP do Servidor
    PORT = int(sys.argv[1]) # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(10)
    while True:
        con, cliente = tcp.accept()
        print ('Conectado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            elif msg == b'list': con.sendall(bytes(listDirectory(), 'utf-8'))
        print ('Finalizando conexao do cliente', cliente)
        con.close()


if __name__ == "__main__":
    main()


