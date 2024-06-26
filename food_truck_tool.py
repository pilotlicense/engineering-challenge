import requests
import pandas as pd
import click

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

# Click CLI setup
@click.group()
def cli():
    """Main CLI group"""
    pass

@cli.command()
@click.option('--cuisine', help='Filter by type of cuisine')
@click.option('--facility-type', help='Filter by facility type (e.g., Truck, Push Cart)')
def list_trucks(cuisine, facility_type):
    """
    List food trucks based on optional filters: cuisine and facility type.
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
