import subprocess
from clear import clear

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

def install_program(package_id):
    print(f"Starting installation for {package_id}...")
    
    command = ["winget", "install", "-e", "--id", package_id, "--silent", "--accept-source-agreements", "--accept-package-agreements"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"Successfully installed {package_id}!")
        if result.stdout:
            print(f"\nOutput: \n{result.stdout}")
        if result.stderr:
            print(f"\nWarnings: \n{result.stderr}")

        input("Press ENTER to get back...")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_id}.")
        print(f"\nReturn Code: \n{e.returncode}")
        if e.stdout:
            print(f"\nOutput: \n{e.stdout}")
        if e.stderr:
            print(f"\nError Output: \n{e.stderr}")

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