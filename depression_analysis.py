# -*- coding: utf-8 -*-
"""Depression Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1akO0dXSGf-PMV1wNnUmjUrBu6hUwIsJ-
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('/content/drive/MyDrive/Depression level analysis 2/PHQ-9 Questionnaire - Sheet1.csv')

"""# **Dataset Visualize**"""

df

df['Anhedonia'].unique()
pd.get_dummies(X['Anhedonia']).head(50)

for col_name in X.columns:
    if X[col_name].dtypes == 'object':
        unique_cat = len(X[col_name].unique())
        print(f"Feature '{col_name}' has {unique_cat} unique categories")

X['Anhedonia'].value_counts().sort_values(ascending=False)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='median')

imputer.fit(X)
X = pd.DataFrame(data=imputer.transform(X) , columns=X.columns)

df.info()

df.describe()

df['Age'].fillna(df['Age'].median(), inplace=True)

x = df.iloc[:,:-1]

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)

pred = knn.predict(X_test)

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

df.head(50)

"""# **Drop Null Value**"""

df.isnull().sum().sort_values(ascending=False).head()

df=df.drop(['Eating Disorder Percentage (%)', 'Fatigue Percentage (%)', 'Suicidal Percentage (%)', 'Anhedonia Percentage (%)', 'Agitation Percentage (%)' ], axis = 1)

df.isnull().sum().sort_values(ascending=False).head()

df=df.drop(['Inadequacy Percentage (%)', 'Depression Percentage (%)', 'Insomnia Percentage (%)', 'Inattentiveness Percentage (%)', 'Depression Level Percentage (%)' ], axis = 1)

df.isnull().sum().sort_values(ascending=False).head()

df

df=df.drop(['Depression Level Class'], axis = 1)

df

df.columns

sns.distplot(df['Depression_Level'])

"""# **Depression Compare**"""

import matplotlib.pyplot as plt
import numpy as np

# Data for the bar graph
categories = ['None', 'Mild', 'Moderate', 'Moderately Severe', 'Severe']
female_data = [0, 23.76237624, 48.51485149, 25.74257426, 0]
male_data = [3.96039604, 26.26262626, 56.70103093, 12.63157895, 0]

# Calculate the percentage values
total_female = sum(female_data)
total_male = sum(male_data)
female_percentages = [round((value/total_female)*100, 1) for value in female_data]
male_percentages = [round((value/total_male)*100, 1) for value in male_data]

# Create the bar graph
x = np.arange(len(categories))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, female_percentages, width, label='Female')
rects2 = ax.bar(x + width/2, male_percentages, width, label='Male')

# Add the percentage values above the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Add labels and legend
ax.set_ylabel('Percentage')
ax.set_xlabel('Depression Level')
ax.set_title('Depression Class Between Male & Female')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

plt.show()

x = df.drop(['Depression_Level', 'Age'], axis = 1)
x

y=df['Depression_Level']
y

from sklearn.preprocessing import LabelEncoder
le_x= LabelEncoder()
x['Gender'] = le_x.fit_transform(x.Gender)
x.Anhedonia = le_x.fit_transform(x.Anhedonia)
x.Depression = le_x.fit_transform(x.Depression)
x.Insomnia = le_x.fit_transform(x.Insomnia)
x.Fatigue = le_x.fit_transform(x.Fatigue)
x.Eating_Disorder = le_x.fit_transform(x.Eating_Disorder)
x.Inadequacy = le_x.fit_transform(x.Inadequacy)
x.Inattentiveness = le_x.fit_transform(x.Inattentiveness)
x.Agitation = le_x.fit_transform(x.Agitation)
x.Suicidal = le_x.fit_transform(x.Suicidal)

x

"""# **Train Test Split**"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=1)

x_train

x_test

y_train

y_test

"""# **Creating and Training the Model Using Linear Regression**"""

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(x_train,y_train)

lm.score(x_test,y_test)

"""# **Prediction from our Model**"""

predictions = lm.predict(x_test)

predictions

y_test

plt.scatter(y_test,predictions)

"""# **Creating and Training the Model Using Logistic Regression**"""

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)

logmodel.score(x_test,y_test)

predictions = logmodel.predict(x_test)

predictions

from sklearn.metrics import classification_report

y_test.shape

print(classification_report(y_test,predictions))

from sklearn.metrics import accuracy_score
from sklearn.metrics import  confusion_matrix

print(confusion_matrix(y_test, predictions))

logmodel.score(x_test,y_test)

"""# **Creating and Training the Model Using Logistic Regression**"""

from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(x_train,y_train)

predictions = dtc.predict(x_test)

predictions

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,predictions))

print(confusion_matrix(y_test,predictions))

dtc.score(x_test,y_test)