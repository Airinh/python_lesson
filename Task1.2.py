time = input('Введите время в секундах: ')
while not time.isdigit():
    time = input('Пожалуйста, введите число правильно: ')
time = int(time)
print(f"{time} секунд в формате чч:мм:сс это {(time // 3600):>02}:{((time % 3600)//60):>02}:{((time % 3600) % 60):>02}")
