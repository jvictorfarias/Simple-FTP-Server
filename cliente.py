#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import AF_INET, SOCK_STREAM, gethostbyname, gethostname, socket
import os
import sys
import time


def uploadFile(SOCKET):
   length = len(sys.argv[5])
   sent = SOCKET.send(sys.argv[5])
      # Envia a opção escolhida
   while(sent < length):
      sent += SOCKET.send(sys.argv[sent:])
   f = open('./' + sys.argv[4], 'r')
   data = f.read(1024)
   while(data):
      SOCKET.send(data)
      data = f.read(1024)
   f.close()
   SOCKET.close()
   print('Enviado')

def main():
   HOST = sys.argv[1]                                          # Endereco IP do Servidor.
   PORT = int(sys.argv[2])                                     # Porta que o Servidor esta.
   MSG = str(sys.argv[3])                                      # Mensagem que o cliente envia
   SOCKET = socket(AF_INET, SOCK_STREAM)                # Socket SOCKET do cliente
   SERVER = (HOST, PORT)                                       # Endereço e porta do servidor
   SOCKET.connect(SERVER)                                      # Conexão estabelecida entre cliente/servidor                          

###  Conexão com o servidor ###
   if(MSG) == 'list':
      SOCKET.send(MSG)                                          # Lista os diretórios do servidor
      filesList = str(SOCKET.recv(1024))              # Recebe a cadeia de bytes e a transforma em string
      SOCKET.close()
      print(filesList)                                         # Mostra a listagem do diretório
   elif(MSG) == 'put':
      length = len(MSG)
      sent = SOCKET.send(MSG)
      # Envia a opção escolhida
      while(sent < length):
         sent += SOCKET.send(MSG[sent:])
      
      time.sleep(1)
      uploadFile(SOCKET)

   elif(MSG) == 'get':
      pass
   elif(MSG) == 'rm':
      pass


if __name__ == '__main__':
   main()