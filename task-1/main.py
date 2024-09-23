from termcolor import colored

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            print(colored(f"Число Fibonacci({n}) взято з кешу: {cache[n]}", "yellow"))
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(colored(f"Число Fibonacci({n}) обчислено: {cache[n]}", "green"))
        return cache[n]

    return fibonacci

def main():
    print(colored("Ласкаво просимо до програми обчислення чисел Фібоначчі!", "cyan"))
    
    while True:
        try:
            user_input = input("Введіть ціле число (або 'exit' для виходу): ")

            if user_input.lower() == 'exit':
                print(colored("Програма завершена. До побачення!", "blue"))
                break

            n = int(user_input)

            if n < 0:
                print(colored("Будь ласка, введіть невід'ємне число.", "red"))
                continue

            fib = caching_fibonacci()
            result = fib(n)
            print(colored(f"Число Фібоначчі для {n} дорівнює: {result}", "magenta"))

        except ValueError:
            print(colored("Помилка: Введіть коректне ціле число!", "red"))

# Приклад використання скрипту
if __name__ == "__main__":
    main()
