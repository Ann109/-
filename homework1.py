import time
from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
                for i in range(word_count):
                        file.write(f"Какое-то слово № {i}\n")
                        time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now()
time_continue = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Работа потоков {time_continue}')

# Взятие текущего времени
time2_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
thr_one = Thread(target=write_words, args= (10, 'example5.txt'))
thr_two = Thread(target=write_words, args= (30, 'example6.txt'))
thr_third = Thread(target=write_words, args= (200, 'example7.txt'))
thr_four = Thread(target=write_words, args= (100, 'example8.txt'))

thr_one.start()
thr_two.start()
thr_third.start()
thr_four.start()

thr_one.join()
thr_two.join()
thr_third.join()
thr_four.join()

# Взятие текущего времени
time2_stop = datetime.now()
time2_continue = time2_stop - time2_start
print(f'Работа потоков {time2_continue}')


