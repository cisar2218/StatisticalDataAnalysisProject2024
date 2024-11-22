import os
import requests
from tqdm import tqdm


url = "https://drive.usercontent.google.com/download?id=1ot_GkrysuArYH2OSm75lYmFXLQXjg0RM&export=download&authuser=0&confirm=t&uuid=4ff580b8-eaa5-4d07-8fdd-6533bca6c28d&at=AENtkXYb_F3B9kJAlI6wg6aSFeSW%3A1732280272793"
output_dir = "data/raw"
output_file = os.path.join(output_dir, "criminality_czech_republic.csv")

os.makedirs(output_dir, exist_ok=True)

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    with open(output_file, "wb") as f, tqdm(
        total=total_size, unit='B', unit_scale=True, desc="Downloading", ascii=True
    ) as pbar:
        for chunk in response.iter_content(chunk_size=8192):  # Download in chunks
            f.write(chunk)
            pbar.update(len(chunk))

    print(f"File downloaded and saved as: {output_file}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
