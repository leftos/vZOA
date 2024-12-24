import json
import os

# resolve the path %localappdata%/crc/profiles
profiles_dir = os.path.join(os.environ['LOCALAPPDATA'], 'crc', 'profiles')
# find the first json file in the directory
for file in os.listdir(profiles_dir):
    if file.endswith('.json'):
        profile_path = os.path.join(profiles_dir, file)
        print(f"Found {profile_path}")
        # parse the file as json
        with open(profile_path, 'r', encoding="utf8") as f:
            data = json.load(f)
            data["FlightPlanEditorSettings"]["WindowSettings"]["IsMaximized"] = True
        with open(profile_path, 'w', encoding="utf8") as f:
            json.dump(data, f, indent=2)
            f.truncate()
            print(f"Maximized the Flight Plan Editor window in {profile_path}")
        break
os.system("pause")
