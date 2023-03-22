#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ##### This project compares the average yearly minimum wage from the years 2015 - 2018 for 31 contries with the average level of happiness for those same countries as reported by the World Happiness Report for the years 2015-2018.
# 
# ##### The amount of money a person makes has traditionally been associated with their capacity for being happy in many parts of the world.  A minimum wage is the lowest renumeration that employers can legally pay their workers--the price floor below which workers may not sell their labor.  Most countries had introduced minimum wage legislation by the end of the 20th century.  
# 
# ##### I would like to explore how the average minimum wage for a country during the years 2015-2018 compares to its average happiness score during those same years.
# 
# ### Question:
# 
# ##### * Do countries with a relatively higher minimum wage correlate significantly with countries that have higher happiness scores?
# 

# # Methodology

# ##### Data was taken from the website https://www.kaggle.com accessed on 3/7/2022
# 
# ##### 1. https://www.kaggle.com/datasets/frtgnn/minimum-wages-between-2001-2018
# 
# ##### CSV name: MINIMUM_WAGES.csv
# ##### The dataset provided by Firat Gonen gives the minimum wage of 31 countries. The minimum wage is yearly in US Dollars. The countries appear to have been selected randomly.
# 
# ##### 2. https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv
# 
# ##### CSV name: 2015.csv, 2016.csv, 2017.csv, 2018.csv
# ##### The datasets provided by Sustainable Development Solutions Network gives the happiness score for 155-158 countries. The happiness scores and rankings use data from the Gallup World Poll. The scores are based on answers to the main life evaluation question asked in the poll.  The dataset for the year 2019 was not included since the MINIMUM_WAGES dataset only goes up to the year 2018.
# 
# 

# # Results

# ### 1. Import Libraries

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy.stats as stats


# ### 2. Import Datasets 

# In[2]:


# Use pandas to read the csv files.

mini = pd.read_csv('data/MINIMUM_WAGES.csv')
hap15 = pd.read_csv('data/2015.csv')
hap16 = pd.read_csv('data/2016.csv')
hap17 = pd.read_csv('data/2017.csv')
hap18 = pd.read_csv('data/2018.csv')


# ### 3. Clean the data

# ##### Strip the string data of whitespace and rename columns and rows in the datasets that use different column names or text ids for the same values between the respective datasets to avoid generating any missing info once the merge function has been deployed. Columns for the years 2001-2014 in the MINIMUM_WAGE dataset have been dropped since those years are not present in the happiness datasets. Columns that are not mutually present across all respective happiness datasets are dropped. 

# In[3]:


# Clean the data.

mini = mini.applymap(lambda x: x.strip() if isinstance (x,str) else x)
hap15 = hap15.applymap(lambda x: x.strip() if isinstance (x, str) else x)
hap16 = hap16.applymap(lambda x: x.strip() if isinstance (x, str) else x)
hap17 = hap17.applymap(lambda x: x.strip() if isinstance (x, str) else x)
hap18 = hap18.applymap(lambda x: x.strip() if isinstance (x, str) else x)

mini['Country'] = mini['Country'].replace(['Korea', 'Slovak Republic', 'Russian Federation'], 
                                        ['South Korea', 'Slovakia', 'Russia'])
mini = mini.drop(['2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                 '2009', '2010', '2011', '2012', '2013', '2014'], axis=1)

hap15 = hap15.drop(['Standard Error', 'Region', 'Happiness Rank', 'Dystopia Residual'], axis=1)
hap15 = hap15.rename(columns={'Family':'Social support','Health (Life Expectancy)':'Healthy life expectancy'})

hap16 = hap16.drop(['Lower Confidence Interval','Upper Confidence Interval', 'Region',
                    'Happiness Rank', 'Dystopia Residual'],axis=1)
hap16 = hap16.rename(columns={'Family':'Social support', 'Health (Life Expectancy)':'Healthy life expectancy'})

hap17 = hap17.drop(['Whisker.high', 'Whisker.low', 'Happiness.Rank', 'Dystopia.Residual'], axis=1)
hap17 = hap17.rename(columns={'Happiness.Score':'Happiness Score', 
                              'Economy..GDP.per.Capita.':'Economy (GDP per Capita)','Family':'Social support', 
                              'Health..Life.Expectancy.':'Healthy life expectancy',
                              'Trust..Government.Corruption.':'Trust (Government Corruption)'})
hap17.insert(7, 'Generosity', hap17.pop('Generosity'))

hap18 = hap18.drop(['Overall rank'], axis=1)
hap18.insert(7, 'Generosity', hap18.pop('Generosity'))
hap18 = hap18.rename(columns={'Country or region':'Country', 'Score':'Happiness Score',
                             'GDP per capita':'Economy (GDP per Capita)', 'Freedom to make life choices':
                             'Freedom', 'Perceptions of corruption':'Trust (Government Corruption)'})




# In[4]:


# Check a sample of the output and headings for minimum wage data.

mini.head()


# In[5]:


# Check data types, etc...
mini.info()


# In[6]:


# Return a statistical summary of the data.
mini.describe()


# In[7]:


# Check headings
hap15.head()


# In[8]:


hap15.info()


# In[9]:


hap16.head()


# In[10]:


hap16.info()


# In[11]:


hap17.head()


# In[12]:


hap17.info()


# In[13]:


hap18.head()


# In[14]:


hap18.info()


# ##### There is a null value present in the 'Trust (Government Corruption)' column.

# In[15]:


# Remove null value by replacing it with a zero.
hap15['Trust (Government Corruption)'] = hap15['Trust (Government Corruption)'].fillna(0)
hap15.info()


# ##### The null value has been removed.

# ### 4. Make a Dataframe

# ##### Create a dataframe by merging the minimum wage dataset with the happiness datasets using countries that are present in all the respective data sets. 

# In[16]:


# Create dataframe.

minihappy = pd.merge(mini, hap15, left_on='Country', right_on='Country', how='inner', suffixes=('', '_2015'))
minihappy = pd.merge(minihappy, hap16, left_on='Country', right_on='Country', how='inner', suffixes=('', '_2016'))
minihappy = pd.merge(minihappy, hap17, left_on='Country', right_on='Country', how='inner', suffixes=('', '_2017'))
minihappy = pd.merge(minihappy, hap18, left_on='Country', right_on='Country', how='inner', suffixes=('', '_2018'))

# Display the maximum columns

pd.set_option('display.max_columns', None)


# In[17]:


minihappy.head()


# In[18]:


# Rename hap15 columns.  


minihappy = minihappy.rename(columns={'Happiness Score':'Happiness Score_2015',
                                      'Economy (GDP per Capita)':'Economy (GDP per Capita)_2015',
                                      'Social support':'Social support_2015',
                                      'Healthy life expectancy':'Healthy life expectancy_2015',
                                      'Freedom':'Freedom_2015',
                                      'Trust (Government Corruption)':'Trust (Government Corruption)_2015',
                                      'Generosity':'Generosity_2015',
                                      })

# Print dataframe
minihappy


# In[19]:


# Check data types, etc...
minihappy.info()


# In[20]:


# Return a statistical summary of the data.
minihappy.describe()


# In[21]:


# Check for null values
minihappy.isna().sum()


# ##### There are no null values

# ### 5. Make a new Dataframe

# ##### Create a new dataframe to compare the relationship between average  minimum wage and happiness scores for the years 2015-2018 by generating several small dataframes and then adding them together into a single dataframe that will be used to compare average minimum wage and happiness scores. We will  begin with the minimum wage data.

# In[22]:


# Create dataframe using minimum wage data.
mini2 = minihappy.loc[:,['Country', '2015','2016','2017','2018']]


# In[23]:


mini2.head()


# In[24]:


# Find the average minimum wage for each country over the years 2015-2018.
mini2['Average Minimum Wage Yearly in USD 2015-2018']=mini2.mean(axis=1)


# In[25]:


mini2.head()


# In[26]:


# Create a series featuring the average minimum wage for the years 2015-2018 for all the countries present
# across the repsective datasets.

mini2 = mini2.set_index('Country')
mini2 = mini2.loc[:,['Average Minimum Wage Yearly in USD 2015-2018']]

# Sort the data from countries with the highest minum wage to the lowest.
mini2 = mini2.sort_values('Average Minimum Wage Yearly in USD 2015-2018', ascending=False)

mini2


# ### Notes on Findings

# ##### Looking at the data we see that Luxembourg has the highest minimum wage and Mexico the lowest for the years 2015-2018

# In[27]:


# Create a data frame of the happiness scores for countries during 
# the years 2015-2018 


 
happiness_score = minihappy.loc[:,['Country', 'Happiness Score_2015', 'Happiness Score_2016', 'Happiness Score_2017',
                                  'Happiness Score_2018']]

happiness_score.head()




# In[28]:


# Find the average happiness score for each country during the years 2015-2018

happiness_score['Average Happiness Score 2015-2018'] = happiness_score.mean(axis=1)

happiness_score.head()


# In[29]:


# Create a series using the average happiness scores for each contry during the year 2015-2018 

happiness_score = happiness_score.set_index('Country')
happiness_score = happiness_score.loc[:,['Average Happiness Score 2015-2018']]

# Sort values by countries with highest happiness score to lowest
happiness_score = happiness_score.sort_values('Average Happiness Score 2015-2018', ascending=False)


happiness_score


# ### Notes on Findings

# ##### Looking at the data we see that the Netherlands has the highest happiness score and Greece the lowest for the years 2015-2018

# ### 6.  Make a New dataframe
# ##### Create a data frame that will be used to create graphs to compare the average minimum wages and happiness scores for all countries during the years 2015-2018

# In[30]:


# Create dataframe
minhap = pd.concat([mini2, happiness_score], axis=1)

# Sorting values for rows by average minimum wage from highest to lowest

minhap = minhap.sort_values('Average Minimum Wage Yearly in USD 2015-2018', ascending=False)

minhap.head()


# In[31]:


# reset index to facilitate creation of charts and plots
minhap = minhap.reset_index()
minhap.head()


# ### Graph 1: Bar Chart of Average Minimum Wage and Happiness Scores 2015-2018

# In[32]:


# Create a new figure and axis object with specified size.
fig, ax = plt.subplots(figsize=(12,8))

# Create a horizontal bar chart of Average Minimum Wage by Country using data from the minhap dataframe.
# Set the color to tab blue, alpha to 0.7, height to 0.5 and label to 'Average Minimum Wage Yearly in USD 2015-2018'.
wages_bars = ax.barh(minhap['Country'], minhap['Average Minimum Wage Yearly in USD 2015-2018'],
                     color='tab:blue', alpha=0.7, height=0.5, label='Average Minimum Wage Yearly in USD 2015-2018')

# Set the x-axis label.
ax.set_xlabel('Average Minimum Wage Yearly in USD 2015-2018')

# Set the y-axis tick labels to the Country column from the minhap dataframe.
# and set the font size to 12.
ax.set_yticklabels(minhap['Country'], fontsize=12)

# Create a new x-axis object that shares the same y-axis as ax.
ax2 = ax.twiny()

# Create a horizontal bar chart of Average Happiness Score by Country using data from the minhap dataframe.
# Set the color to tab orange, alpha to 0.7, height to 0.3 and label to 'Average Happiness Score 2015-2018'.
happiness_bars = ax2.barh(minhap['Country'], minhap['Average Happiness Score 2015-2018'], color='tab:orange',
                          alpha=0.7, height=0.3, label='Average Happiness Score 2015-2018')

# Set the x-axis label. 
ax2.set_xlabel('Average Happiness Score 2015-2018')

# Set the x-axis limits from 0 to 8.
ax2.set_xlim(0, 8)

# Set the y-axis limits from -0.5 to the length of the Country column minus 0.5.
ax.set_ylim(-0.5, len(minhap['Country'])-0.5)

# Set the title of the chart with font size of 16.
plt.title('Average Minimum Wage and Happiness Score by Country 2015-2018', fontsize=16)

# Set the legend to show both Average Minimum Wage and Average Happiness Score and place it outside the figure.
# Set the legend handles to the wages_bars and happiness_bars objects.
# Set the location to the center left and the bbox_to_anchor to (1.0, 0.5) to place it outside the figure.
# Set the frameon parameter to False to remove the legend box.
ax.legend(handles=[wages_bars, happiness_bars], loc='center left', bbox_to_anchor=(1.0, 0.5), frameon=False)

# Show the chart.
plt.show()


#  ### Notes on Findings
#  
#  ##### This chart shows the average minimum wage and happiness score by country for the years 2015-2018, but it doesn't provide a clear indication of whether there is a significant correlation between the two variables. Nonetheless, it could prove beneficial for providing a more detailed and comprehensive understanding of the data.  A scatter plot with a regression line would be more useful for evaluating the correlation between average minimum wages and happiness scores.

# ### Graph 2: Scatterplot with Regression Line for Average Minimum Wage and Happiness Scores 2015-2018

# In[33]:


sns.regplot(x='Average Minimum Wage Yearly in USD 2015-2018', y='Average Happiness Score 2015-2018', data=minhap)

# Set the x and y axis labels.
plt.xlabel('Average Minimum Wage Yearly in USD 2015-2018')
plt.ylabel('Average Happiness Score 2015-2018')

# Set the title of the plot.
plt.title('Average Minimum Wage and Happiness Score 2015-2018')

# Calculate the regression equation and p-value.
slope, intercept, r_value, p_value, std_err = stats.linregress(minhap['Average Minimum Wage Yearly in USD 2015-2018'], 
                                                               minhap['Average Happiness Score 2015-2018'])

# Display the regression equation and p-value. 
# Set the slope, intercept and p_value to .3f to round the numbers to three decimal places.
print(f"Regression Equation: y = {slope:.3f}x + {intercept:.3f}")
print(f"p-value: {p_value:.3f}")

# Display the plot.
plt.show()


# ### Notes on Findings

# ##### There is a positive correlation between average minimum wages and average happiness scores. As the average minimum wage increases, so does the average happiness score. 
# 
# ##### With a p-value less than 0.05 the correlation between between minimum wage and happiness appears to be statistically significant. 
# 
# 
# 
# 

# # Conclusion

# ##### Although there is a significant correlation between minimum wage and happiness scores with a p-value of 0.011, this does not imply causation and there may be other factors influencing happiness scores.
# 
# #####  The sample size is relatively small so the results may not be generalizable to countries not present in the data or other time periods.
# 
# ##### The presence of outliers as seen in both the barchart and scatterplot suggests some variability in the relationship between minimum wage and happiness among different countries.  
#  

# ## Suggestions for Further Study

# ##### It may be useful to expand the study to include more countries and cover a larger time period.
# 
# ##### Explore the relationships between other variables in the datasets:
# ##### 1. Compare happiness scores with social support.
# ##### 2. Compare happiness scores and minimum wage with generosity.
# ##### 3. Compare minimum wage and happiness scores with government corruption.
# ##### 4. Make a subset of data for countries witth relatively low minimum wage and high happiness scores and compare it with indicators like social support and generosity and do the same for countries with relatively high minimum wage but low happiness scores.
# 
# ##### Explore the relationship between happiness and other socioeconomic factors not present in these datasets such as income inequlity, education level and employment rate and how they interact with minimum wage.
# 
# ##### Explore the relationship between minimum wage and different demographic groups, such as age, gender and race to understand how it impacts happiness among these different groups.
# 
# 

# In[ ]:




