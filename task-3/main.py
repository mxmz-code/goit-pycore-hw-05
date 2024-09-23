from termcolor import colored
import os

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
    print(colored("Ласкаво просимо до програми аналізу лог-файлів!", "cyan"))
    
    while True:
        file_path = input("Введіть шлях до лог-файлу (або 'exit' для виходу): ")

        if file_path.lower() == 'exit':
            print(colored("Програма завершена. До побачення!", "blue"))
            break

        logs = load_logs(file_path)
        if logs is None:
            continue

        # Виведення кількості записів за рівнями
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

        # Фільтрація логів за рівнем (за бажанням користувача)
        filter_level = input("Введіть рівень логування для фільтрації (INFO, DEBUG, ERROR, WARNING) або 'skip' для пропуску: ").upper()

        if filter_level == 'SKIP':
            continue

        filtered_logs = filter_logs_by_level(logs, filter_level)
        if filtered_logs:
            print(colored(f"\nЛоги для рівня '{filter_level}':", "yellow"))
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(colored(f"Немає записів для рівня '{filter_level}'", "red"))

# Приклад використання скрипту
if __name__ == "__main__":
    main()
