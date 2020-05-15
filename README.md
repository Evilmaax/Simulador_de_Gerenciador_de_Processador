# Simulador de Gerenciador de Processador

Este projeto foi desenvolvido para a disciplina de Sistemas Operacionais, do 5º semestre do curso de Ciências da Computação da Universidade de Santa Cruz do Sul. O projeto foi desenvolvido por mim e 2 colegas.

O desafio consistia em criar um simulador que fizesse o gerenciamento do processador utilizando algoritmos de escalonamento de curto prazo. A fatia de tempo utilizada deve ser escolhida pelo usuário.
A entrada de dados ocorre por meio do arquivo **entrada.txt**, onde cada linha representa um processo. 

O primeiro campo é o identificador do processo; Os campos seguintes indicam o tipo de operação que o processo irá fazer a cada ciclo de processador. Por exemplo, a linha a seguir indica que o processo de id 777 começa com 5 ciclos de processador, depois solicita uma operação de entrada e saída que irá durar 2 ciclos e por fim executa mais 2 ciclos de CPU. 

**777;CPU;CPU;CPU;CPU;CPU;ES;ES;CPU;CPU**

Como saída o programa deve exibir um log (em tela ou arquivo) para cada algoritmo de escalonamento com os seguintes dados:

* Sequência de uso do processador (qual processo ocupou cada fatia de tempo);
* Número total de trocas de contexto;
* Tempo médio de espera (de todos os processos do arquivo);
* Variância do tempo de espera (de todos os processos do arquivo).

O código foi desenvolvido em Python 3.6
