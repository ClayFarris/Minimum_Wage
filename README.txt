INTRODUCTION

Minimum Wage and Happiness

This project compares the average yearly minimum wage from the years 2015 - 2018 for 31 countries with the average level of happiness for those same countries as reported by the World Happiness Report for the years 2015-2018.

The amount of money a person makes has traditionally been associated with their capacity for being happy in many parts of the world. A minimum wage is the lowest renumeration that employers can legally pay their workers--the price floor below which workers may not sell their labor. Most countries had introduced minimum wage legislation by the end of the 20th century.

I would like to explore how the average minimum wage for a country during the years 2015-2018 compares to its average happiness score during those same years.

Question:
* Do countries with a relatively higher minimum wage correlate significantly with countries that have higher happiness scores?



REQUIREMENTS

The necessary libraries to be installed are listed in the 'Requirements.txt' folder.

This project was created working in Jupyter Notebook with Python 3.9.13 (ipykernel).

To run this project it is necessary to do the following:

Clone the repository to your local machine.

Navigate to the cloned repo folder in the terminal and run:

	pip install -r requirements

In case there is a problem with this method I have included a list of the libraries below to be installed individually:

	import ipykernel
	import matplotlib.pyplot as plt
	import pandas as pd
	import seaborn as sns
	import scipy.stats as stats

The datasets analyzed in this project are included in the `data` folder:
	
	`MINIMUM_WAGES.csv`
	`2015.csv`
	`2016.csv`
	`2017.csv`
	`2018.csv`

In order to make them run from the `data` folder in `Minimujm_Wage_Happiness.ipynb`, in the second code block you will need to change the names to:
	
	`data/MINIMUM_WAGES.csv`
	`data/2015.csv`
	`data/2016.csv`
	`data/2017.csv`
	`data/2018.csv`

Otherwise you can download the .csv files from the links listed below and run them from your local machine.

The main file in this project is called `Minimum_Wage_Happiness.ipynb` and contains the data analysis conducted in this project.


HOW TO RUN THE PROGRAM IN JUPYTER NOTEBOOK

	1. Clone the repository.
	2. Save the Folder.
	3. Open `Jupyter Notebook` from the command line or start menu.
	4. Go to the saved location of the repo.
	5. Open `Minimum_Wage_Happiness.ipynb`.
	6. Open the `Cell` tab and click `Run All`.

HOW TO RUN THE PROGRAM IN PYTHON

	1. Clone the Repository.
	2. Save the folder.
	3. Open the saved repository in your terminal or IDE.
	4. Run the `Minimum_Wage_Happiness.py` file.


METHODOLOGY

Data was taken from the website https://www.kaggle.com accessed on 3/7/2022

1. https://www.kaggle.com/datasets/frtgnn/minimum-wages-between-2001-2018

CSV name: MINIMUM_WAGES.csv

The dataset provided by Firat Gonen gives the minimum wage of 31 countries. The minimum wage is yearly in US Dollars. The countries appear to have been selected randomly.

2. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv

3. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2016.csv
   
4. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2017.csv

5. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2018.csv


CSV names: 2015.csv
	   2016.csv
           2017.csv
           2018.csv

The datasets provided by Sustainable Development Solutions Network gives the happiness score for 155-158 countries. The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll. The dataset for 2019.csv was not included since the MINIMUM_WAGES dataset only goes up to the year 2018.



FEATURES UTILIZED

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


CITATIONS


1. https://www.kaggle.com/datasets/frtgnn/minimum-wages-between-2001-2018

2. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv

3. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2016.csv
   
4. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2017.csv

5. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2018.csv



