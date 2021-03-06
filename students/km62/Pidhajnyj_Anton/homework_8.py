#task1------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
В результате единицы в массиве должны образовывать изображение звездочки.
Выведите полученный массив на экран, разделяя элементы массива пробелами. 

"""



number = int(input())

list_=[['.'] * number for i in range(number)]
for i in range(number):
    for j in range(number):
        if i == ( number // 2 ) :
            list_[i][j]='*'
        if j == ( number // 2 ) :
            list_[i][j]='*'
        if i==j:
            list_[i][j]='*'
        if (i+j)==number-1:
            list_[i][j]='*'
            
for i in range(number):
    print()
    for j in range(number):
        print(list_[i][j],end=' ')

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д. 
"""



def print_array(array):
    for str in array:
        print()
        for elem in str:
            print(elem,end=' ')
n=int(input())

array=[[0] * n for i in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i<j:
                array[i][j]=array[i+1][j]+1
            if j<i:
                array[i][j]=array[i][j+1]+1
print_array(array)

#-----------------------------------------------------------------


#task3---------------------------------------------------------------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""



def create_list(n,list_):
    for i in range(n):
        list_.append(('0 '*n).split())
    return(list_)
#default
list_=[]
#input
n=int(input())
#main
list_=create_list(n,list_)

for i in range(n):
    for j in range(n):
        if i+j==n-1:
            list_[i][j]=1
        if i+j>n-1:
            list_[i][j]=2
#print          
for i in range(n):
    if i!=0:
        print()
    for j in range(n):
        print(list_[i][j], end=' ')

#-----------------------------------------------------------------


