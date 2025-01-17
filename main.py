import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Load data into dataframes and visualize structure
sightings_df = pd.read_csv('observations.csv')
species_df = pd.read_csv('species_info.csv')

print(sightings_df.head())
print(species_df.head())

#Initally Explore Data

print("number of distinct species in dataset: ", species_df.scientific_name.nunique())

