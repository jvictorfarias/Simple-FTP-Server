#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import socket

### Listando arquivos no diretório atual ###
def listDirectory():
    localFiles = os.listdir(os.getcwd())                                # Lê o caminho do arquivo
    files = ""
    for file in localFiles:                                             # Cria uma lista que contém a listagem de arquivos
        files += file + '\t'
    return files


def putFile():                                                          # Em produção...
    pass

def removeFile():                                                       # Em produção...
    pass

### Download de arquivos ###
def getFile(fileName):                                                  # Em produção...
    f = open(os.getcwd() + '/{fileName}', 'rb')                        
    return f


def main():
    HOST = socket.gethostbyname(socket.gethostname())                   # Endereco IP do Servidor
    PORT = int(sys.argv[1])                                             # Porta que o servidor esta                 
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Socket do servidor
    ADDRESS = (HOST, PORT)                                              # Endereço do servidor/porta
    SOCKET.bind(ADDRESS)                                                # Designa o endereço e porta para o socket
    SOCKET.listen(10)                                                   # Escuta em até 10 conexões
    while True:
        con, cliente = SOCKET.accept()                                  # Aceita a conexão do cliente
        print ('Conectado por', cliente)                                    
        while True:
            MSG = bytes(con.recv(1024), 'utf-8')                        # Recebe a mensagem do cliente em bytes
            if not MSG: pass
            elif MSG == 'list':                                         # Verifica se a mensagem é de listagem e decodifica
                con.sendall(bytes(listDirectory(), 'utf-8'))            # Responde com a listagem do diretório
            elif MSG.count('put', 0, 3):                                # Recebe o arquivo do cliente e salva no servidor
                pass                                                    # Em andamento ...
        print ('Finalizando conexao do cliente', cliente)
        con.close()                                                     # Fecha a conexão


if __name__ == "__main__":
    main()


