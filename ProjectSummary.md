# Project Summary

### Project Selection

This project was a little harder for me come up with a topic for than the linear regression project, but ultimately I settled on a dataset from the National Transportation Safety Board, which had a dataset full of all aviation accidents and incidents since 1962.

Once I got acquainted with the dataset, it became clear to me that there was one obvious classification problem I had ready for me in the data. There were columns on the total number of uninjured passengers, in addition to the number of passengers with minor injuries, serious injuries, and the total number of fatalities. It wasn't a far jump for me then to create a binary classifying column indicating whether or not an accident had proven to be fatal or not.

### EDA and Initial Feature Engineering

When initially looking at the potential features for this classification problem, I was excited at the prospects of having geographical information, basic weather conditions, and dates for each accident. My initial intention was to be able to have interactive plots over a map indicative of each crash and whether or not it was fatal, in addition to determining whether or not there was a trend in fatalities over the last 50 years. Finally, because the dataset only came with basic weather classifiers (VMC or IMC), I was hoping to gather more specific weather results for each flight, but gathering that information proved to be difficult because I not only had to retrieve weather data from that specific date-time, but also correlate it to that specific geographic location. Ultimately, these more robust methods of feature engineering were not incorporated into my analysis, but is something I would definitely be interested in exploring in the future.

Other features that I wanted to focus on included the damage the aircraft sustained, the make and model of the aircraft, the number of engines and engine types, the purpose of the flight, the air carrier, basic weather conditions, and the phase of the flight that the crash occurred.

In order to get an initial understanding of how these features would be impacting my models, I created bar charts plotting the percentage of fatalities per each category in each feature, to see which instances would lead to the highest probability of a crash being fatal.

I also created a bar chart plotting the difference in class count between fatal and non-fatal crashes, with non-fatal crashes outweighing fatal crashes 80/20. Therefore I kept it in mind to try different oversampling/undersampling techniques to see if they made a positive impact when modeling.

### Model creation

When revisiting my business use case, I decided that the most important metric I needed to look at when evaluating my models was recall, which penalizes against false negatives. False negatives in this case are plane crashes that the model predicts to be non-fatal, which are in fact fatal crashes. If we were to put this model into production, we wouldn't want to falsely classify any crash to think they would be safer than they actually are, and thus I decided to err on the side of caution.

I created my initial model using the columns stated above as my main features, and then began my process of adjusting for the class imbalance and feature selection to improve my models. However, I ran into an issue when I found that the main factor determining the fatality probability in my model was the damage that the aircraft sustained. I ended up removing plane damage as a feature because it doesn't contain any predictive power in that it doesn't occur before the plane crash occurs. It is a similar result of the plane crash as fatalities, and has potential to be a dependent variable that could be predicted as a separate project.

The removal of damage as a feature greatly impacted the performance of my model, and I returned to try more creative feature engineering techniques to try and glean some more interesting features for my model. In doing so, I came up with a column that indicated whether a plane had been built by one of the top 10 plane manufacturers, whether or not the flight was commercial (greater than 25 passengers) or private, whether it was a solo flight, and created a category for the four seasons based on the datetime as well.

I then returned to my modeling process, and scaled my numerical columns and dummified my categorical variables for use in modeling. After a train/test split, I tested Logistic Regression, KNN, Naive Bayes, SVC, Decision Tree, Random Forest, and Gradient Boosted Trees models on my data set as it was. I ran all of these models on all of my initial features, without any adjustment for my imbalanced classes, and without any hyperparameter tuning in order to get a baseline reference point for how my MVP model would perform.

I obtained feature importances from the Random Forest model and observed the coefficients from my Logistic Regression model to see which features were having the largest impact on my model. However, I didn't make any adjustments from this information just yet, because I still needed to adjust for my imbalanced classes before making any big selections.

However, I also wanted to try some hyperparameter tuning to have each model perform to its maximum potential on my dataset, and so I used GridsearchCV to cycle through possible parameters for each of the possible models and obtain the best fit. I then ran a K-fold cross validation on my training data to see how each model was performing on its updated parameters. As expected, most of the models improved.

However, my next step was to try the four different oversampling/undersampling techniques covered in class (random oversampling, SMOTE oversampling, ADASYN oversampling, and random undersampling) to observe their impact on my models. SMOTE oversampling had the largest positive impact on my model, and therefore I decided to use it going forward with my modeling process.

After I had used SMOTE to oversample my training data, I repeated the process I had performed with just my original MVP model. This included running a K-fold cross validation on my models without hyperparameter tuning, using GridsearchCV to find the best parameters for each model individually and then fit those models with my SMOTEd data. These models returned much better recall scores than their MVP counterparts, but still I had some work that could be done.

I decided to take a look at the feature importances from the Random Forest model, and the coefficients from the Logistic Regression models, as they were two of my stronger models, to determine if there were any features that weren't making a large impact on my result and could possibly be fitting only noise in the training data. I iterated through this process of feature removal, K-fold cross validation and hyperparameter tuning until I felt that I had the strongest model I could with my given data and features, and picked my best model to run on my test set, Support Vector Machine. My final results on my testing set using this optimally tuned model resulted the following scores.

| Model Name | Accuracy | Recall | F-beta Score (beta = 2.0) |
|------------|:--------:|:------:|:-------------------------:|
| Support Vector Machine | 0.73 | 0.72 | 0.6039 |

### Flask App

After producing my model's final scoring metrics, I decided to create a flask app for practical application of my model, and to interactively find how different features were affecting my model. Therefore, I retrained my model on the entire dataset and created a function that would feed the output of the model to javascript so that it could provide interactive functionality. I used Bootstrap to make my webpage look like something of the 21st century, and added functionality to cycle through 8 different gifs depending on the result of the flight, either fatal or non-fatal.
