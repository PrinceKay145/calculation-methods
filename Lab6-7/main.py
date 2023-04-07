import numpy as np
from math import pi
from numpy import dot

# # take the inputs
#
# # size of the matrices
# M = int(input())
# # filling the matrices up (A)
# matr = []
# for i in range(M):
#     matrix = input()  # note: input a column at once separated by just spacebar
#     matr.append(matrix.split(' '))
# for i in range(M):
#     for j in range(M):
#         matr[i][j] = int(matr[i][j])
#
# print(matr)
# # the vector (B)
# vectr = []
# for i in range(M):
#     matrix = input()  # note: input a column at once separated by just spacebar
#     vectr.append(matrix.split(' '))
# for i in range(M):
#     for j in range(1):
#         vectr[i][j] = int(vectr[i][j])
# print(vectr)
# # print(matr)        --test
# # method 1(using the inverse matrices method)
#
#
# # method 2


# add two vectors
def add(A, B):
    result = []
    if len(A) == len(B):
        for i in range(len(A)):
            result.append(A[i] + B[i])
    return result


# subtract two vectors
def subtr(A, B):
    result = []
    if len(A) == len(B):
        for i in range(len(A)):
            temp=A[i] - B[i]
            result.append(temp)
    return result


def multi(A, B):
    result = []
    for i in range(len(A)):
        total = 0
        for j in range(len(B)):
            total += A[i, j] * B[j]
        result.append(total)
    return result


def gaussElimin(A, B, N, X):
    # Elimination Phase
    for k in range(0, N - 1):       #to index the fived rows and eliminated columns
        for i in range(k + 1, N):   #to index the subtracted rows
            if A[i, k] == 0:
                continue
            var = A[k, k] / A[i, k]
            for j in range(k,N):    #to index the column for subtraction
                A[i,j]=A[k,j]-A[i,j]*var
            B[i] = B[k] - B[i]*var  #to print the elimination matrices with the vector
    print("\nUpper triangle A and vector b")
    for i in range(my_A_rows):
        print(np.round(A[i],2), np.round(B[i],2))

    # Back substitution
    X[N-1]=B[N-1]/A[N-1,N-1]        #start from the last row
    for i in range(N - 1, -1, -1):  #to loop from n-2 to 0
        sum_ax=0
        for j in range(i+1, N):     #to loop from i+1 to n-1 for the summation
            sum_ax+=A[i,j]*X[j]
        X[i]=(B[i]-sum_ax)/A[i,i]   #to print the solution vector
    print("\nSolution vector")
    for i in range (my_A_rows):
        print(f"x{[i]} = {np.round(X[i],2)}")
    return X
# def elimin(A, B, N):
#     for k in range(0, N - 1):
#         for i in range(k + 1, N):
#             if A[i, k] == 0:
#                 continue
#             var = A[k, k] / A[i, k]
#             for j in range(k, N):
#                 A[i, j] = A[k, j] - A[i, j] * var
#             B[i] = B[k] - B[i] * var
#     for i in range(my_A_rows):
#         print(np.round(A[i],2), np.round(B[i],2))
# def res(A, B, N, X):
#     X[N - 1] = B[N - 1] / A[N - 1, N - 1]
#     for i in range(N - 1, -1, -1):
#         sum_ax = 0
#         for j in range(i + 1, N):
#             sum_ax += A[i, j] * X[j]
#         X[i] = (B[i] - sum_ax) / A[i, i]
#     return X

print("--------------")
print('For now, please convert pi before input')
print("---------------")
my_A_rows = int(input("введите число строк матрицы коэфициентов: "))

print("введите матрицу коэфициентов (по строках, пробелы между коэффициентами")
myA = [list(map(float, (input(f"строка {i + 1}: ").split())))
       for i in range(my_A_rows)]


myB = map(float, input("Введите матрицу правых частей, пробелы между числами: ").split())
myB = list(myB)

x_val= np.zeros(len(myB), float)
A = np.array(myA)
B = np.array(myB)


print("\nMatrix A and vector b")
for i in range (my_A_rows):
    print(A[i], B[i])
gauss_x = gaussElimin(A, B, my_A_rows, x_val)
mm = multi(np.array(myA),gauss_x)
res = subtr(mm,np.array(myB))

delta=np.sqrt(np.sum(np.square(res)))
print(f"\ndelta = {delta}")


