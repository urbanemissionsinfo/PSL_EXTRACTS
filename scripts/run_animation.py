import pandas as pd
import subprocess
from tqdm import tqdm

cities = pd.read_csv(r'C:\Users\dskcy\UEInfo\PSL_EXTRACTS\assets\city_state_file_names.csv')

for city in tqdm(cities['filename']):
    print("Producing animation for: ", city)
    subprocess.run(["python", "scripts/animation_timeseries.py", "era5", "temp2m", city])