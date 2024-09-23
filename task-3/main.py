import os
import sys
import argparse
from termcolor import colored

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
        print(colored(f"Помилка: Файл {file_path} не знайдено!", "red"))
        return None

    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Перевірка на порожні рядки
                logs.append(parse_log_line(line))

    if not logs:
        print(colored(f"Помилка: Файл {file_path} порожній або не містить коректних логів!", "red"))
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
    print(f"{colored('Рівень логування', 'cyan'):<15} | {colored('Кількість', 'cyan'):<10}")
    print('-' * 30)
    for level, count in counts.items():
        bars = '█' * count  # Псевдографіка
        color = 'green' if level == 'INFO' else 'yellow' if level == 'DEBUG' else 'red'
        print(f"{colored(level, color):<15} | {count:<10} {bars}")

def main():
    parser = argparse.ArgumentParser(description="Програма для аналізу лог-файлів.")
    parser.add_argument("file_path", type=str, help="Шлях до лог-файлу")
    parser.add_argument("log_level", nargs='?', type=str, help="Рівень логування для фільтрації (INFO, DEBUG, ERROR, WARNING)", default=None)
    
    args = parser.parse_args()

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
            print(colored(f"\nЛоги для рівня '{filter_level}':", "yellow"))
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(colored(f"Немає записів для рівня '{filter_level}'", "red"))

# Виклик основної функції
if __name__ == "__main__":
    main()
