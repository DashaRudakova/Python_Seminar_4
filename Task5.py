# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('C:\Users\darud\Desktop\python\Seminar4\Task5_1.txt', 'r') as file:
   mnog1 = file.read()
   mnog1 = mnog1[0:-4]

with open('C:\Users\darud\Desktop\python\Seminar4\Task5_2.txt', 'r') as file:
   mnog2 = file.read()

with open('C:\Users\darud\Desktop\python\Seminar4\Task5.txt', 'w', encoding='utf-8') as file:
   file.write(f'{mnog1} + {mnog2}')