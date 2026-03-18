#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Практическое задание №1

## Лабораторная работа по Jupyter
### Вариант 17: Вычисление собственных значений матриц

**Дата:** 14.02.2026  
**Студент:** Мендеш Пашкоал  
**Python:** 3.13.7  

**Цель работы:** Реализовать и визуализировать вычисление собственных значений матриц с использованием Python и JupyterLab.

### Нумерованный список (задачи лабораторной работы):

1. Изучить теоретический материал по собственным значениям матриц
2. Реализовать вычисление собственных значений для матрицы 2×2
3. Проверить результат ручным вычислением по формуле
4. Построить визуализацию на комплексной плоскости
5. Изучить магические команды Jupyter
6. Создать файлы с результатами (.txt и .json)
7. Выполнить команды терминала для резервного копирования

### Маркированный список (используемые библиотеки):

- NumPy — для вычисления собственных значений
- Matplotlib — для визуализации графиков
- OS — для работы с файловой системой
- JSON — для сохранения структурированных данных
- Time — для измерения времени выполнения

### Изображение (формула для варианта 17):

Собственные значения матрицы находятся из характеристического уравнения:

get_ipython().system('[Формула собственных значений](https://github.com/Pascoalpm/lab-jupyter-autovalores/blob/main/Lab%201/Imagem%20do%20exemplo/grafico-variante17.png?raw=true)')


*Рисунок 1: Характеристическое уравнение det(A — λI) = 0*


# In[ ]:


# Запрос имени пользователя
name = input("Введите ваше имя: ")

# Вывод приветствия
print(f"Привет, {name}! Добро пожаловать в JupyterLab!")


# In[ ]:


# Проверка версии Python и установка необходимых библиотек
import sys
print(f"Версия Python: {sys.version}")

# Установка библиотек (если не установлены)
get_ipython().run_line_magic('pip', 'install numpy matplotlib')


# In[ ]:


### Теоретическая справка

Собственные значения матрицы **A** находятся из характеристического уравнения:

$$det(A - \lambda I) = 0$$

где:
- **A** - исходная матрица
- **λ** - собственное значение (лямбда)
- **I** - единичная матрица
- **det** - определитель

Для матрицы 2×2:
$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

Характеристическое уравнение:
$$\lambda^2 - (a+d)\lambda + (ad - bc) = 0$$

Решение:
$$\lambda_{1,2} = \frac{(a+d) \pm \sqrt{(a+d)^2 - 4(ad-bc)}}{2}$$


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

print("ВЫЧИСЛЕНИЕ СОБСТВЕННЫХ ЗНАЧЕНИЙ МАТРИЦЫ")
print("="*60)

# Матрица 2x2 (exemplo)
A = np.array([[4, 2],
              [1, 3]])

print("Матрица A:")
print(A)

# Вычисление собственных значений
eigenvalues = np.linalg.eigvals(A)
print(f"\nСобственные значения: {eigenvalues}")

# Ручное вычисление
a, b, c, d = A.flatten()
trace = a + d
det = a*d - b*c

lambda1 = (trace + np.sqrt(trace**2 - 4*det)) / 2
lambda2 = (trace - np.sqrt(trace**2 - 4*det)) / 2

print(f"\nРучное вычисление:")
print(f"λ₁ = {lambda1:.6f}")
print(f"λ₂ = {lambda2:.6f}")
print(f"Результаты совпадают: {np.isclose(lambda1, eigenvalues[0]) and np.isclose(lambda2, eigenvalues[1])}")


# # Gráfico 
# plt.figure(figsize=(6,4))
# plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), s=200, c='red')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid()
# plt.xlabel('Re(λ)')
# plt.ylabel('Im(λ)')
# plt.title('Собственные значения матрицы A')
# plt.show()

# In[ ]:


import os

# Пункты 1-2: Создание и запись
with open("teste_variante17.txt", "w") as f:
    f.write("Вариант 17: Собственные значения матриц\n")
    f.write("Матрица A = [[4,2],[1,3]] → [5, 2]\n")

# Пункт 3: Чтение файла
with open("teste_variante17.txt", "r") as f:
    print(f.read())

# Пункт 4: Проверка существования
print("Файл существует:", os.path.exists("teste_variante17.txt"))

# Пункт 5: Удаление файла
os.remove("teste_variante17.txt")
print("Файл удален.")


# In[27]:


print(" МАГИЧЕСКИЕ КОМАНДЫ JUPYTER")
print("="*60)

# %lsmagic - список всех магических команд
print("\n1️ Список доступных магических команд:")
get_ipython().run_line_magic('lsmagic', '')

# %time - измерение времени
print("\n2️ Измерение времени выполнения (%time):")
get_ipython().run_line_magic('time', 'resultado = sum([i**2 for i in range(1000000)])')

# %timeit - точное измерение
print("\n3️ Точное измерение (%timeit):")
get_ipython().run_line_magic('timeit', 'np.linalg.eigvals(np.random.rand(10,10))')

print("\n4️ Измерение времени для всей ячейки (%%time):")


# In[ ]:


# %who - список переменных
print("\n5️ Текущие переменные в памяти (%who):")
get_ipython().run_line_magic('who', '')

# %env - переменные окружения (сокращенно)
print("\n6️ Переменные окружения (первые 5):")
import os
dict(list(os.environ.items())[:5])

print("\n Все магические команды выполнены успешно!")


# In[ ]:


print("ВЗАИМОДЕЙСТВИЕ С ОБОЛОЧКОЙ СИСТЕМЫ (WINDOWS)")


# Пункт 1: Список файлов
print("\n  Список файлов в текущей директории")
get_ipython().system('dir')

# Пункт 2: Версия Python
print("\n  Версия Python")
get_ipython().system('python --version')

# Пункт 3: Создание папки
print("\n Создание папки test_folder_v17")
get_ipython().system('mkdir test_folder_v17')
get_ipython().system('dir test_folder_v17')

# Пункт 4: Перемещение файла
print("\n Копирование и удаление файла")
# Primeiro, criar um arquivo para testar
with open("teste_mover.txt", "w") as f:
    f.write("Arquivo para testar movimento")
get_ipython().system('copy teste_mover.txt test_folder_v17 !del teste_mover.txt')
get_ipython().system('dir test_folder_v17')

# Пункт 5: Очистка вывода
print("\n Пункт 5: Очистка экрана (!cls)")
get_ipython().system('cls')


# %%time
# # Создадим большую матрицу
# matriz_grande = np.random.rand(50, 50)
# autovalores_grandes = np.linalg.eigvals(matriz_grande)
# print(f"Найдено {len(autovalores_grandes)} собственных значений")

# # Заголовок первого уровня
# ## Заголовок второго уровня
# 
# **Полужирный текст**, *курсив*, `код в строке`
# 
# Список:
# - Пункт 1
# - Пункт 2
# - Пункт 3
# 
# Формула: \( y = mx + b \)

# In[4]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

x = [i for i in range(50)]
y = [i**2 for i in range(50)]
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("График y = x²")
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("График синусоиды")
plt.grid(True)
plt.show()


# In[6]:


get_ipython().run_line_magic('timeit', 'sum(range(1000))')


# In[7]:


get_ipython().run_cell_magic('time', '', 'total = 0\nfor i in range(10**6):\n    total += i\nprint(f"Сумма: {total}")\n')


# In[9]:


get_ipython().run_line_magic('pip', 'install pandas')


# In[10]:


import pandas as pd

# Создание примера данных
data = {
    'Имя': ['Иван', 'Мария', 'Петр'],
    'Возраст': [25, 30, 22],
    'Город': ['Москва', 'СПб', 'Казань']
}

df = pd.DataFrame(data)
df.to_csv('example.csv', index=False)

# Чтение CSV
df_read = pd.read_csv('example.csv')
df_read.head()


# In[11]:


# Сложение
print(2 + 3)

# Переменные
a = 5
b = 7
print(a + b)


# In[12]:


n = 7
for i in range(n):
    print(i * 10)


# In[13]:


i = 0
while True:
    i += 1
    if i > 5:
        break
    print("Test while")


# In[ ]:




