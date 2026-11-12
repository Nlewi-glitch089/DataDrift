# DataDrift

DataDrift is a small Python command-line exercise that combines a ZIP-code lookup with a randomized package scenario. It was built to practice API requests, user input, lists, random selection, and basic control flow.

## What it does

1. Asks the user for a US ZIP code.
2. Looks up the place name using the Zippopotam.us API.
3. Generates a temporary password and asks the user to verify it.
4. Selects sample package contents, a serial number, and a randomized delivery estimate.
5. Prints the generated package summary in the terminal.

**Important:** This is a demonstration, not a real package-tracking service. The delivery estimate, package contents, and serial number are randomly generated. It does not connect to carriers, track a real shipment, or provide a real delivery date. The ZIP-code API is used to look up a place name; it does not provide shipment information.

## Technology

- Python 3
- Requests
- Zippopotam.us ZIP-code API

## Requirements

- Python 3
- pip
- Internet access for the ZIP-code lookup

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Nlewi-glitch089/DataDrift.git
   cd DataDrift
   ```

2. (Recommended) Create and activate a virtual environment:

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python student_project.py
   ```

Enter a valid five-digit US ZIP code when prompted.

## Hosting

This repository is a terminal-based Python program, not a web application. It does not currently have a hosted public demo. Run it locally from a terminal to try it.

## Current limitations

- Package details and delivery timing are generated randomly.
- Serial numbers and password examples are hard-coded demonstration data, not a real authentication or shipment-security system.
- The program uses a simple terminal flow rather than a graphical interface.
- The ZIP lookup requires an internet connection.

This repository preserves the original learning exercise; it should not be presented as a live carrier-tracking product.
