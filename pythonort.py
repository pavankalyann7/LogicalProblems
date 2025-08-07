


'''
x = [1, 2, 3]
y = [2, 4, 1]

plt.scatter(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
#plt.grid(True)
plt.show()'''
''''
import matplotlib.pyplot as plt
import numpy as np
'''
ylabel = ['20-09-2025', '20-09-2025', '20-09-2025']
xlabel = ['biriyani', 'chicken', 'mutton']
sales = [[10, 20, 30], [30, 40, 50], [50, 60, 70]]
'''
sales = np.array(sales)

plt.imshow(sales, cmap='YlOrRd')  # You can use other colormaps too
plt.colorbar(label="Sales")

plt.xticks(ticks=range(len(xlabel)), labels=xlabel)
plt.yticks(ticks=range(len(ylabel)), labels=ylabel)

plt.title("Sales Data")
plt.xlabel("Items")
plt.ylabel("Date")
plt.show()

'''
import matplotlib.pyplot as plt

ylabel = ['20-09-2025', '20-09-2025', '20-09-2025']
xlabel = ['biriyani', 'chicken', 'mutton']
sales = [[10, 20, 30], [30, 40, 50], [50, 60, 70]]



for i in range(len(ylabel)):
    plt.subplot(1, 3, i+1)  # 1 row, 3 columns
    plt.bar(xlabel, sales[i])
    plt.title(f"Sales on {ylabel[i]}")
    plt.xlabel("Items")
    plt.ylabel("Sales")

plt.tight_layout()
plt.show()



