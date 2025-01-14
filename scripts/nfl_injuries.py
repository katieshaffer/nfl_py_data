# This script fetches information for 2023 injuries in the NFL
# Reference: nfl_data_py GitHub repo - https://github.com/nflverse/nfl_data_py
# Use this script as a guide to pull additional data from nfl_data_py if needed.

import nfl_data_py as nfl
import pandas as pd

# Limit to 2023
years = [2023]  # Only 2023 season

# Import Injuries Data for 2023
print("Fetching injury data...")
team_data = nfl.import_injuries(years=years)

# Save the dataset to a CSV file
output_file = "nfl_injuries_2023.csv"
print(f"Saving data to {output_file}...")
team_data.to_csv(output_file, index=False)

print("Injuries data saved successfully!")