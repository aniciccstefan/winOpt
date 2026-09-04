import os
import subprocess
import sys
import time
import ctypes
import shutil

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

balanced_guid = "381b4222-f694-41f0-9685-ff5bb260df2e"
high_guid = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
power_saver_guid = "a1841308-3541-4fab-bc81-f71556f20b4a"
ultimate_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"

apps = {
    "1": ("Google Chrome", "Google.Chrome"),
    "2": ("Steam", "Valve.Steam"),
    "3": ("OBS Studio", "OBSProject.OBSStudio"),
    "4": ("Discord", "Discord.Discord"),
    "5": ("Visual Studio Code", "Microsoft.VisualStudioCode"),
    "6": ("Spotify", "Spotify.Spotify"),
    "7": ("VLC Player", "VideoLAN.VLC"),
    "8": ("InkScape", "Inkscape.Inkscape"),
    "9": ("Audacity", "Audacity.Audacity"),
    "10": ("uTorrent", "BitTorrent.uTorrent"),
    "11": ("Git", "Git.Git"),
    "12": ("GIMP", "GIMP.GIMP"),
    "13": ("Krita", "Krita.Krita"),
    "14": ("WhatsApp", "WhatsApp.WhatsApp"),
    "15": ("7Zip", "7zip.7zip")
}


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
[1] Change Power Plan
[2] Disk defrag
[3] Install Drivers (AT YOUR OWN RISK!!!)
[4] Install programs
[5] Clear cache
[6] Exit""")
            print(" ")
            main_menu_input = input("Enter your choice: ").strip().lower()
            if main_menu_input == "1":
                clear()
                power_plan()
            elif main_menu_input == "2":
                clear()
                disk_defrag()
            elif main_menu_input == "4":
                clear()
                app_selection()
            elif main_menu_input == "5":
                clear()
                clear_cache()
            elif main_menu_input == "6":
                break
            else:
                print("Invalid option.")
                time.sleep(3)

def set_power_plan(guid, name):
    try:
        subprocess.run(["powercfg", "/setactive", guid], check=True)
    except Exception as e:
        print("[ERROR]:", e)
        input("Press Enter to return... ")
        clear()
        return
    print(" ")
    print("Changing your power plan...")
    time.sleep(2)
    print("Done.")
    print(f"Power plan changed to {name}.")
    input("Press Enter to return...")
    clear()

def power_plan():
    print("""
Choose a power plan:
[1] Power Saver
[2] Balanced
[3] High Performance
[4] Ultimate Performance
[0] Exit""")
    print(" ")
    power_plan_input = input("Enter an option: ").strip().lower()
    if(power_plan_input == "1"):
        set_power_plan(power_saver_guid, "Power Saver")
    elif(power_plan_input == "2"):
        set_power_plan(balanced_guid, "Balanced")
    elif(power_plan_input == "3"):
        set_power_plan(high_guid, "High Performance")
    elif(power_plan_input == "4"):
        result = subprocess.run(["powercfg", "/list"], capture_output=True, text=True)
        if ultimate_guid in result.stdout:
            print("Ultimate Performance plan detected.")
            set_power_plan(ultimate_guid, "Ultimate Performance")
        else:
            print("Ultimate Performance plan is not detected.")
            time.sleep(2)
            print("Adding...")
            time.sleep(3)
            print("Successful.")
            time.sleep(3)
            subprocess.run(["powercfg", "-duplicatescheme", ultimate_guid], check=True)
            set_power_plan(ultimate_guid, "Ultimate Performance")

def clear():
    os.system("cls")


def disk_defrag():
    print("""
HDD or SSD?:
[1] HDD
[2] SSD
""")
    disk_defrag_input = input("Enter an option: ").lower().strip()
    c_or_d = input("Enter a letter of your disk (ex. C, D): ").lower().strip()
    if disk_defrag_input == "1":
        try:
            subprocess.run(["defrag", f"{c_or_d}:", "/U", "/V"], check=True)
            input("Done! Press Enter to return...")
            return
        except subprocess.CalledProcessError as e:
            print(f"\nDefragmentation failed!")
            print(f"Error code: {e.returncode}")
            input("\nPress Enter to return...")
        return
    elif disk_defrag_input == "2":
        print("SSDs do not need defragmentation and optimization!")
        time.sleep(3)
        input("Press Enter to return...")
        return
    else:
        print("\nInvalid option!")
        input("Press Enter to return...")
    
    

def clear_cache():
    paths = [
        os.environ.get('TEMP'),
        r"C:\Windows\Prefetch",
        r"C:\Windows\Temp"
    ]

    for path in paths:
        if not path or not os.path.exists(path):
            continue

        print(f"Deleting {path}...")
        time.sleep(5)

        for item in os.listdir(path):
            item_path = os.path.join(path, item)

            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"[ERROR] Error has occured while deleting {item_path}: {e}")
    
    print("Temporary folders successfully deleted.")
    input("Press Enter to return...")

def install_program(package_id):
    print(f"Starting installation for {package_id}...")
    
    # Construct the winget command
    # -e matches the exact ID, --silent handles background installation
    command = ["winget", "install", "-e", "--id", package_id, "--silent", "--accept-source-agreements", "--accept-package-agreements"]
    
    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully installed {package_id}!")
        input("Press ENTER to get back...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_id}.")
        print(f"Error output:\n{e.stderr}")
        input("Press ENTER to get back...")


def app_selection():
    app_selector = """
Choose an app to install:
[1] Google Chrome
[2] Steam
[3] OBS Studio
[4] Discord
[5] Visual Studio Code
[6] Spotify
[7] VLC Player
[8] InkScape
[9] Audacity
[10] uTorrent
[11] Git
[12] GIMP
[13] Krita
[14] WhatsApp
[15] 7Zip
[0] Exit
"""
    clear()
    print(app_selector)
    app_selected = input("Enter an option: ").strip().lower()
    if app_selected == "0":
        input("Press ENTER to go back...")

    if app_selected in apps:
        app_name, package_id = apps[app_selected]
        print(f"Selected {app_name}")
        install_program(package_id)
    else:
        print("Invalid option.")
        print("Press ENTER to return...")
    

main_menu()