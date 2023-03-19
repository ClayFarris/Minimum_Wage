INTRODUCTION

Minimum Wage and Happiness

This project compares the average yearly minimum wage from the years 2015 - 2018 for 31 countries with the average level of happiness for those same countries as reported by the World Happiness Report for the years 2015-2018.

The amount of money a person makes has traditionally been associated with their capacity for being happy in many parts of the world. A minimum wage is the lowest renumeration that employers can legally pay their workers--the price floor below which workers may not sell their labor. Most countries had introduced minimum wage legislation by the end of the 20th century.

I would like to explore how the average minimum wage for a country during the years 2015-2018 compares to its average happiness score during those same years.

Question:
* Do countries with a relatively higher minimum wage correlate significantly with countries that have higher happiness scores?



REQUIREMENTS

The necessary packages to be installed are listed in the 'Requirements.txt' folder.
This project was created working in Jupyter Notebook with Python 3 (ipykernel).
To run this project it is necessary to do the following:

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats

The datasets analyzed in this project are included in the 'data' folder.



METHODOLOGY

Data was taken from the website https://www.kaggle.com accessed on 3/7/2022

1. https://www.kaggle.com/datasets/frtgnn/minimum-wages-between-2001-2018

CSV name: MINIMUM_WAGES.csv

The dataset provided by Firat Gonen gives the minimum wage of 31 countries. The minimum wage is yearly in US Dollars. The countries appear to have been selected randomly.

2. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv

CSV name: 2015.csv, 2016.csv, 2017.csv, 2018.csv

The datasets provided by Sustainable Development Solutions Network gives the happiness score for 155-158 countries. The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll. The dataset for the year 2019 was not included since the MINIMUM_WAGES dataset only goes up to the year 2018.



FEATURES

1. Read data:
I read in CSV data from the website Kaggle.com.

2. Manipulate and clean your data:
I used '.strip()', '.drop()', '.rename()', '.insert()', '.fillna()', '.merge()', etc... to clean and manipulate the data. 

3. Analyze your data:
I used '.head()', '.info()', ','.describe()', '.isna().sum()', '.fillna()', '.sort_values()', '.mean(), etc... to analyze the data.

4. Visualize your data:
I used matplotlib to create a bar chart and seaborn and scipy.stats to create a scatterplot and calculate the regression equation and p value.

5. Interpret your data:
The interpretation of the data is included in the Markdown cells.  

CONCLUSION:

There is a positive correlation between average minimum wages and average happiness scores. As the average minimum wage increases, so does the average happiness score.

With a p-value less than 0.05 the correlation between between minimum wage and happiness appears to be statistically significant.


Although there is a significant correlation between minimum wage and happiness scores with a p-value of 0.011, this does not imply causation and there may be other factors influencing happiness scores.

The sample size is relatively small so the results may not be generalizable to countries not present in the data or other time periods.

The presence of outliers as seen in both the bar chart and scatterplot suggests some variability in the relationship between minimum wage and happiness among different countries


