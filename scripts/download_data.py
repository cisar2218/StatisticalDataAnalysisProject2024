import os
import requests
from tqdm import tqdm


def download_data(output_dir, ouput_file, src_url):
    
    output_file = os.path.join(output_dir, ouput_file)

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

def download_data_raw():
    url = "https://drive.usercontent.google.com/download?id=1ot_GkrysuArYH2OSm75lYmFXLQXjg0RM&export=download&authuser=0&confirm=t&uuid=4ff580b8-eaa5-4d07-8fdd-6533bca6c28d&at=AENtkXYb_F3B9kJAlI6wg6aSFeSW%3A1732280272793"
    output_dir = "data/raw"
    output_filename = 'criminality_czech_republic.csv'
    download_data(output_dir, output_filename, url)


if __name__=='__main__':
    url = "https://drive.usercontent.google.com/download?id=1OVmUzzN87cPnvY-yqipnuyxLPZaXlXyh&export=download&authuser=0&confirm=t&uuid=66af4879-1ef8-4674-83d9-ff2add51ac7c&at=APvzH3qpNYiSN70Za9X-9X3DGvmH%3A1735654572350"
    output_dir = "data/processed"
    output_filename = 'updated_regions.csv'
    download_data(output_dir, output_filename, url)