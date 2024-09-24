import re
import os
import sys
from termcolor import colored

def supports_color():
    """
    Перевірка підтримки кольорів в терміналі Windows.
    Якщо кольори не підтримуються, то повертає False.
    """
    if sys.platform == 'win32' and not os.getenv('ANSICON'):
        return False
    return True

# Виведення кольорового тексту або звичайного, якщо кольори не підтримуються
def print_colored(text, color):
    if supports_color():
        print(colored(text, color))
    else:
        print(text)

def generator_numbers(text):
    """Генератор чисел з тексту (підтримує крапку та кому)."""
    text = text.replace(',', '.')  # Заміна коми на крапку для коректного перетворення в float
    for num in re.findall(r'-?\d+\.?\d*', text):
        yield float(num)

def sum_profit(text, func):
    """Функція для підрахунку суми чисел з тексту."""
    return sum(func(text))

def print_boxed_message(messages, color="magenta"):
    """
    Функція для виведення повідомлень у рамці з вирівнюванням по центру.
    Приймає список рядків `messages`, де кожен рядок буде вирівняний.
    """
    if isinstance(messages, str):
        messages = [messages]
        
    # Знаходимо найдовший рядок
    max_length = max(len(msg) for msg in messages) + 2  # +2 для відступів у боках
    
    # Виводимо верхню частину рамки
    print_colored("╔" + "═" * max_length + "╗", color)
    
    # Виводимо кожен рядок, вирівняний по центру
    for msg in messages:
        padded_message = msg.center(max_length)
        print_colored(f"║{padded_message}║", color)
    
    # Виводимо нижню частину рамки
    print_colored("╚" + "═" * max_length + "╝", color)

def main():
    print_boxed_message(["Ласкаво просимо до програми підрахунку прибутку", 
                         "з тексту!"], "cyan")
    print()
    print("Приклад тексту для введення:")
    print_colored("├── 'Ваш дохід становить 12.34, додатковий дохід - 56,78'", "green")
    print()

    while True:
        try:
            user_input = input("Введіть текст з числами (або 'exit' для виходу): ")

            if user_input.lower() == 'exit':
                print()
                print_boxed_message("Програма завершена. До побачення!", "blue")
                break

            # Підрахунок прибутку
            total_income = sum_profit(user_input, generator_numbers)

            # Виведення результату з урахуванням боргу чи доходу
            print()
            if total_income >= 0:
                print_boxed_message(f"Загальний дохід: {total_income:.2f}", "magenta")
            else:
                print_boxed_message(f"Борг: {abs(total_income):.2f}", "red")
            print()

        except ValueError:
            print()
            print_boxed_message("Помилка: Текст не містить дійсних чисел!", "red")
            print()

# Приклад використання скрипту
if __name__ == "__main__":
    main()
