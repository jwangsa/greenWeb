# Power Consumption Monitor

## Description
This script provides a graphical interface for tracking the power consumption of a specific application running on the system. The program uses Python's psutil library to monitor system processes and calculate the power usage, while the GUI is built using the tkinter library.

## Functions
1. **get_process_name(pid):** This function accepts a process ID (PID) as an argument and returns the name of the corresponding process.

2. **calculate_power_consumption(pid):** This function takes a PID as input and returns an estimated power usage of the corresponding process. The power consumption is calculated based on both the CPU usage and the memory usage (RAM) of the process.

3. **start_monitoring():** This function starts the power consumption monitoring for the process specified in the entry field of the GUI. It sets a global flag `monitoring` to `True` and begins the recursive calling of `monitor_process()`. If the process is not found, it shows an error message.

4. **stop_monitoring():** This function stops the power consumption monitoring by setting the global flag `monitoring` to `False`, which ends the recursive calling of `monitor_process()`.

5. **clear_log():** This function clears the content of the text widget in the GUI, removing all the previous power consumption logs.

6. **monitor_process():** This function is recursively called when the monitoring is active. It calculates and logs the power consumption of the monitored process and then schedules itself to be called again after one second.

## Usage
When the script is run, the window 'Power Consumption Monitor' opens. The user can enter the name of the process to be monitored in the provided field and click the 'Start Monitoring' button to start the power consumption tracking. The estimated power consumption of the specified process is updated every second and displayed in the text area of the window.

The 'Stop Monitoring' button can be used to stop the power consumption tracking. The 'Clear Log' button can be used to clear all previous power consumption logs from the text area. This helps with maintaining interface performance as well.

## Note
The power consumption values provided by this tool are only estimates. The actual power usage of a process can vary and depends on many factors, including the system's hardware configuration and the process's current activity.