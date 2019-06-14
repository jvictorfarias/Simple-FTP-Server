#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gethostname


# Listando arquivos no diretório atual #
def listDirectory():
    localFiles = os.listdir(os.getcwd())                                # Lê o caminho do arquivo
    files = ""
    for file in localFiles:                                             # Cria uma lista que contém a listagem de arquivos
        files += file + '\t'
    return files


# Upload de arquivos para o servidor #
def recvFile(SOCKET):
    fileName = SOCKET.recv(1024)                                        # Recebe o nome do arquivo
    f = open('./' + str(fileName), 'w')                                 # Abre o arquivo que irá receber dados do cliente
    data = SOCKET.recv(1024)
    while(data):                                                        # Enquanto houver dados, salva no arquivo
        f.write(data)
        data = SOCKET.recv(1024)
    f.close()
    SOCKET.close()
    print('Recebido')

# Remoção de arquivos do servidor #
def removeFile(SOCKET):
    fileName = SOCKET.recv(1024)
    os.remove('./' + str(fileName))
    time.sleep(3)
    SOCKET.close()                                   # Em produção...
# Download de arquivos #
def getFile(fileName):
    print(fileName)                                                     # Em produção...
    #f = open(os.getcwd() + f'/{fileName}', 'rb')                        


def main():
    HOST = gethostbyname(gethostname())                                 # Endereco IP do Servidor
    PORT = int(sys.argv[1])                                             # Porta que o servidor esta                 
    SOCKET = socket(AF_INET, SOCK_STREAM)                               # Socket do servidor
    ADDRESS = (HOST, PORT)                                              # Endereço do servidor/porta
    SOCKET.bind(ADDRESS)                                                # Designa o endereço e porta para o socket
    SOCKET.listen(10)                                                   # Escuta em até 10 conexões
    while True:
        con, cliente = SOCKET.accept()                                  # Aceita a conexão do cliente
        print ('Servidor FTP executando.')                                    
        while True:
            MSG = con.recv(1024)                                        # Recebe a mensagem do cliente
            if not MSG: pass
            elif MSG == 'list':                                        
                con.send(bytes(listDirectory()))                        # Responde com a listagem do diretório                   
            elif MSG == 'put':
                recvFile(con)                                           # Aciona a função de recepção
            elif MSG == 'rm':
                removeFile(con)

            else:
                break
            con.close()
            break                                                # Em andamento ...
        print ('Finalizando conexao do cliente', cliente)
        con.close()                                                     # Fecha a conexão
    SOCKET.close()

if __name__ == "__main__":
    main()


