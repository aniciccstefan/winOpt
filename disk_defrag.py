import subprocess
import time

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