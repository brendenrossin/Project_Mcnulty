import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cross_validation import KFold
from sklearn.model_selection import learning_curve
import matplotlib.style as style
style.use('fivethirtyeight')
# %matplotlib inline

f = open('AviationData.txt')

aviation_data = f.readlines()
aviation_list = []
lax = []

for line in aviation_data:
    aviation_list.append(line.split(" | "))

for line in aviation_list:
    if 'LAX94LA336' in line:
        lax.append(line)
print(lax)

print(aviation_list[0:5])

aviation = [i[:-1] for i in aviation_list]

headers = aviation.pop(0)
df = pd.DataFrame(aviation, columns=headers)

df = df.replace('', np.nan)

df.info()

df.columns = ['Event_Id', 'Investigation_Type', 'Accident_Number', 'Event_Date', 'Location',
              'Country', 'Latitude', 'Longitude', 'Airport_Code', 'Airport_Name', 'Injury_Severity',
              'Aircraft_Damage', 'Aircraft_Category', 'Registration_Number', 'Make', 'Model',
              'Amateur_Built', 'Number_Engines', 'Engine_Type', 'FAR_Description', 'Schedule',
              'Flight_Purpose', 'Air_Carrier', 'Total_Fatal_Injuries', 'Total_Serious_Injuries',
              'Total_Minor_Injuries', 'Total_Uninjured', 'Weather_Condition', 'Broad_Phase_of_Flight',
              'Report_Status', 'Publication_Date']

df.Weather_Condition.unique()

# VMC and IMC are aviation terms used to describe meteorological conditions during flight. VMC stands for visual meteorological conditions, and IMC stands for instrument meteorological conditions. The definition of IMC, according to the FAA, is meteorological conditions expressed in terms of visibility, distance from clouds, and ceiling less than the minima specified for visual meteorological conditions (VMC). IMC is any meteorological condition that doesn’t qualify as visual meteorological conditions, or weather conditions worse than VMC. UNK is most likely unknown.

df.Total_Uninjured.value_counts()

df.Injury_Severity

state_df = pd.concat([df['Event_Id'], df['Location'].str.split(', ', expand=True)], axis=1)

state_df['City'] = state_df[0]
state_df['State'] = state_df[1]

state_df = state_df.drop([0, 1, 2, 3, 4], 1)
df.reset_index(inplace=True)
state_df.reset_index(inplace=True)

df = pd.merge(df, state_df, on='index')

df = df.drop(['Location'], 1)

df.set_index('index', inplace=True)

df.info()

df.Aircraft_Damage.value_counts()

df.Latitude = df.Latitude.astype('float')
df.Longitude = df.Longitude.astype('float')
df.Total_Fatal_Injuries = df.Total_Fatal_Injuries.astype('float')
df.Total_Serious_Injuries = df.Total_Serious_Injuries.astype('float')
df.Total_Minor_Injuries = df.Total_Minor_Injuries.astype('float')
df.Total_Uninjured = df.Total_Uninjured.astype('float')

df.describe()

no_deaths = df[df['Total_Fatal_Injuries'] == 0]
