from system_info import system_info
from clear import clear
from power_plan import power_plan
from clear_cache import clear_cache
from disk_defrag import disk_defrag
from install_program import app_selection
import sys
import time
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Running as Administrator...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

sys.stdout.reconfigure(encoding='utf-8')

greets = """
winOpt v0.4.0-alpha.1
Project made by Stefan Aničić aka aniciccstefan
This program may not be compatible with all Windows computers! (JUST A PROTOTYPE, DO AT YOUR OWN RISK)
"""

ascii_banner = """
██╗    ██╗██╗███╗   ██╗ ██████╗ ██████╗ ████████╗
██║    ██║██║████╗  ██║██╔═══██╗██╔══██╗╚══██╔══╝
██║ █╗ ██║██║██╔██╗ ██║██║   ██║██████╔╝   ██║   
██║███╗██║██║██║╚██╗██║██║   ██║██╔═══╝    ██║   
╚███╔███╔╝██║██║ ╚████║╚██████╔╝██║        ██║   
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝        ╚═╝   """

def main_menu():
    while True:
            clear()
            print(ascii_banner)
            print(greets)
            print("""
Select an option:
[1] System Info
[2] Change Power Plan
[3] Disk defrag
[4] Install Drivers (AT YOUR OWN RISK!!!)
[5] Install programs
[6] Clear cache
[0] Exit""")
            print(" ")
            main_menu_input = input("Enter your choice: ").strip().lower()
            if main_menu_input == "1":
                clear()
                system_info()
            elif main_menu_input == "2":
                clear()
                power_plan()
            elif main_menu_input == "3":
                clear()
                disk_defrag()
            elif main_menu_input == "5":
                clear()
                app_selection()
            elif main_menu_input == "6":
                clear()
                clear_cache()
            elif main_menu_input == "0":
                break
            else:
                print("Invalid option.")
                time.sleep(3)

main_menu()