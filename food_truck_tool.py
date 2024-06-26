import requests
import pandas as pd
import click
from datetime import datetime

# Function to download food truck data
def download_food_truck_data(url, output_file):
    """
    Downloads the food truck data from the specified URL and saves it to the output file.
    """
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(output_file, 'wb') as file:
        file.write(response.content)
    print(f"Data downloaded and saved to {output_file}")

# Function to load and clean data
def load_and_clean_data(file_path):
    """
    Loads the food truck data from the file, cleans it by removing entries without location data,
    and entries with status 'SUSPENDED' or 'EXPIRED'.
    """
    df = pd.read_csv(file_path)
    print(df.columns)  # Print column names to verify
    df = df.dropna(subset=['Latitude', 'Longitude'])
    df = df[~df['Status'].isin(['SUSPENDED', 'EXPIRED'])]
    return df

# Function to check if a food truck is open now
def is_open_now(dayshours):
    """
    Checks if a food truck is open now based on the dayshours column.
    """
    if not dayshours:
        return False

    # Get current day and time
    now = datetime.now()
    current_day = now.strftime("%a").upper()
    current_time = now.time()

    # Split dayshours into individual periods
    for period in dayshours.split(';'):
        day_hours = period.split('/')
        if len(day_hours) != 2:
            continue
        
        days, hours = day_hours
        if current_day in days:
            # Split hours into start and end times
            start_time_str, end_time_str = hours.split('-')
            start_time = datetime.strptime(start_time_str, "%I%p").time()
            end_time = datetime.strptime(end_time_str, "%I%p").time()
            # Check if current time is within the start and end times
            if start_time <= current_time <= end_time:
                return True

    return False

# Click CLI setup
@click.group()
def cli():
    """Main CLI group"""
    pass

@cli.command()
@click.option('--cuisine', help='Filter by type of cuisine')
@click.option('--facility-type', help='Filter by facility type (e.g., Truck, Push Cart)')
@click.option('--open-now', is_flag=True, help='Show food trucks open now')
def list_trucks(cuisine, facility_type, open_now):
    """
    List food trucks based on optional filters: cuisine, facility type, and whether they are open now.
    """
    # Load data globally to use in all commands
    df = load_and_clean_data("food_trucks.csv")
    
    result = df
    # Filter by cuisine if provided
    if cuisine:
        result = result[result['FoodItems'].str.contains(cuisine, case=False, na=False)]
    # Filter by facility type if provided
    if facility_type:
        result = result[result['FacilityType'].str.contains(facility_type, case=False, na=False)]
    # Filter by whether the food truck is open now if the flag is set
    if open_now:
        result = result[result['dayshours'].apply(is_open_now)]

    click.echo(result[['Applicant', 'FoodItems', 'Address']])

@cli.command()
def download():
    """
    Download the latest food truck data.
    """
    data_url = "https://data.sfgov.org/api/views/rqzj-sfat/rows.csv"
    output_path = "food_trucks.csv"
    download_food_truck_data(data_url, output_path)

if __name__ == "__main__":
    cli()
