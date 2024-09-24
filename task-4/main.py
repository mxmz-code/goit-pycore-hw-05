import os
from termcolor import colored

# Перевірка, чи підтримуються кольори в консольному виводі
def supports_color():
    if os.name == 'nt':
        return False  # В Windows кольори за замовчуванням можуть не відображатися
    return True

# Декоратор для обробки помилок вводу
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return colored("Помилка: Користувач з таким ім'ям не знайдений!", "red") if supports_color() else "Помилка: Користувач з таким ім'ям не знайдений!"
        except ValueError:
            return colored("Помилка: Введіть ім'я та телефон у правильному форматі!", "red") if supports_color() else "Помилка: Введіть ім'я та телефон у правильному форматі!"
        except IndexError:
            return colored("Помилка: Введено недостатньо аргументів!", "red") if supports_color() else "Помилка: Введено недостатньо аргументів!"
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return colored(f"Контакт {name} додано з телефоном {phone}.", "green") if supports_color() else f"Контакт {name} додано з телефоном {phone}."

# Функція для отримання телефону за ім'ям
@input_error
def get_phone(args, contacts):
    name = args[0]
    return colored(f"Телефон {name}: {contacts[name]}", "blue") if supports_color() else f"Телефон {name}: {contacts[name]}"

# Функція для показу всіх контактів
@input_error
def show_all_contacts(contacts):
    if not contacts:
        return colored("Немає жодного контакту в книзі.", "yellow") if supports_color() else "Немає жодного контакту в книзі."
    result = []
    for name, phone in contacts.items():
        result.append(colored(f"{name}: {phone}", "green") if supports_color() else f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print(colored("Ласкаво просимо до телефонної книги!", "cyan") if supports_color() else "Ласкаво просимо до телефонної книги!")
    
    while True:
        user_input = input(colored("\nВведіть команду (add, phone, show all, exit): ", "cyan") if supports_color() else "\nВведіть команду (add, phone, show all, exit): ").lower()

        if user_input == 'exit':
            print(colored("\nПрограма завершена. До побачення!", "blue") if supports_color() else "\nПрограма завершена. До побачення!")
            break

        # Додавання нового контакту
        elif user_input == 'add':
            args = input(colored("\nВведіть ім'я та телефон через пробіл: ", "cyan") if supports_color() else "\nВведіть ім'я та телефон через пробіл: ").split()
            if len(args) < 2:
                print(colored("\nПомилка: Необхідно ввести і ім'я, і телефон!", "red") if supports_color() else "\nПомилка: Необхідно ввести і ім'я, і телефон!")
                continue
            print("\n" + add_contact(args, contacts) + "\n")

        # Пошук телефону за ім'ям
        elif user_input == 'phone':
            name = input(colored("\nВведіть ім'я: ", "cyan") if supports_color() else "\nВведіть ім'я: ").split()
            print("\n" + get_phone(name, contacts) + "\n")

        # Показ всіх контактів
        elif user_input == 'show all':
            print("\n" + show_all_contacts(contacts) + "\n")

        # Невідома команда
        else:
            print(colored("\nНевідома команда. Спробуйте ще раз.", "red") if supports_color() else "\nНевідома команда. Спробуйте ще раз.")

# Приклад використання скрипту
if __name__ == "__main__":
    main()
