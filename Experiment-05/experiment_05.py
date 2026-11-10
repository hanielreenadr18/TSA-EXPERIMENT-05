import numpy as np
import matplotlib.pyplot as plt
year = np.array([2020, 2021, 2022, 2023, 2024])
population = np.array([10000, 10500, 11000, 11600, 12000])
t = np.array([0, 1, 2, 3, 4])
plt.figure(figsize=(10, 5))
plt.plot(year, population, marker='o', label='Actual')
b, a = np.polyfit(t, population, 1)
predicted = a + b * t
print("Starting Population =", a)
print("Growth per Year =", b)
print("\nYear Actual Predicted")
for i in range(len(year)):
    print(year[i], population[i], round(predicted[i], 2))
future_year = np.array([2025, 2026, 2027])
future_t = np.array([5, 6, 7])
future_population = a + b * future_t
print("\nFuture Population")
for i in range(len(future_year)):
    print(future_year[i], round(future_population[i], 2))
plt.plot(year, predicted, marker='x', linestyle='--', label='Model')
plt.plot(future_year, future_population, marker='s',
         linestyle=':', label='Forecast')
plt.title("Population Growth Model")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid()
plt.show()
