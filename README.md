Trabalho final da disciplina de Internet e Arquitetura TCP-IP

Nome da Equipe: Jamerson Aguiar     Nº 418866,
                João Victor Farias  Nº 418082

Foi utilizada a linguagem Python na versão 2.7.15 para a implementação do trabalho.
Não foram utilizadas bibliotecas ou ferramentas externas, tudo que foi utilizado está presente na linguagem em questão.

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