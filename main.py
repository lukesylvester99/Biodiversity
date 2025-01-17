import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Load data into dataframes and visualize structure
sightings_df = pd.read_csv('observations.csv')
species_df = pd.read_csv('species_info.csv')

print(sightings_df.head())
print(species_df.head())

#Initally Explore Data

print("number of distinct species in dataset: ", species_df.scientific_name.nunique()) #how many animals are in our data set 

print("number of animal classifications: ", species_df.category.nunique()) #how many types of species are in our data set
print("species diversity: ", species_df.category.unique())

print(species_df.groupby('category').size()) # of the types of species, how many animals belong to each one

print("number of conservation statuses: ", species_df.conservation_status.nunique()) #what are the conservation designations
print("unique conservation statuses: ", species_df.conservation_status.unique()) 
print(species_df.groupby('conservation_status').size()) #of those designations, what statuses are the biggest


