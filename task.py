import random
import time
import math
import csv
import os

def run_monte_carlo_experiment(n_values):

    file_path = 'results/pi_monte_carlo_results.csv'
    headers = ['N', 'pi_estimated', 'accuracy_error', 'total_time_sec', 'time_per_point']

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for n in n_values:

            print(f"Розраховуємо {n}")

            n_ins = 0
            start_time = time.time()

            for _ in range(n):
                x = random.random()
                y = random.random()
                if x*x + y*y <= 1:
                    n_ins += 1

            end_time = time.time()
            
            # Розрахунок метрик
            execution_time = end_time - start_time
            pi_estimated = (4.0 * n_ins) / n
            accuracy_error = abs(pi_estimated - math.pi)
            time_per_point = execution_time / n

            # Запис у CSV
            writer.writerow([n, pi_estimated, accuracy_error, execution_time, time_per_point])

    print("Успіх")

if __name__ == "__main__":

    target_n = [
        1000000, 
        10000000, 
        100000000, 
        1000000000, 
        10000000000,
        100000000000
    ]
    
    run_monte_carlo_experiment(target_n)