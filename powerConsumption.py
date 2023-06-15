import psutil
import tkinter as tk
from tkinter import messagebox

def get_process_name(pid):
    # get process details as process object
    proc_obj = psutil.Process(pid)

    # get process name from its pid
    return proc_obj.name()

def calculate_power_consumption(pid):
    # create Process object
    proc = psutil.Process(pid)

    # define power constant
    power_constant = 0.000001

    # CPU usage of the process
    cpu_usage = proc.cpu_percent()

    # memory usage of the process
    memory_info = proc.memory_info()
    mem_usage = memory_info.rss  # rss: memory retained in RAM

    # estimate power usage
    power_usage = (cpu_usage + mem_usage) * power_constant

    return power_usage

def start_monitoring():
    global monitoring, process_name, monitored_process_id
    process_name = entry.get()

    # obtain list of all running processes
    all_processes = psutil.pids()

    for process in all_processes:
        if get_process_name(process) == process_name:
            monitored_process_id = process
            monitoring = True
            monitor_process()
            break
    else:
        messagebox.showerror("Error", "Process not found. Please ensure the process is running and the name is correct.")

def stop_monitoring():
    global monitoring
    monitoring = False

def clear_log():
    text.delete(1.0, tk.END)

def monitor_process():
    if monitoring:  # check global flag
        output = f'{process_name} power consumption: {calculate_power_consumption(monitored_process_id)} W'
        text.insert(tk.END, output + '\n')
        root.after(1000, monitor_process)  # recall function after 1 second

root = tk.Tk()
root.title('Power Consumption Monitor')

label = tk.Label(root, text='Enter process name:')
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text='Start Monitoring', command=start_monitoring)
start_button.pack()

stop_button = tk.Button(root, text='Stop Monitoring', command=stop_monitoring)
stop_button.pack()

clear_button = tk.Button(root, text='Clear Log', command=clear_log)
clear_button.pack()

text = tk.Text(root)
text.pack()

root.mainloop()