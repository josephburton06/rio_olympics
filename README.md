### This repo uses a dataset from Kaggle that contains data on athletes from the 2016 Rio Olympics.

### First iteration: Can country of origin be classified for medalists based on features such as height, weight, etc.?

### We first run a model on all athletes that earned a medal.  After that, we split our dataset into two dataframes, each in their own notebook, that contain athletes listed as 'athletics' in sports and those in anything other than 'athletics'.  Athletics is used for track and field.  Most of the other sports would most likely contain individuals of similar heights and weights.  Track and field is vastly different in that a lighter 10k runner would be included in the same sport as a larger shot put thrower.  

### After we make the split, we can see improvements in the results.

### In the all_sports_model Jupyter Notebook, we work on predicting an athlete's sport based on height and weight.