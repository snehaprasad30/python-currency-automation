# Automated Currency Converter & Report Generator

## Description
A resilient Python backend automation script that fetches live global exchange rates for CHF/INR currency pairs using a REST API. To guarantee institutional stability, the script implements an advanced fallback exception-handling mechanism (`try-except` architecture) to ensure continuous report generation even during API website downtimes.

## Core MCA Concepts Demonstrated
* **API Integration:** Consuming and handling HTTP REST requests.
* **Fault Tolerance & Exception Handling:** Ensuring system uptime with automated backup data models during live environment drops.
* **File I/O Automation:** Dynamically parsing and writing system file payloads.

## Technology Stack
* **Language:** Python 3
* **Libraries:** Requests, JSON, OS, Datetime
