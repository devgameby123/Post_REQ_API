import requests
import json
import os

folder_path = "./image"
Allfile = []
if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(file)
            Allfile.append(file_name+file_extension)
else:
    print("โฟลเดอร์ไม่พบ")

# Replace with your actual FastAPI server endpoint
url = 'https://c6c4-161-246-147-96.ngrok-free.app/create_movie'

# Load JSON data from file
with open('./data.json', 'r') as json_file:
    movie_data = json.load(json_file)
i = 0
for value in movie_data:
    fileInput = "image/"+Allfile[i]
    # Prepare the files
    files = {
        'file': (Allfile[i], open(fileInput, 'rb')),
        'movie_data': ('movie_data.json', json.dumps(value), 'application/json')
    }
    i += 1
    # Make the POST request
    response = requests.post(url, files=files)

    # Check the response
    if response.status_code == 200:
        print("Movie creation successful")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
