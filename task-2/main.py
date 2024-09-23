import re
from termcolor import colored

def generator_numbers(text):
    """Генератор чисел з тексту."""
    for num in re.findall(r'\d+\.\d+', text):
        yield float(num)

def sum_profit(text, func):
    """Функція для підрахунку суми чисел з тексту."""
    return sum(func(text))

def main():
    print(colored("Ласкаво просимо до програми підрахунку прибутку з тексту!", "cyan"))
    
    while True:
        try:
            user_input = input("Введіть текст з числами (або 'exit' для виходу): ")

            if user_input.lower() == 'exit':
                print(colored("Програма завершена. До побачення!", "blue"))
                break

            # Підрахунок прибутку
            total_income = sum_profit(user_input, generator_numbers)
            print(colored(f"Загальний дохід: {total_income:.2f}", "magenta"))

        except ValueError:
            print(colored("Помилка: Текст не містить дійсних чисел!", "red"))

# Приклад використання скрипту
if __name__ == "__main__":
    main()
