#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import os
import sys

def main():
   HOST = sys.argv[1]                                          # Endereco IP do Servidor.
   PORT = int(sys.argv[2])                                     # Porta que o Servidor esta.
   MSG = str(sys.argv[3])                                      # Mensagem que o cliente envia
   SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket SOCKET do cliente
   SERVER = (HOST, PORT)                                       # Endereço e porta do servidor
   SOCKET.connect(SERVER)                                      # Conexão estabelecida entre cliente/servidor


###  Conexão com o servidor ###
   if(MSG) == 'list':                                          # Lista os diretórios do servidor
      SOCKET.sendto(bytes(MSG, 'utf-8'), SERVER)
      filesList = str(SOCKET.recv(4096), 'utf-8')              # Recebe a cadeia de bytes e a transforma em string
      SOCKET.close()
      print(filesList)                                         # Mostra a listagem do diretório
   elif(MSG) == 'put':
      print('Enviando o arquivo: {sys.argv[4]}')
      with open(os.getcwd() + '/{sys.argv[4]}', 'rb') as f:
         file = f.read()
      SOCKET.sendto(MSG.encode(), SERVER)
      SOCKET.sendall(os.stat(os.getcwd() + '/{sys.argv[4]}').st_size) # Notifica ao servidor o tamanho do arquivo
      SOCKET.sendfile(file)                                    # Envia o arquivo para o servidor



if __name__ == '__main__':
   main()