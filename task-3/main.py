import os
import sys
import argparse
import colorama
from termcolor import colored

colorama.init()  # Ініціалізація colorama для кросплатформеного відображення кольорів

def can_display_colors():
    """Перевіряє, чи можна відображати кольори."""
    return sys.stdout.isatty()

def parse_log_line(line):
    """Парсинг рядка логу."""
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path):
    """Завантаження логів з файлу з перевіркою на наявність даних."""
    if not os.path.exists(file_path):
        print(colored(f"Помилка: Файл {file_path} не знайдено!", "red") if can_display_colors() else f"Помилка: Файл {file_path} не знайдено!")
        return None

    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Перевірка на порожні рядки
                logs.append(parse_log_line(line))

    if not logs:
        print(colored(f"Помилка: Файл {file_path} порожній або не містить коректних логів!", "red") if can_display_colors() else f"Помилка: Файл {file_path} порожній або не містить коректних логів!")
        return None

    return logs

def filter_logs_by_level(logs, level):
    """Фільтрація логів за рівнем."""
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs):
    """Підрахунок кількості записів за рівнями логування."""
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts):
    """Виведення підрахунку записів за рівнями."""
    header_color = 'cyan' if can_display_colors() else ''
    print(f"\n{colored('Рівень логування', header_color):<15} | {colored('Кількість', header_color):<10}")
    print('-' * 40)  # Довша лінія для псевдографіки
    for level, count in counts.items():
        bars = '█' * count  # Псевдографіка
        color = 'green' if level == 'INFO' else 'yellow' if level == 'DEBUG' else 'red'
        color = color if can_display_colors() else ''
        print(f"{colored(level, color):<15} | {count:<10} {bars}")
        print()  # Відступ між рядками

def get_log_level():
    """Отримує рівень логування через інтерактивний діалог."""
    levels = {
        '1': 'INFO',
        '2': 'DEBUG',
        '3': 'ERROR',
        '4': 'WARNING',
        '5': 'ALL'
    }
    while True:
        print("\nОберіть рівень логування:")
        for key, value in levels.items():
            print(f"{key}: {value}")
        choice = input("Введіть номер рівня: ")

        if choice in levels:
            return levels[choice]
        else:
            print(colored("Помилка: Введіть правильний номер (1-5).", "red") if can_display_colors() else "Помилка: Введіть правильний номер (1-5).")

def interactive_mode():
    """Інтерактивний діалог з користувачем."""
    while True:
        file_path = input("Введіть шлях до лог-файлу (або 'вихід' для завершення): ")
        if file_path.lower() == 'вихід':
            break
        
        logs = load_logs(file_path)
        if logs:
            log_level = get_log_level()
            if log_level != 'ALL':
                filtered_logs = filter_logs_by_level(logs, log_level)
                counts = count_logs_by_level(filtered_logs)
                display_log_counts(counts)
            else:
                counts = count_logs_by_level(logs)
                display_log_counts(counts)

def main():
    parser = argparse.ArgumentParser(description="Програма для аналізу лог-файлів.")
    parser.add_argument("file_path", nargs='?', type=str, help="Шлях до лог-файлу")
    parser.add_argument("log_level", nargs='?', type=str, help="Рівень логування для фільтрації (INFO, DEBUG, ERROR, WARNING)", default=None)
    
    args = parser.parse_args()

    if args.file_path:
        # Завантаження логів
        logs = load_logs(args.file_path)
        if logs is None:
            sys.exit()

        # Виведення підрахунку логів за рівнями
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        # Якщо задано рівень логування, фільтруємо лог за рівнем
        if args.log_level:
            filter_level = args.log_level.upper()
            filtered_logs = filter_logs_by_level(logs, filter_level)
            if filtered_logs:
                print(colored(f"\nЛоги для рівня '{filter_level}':", "yellow") if can_display_colors() else f"\nЛоги для рівня '{filter_level}':")
                for log in filtered_logs:
                    print(f"{log['date']} {log['time']} - {log['message']}")
                print()  # Відступ після виводу логів
            else:
                print(colored(f"Немає записів для рівня '{filter_level}'", "red") if can_display_colors() else f"Немає записів для рівня '{filter_level}'")
    else:
        interactive_mode()

# Виклик основної функції
if __name__ == "__main__":
    main()
