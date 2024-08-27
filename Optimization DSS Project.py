import tkinter as tk
import numpy as np


def vogels_approximation():
   
    cost_matrix = np.array([[int(entry.get()) for entry in row] for row in cost_entries])
    supply = [int(entry.get()) for entry in supply_entries]
    demand = [int(entry.get()) for entry in demand_entries]
    
    supply_sum = np.sum(supply)
    demand_sum = np.sum(demand)
    
    supply_sum_label.configure(text="Total Supply: " + str(supply_sum))
    demand_sum_label.configure(text="Total Demand: " + str(demand_sum))

    if supply_sum != demand_sum:
        message_label.configure(text="Total supply must be equal to total demand", fg="red")
    else:
            num_supply = len(supply)
    num_demand = len(demand)
    allocation = np.zeros((num_supply, num_demand))

    while np.sum(supply) > 0 and np.sum(demand) > 0:
        penalty_rows = np.zeros(num_supply)
        penalty_cols = np.zeros(num_demand)

        for i in range(num_supply):
            if supply[i] > 0:
                min_cost1 = np.inf
                min_cost2 = np.inf

                for j in range(num_demand):
                    if demand[j] > 0:
                        cost = cost_matrix[i][j]
                        if cost < min_cost1:
                            min_cost2 = min_cost1
                            min_cost1 = cost
                        elif cost < min_cost2:
                            min_cost2 = cost

                penalty_rows[i] = min_cost2 - min_cost1

        for j in range(num_demand):
            if demand[j] > 0:
                min_cost1 = np.inf
                min_cost2 = np.inf

                for i in range(num_supply):
                    if supply[i] > 0:
                        cost = cost_matrix[i][j]
                        if cost < min_cost1:
                            min_cost2 = min_cost1
                            min_cost1 = cost
                        elif cost < min_cost2:
                            min_cost2 = cost

                penalty_cols[j] = min_cost2 - min_cost1

        max_penalty_row = np.argmax(penalty_rows)
        max_penalty_col = np.argmax(penalty_cols)

        if penalty_rows[max_penalty_row] > penalty_cols[max_penalty_col]:
            min_cost = np.inf
            min_cost_col = -1

            for j in range(num_demand):
                if demand[j] > 0:
                    cost = cost_matrix[max_penalty_row][j]
                    if cost < min_cost:
                        min_cost = cost
                        min_cost_col = j

            allocation[max_penalty_row][min_cost_col] = min(supply[max_penalty_row], demand[min_cost_col])
            supply[max_penalty_row] -= allocation[max_penalty_row][min_cost_col]
            demand[min_cost_col] -= allocation[max_penalty_row][min_cost_col]
        else:
            min_cost = np.inf
            min_cost_row = -1

            for i in range(num_supply):
                if supply[i] > 0:
                    cost = cost_matrix[i][max_penalty_col]
                    if cost < min_cost:
                        min_cost = cost
                        min_cost_row = i

            allocation[min_cost_row][max_penalty_col] = min(supply[min_cost_row], demand[max_penalty_col])
            supply[min_cost_row] -= allocation[min_cost_row][max_penalty_col]
            demand[max_penalty_col] -= allocation[min_cost_row][max_penalty_col]

    result_matrix = allocation.reshape(num_supply, num_demand)
    for i in range(num_supply):
        for j in range(num_demand):
            result_labels[i][j].configure(text=str(result_matrix[i][j]))

    
    
root = tk.Tk()
root.title("Vogel's Approximation Method")
root.geometry("1920x1080")
root.configure(bg="#f2f2f2")


title_label = tk.Label(root, text="Vogel's Approximation Method", font=("Arial", 16, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)


header_frame = tk.Frame(root, bg="#f2f2f2")
header_frame.pack()


header_label = tk.Label(header_frame, text="This system is designed specifically for the Balanced Transportation Problem, meaning that it will only function effectively when the total supply and total demand are equal.", font=("Arial", 12), bg="#f2f2f2")
header_label.pack(padx=15, pady=5)



header_label = tk.Label(header_frame, text="Destination 1       Destination 2       Destination 3", font=("Arial", 12), bg="#f2f2f2")
header_label.pack(padx=10, pady=5)




cost_frame = tk.Frame(root, bg="#f2f2f2")
cost_frame.pack()


cost_entries = []
for i in range(3):
    row_entries = []
    row_header = tk.Label(cost_frame, text="Source " + str(i + 1) + ":", font=("Arial", 12), bg="#f2f2f2")
    row_header.grid(row=i + 1, column=0, padx=15, pady=5)
    for j in range(3):
        entry = tk.Entry(cost_frame, width=10, font=("Arial", 12))
        entry.grid(row=i + 1, column=j + 1, padx=15, pady=5)
        row_entries.append(entry)
    cost_entries.append(row_entries)


supply_frame = tk.Frame(root, bg="#f2f2f2")
supply_frame.pack()


supply_entries = []
for i in range(3):
    label = tk.Label(supply_frame, text="Supply " + str(i + 1) + ":", font=("Arial", 12), bg="#f2f2f2")
    label.grid(row=0, column=i, padx=15, pady=5)
    entry = tk.Entry(supply_frame, width=10, font=("Arial", 12))
    entry.grid(row=1, column=i, padx=15, pady=5)
    supply_entries.append(entry)


demand_frame = tk.Frame(root, bg="#f2f2f2")
demand_frame.pack()


demand_entries = []
for i in range(3):
    label = tk.Label(demand_frame, text="Demand " + str(i + 1) + ":", font=("Arial", 12), bg="#f2f2f2")
    label.grid(row=0, column=i, padx=15, pady=5)
    entry = tk.Entry(demand_frame, width=10, font=("Arial", 12))
    entry.grid(row=1, column=i, padx=15, pady=5)
    demand_entries.append(entry)
    

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=vogels_approximation)
calculate_button.pack(pady=15)


supply_sum_label = tk.Label(root, text="Supply Sum: 0", font=("Arial", 12), bg="#f2f2f2")
supply_sum_label.pack()


demand_sum_label = tk.Label(root, text="Demand Sum: 0", font=("Arial", 12), bg="#f2f2f2")
demand_sum_label.pack()


result_frame = tk.Frame(root, bg="#f2f2f2")
result_frame.pack()


result_labels = []
for i in range(3):
    row_labels = []
    for j in range(3):
        label = tk.Label(result_frame, width=10, relief="ridge", font=("Arial", 12), bg="white")
        label.grid(row=i, column=j, padx=15, pady=5)
        row_labels.append(label)
    result_labels.append(row_labels)



message_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f2f2f2")
message_label.pack(pady=10)

root.mainloop()
