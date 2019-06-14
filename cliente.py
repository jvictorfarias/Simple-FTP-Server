#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
import os
import sys
import time


def listFiles(SOCKET):
   filesList = str(SOCKET.recv(1024))              # Recebe a cadeia de bytes e a transforma em string
   SOCKET.close()
   print(filesList)                                # Mostra os arquivos que existem no diretório do servidor

def uploadFile(SOCKET):
   print('Enviando arquivo: ' + sys.argv[4]) 
   length = len(sys.argv[5])
   sent = SOCKET.send(sys.argv[5])                 # Essa parte envia o nome do arquivo a ser salvo no servidor
   while(sent < length):                     
      sent += SOCKET.send(sys.argv[sent:])
   f = open('./' + sys.argv[4], 'r')               # Leitura do arquivo para envio
   data = f.read(1024)
   while(data):                                    # Enquanto houver dados no buffer, ele continua enviando
      SOCKET.send(data)
      data = f.read(1024)
   f.close()
   SOCKET.close()
   print('Envio completo, salvo no servidor como: ' + sys.argv[5])

def removeFile(SOCKET):
   print('Removendo arquivo : ' + sys.argv[4] ) 
   length = len(sys.argv[4])
   sent = SOCKET.send(sys.argv[4])                 # Essa parte envia o nome do arquivo a ser removido no servidor
   while(sent < length):                     
      sent += SOCKET.send(sys.argv[sent:])
   SOCKET.close()
   print('Arquivo removido.')

def main():
   HOST = sys.argv[1]                                          # Endereco IP do Servidor.
   PORT = int(sys.argv[2])                                     # Porta que o Servidor esta.
   MSG = str(sys.argv[3])                                      # Mensagem que o cliente envia
   SOCKET = socket(AF_INET, SOCK_STREAM)                       # Socket SOCKET do cliente
   SERVER = (HOST, PORT)                                       # Endereço e porta do servidor
   SOCKET.connect(SERVER)                                      # Conexão estabelecida entre cliente/servidor                          
   length = len(MSG)
   sent = SOCKET.send(MSG)
   while(sent < length):                                       # Envia a opção escolhida
         sent += SOCKET.send(MSG[sent:])
   time.sleep(1)
###  Conexão com o servidor ###
   if(MSG) == 'list':                                          # Lista os diretórios do servidor
      listFiles(SOCKET)                                        
   elif(MSG) == 'put':                                         # Adiciona arquivos no servidor
      uploadFile(SOCKET)
   elif(MSG) == 'get':                                         # Download de arquivos do servidor
      pass
   elif(MSG) == 'rm':                                          # Remoção de arquivos do servidor
      removeFile(SOCKET)


if __name__ == '__main__':
   main()