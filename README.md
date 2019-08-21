## Simple FTP Server
O programa implementa as funções de LISTAGEM ('list'), DOWNLOAD ('get'), UPLOAD ('put') e REMOÇÃO ('rm').

Exemplos de execução:

    O servidor executa passando como parâmetro apenas a porta.
        usr@usr-pc:/arquiteturatcpip$ ./server.py [PORTA]
    
    O cliente passa parâmetros de acordo com a funcionalidade requerida.
    LISTAGEM:
        usr@usr-pc:/arquiteturatcpip$ ./cliente [IP DO SERVIDOR] [PORTA DE EXECUÇÃO DO SERVIDOR] list
    DOWNLOAD:
        usr@usr-pc:/arquiteturatcpip$ ./cliente [IP DO SERVIDOR] [PORTA DE EXECUÇÃO DO SERVIDOR] get [NOME DO ARQUIVO A SER BAIXADO] [NOVO NOME DO ARQUIVO BAIXADO]
    UPLOAD:
        usr@usr-pc:/arquiteturatcpip$ ./cliente [IP DO SERVIDOR] [PORTA DE EXECUÇÃO DO SERVIDOR] put [NOME DO ARQUIVO A SER ENVIADO] [NOVO NOME DO ARQUIVO ENVIADO]
    REMOÇÃO:
        usr@usr-pc:/arquiteturatcpip$ ./cliente [IP DO SERVIDOR] [PORTA DE EXECUÇÃO DO SERVIDOR] rm [NOME DO ARQUIVO A SER REMOVIDO]
