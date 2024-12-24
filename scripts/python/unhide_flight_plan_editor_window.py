# unhide_flight_plan_editor_window

import json
import os

# resolve the path %localappdata%/crc/profiles
profiles_dir = os.path.join(os.environ['LOCALAPPDATA'], 'crc', 'profiles')
if not os.path.exists(profiles_dir):
    print(f"Could not find the profiles directory at {profiles_dir}")
    os.system("pause")
    exit(1)
# find the first json file in the directory
found_file = False
for file in os.listdir(profiles_dir):
    if file.endswith('.json'):
        profile_path = os.path.join(profiles_dir, file)
        found_file = True
        print(f"Found {profile_path}")
        data = None
        # parse the file as json
        try:
            with open(profile_path, 'r', encoding="utf8") as f:
                data = json.load(f)
                # maximize the Flight Plan Editor window so that it unhides itself
                data["FlightPlanEditorSettings"]["WindowSettings"]["IsMaximized"] = True
        except json.JSONDecodeError as e:
            print(f"Failed to parse the json file: {e}")
            os.system("pause")
            exit(1)
        if data:
            try:
                with open(profile_path, 'w', encoding="utf8") as f:
                    json.dump(data, f, indent=2)
                    f.truncate()
                    print(f"Maximized the Flight Plan Editor window in {profile_path}")
            except Exception as e:
                print(f"Failed to write the json file: {e}")
        break

if not found_file:
    print("Could not find a profile json file in the profiles directory")

os.system("pause")
