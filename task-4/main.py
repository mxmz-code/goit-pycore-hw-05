from termcolor import colored

# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return colored("Помилка: Користувач з таким ім'ям не знайдений!", "red")
        except ValueError:
            return colored("Помилка: Введіть ім'я та телефон у правильному форматі!", "red")
        except IndexError:
            return colored("Помилка: Введено недостатньо аргументів!", "red")
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return colored(f"Контакт {name} додано з телефоном {phone}.", "green")

# Функція для отримання телефону за ім'ям
@input_error
def get_phone(args, contacts):
    name = args[0]
    return colored(f"Телефон {name}: {contacts[name]}", "blue")

# Функція для показу всіх контактів
@input_error
def show_all_contacts(contacts):
    if not contacts:
        return colored("Немає жодного контакту в книзі.", "yellow")
    result = []
    for name, phone in contacts.items():
        result.append(colored(f"{name}: {phone}", "green"))
    return "\n".join(result)

def main():
    contacts = {}
    print(colored("Ласкаво просимо до телефонної книги!", "cyan"))
    
    while True:
        user_input = input(colored("\nВведіть команду (add, phone, show all, exit): ", "cyan")).lower()

        if user_input == 'exit':
            print(colored("Програма завершена. До побачення!", "blue"))
            break

        # Додавання нового контакту
        elif user_input == 'add':
            args = input(colored("Введіть ім'я та телефон через пробіл: ", "cyan")).split()
            if len(args) < 2:
                print(colored("Помилка: Необхідно ввести і ім'я, і телефон!", "red"))
                continue
            print(add_contact(args, contacts))

        # Пошук телефону за ім'ям
        elif user_input == 'phone':
            name = input(colored("Введіть ім'я: ", "cyan")).split()
            print(get_phone(name, contacts))

        # Показ всіх контактів
        elif user_input == 'show all':
            print(show_all_contacts(contacts))

        # Невідома команда
        else:
            print(colored("Невідома команда. Спробуйте ще раз.", "red"))

# Приклад використання скрипту
if __name__ == "__main__":
    main()
