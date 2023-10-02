import numpy as np


def frequencia_relativa(freq):
    result = []
    total = np.sum(freq)
    for f in freq:
        result.append(np.round(f / total * 100.0, 2))

    erro = 100.00 - np.sum(result)
    index = result.index(np.max(result))
    if 0.00 < erro or erro < 0:
        result[index] = result[index] + erro
    for l in result:
        print(f'{l:.3f}', end='\t')
    print(f'{np.sum(result):.3f}')


def media(valores):
    '''
    Funça media, somo todos os valores na lista recebida
    e imprime a sama pelo número de elementos
    :param valores:
    '''
    n = len(valores)  # numero de elementos
    s = 0  # Soma dos valores observados
    for v in valores:
        s += v
    media = s / n
    print(media)

def mediana(valores):
    '''
    Funçao mediana, localiza o valor do centro para n impar
    e a soma dos dois valores centrais para n par
    :param valores:
    '''
    dados_idades = np.sort(valores)
    n = len(dados_idades)
    if n % 2 != 0:
        inicio = (n // 2)
        mediana = dados_idades[inicio]
        print(mediana)
    else:
        inicio = (n // 2) - 1
        fim = (n // 2) + 1
        media = dados_idades[inicio : fim]
        print(media)