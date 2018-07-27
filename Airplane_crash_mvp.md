## Dataset

https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx

### Domain

I ended up settling on a project that deals with aviation accidents and, additionally, certain incidents. According to Wikipedia, "in aviation, an accident is defined by the Convention on International Civil Aviation Annex 13 as an occurrence associated with the operation of an aircraft, which takes place from the time any person boards the aircraft with the intention of flight until all such persons have disembarked, and in which a) a person is fatally or seriously injured, b) the aircraft sustains significant damage or structural failure, or c) the aircraft goes missing or becomes completely inaccessible". On the other hand, "Annex 13 defines an incident as an occurrence, other than an accident, associated with the operation of an aircraft which affects or could affect the safety of operation".

The goal of my project can take a couple of different directions, but is constrained in the sense that my entire data set only includes flights that have been involved in accidents or incidents. My intention is to build a model that can predict whether or not an accident will be fatal or not.

I'm unfamiliar with the domain as a whole, but I feel like the features don't contain any information technical enough to prevent me from making any decisions when creating my model and evaluating the data.

### Data

"The NTSB aviation accident database contains information from 1962 and later about civil aviation accidents and selected incidents within the United States, its territories and possessions, and in international waters".

| Variable Name | Variable Type |
| ------------- |:-------------:|
| Investigation_Type | String (Accident or Incident) |
| Event_Date     | Datetime      |
| Country | String      |
| Latitude | Float |
| Longitude | Float |
| Airport_Code | String |
| Injury_Severity | String |
| Aircraft_Damage | String |
| Aircraft_Category  | String      |
| Make | String |
| Model | String |
| Amateur_Built  | String      |  
| Number_Engines | Integer |
| Engine_Type | String |
| Flight_Purpose  | String      |
| Air_Carrier | String |
| Total_Fatal_Injuries | Integer |
| Total_Serious_Injuries  | Integer      |
| Total_Minor_Injuries | Integer |
| Total_Uninjured | Integer |
| Weather_Condition  | String      |
| Broad_Phase_of_Flight | String      |
| City  | String      |
| State | String      |

### Known unknowns

I need to determine the best way to break down the features and their importance and how to classify my dependent variable. At this point I imagine that I will end up predicting whether or not an accident will result in fatalities, but I could potentially try to classify accidents into 3 groups between fatal, resulting in injuries, and no injuries. I'm unfamiliar with the dataset and how many dummy variables I'm going to need to create from my categorical features, so I think my biggest learning curve in this project will be understanding the domain and leveraging that knowledge to choose features and determine the models that will perform the best.
