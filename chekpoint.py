import random
import time

#Merge Sort
def merge_sort(list):
    if len(list) > 1:
        meio = len(list) // 2
        esquerda = list[:meio]
        direita = list[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                list[k] = esquerda[i]
                i += 1
            else:
                list[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            list[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            list[k] = direita[j]
            j += 1
            k += 1

#Insertion Sort
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

#Selection Sort
def selection_sort(list):
    for i in range(len(list)):
        min_index = i

        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

#Bubble Sort
def bubble_sort(list):
    n = len(list)
    for i in range(n):
       
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def get_time(func, lista):
    inicio = time.time()
    func(lista)
    fim = time.time()   
    return fim - inicio

#principal
def menu():
    print("Escolha um algoritmo de ordenação:")
    print("1. Merge Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. Bubble Sort")

    opcao = input("Digite o número da opção desejada: ")

    n = int(input("Digite o tamanho da lista a ser ordenada: "))
    lista = [random.randint(1, 1000) for i in range(n)]  

    if opcao == '1':
        tempo = get_time(merge_sort, lista)
        print(f"Lista Ordenada em: {tempo:.2f}")
        
    elif opcao == '2':
        tempo = get_time(insertion_sort, lista)
        print(f"Lista Ordenada em: {tempo:.2f}")
        
    elif opcao == '3':
        tempo = get_time(selection_sort, lista)
        print(f"Lista Ordenada em: {tempo:.2f}")

    elif opcao == '4':
        tempo = get_time(bubble_sort, lista)
        print(f"Lista Ordenada em: {tempo:.2f}")
        

    print(lista)

menu()
