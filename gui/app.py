import tkinter as tk
from tkinter import ttk, messagebox
from database.db_operations import query_real_time, view_statistics

def setup_gui():
    def query_data():
        device_id = device_id_var.get()
        data = query_real_time(device_id)
        if data:
            messagebox.showinfo("Real-time Data", f"Device ID: {data[1]}\nTimestamp: {data[2]}\nPower Consumption: {data[3]:.2f} watts")
        else:
            messagebox.showwarning("No Data", "No data available for the specified device.")

    def view_stats():
        device_id = device_id_var.get()
        avg, peak = view_statistics(device_id)
        messagebox.showinfo("Statistics", f"Average Power Consumption: {avg:.2f} watts\nPeak Power Consumption: {peak:.2f} watts")

    root = tk.Tk()
    root.title("Energy Monitoring System")

    mainframe = ttk.Frame(root, padding="10")
    mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(mainframe, text="Device ID:").grid(row=1, column=1, sticky=tk.W)

    # Dropdown for device ID selection
    device_id_var = tk.StringVar()
    device_id_combobox = ttk.Combobox(mainframe, textvariable=device_id_var, values=["device_1", "device_2", "device_3"])
    device_id_combobox.grid(row=1, column=2, sticky=(tk.W, tk.E))
    device_id_combobox.set("device_1")  # Set default value

    ttk.Button(mainframe, text="Query Real-time Data", command=query_data).grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))
    ttk.Button(mainframe, text="View Statistics", command=view_stats).grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E))

    root.mainloop()