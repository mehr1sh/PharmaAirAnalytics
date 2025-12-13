#!/usr/bin/env python3
"""thingspeak_read.py

Fetch ThingSpeak channel feeds for a given date range and save to CSV.

Usage: run without arguments — the script is preconfigured to fetch
2025-10-15 00:00:00 through 2025-10-25 23:59:59 UTC for channel 937750.

This uses only the Python standard library.
"""
from __future__ import annotations

import csv
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from typing import List, Dict, Any


API_KEY = "60NLXBD7BWW10LRV"
CHANNEL_ID = 947311
START = "2025-07-15 00:00:00"
END = "2025-07-25 23:59:59"
OUT_CSV = "feeds_t-hub_july.csv"


def fetch_feeds(start: str, end: str, api_key: str = API_KEY, channel: int = CHANNEL_ID) -> Dict[str, Any]:
    """Fetch feeds JSON from ThingSpeak for the given start/end (UTC)."""
    base = f"https://api.thingspeak.com/channels/{channel}/feeds.json"
    params = {
        "api_key": api_key,
        "start": start,
        "end": end,
    }
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            return json.loads(body)
    except Exception as exc:
        print(f"Error fetching feeds: {exc}", file=sys.stderr)
        raise


def save_csv(feeds_json: Dict[str, Any], out_path: str = OUT_CSV) -> None:
    """Save feeds JSON to CSV with timestamp and fields 1..8."""
    feeds = feeds_json.get("feeds", [])
    if not feeds:
        print("No feeds found for the given range.")

    # Determine field columns present
    field_cols = [f"field{i}" for i in range(1, 9)]
    header = ["created_at", "entry_id"] + field_cols

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for item in feeds:
            row = [item.get("created_at"), item.get("entry_id")]
            for col in field_cols:
                row.append(item.get(col, ""))
            writer.writerow(row)

    print(f"Saved {len(feeds)} rows to {out_path}")


def main() -> int:
    try:
        print(f"Fetching feeds {START} -> {END} for channel {CHANNEL_ID} ...")
        data = fetch_feeds(START, END)
        save_csv(data, OUT_CSV)
    except Exception:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
import requests
import os

# --- ThingSpeak Channel Details ---
# !!! REPLACE 'YOUR_CHANNEL_ID' WITH THE ACTUAL NUMBER !!!
CHANNEL_ID = '937750' 
READ_API_KEY = 'EWD8UER61NQ0ZRTJ' 

# --- Date Range ---
START_DATE_TIME = '2025-10-15 00:00:00'
END_DATE_TIME = '2025-10-25 23:59:59'

# --- File Output ---
OUTPUT_FILENAME = 'thingspeak_data_oct_2025.csv'

def get_thingspeak_data_to_csv():
    """
    Fetches the ThingSpeak data in CSV format and saves it locally.
    """

    # Base URL for the CSV feed endpoint
    base_url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.csv"

    # Parameters for the API request
    params = {
        'api_key': READ_API_KEY,
        # ThingSpeak requires URL-encoded spaces (%20)
        'start': START_DATE_TIME.replace(' ', '%20'),
        'end': END_DATE_TIME.replace(' ', '%20'),
        'results': 0 # Fetch all data for the time window
    }

    # Construct the full request URL
    request_url = f"{base_url}?api_key={params['api_key']}&start={params['start']}&end={params['end']}&results={params['results']}"

    print(f"Attempting to fetch data from Channel ID: {CHANNEL_ID}...")

    try:
        response = requests.get(request_url)

        if response.status_code == 200:
            csv_data = response.text

            # Check for actual data content
            if csv_data and len(csv_data.splitlines()) > 1:
                with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
                    file.write(csv_data)

                print("-" * 50)
                print(f"✅ Success! Data saved to **{OUTPUT_FILENAME}**")
                print(f"File location: {os.path.abspath(OUTPUT_FILENAME)}")
                print("-" * 50)
            else:
                print(f"⚠️ Warning: No data returned for the dates **{START_DATE_TIME}** to **{END_DATE_TIME}**.")
        else:
            print(f"❌ Error: Failed to retrieve data. HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the request: {e}")

# Run the function
if __name__ == "__main__":
    if CHANNEL_ID == 'YOUR_CHANNEL_ID':
        print("\n*** ERROR: Please update the 'CHANNEL_ID' variable in the script. ***\n")
    else:
        get_thingspeak_data_to_csv()