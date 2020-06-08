from random import randint
import time


# ------------------------------------------------------------------------------


def bubbleSort(lista):  # Maior vai pro ultimo
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista


# ------------------------------------------------------------------------------


def insertionSort(lista):  # sorted (esq) x unsorted (dir)
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:  # se j>=0 e i-1 > i, entra aqui
            lista[j + 1] = lista[j]  # lis[j+1] troca com lis[j]
            j = j - 1  # vai ordenando td mundo antes da chave
        lista[j + 1] = chave
    return lista


# ------------------------------------------------------------------------------


def quicksort(lista, inicio=0, fim=None):
    if fim == None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)  # irá deixar o "fim" no local ideal p
        quicksort(lista, inicio, p - 1)  # quicksort na esquerda
        quicksort(lista, p + 1, fim)  # quicksort na direita
    return lista


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:  # se o pivot >= li[j], entao:
            lista[j], lista[i] = lista[i], lista[j]  # lis[i] troca com lis[j]
            i = i + 1  # e i aumenta 1
        else:  # se não,
            continue  # nada ocorre
    lista[i], lista[fim] = lista[fim], lista[i]  # agora o "fim" ta no seu canto
    return i


# ------------------------------------------------------------------------------


def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)  # quebrando esquerda
        mergesort(lista, meio, fim)  # quebrando direita
        merge(lista, inicio, meio, fim)  # juntando ordenado
    return lista


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]  # lis de inicio ate meio -1
    right = lista[meio:fim]  # lis de meio ate fim -1
    topesq, topdir = 0, 0
    for i in range(inicio, fim):
        if topesq >= len(left):  # ja viu td em left
            lista[i] = right[topdir]
            topdir = topdir + 1
        elif topdir >= len(right):  # ja viu td em right
            lista[i] = left[topesq]
            topesq = topesq + 1
        elif left[topesq] < right[topdir]:  # l[te] < r[td]
            lista[i] = left[topesq]
            topesq = topesq + 1
        else:  # l[te] > r[td]
            lista[i] = right[topdir]
            topdir = topdir + 1


# ------------------------------------------------------------------------------


def shellSort(lista):
    gap = len(lista) // 2
    while gap > 0:  # garante que va até o gap == 1
        for i in range(gap, len(lista)):  # garante que andará a lista toda
            atual = lista[i]
            while i >= gap and lista[i - gap] > atual:  # garante que passará em todos com distância gap
                lista[i] = lista[i - gap]
                i = i - gap
            lista[i] = atual
        gap = gap // 2

    return lista


# ------------------------------------------------------------------------------


def HeapAdjust(lista, inicio, fim):  # o root tem q ser o max da lista, depois troca com o
    root = inicio  # o filho q esta em ultimo na lista sequencial e então sai da Heap,
    while True:  # uma vez que ele já em seu lugar, isso acontece até sobrar apenas 1 elemento
        filho = 2 * root + 1
        if filho > fim:
            break
        if filho + 1 <= fim and lista[filho] < lista[filho + 1]:
            filho += 1

        if lista[root] < lista[filho]:
            lista[root], lista[filho] = lista[filho], lista[root]
            root = filho
        else:
            break


def HeapSort(lista):
    inicio = len(lista) // 2 - 1  # inicio = metade - 1
    for inicio in range(inicio, - 1, -1):  # Montando Heap
        HeapAdjust(lista, inicio, len(lista) - 1)
    for fim in range(len(lista) - 1, 0, -1):  # Desmontando Heap
        lista[0], lista[fim] = lista[fim], lista[0]
        HeapAdjust(lista, 0, fim - 1)
    return lista


# ------------------------------------------------------------------------------


def combSort(lista):  # ideia é tipo o shell e bubble, mas sem o for
    escolhe = 1.3  # a condição de parada é o parte <= 1
    parte = len(lista)

    while parte > 1:
        parte = int(float(parte) / escolhe)
        i = 0

        while parte + i < len(lista):
            if lista[i] > lista[i + parte]:
                lista[i], lista[i + parte] = lista[i + parte], lista[i]

            i += 1

    return lista


# ------------------------------------------------------------------------------


lista = []
for i in range(20000):
    lista.append(randint(1, 5000))

listaBuble = lista.copy()
listaInsetion = lista.copy()
listaQuick = lista.copy()
listaMerge = lista.copy()
listaShell = lista.copy()
listaHeap = lista.copy()
listaComb = lista.copy()
inicioBubble = time.time()

print(bubbleSort(listaBuble))
fimBubble = time.time()
tempoBubble = fimBubble - inicioBubble
print('Tempo Bubble: ', tempoBubble)

inicioinsertion = time.time()
print(insertionSort(listaInsetion))
fiminsertion = time.time()
tempoInsertion = fiminsertion - inicioinsertion
print('Tempo do insertion:', tempoInsertion)

inicioQuick = time.time()
print(quicksort(listaQuick))
fimQuick = time.time()
tempoQuick = fimQuick - inicioQuick
print('Tempo do Quick ', tempoQuick)

inicioMerge = time.time()
print(mergesort(listaMerge))
fimMerge = time.time()
tempoMerge = fimMerge - inicioMerge
print(' Tempo do Merge: ', tempoMerge)

inicioShell = time.time()
print(shellSort(listaShell))
fimShell = time.time()
tempoShell = fimShell - inicioShell
print('Tempo do Shell: ', tempoShell)

inicioHeap = time.time()
print(HeapSort(listaHeap))
fimHeap = time.time()
tempoHeap = fimHeap - inicioHeap
print('Tempo de Heap: ', tempoHeap)

inicioComb = time.time()
print(combSort(listaComb))
fimComb = time.time()
tempoComb = fimComb - inicioComb
print('Tempo do Comb: ', tempoComb)

melhor = min(tempoBubble, tempoInsertion, tempoHeap, tempoShell, tempoMerge, tempoQuick, tempoComb)
if melhor == tempoBubble:
    print('\nO melhor é o BubbleSort')
elif melhor == tempoInsertion:
    print('\nO melhor é o InsertionSort ')
elif melhor == tempoHeap:
    print('\nO melhor é o HeapSort')
elif melhor == tempoShell:
    print('\nO melhor é o ShellSort')
elif melhor == tempoMerge:
    print('\nO melhor é o MergeSort')
elif melhor == tempoQuick:
    print('\nO melhor é o QuickSort')
else:
    print('\nO melhor é o CombSort')
print('Com: ', melhor)
