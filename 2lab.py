import math #Мат.Библиоткена импорттаймыз
a = 3 #Үшбұрыштың 1-ші қабырғасы
b = 4 #Үшбұрыштың 2-ші қабырғасы
c = 2 #Үшбұрыштың 3-ші қабырғасы
P = a+b+c #Үшбұрыштың периметрі
print(P)
S = math.sqrt(P*(P-a)*(P-b)*(P-c)) #Үшбұрыштың ауданы
print(S)