# Food Truck Tool

This repository contains a Python-based command-line tool to manage and query food truck data in San Francisco. The tool can download the latest food truck data, clean it, and filter it based on cuisine type and facility type.

## Features

- **Download Food Truck Data**: Fetch the latest data from San Francisco's open data portal and remove entries without location data and those with status 'SUSPENDED' or 'EXPIRED'.
- **List Food Trucks**: List all of the food trucks in the San Francisco area.
- **Filter Data**: List food trucks based on cuisine type and facility type (e.g., Truck, Push Cart).

## Prerequisites

- Python 3.6 or higher
- `pandas`, `requests`, and `click` libraries

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/pilotlicense/engineering-challenge.git
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m food_truck_tool env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install pandas requests click
    ```

## Usage

### Download the Latest Food Truck Data

To download the latest food truck data from San Francisco's open data portal:
```bash
python food_truck_tool.py download
```
This will fetch the data and save it to food_trucks.csv.

### List All Food Trucks

To list all food trucks:
```bash
python food_truck_tool.py list-trucks
```

### Filter Food Trucks by Cuisine

To filter food trucks by a specific cuisine:
```bash
python food_truck_tool.py list-trucks --cuisine "Tacos"
```

### Filter Food Trucks by Facility Type

To filter food trucks by facility type (ie: Truck, Push Cart):
```bash
python food_truck_tool.py list-trucks --facility-type "Truck"
```

### Combine Filters

To combine filters for cuisine and facility type:
```bash
python food_truck_tool.py list-trucks --cuisine "Tacos" --facility-type "Truck"
```

## Acknowledgments
Thanks to the San Francisco government for providing the open data used in this project.