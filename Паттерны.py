#Паттерны

# 1) обработка поиска значений
mas = []
n = int(input())
for i in range (n):
	mas.append(int(input()))
# заполнение массива
count = 0
c2 = 0
for i in range (len(mas)):
	if mas [i]%2==0:
		count+=mas[i]
	else:
		c2+=mas[i]
		
# 2) minmax
mas = []
n = int(input())
for i in range(n):
	mas.append(int(input())) # добавляет новый элемент в массив
# заполнение массива
print (mas)
min = mas[0]
max = mas[0]
for i in range(len(mas)):
	if mas [i]> max:
		max = mas[i]
	if mas[i] <min:
		min = mas[i]
print (min, " ", max)
	
# 3) ревересы
mas = []
n = int(input())
for i in range (n):
	mas.append(int(input())) # добавляет новый элемент в массив
# заполнение массива
print (mas)
for i in range (len(mas)//2):
	temp = mas[i]
	mas [i] = mas[len(mas)-1-i]
	mas[len(mas)-1-i]=temp
print (mas)

# 3.1) реверсы
mas = []
mas2 = []
n = int(input())
for i in range(n):
	mas.append(int(input()))
for i in range (len(mas)):
	mas2.append(mas[len(mas)-1-i])
print (mas)
print (mas)

# 4) сдвиг вправо
mas = []
count = 0
n = int(input())
for i in range(n):
	mas.append(int(input()))
print (mas)
n = int(input())
for i in range(n):
	temp = mas[len(mas)-1]
	for i in range (0, len(mas)-1):
		mas[len(mas)-1-i] = mas[len(mas)-i-2]
	mas[0] = temp
print (mas)

# 5) замены
mas = []
count = 0
n = int(input())
for i in range(n):
	mas.append(int(input()))
print(mas)
for i in range(len(mas)):
	if mas[i]%2==0:
		mas[i]=0
print(mas)

# 5.1) удаление
mas = []
n = int(input())
for i in range(n):
	mas.append(int(input()))
print (mas)
for i in mas: # вместо range дфем имя массива, ш перебирает не числа от и до, а равна элемнту массива
	if i%2==0:
		mas.pop(mas.index(i)) # команда удаления i элемента из массива
print(mas)

# имя массива.pop() удаляет элемент с номером массива
# имя массива.index() возвращает номер элемента с таким то значением (первого встречного)

# 6) рекурсия
             #1
def S(n):
	if n>0:
		return S(n//10)+n%10
	if n==0:
		return 0
n = int(input())
print(S(n))
			#2
def F(n):
	if n == 1:
		return 1
	if n%2 == 1 and n>1:
		return n+F(n-2)
	if n%2==0:
		return n*F(n-1)
print(F(60))

# 7) палиндром числа
a = int(input())
s = ''
n = a
while a > 0:
	s+=str(a%10)
	a//=10
if n == int(s):
	print("yes")
else:
	print("no")
	
# 7.1) разбор палиндрома по составу числа
def S(n):
	if n>0:
		return str(n%10) + str(S(n//10))
	if n == 0:
		return ""
	def X(n):
		if n == int(S(n)):
			return True
		else:
			return False
n=int(input())
print(x(n))

# 8) поиск трех наиболее встречающихся букв
s="текстт"
max = 0
h = ""
for i in range (len(s)):
	if s.count(s[i])>max and s[i]!=" ":
		h=s[i]
		max=s.count(s[i])
print(h)
s=s.replace(h, "")
max = 0
h = ""
for i in range (len(s)):
	if s.count(s[i])>max and s[i]!=" ":
		h=s[i]
		max=s.count(s[i])
print(h)
s=s.replace(h, "")

# 9) чтение файла
x = open("xx.txt")
a=[]
S=X.readline()
while S:
	a.append(int(S))
	S = X.readline()
print(a) #Паттенр
count = 0
min = 10001
for i in range (len(a)-1):
	if a[i]%5==0 or a[i+1]==0:
		count+=1
		if a[i]+a[i+1]<min:
			min = a[i]+a[i+1]
print(count, " ", min)

# 10) Если пара считает два подряд идущих элемента
f = open("17.txt")
a = []
for line in f:
	a.append(int(line))
max = 0
count = 0
for i in range(len(a)):
	if (a[i]+a[i+1])%9 == 0:
			count+=1
	if (a[i]+a[i+1])%9 == 0 and a[i]+a[i+1]>max:
			max = a[i] + a[i+1]
print(count, max)

# 10.1) Если пара считает все числа идущие не подряд
f = open("17.txt")
a = []
for line in f:
	a.append(int(line))
max = 0
count = 0
for i in range(len(a)):
	for j in range(len(a)):
		if (a[i]+a[j])%9 == 0 and i != j:
			count+=1
		if (a[i]+a[j])%9 == 0 and a[i]+a[j]>max and i !=j:
			max = a[i] + a[j]
print(count//2, max)

# 11) оптимизированный паттерн для задания 25
			#1
count = 0
for i in range(10000, 200001):
	a = []
	for j in range(1, int(i**(1/2))+1):
		if i%j==0:
			a.append(j)
		if len(a)==2:
			count+=1
print(count)
			#2
count = 0
for i in range(0, 10000):
	a = []
	for j in range(2, int(i**(1/2))+1):
		#перебор делителей
		if i%j==0:
			a.append(j)
		# 1 делитель
		if a.count(i//j)==0:
			a.append(i//j)
		# противоположный делитель
	if len(a)==3:
		count+=1
print(count)
        # условие вывода
		
# 12) если строка в файле одна
f = open("24,1.txt")
a = []
for i in f:
	a.append(i)
count = 0
maxc = 0

for i in a[0]:
	if i =='D':
		count+=1
	else:
		if count > maxc:
			maxc = count
			count = 0
print(maxc)

#12.1) если строк несколько
f = open("24,1.txt")
a = []
for i in f:
	a.append(i)
minc = 10000000
s = ""
for j in range(len(a)):
	count = 0
	for i in a[j]:
		if i =='N':
			count+=1
		if count < minc:
			minc = count
			s = a[j]
b = {} # работа со словарем
for i in s:
	if i in b:
		b[i]+=1
	else:
		b[i]=1
print(b)
	
			




#8
from itertools import product
a = 'АБРТЫ'
s = list(product(a, repeat = 5))
k = 0
for i in s:
	k += 1
	i = ''.join(i)
	if 'Ы' not in i and 'АА' not in i:
		print(k, i)
		break
"""
	#Номер 17

f = open("/Users/vladimir/Downloads/17.txt")
a = []
k = 0 # Счетчик пар
m = 0
for line in f:
	a.append(int(line))
for i in range(1, len(a)):
	if a[i] % 3 == 0 or a[i-1] % 3 == 0:
		k += 1
		if a[i] + a[i-1] > m:
			m = a[i] + a[i-1]
print(k, m, len(a))

----------

f = open("/Users/vladimir/Downloads/17 (5).txt")
a = []
k = 0 # Счетчик пар
m = 0
kn = 0
sn = 0
for line in f:
	a.append(int(line))
for chislo in a:
	if chislo % 2 == 1:
		kn += 1
		sn += chislo
sa = sn / kn
for i in range(1, len(a)):
	if (a[i] % 5 == 0 or a[i-1] % 5 == 0) and (a[i] < sa or a[i-1] < sa):
		k += 1
		if a[i] + a[i-1] > m:
			m = a[i] + a[i-1]
			
print(k,m)
"""

"""
Задание 5

for i in range(1, 1000):
	N = i
	if N % 2 == 1:
		s = bin(N)
		s = s[2:]
		s = '1' + s + '00'
		R = int(s, 2)
	else:
		s = bin(N)
		s = s[2:]
		pr = bin(s.count('1'))
		pr = pr[2:]
		R = int(s + pr, 2)
	if R > 215:
	print(R, i)

"""
#Номер 2 ЕГЭ
print('x z y w')
for x in range(2):
	for z in range(2):
		for y in range(2):
			for w in range(2):
				if (((x <= y) == (w <= x)) and (z <= w)) == 1:
					print(x, z, y, w)
					
#Номер 6 ЕГЭ
for i in range(1000):
	s = i
	n = 11
	while s > -9:
		s = s - 4
		n = n + 5
	if n == 56:
		print(i)
#Номер 14 ЕГЭ
n = 5**2*7**25+6**2*7**36-4**2*9**3
b = ''
while n > 0:
	b = str(n%7)+b
	n = n//7
print(b)
#Номер 15 ЕГЭ
for A in range(1000):
	check = True
	for x in range(1000):
		F = ((X & 29 != 0) <= ((X & 9 == 0) <= (X & A != 0)))
		if not F:
			check = False
	if check:
		print(A)
		
		
#Номер 23 ЕГЭ
def f(start, end):
	if start > end or start == 10 or start == 15:
		return 0
	if start == end:
		return 1
	if start < end:
		return f(start + 1, end) + f(start + 2, end) + f(start + 3, end)
print(f(5, 11) * f(11, 18))


#19
def f(x, y, p): #Рекурсивная функция
	if x + y >= 231 or p > 3:
		return p == 3 #Условия завершения игры
	return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1) #Варианты действий
for i in range(1, 214):
	if f(17, i, 1): #Начали с 17 камней
		print(i)
		break
# 20
# x - кол-во камней в первой куче, y - во второй, p - ход
# p - 1 (1 ход ПЕТИ), p - 2 (1 ход ВАНИ)
def f(x, y, p): 
	if x + y >= 231 or p > 4:
		return p == 4 # True or False
	if p % 2 == 0:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1) # У проигравшего ВСЕ ходы должны быть проигрышными. 
	if p % 2 == 1:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1) # У победителя, ХОТЯ БЫ ОДИН должен быть победным
for i in range(1, 214):
	if f(17, i, 1):
		print(i)
# 21
def f(x, y, p): 
	if x + y >= 231 or p > 5:
		return p == 5 or p == 3 # True or False
	if p % 2 == 1:
		return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1) 
	if p % 2 == 0:
		return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1) 
for i in range(1, 214):
	if f(17, i, 1):
		print(i)
		
		
		
#Номер 24 ЕГЭ
f = open('/Users/vladimir/Downloads/24 (6).txt')
a = f.readline()
a = a.split("1")
m = 0
for i in range(len(a)):
	x = len(a[i])
	if i == 0 or i == len(a) - 1:
		x += 4
	else:
		x += 8
	if x > m:
		m = x	
print(m)
#24.2
f = open('/Users/vladimir/Downloads/24 (5).txt')
a = f.readline()
a = a.replace('ad','da')
a = a.split("da")
m = 0
for i in range(len(a)):
	x = len(a[i])
	if i == 0 or i == len(a) - 1:
		x += 1
	else:
		x += 2
	if x > m:
		m = x	
print(m)

		

#Номер 25 ЕГЭ
a = 11000000
k = 0
while True:
	a += 1
	d1 = 0
	d2 = 0
	for i in range(2, int(a ** 0.5) + 1):
		if a % i == 0:
			if d1 == 0:
				d1 = a // i
			else:
				d2 = a // i
				break
	if d2 == 0 and d1 != 0:
		d2 = a // d1
	if 0 < d1 + d2 < 10000:
		print(a, d1 + d2)
		k += 1
	if k == 5:
		break
#25 .2
for i in range(10):
	for j in range(10):
		a = '12345' + str(i) + '7' + str(j) + '8'
		a = int(a)
		if a % 23 == 0:
			print(a, a // 23)
	
	
	
#Проверка простных натуральных чисел
a = int(input())
k = 0
for i in range(1, int(a ** 0.5) +1):
	if a % i == 0:
		k += 1
k *= 2
if int(a ** 0.5) ** 2 == a:
	k -= 1
if k == 2:
	print('Простое')