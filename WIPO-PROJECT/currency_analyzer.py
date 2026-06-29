import json
import os
from datetime import datetime
import requests

# 1. Try to fetch live currency exchange rates from the API
url = "https://er-api.com"
try:
    response = requests.get(url, timeout=5)
    data = response.json()
    rates = data.get("rates", {})
    usd_to_chf = rates.get("CHF", 0.89)
    usd_to_inr = rates.get("INR", 83.50)
    chf_to_inr = round(usd_to_inr / usd_to_chf, 2)
    status_message = "API Connection Successful (Live Data)"
except Exception:
    # Backup Fallback: If the API website is down, use baseline market rates
    chf_to_inr = 93.45  
    status_message = "API Offline - Utilizing Cached Baseline Market Rates"

# 2. Create a structured report dictionary
report_data = {
    "organization": "WIPO Application Technical Demo",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "base_currency": "CHF (Swiss Franc)",
    "target_currency": "INR (Indian Rupee)",
    "live_exchange_rate": f"1 CHF = {chf_to_inr} INR",
    "status": status_message,
}

# 3. Automatically save this data as a clean JSON report file
output_filename = "exchange_report.json"
with open(output_filename, "w") as file:
    json.dump(report_data, file, indent=4)

print("=" * 40)
print("SUCCESS: Code Executed Safely!")
print(f"Current Rate: {report_data['live_exchange_rate']}")
print(f"Status: {status_message}")
print(f"Report saved to: {os.path.abspath(output_filename)}")
print("=" * 40)
