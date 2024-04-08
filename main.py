import random
import time

class OrdenacaoLinear:
    @staticmethod
    def insertion_sort(a):
        for sort_len in range(1, len(a)):
            cur_item = a[sort_len]
            insert_idx = sort_len
            while insert_idx > 0 and cur_item < a[insert_idx - 1]:
                a[insert_idx] = a[insert_idx - 1]
                insert_idx += -1
            a[insert_idx] = cur_item
        return a

    @staticmethod
    def selection_sort(arr):
        sort_idx = 0
        while sort_idx < len(arr):
            min_idx = arr[sort_idx:].index(min(arr[sort_idx:])) + sort_idx
            arr[sort_idx], arr[min_idx] = arr[min_idx], arr[sort_idx]
            sort_idx += 1
        return arr 

    @staticmethod
    def bubble_sort(arr):
        start_time = time.time()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        end_time = time.time()
        return end_time - start_time

if __name__ == "__main__":
    ordenacao = OrdenacaoLinear()

    # Vetores randômicos
    tamanho_vetores = [1000, 10000, 100000]
    for tamanho in tamanho_vetores:
        vetor = [random.randint(1, 1000) for _ in range(tamanho)]

        # Insertion Sort
        print(f"\nTamanho do vetor: {tamanho}")
        print("Executando Insertion Sort...")
        start_time = time.time()
        ordenacao.insertion_sort(vetor.copy())
        end_time = time.time()
        tempo_insertion_sort = end_time - start_time
        print(f"Tempo de execução do Insertion Sort: {tempo_insertion_sort:.6f} segundos")

        # Selection Sort
        print("Executando Selection Sort...")
        start_time = time.time()
        ordenacao.selection_sort(vetor.copy())
        end_time = time.time()
        tempo_selection_sort = end_time - start_time
        print(f"Tempo de execução do Selection Sort: {tempo_selection_sort:.6f} segundos")

        # Bubble Sort
        print("Executando Bubble Sort...")
        start_time = time.time()
        ordenacao.bubble_sort(vetor.copy())
        end_time = time.time()
        tempo_bubble_sort = end_time - start_time
        print(f"Tempo de execução do Bubble Sort: {tempo_bubble_sort:.6f} segundos")

        print("Ordenação concluída.")
