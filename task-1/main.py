from termcolor import colored
import os
import sys
from colorama import init

# Ініціалізація colorama
init(autoreset=True)

def is_color_supported():
    """Перевіряємо, чи підтримує термінал кольоровий вивід."""
    if os.name == 'nt':
        return sys.stdout.isatty()  # Перевірка на Windows
    return True  # Інші платформи підтримують кольоровий вивід

def c(text, color):
    """Функція для кольорового виводу, або повертаємо текст без кольору."""
    if is_color_supported():
        return colored(text, color)
    return text  # Повертаємо текст без кольору

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def print_fibonacci_histogram(n):
    """Виводимо компактну гістограму чисел Фібоначчі."""
    fib = caching_fibonacci()
    values = [fib(i) for i in range(n)]

    print("\nЧисла Фібоначчі:")
    print("Індекс | Значення | Гістограма")
    print("-" * 40)

    max_length = 30  # Максимальна довжина гістограми
    max_value = max(values) if values else 1  # Уникаємо ділення на нуль

    for i in range(n):
        value = values[i]
        bar_length = (value * max_length) // max_value  # Масштаб для гістограми
        bar = "█" * bar_length
        print(f"{i:<7} | {value:<8} | {bar}")

    # Виводимо тільки останнє значення
    print(f"\nОстаннє значення: Fibonacci({n - 1}) = {values[-1]}\n")  # Додано відступ

def main():
    print(c("Ласкаво просимо до програми обчислення чисел Фібоначчі!", "cyan"))
    
    while True:
        try:
            user_input = input("Введіть ціле число (або 'exit' для виходу): ")

            if user_input.lower() == 'exit':
                print(c("Програма завершена. До побачення!", "blue"))
                break

            n = int(user_input)

            if n < 0:
                print(c("Будь ласка, введіть невід'ємне число.", "red"))
                continue

            if n > 100:
                print(c("Будь ласка, введіть число не більше 100.", "red"))
                continue

            print_fibonacci_histogram(n)

        except ValueError:
            print(c("Помилка: Введіть коректне ціле число!", "red"))

# Приклад використання скрипту
if __name__ == "__main__":
    main()
