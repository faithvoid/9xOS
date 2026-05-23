import os
import subprocess
from pathlib import Path

def extract_icon(exe_path, app_name):
    icon_dir = os.path.expanduser("~/.local/share/icons/wine_apps")
    os.makedirs(icon_dir, exist_ok=True)
    
    icon_output_path = os.path.join(icon_dir, f"{app_name.replace(' ', '_')}.png")
    
    try:
        temp_dir = "/tmp/exe_icons"
        os.makedirs(temp_dir, exist_ok=True)
        
        subprocess.run(['wrestool', '-x', '-t', '14', exe_path, '-o', temp_dir], check=True, capture_output=True)
        
        extracted_files = [os.path.join(temp_dir, f) for f in os.listdir(temp_dir)]
        if not extracted_files:
            return "wine" # Fallback to default wine icon
            
        subprocess.run(['icotool', '-x', '-o', icon_output_path, extracted_files[0]], check=True, capture_output=True)
        
        for f in extracted_files: os.remove(f)
        
        return icon_output_path
    except Exception as e:
        print(f"Could not extract icon: {e}")
        return "wine"

def create_desktop_file(exe_path, app_name):
    home = str(Path.home())
    desktop_folder = os.path.join(home, ".local/share/applications")
    os.makedirs(desktop_folder, exist_ok=True)
    
    icon_path = extract_icon(exe_path, app_name)
    
    file_path = os.path.join(desktop_folder, f"{app_name.replace(' ', '_')}.desktop")
    
    content = f"""[Desktop Entry]
Name={app_name}
Exec=wine "{exe_path}"
Type=Application
Categories=Wine;
Terminal=false
Icon={icon_path}
Path={os.path.dirname(exe_path)}
"""
    with open(file_path, "w") as f:
        f.write(content)
    
    os.chmod(file_path, 0o755)
    print(f"Created: {file_path}")

def scan_and_create():
    root_dir = input("Enter the (batch) path to scan: ").strip()
    if not os.path.isdir(root_dir):
        print("Invalid directory.")
        return

    for root, dirs, files in os.walk(root_dir):
        exes = [f for f in files if f.lower().endswith('.exe')]
        if not exes: continue

        print(f"\nFolder: {root}")
        for i, exe in enumerate(exes):
            print(f" [{i + 1}] {exe}")
        print(f" [0] Skip")

        choice = input("Select EXE: ")
        try:
            idx = int(choice) - 1
            if idx == -1: continue
            if 0 <= idx < len(exes):
                selected_exe = os.path.join(root, exes[idx])
                app_name = input(f"Enter name for '{exes[idx]}': ")
                create_desktop_file(selected_exe, app_name)
        except ValueError:
            pass

if __name__ == "__main__":
    scan_and_create()
