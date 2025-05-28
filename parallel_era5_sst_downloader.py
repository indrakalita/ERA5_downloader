import cdsapi
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure output directory exists
os.makedirs("sst_downloads", exist_ok=True)

# Define all years and chunk size
years = [str(y) for y in range(2000, 2025)]
chunk_size = 8
chunks = [years[i:i + chunk_size] for i in range(0, len(years), chunk_size)]

# Dataset and base request parameters
dataset = "reanalysis-era5-single-levels"
base_request = {
    "product_type": "reanalysis",
    "variable": "sea_surface_temperature",
    "month": [f"{m:02d}" for m in range(1, 13)],
    "day": [f"{d:02d}" for d in range(1, 32)],
    "time": ["00:00", "06:00", "12:00", "18:00"],
    "data_format": "netcdf",
    "area": [5, -31, -25, 9]  # [N, W, S, E]
}

def download_chunk(year_chunk):
    """Download a chunk of years as a NetCDF file."""
    client = cdsapi.Client()
    request = base_request.copy()
    request["year"] = year_chunk
    filename = f"sst_downloads/era5_sst_{year_chunk[0]}_{year_chunk[-1]}.nc"

    print(f"[START] Downloading {filename}")
    try:
        client.retrieve(dataset, request).download(filename)
        print(f"[DONE]  Saved {filename}")
    except Exception as e:
        print(f"[ERROR] Failed for years {year_chunk}: {e}")

# Run parallel downloads
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download_chunk, chunk) for chunk in chunks]
    for future in as_completed(futures):
        pass  # Output is already printed inside download_chunk()
