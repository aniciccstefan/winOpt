from clear import clear
from cpuinfo import get_cpu_info
import psutil
import platform
import wmi

def system_info():

    clear()
    info = get_cpu_info()
    cpu_model = info.get('brand_raw', 'Nepoznat CPU')

    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)

    gpu_model = "Nepoznat GPU"
    try:
        w = wmi.WMI()
        gpus = [gpu.Name for gpu in w.Win32_VideoController()]
        if gpus:
            gpu_model = ", ".join(gpus)
    except Exception:
        gpu_model = "Nije moguće učitati GPU"

    ram = psutil.virtual_memory()
    total_ram_raw = round(ram.total / (1024 ** 3))
    total_ram = f"{total_ram_raw}.00"
    used_ram = round(ram.used / (1024 ** 3), 2)
    free_ram = round(ram.available / (1024 ** 3), 2)

    print("""
=============================
       SYSTEM INFORMATION
=============================
""")

    print(f"OS:           {platform.system()} {platform.release()}")
    print(f"Version:      {platform.version()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor:    {cpu_model}")
    print(f"CPU Cores:    {cores} Cores")
    print(f"CPU Threads:  {threads} Threads")
    print(f"GPU:          {gpu_model}")
    print(f"RAM Memory:   {total_ram} GB total ({used_ram} GB used, {free_ram} GB free)")
    print(f"Computer:     {platform.node()}")

    print("""
=============================
""")
    input("Press ENTER to go back...")