#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gethostname

HEADER = 20
# Listando arquivos no diretório atual ###
def listDirectory():
    localFiles = os.listdir(os.getcwd())                                # Lê o caminho do arquivo
    files = ""
    for file in localFiles:                                             # Cria uma lista que contém a listagem de arquivos
        files += file + '\t'
    return files

### Upload de arquivos para o servidor ###
'''
def putFile(con):                                             # Em produção...
    vetorBytes = []
    bytes_rcvd = 0
    MSGLEN = len(os.getcwd() + '/envio.darksouls')
    while bytes_rcvd < MSGLEN:
        bytes_uploaded = con.recv(min(MSGLEN - bytes_rcvd, 2048))
        if bytes_uploaded == '':
            raise RuntimeError("conexão interrompida")
        vetorBytes.append(bytes_uploaded)
        bytes_rcvd = bytes_rcvd + len(bytes_uploaded)
    vetorBytes = str(vetorBytes)
    with open('test.txt', 'w') as f:
        f.write(vetorBytes)
'''
# Upload de arquivos para o servidor
def recvFile(SOCKET):

    with open('ArquivoJPG.jpg') as f:
        pass
    data = SOCKET.recv(1024)
    while(data):
        data = SOCKET.recv(1024)
        f.write(data)
    f.close()
    SOCKET.close()
    print('Recebido')
### Remoção de arquivos do servidor ###
def removeFile():                                                       # Em produção...
    pass

### Download de arquivos ###
def getFile(fileName):
    print(fileName)                                                  # Em produção...
    #f = open(os.getcwd() + f'/{fileName}', 'rb')                        


def main():
    HOST = gethostbyname(gethostname())                   # Endereco IP do Servidor
    PORT = int(sys.argv[1])                                             # Porta que o servidor esta                 
    SOCKET = socket(AF_INET, SOCK_STREAM)          # Socket do servidor
    ADDRESS = (HOST, PORT)                                              # Endereço do servidor/porta
    SOCKET.bind(ADDRESS)                                                # Designa o endereço e porta para o socket
    SOCKET.listen(10)                                                   # Escuta em até 10 conexões
    while True:
        con, cliente = SOCKET.accept()                                  # Aceita a conexão do cliente
        print ('Conectado por', cliente)                                    
        while True:
            MSG = con.recv(1024)                        # Recebe a mensagem do cliente em bytes
            print MSG
            if not MSG: pass
            elif MSG[:4] == 'list':                                         # Verifica se a mensagem é de listagem e decodifica
                con.send(bytes(listDirectory()))
                con.close()            # Responde com a listagem do diretório           
            elif MSG[:3] == 'put':
                print 'hue'
                recvFile(con)

            else:
                break
            con.close()
            break                                                # Em andamento ...
        print ('Finalizando conexao do cliente', cliente)
        con.close()                                                     # Fecha a conexão
    SOCKET.close()

if __name__ == "__main__":
    main()


