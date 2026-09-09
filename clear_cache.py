import os
import time
import shutil

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