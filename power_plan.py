from clear import clear
import subprocess
import time

balanced_guid = "381b4222-f694-41f0-9685-ff5bb260df2e"
high_guid = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
power_saver_guid = "a1841308-3541-4fab-bc81-f71556f20b4a"
ultimate_guid = "e9a42b02-d5df-448d-aa00-03f14749eb61"

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