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
    print(f'A média é {media:.3f}')


def mediana(valores):
    '''
    Funçao mediana, localiza o valor do centro para n impar
    e a soma dos dois valores centrais para n par
    :param valores:
    '''
    dados_idades = np.sort(valores)
    n = len(dados_idades)
    mediana = None
    if n % 2 != 0:
        inicio = (n // 2)
        mediana = dados_idades[inicio]
    else:
        inicio = (n // 2) - 1
        fim = (n + 2) // 2
        mediana = np.sum(dados_idades[inicio: fim]) // 2
    print(f'A Mediana é {mediana:.3f}')

def moda(valores):
    moda = valores.value_counts().keys()[0]
    print(f"A moda é {moda:.3f}")

#MEDIDA DE DISPERSÃO
# Variancia
# S^2 = (Somatório (x_i-media)^2) / (n - 1) de i = 1 ate i = n
# S^2 = (Somatório x_i^2-n*media^2) / (n - 1) de i = 1 ate i = n

def variancia(dados):
    soma = 0
    n = len(dados)
    media = np.sum(dados) / n
    for i in dados:
        soma += (i - media) ** 2
    var = soma / (n - 1)
    print(f'A Variancia é {var:.3f}')


def desvio_padrao(dados):
    """
    Raiz quadrada da Variância
    :param dados:
    :return:
    """
    soma = 0
    n = len(dados)
    media = np.sum(dados) / n
    for i in dados:
        soma += (i - media) ** 2
    var = soma / (n - 1)
    desv_pad = var ** .5
    print(f'O Desvio Padrão é {desv_pad:.3f}')


# Coeficiente de Variação
#    (Desvio Padrão) / Media
def coeficinete_variacao(dados):
    soma = 0
    n = len(dados)
    media = np.sum(dados) / n
    for i in dados:
        soma += (i - media) ** 2
    var = soma / (n - 1)
    desv_pad = var ** .5
    cv = desv_pad / media
    print(f'O CV é {cv:.3f}')