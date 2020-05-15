#Desenvolvido por Maximiliano Meyer

def fifo(lista, tempo):
    trocas_total, soma_total, x_processo, processo_atual = 0, 0, 0, 1
    qtd_processos = len(lista)

    print()
    print('{:^80}'.format(' Relatório First In First Out - FIFO '))
    print('-' * 80)
    print('{:^15}{:^20}{:^25}{:^15}'.format('Processo', 'Trocas de estado', 'Ciclos', 'Tempo gasto (ms)'))
    print('-' * 80)

    while processo_atual <= qtd_processos:
        estado, flag = 'a', 'a'  # Estado pode ser 'a' para apto, 'e' para executando e 'b' para bloqueado
        pos, trocas, soma = 1, 0, 0
        while pos <= len(lista[x_processo]) - 1:
            if lista[x_processo][pos] == 'CPU':
                soma += 1  # Para registrar o número de ciclos
                flag = 'e'  # Para controlar o número de trocas de estados
                if flag != estado:
                    trocas += 1
                    estado = flag
            else:
                soma += 1
                flag = 'b'
                if flag != estado:
                    trocas += 1
                    estado = flag
            pos += 1
        print('{:^15}{:^20}{:^25}{:^15}'.format(processo_atual, trocas, soma, soma * tempo))
        x_processo += 1
        trocas_total += trocas
        if processo_atual != qtd_processos:
            soma_total += soma
        processo_atual += 1
    print('-' * 95)
    print('{:^60}{:^15}{:^25}'.format('TOTAL', 'TEMPO MÉDIO', 'DESVIO PADRÃO'))
    print('-' * 95)
    print('{:^15}{:^20}{:^26}{:^15}{:^23}'.format(processo_atual - 1, trocas_total, soma_total,
                                                  (soma_total * tempo) / (processo_atual - 1), "???"))
    input('\nAperte qualquer tecla para voltar ao menu!')


def sjf(lista, tempo):
    trocas_total, soma_total, x_processo, processo_atual = 0, 0, 0, 1
    qtd_processos = len(lista)
    lista.sort(key=len)

    print()
    print('{:^80}'.format(' Relatório Shortest First Job - SJS'))
    print('-' * 80)
    print('{:^15}{:^20}{:^25}{:^15}'.format('Processo', 'Trocas de estado', 'Ciclos', 'Tempo gasto (ms)'))
    print('-' * 80)

    while processo_atual <= qtd_processos:
        estado, flag = 'a', 'a'  # Estado pode ser 'a' para apto, 'e' para executando e 'b' para bloqueado
        pos, trocas, soma = 1, 0, 0
        while pos <= len(lista[x_processo]) - 1:
            if lista[x_processo][pos] == 'CPU':
                soma += 1  # Para registrar o número de ciclos
                flag = 'e'  # Para controlar o número de trocas de estados
                if flag != estado:
                    trocas += 1
                    estado = flag
            else:
                soma += 1
                flag = 'b'
                if flag != estado:
                    trocas += 1
                    estado = flag
            pos += 1
        print('{:^15}{:^20}{:^25}{:^15}'.format(lista[x_processo][0], trocas, soma, soma * tempo))
        x_processo += 1
        trocas_total += trocas
        if processo_atual != qtd_processos:
            soma_total += soma
        processo_atual += 1
    print('-' * 95)
    print('{:^60}{:^15}{:^25}'.format('TOTAL', 'TEMPO MÉDIO', 'DESVIO PADRÃO'))
    print('-' * 95)
    print('{:^15}{:^20}{:^26}{:^15}{:^23}'.format(processo_atual - 1, trocas_total, soma_total,
                                                  (soma_total * tempo) / (processo_atual - 1), "???"))
    input('\nAperte qualquer tecla para voltar ao menu!')


def rr(lista, tempo):
    trocas_total, soma_total, x_processo, tempo_aux, ciclo_inicio, ciclo_fim = 0, 0, 0, 0, 0, 0
    qtd_processos = len(lista)

    print('\n{:^105}'.format(' Relatório Round Robin - RR'))
    print('-' * 105)
    print('{:^15}{:^15}{:^15}{:^15}{:^25}{:^13}'.format('Processo', 'Trocas estado', 'ciclo inicio', 'ciclo final',
                                                        'Tempo gasto (ms)', 'execuções restantes'))
    print('-' * 105)

    while len(lista) > 0:
        tempo_aux, trocas, soma = 0, 0, 0
        estado, flag = 'a', 'a'  # Estado pode ser 'a' para apto, 'e' para executando e 'b' para bloqueado

        ciclo_inicio = ciclo_fim + 1
        try:
            while tempo_aux < tempo and len(lista[x_processo]) > 1:
                pos = 1
                if lista[x_processo][pos] == 'CPU':
                    soma += 1  # Para registrar o número de ciclos
                    flag = 'e'  # Para controlar o número de trocas de estados
                    lista[x_processo].pop(pos)
                    ciclo_fim += 1
                    if flag != estado:
                        trocas += 1
                        estado = flag
                else:
                    soma += 1
                    flag = 'b'
                    lista[x_processo].pop(pos)
                    ciclo_fim += 1
                    if flag != estado:
                        trocas += 1
                        estado = flag
                tempo_aux += 1
                if len(lista[x_processo]) == 1:
                    print(
                        '{:^15}{:^15}{:^15}{:^15}{:^25}{:^15}'.format(lista[x_processo][0], trocas, ciclo_inicio,
                                                                      ciclo_fim,
                                                                      soma * tempo,
                                                                      len(lista[x_processo]) - 1))

                    lista.pop(x_processo)
                    ciclo_inicio = ciclo_fim + 1
                    soma_total += soma
                    tempo_aux, soma = 0, 0
                    if x_processo >= len(lista):
                        x_processo = 0
            if len(lista) > 1:
                print(
                    '{:^15}{:^15}{:^15}{:^15}{:^25}{:^15}'.format(lista[x_processo][0], trocas, ciclo_inicio, ciclo_fim,
                                                                  soma * tempo,
                                                                  len(lista[x_processo]) - 1))
                x_processo += 1

            trocas_total += trocas
            if len(lista) > 1:
                soma_total += soma
            if x_processo == len(lista):
                x_processo = 0

        except:
            print('-' * 105)
            print('{:^105}'.format('TOTAL'))
    print('-' * 105)
    print(
        '{:^15}{:^15}{:^15}{:^15}{:^25}{:^15}'.format('Processos', 'Trocas estado', 'ciclos totais', 'tempo total (ms)',
                                                      'Tempo médio (ms)', 'Desvio padrão'))
    print('-' * 105)
    print('{:^15}{:^15}{:^15}{:^15}{:^25}{:^15}'.format(qtd_processos, trocas_total, ciclo_fim, soma_total * tempo,
                                                        (soma_total * tempo) / 8, '???'))
    input('\nAperte qualquer tecla para voltar ao menu!')


while True:
    op = int(input("\n1 - First In First Out - FIFO\n2 - Shortest Job First - SJF\n3 - Round Robin - RR\n4 - Sair\n\nSua resposta: "))
    tempo = int(input("Informe a fatia de tempo desejada: "))

    lista, cont = [], 0
    nomeArquivo = 'entrada.txt'
    f = open(nomeArquivo, 'r')

    for a in f.readlines():
        linha = a.replace('\n', '')
        lista.append(linha.split(";"))
        cont += 1

    if op == 1:
        fifo(lista, tempo)
    elif op == 2:
        sjf(lista, tempo)
    elif op == 3:
        rr(lista, tempo)
    else:
        exit()
