import random
import time

class OrdenacaoLinear:
    @staticmethod
    def insertion_sort(A):
        start_time = time.time()
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while (i > -1) and key < A[i]:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        end_time = time.time()
        return A, end_time - start_time

    @staticmethod
    def selection_sort(A):
        start_time = time.time()
        for j in range(len(A) - 1):
            minimum = j
            for i in range(j + 1, len(A)):
                if A[i] < A[minimum]:
                    minimum = i
            A[j], A[minimum] = A[minimum], A[j]
        end_time = time.time()
        return end_time - start_time

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
    tamanho_vetores = [10000, 100000, 1000000]
    for tamanho in tamanho_vetores:
        vetor = [random.randint(1, 1000) for _ in range(tamanho)]

        # Insertion Sort
        print(f"\nTamanho do vetor: {tamanho}")
        print("Executando Insertion Sort...")
        vetor_insertion_sort, tempo_insertion_sort = ordenacao.insertion_sort(vetor.copy())
        print(f"Tempo de execução do Insertion Sort: {tempo_insertion_sort:.6f} segundos")

        # Selection Sort
        print("Executando Selection Sort...")
        tempo_selection_sort = ordenacao.selection_sort(vetor.copy())
        print(f"Tempo de execução do Selection Sort: {tempo_selection_sort:.6f} segundos")

        # Bubble Sort
        print("Executando Bubble Sort...")
        tempo_bubble_sort = ordenacao.bubble_sort(vetor.copy())
        print(f"Tempo de execução do Bubble Sort: {tempo_bubble_sort:.6f} segundos")

        print("Ordenação concluída.")