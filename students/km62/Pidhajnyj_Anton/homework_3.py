#task1------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.

По данному натуральному n вычислите значение n!.
Пользоваться математической библиотекой math в этой задаче запрещено. 
"""



#Factorial
n=int(input())

result=1
for i in range(n):
    result*=i+1
print(result)

	
	
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.
"""



#Sum of factorials
n=int(input())

fact=1
sum=0
for i in range(n):
    fact*=i+1
    sum+=fact
print(sum)

	
	
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
Подсчитайте количество нулей среди введенных чисел и выведите это количество.
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр. 
"""



#Number of zeros
n=int(input())

count=0
for i in range(n):
    number=int(input())
    if not(number):
        count+=1
print(count)
	
	
	
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов. 
"""


#Stairway
n=int(input())

for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()

	
	
#-----------------------------------------------------------------

