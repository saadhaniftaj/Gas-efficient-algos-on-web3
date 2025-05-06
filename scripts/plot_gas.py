import matplotlib.pyplot as plt

n = [10, 100, 1000]
insertion_gas = [50000, 200000, 2000000]
merge_gas = [300000, 800000, 1500000]

plt.plot(n, insertion_gas, label="Insertion Sort (O(n²))")
plt.plot(n, merge_gas, label="Merge Sort (O(n log n))")
plt.xlabel("Input Size (n)")
plt.ylabel("Gas Used")
plt.legend()
plt.savefig("gas_complexity.png")
