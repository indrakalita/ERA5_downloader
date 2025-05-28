# 🌍 ERA5 SST Downloader – Chunked & Parallel 🚀

Have you ever tried downloading **ERA5 reanalysis data** (like **sea surface temperature - SST**) and got hit with this message?

> ❌ "Your request is too large."

Or maybe your download just sat in a **long queue**... and sat... and sat...

### 😩 We've all been there.

The CDS API is a powerful tool, but it doesn’t love huge multi-year, multi-variable, high-frequency requests.  
That's where this script comes in.

---

## ✅ What This Script Does

This Python script:

- Splits a large ERA5 SST download request into **smaller chunks** (e.g., 8 years at a time)
- Uses `concurrent.futures` to download those chunks **in parallel**
- Saves each NetCDF file separately in a `sst_downloads/` folder
- Works for custom **date ranges**, **regions**, and **variables**
- Helps you **avoid timeouts, size errors, and long queues**

---

## 🔧 Requirements

- Python 3.x
- `cdsapi` (`pip install cdsapi`)
- CDS API credentials in your `~/.cdsapirc` file  
  👉 [How to set it up](https://cds.climate.copernicus.eu/api-how-to)

---

## ▶️ How to Use

1. Clone this repo or copy the script.
2. Run it:

```bash
python parallel_era5_sst_downloader.py
