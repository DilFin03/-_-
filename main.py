import tkinter as tk
import psutil
import time

class NetworkMonitorApp:
    def __init__(self, master):
        self.master = master
        master.title("Моніторинг мережі")

        self.label_cpu = tk.Label(master, text="CPU використання:")
        self.label_cpu.grid(row=0, column=0, sticky="w")

        self.label_memory = tk.Label(master, text="Використання пам'яті:")
        self.label_memory.grid(row=1, column=0, sticky="w")

        self.label_disk = tk.Label(master, text="Використання диску:")
        self.label_disk.grid(row=2, column=0, sticky="w")

        self.label_network = tk.Label(master, text="Мережевий трафік:")
        self.label_network.grid(row=3, column=0, sticky="w")

        self.update_labels()

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        network_stats = psutil.net_io_counters()

        self.label_cpu.config(text=f"CPU використання: {cpu_percent}%")
        self.label_memory.config(text=f"Використання пам'яті: {memory_percent}%")
        self.label_disk.config(text=f"Використання диску: {disk_percent}%")
        self.label_network.config(text=f"Мережевий трафік: "
                                        f"Вхідний - {network_stats.bytes_recv} байт, "
                                        f"Вихідний - {network_stats.bytes_sent} байт")

        self.master.after(1000, self.update_labels)  # Оновлення кожну секунду

def main():
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
