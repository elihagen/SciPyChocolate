import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib 
from matplotlib import pyplot as plt
import plotly.express as px
import ipywidgets as widgets



def review_dates(df):
    '''
    Histograms of when the reviews took place
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            rel(Axes): axes with plot for the years and number of reviews
    '''
    #description that is printed to describe what the user sees
    description = "Description: The reviews took place between 2006 and 2020. Most of the surveys were conducted in 2015. In the years before and after, the number of surveys decreases quite steadily. However, after the year 2015 there was a stronger decrease and the lowest number of surveys was in 2020."

    #plot for review dates
    rel = sns.displot(df["review date"], kde=True)

    print(description)
    return rel


def ratings(df):
    '''
    Histograms showing the density per rating
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            rel(Axes): density of the ratings
    '''
    #description that is printed to describe what the user sees
    description= "Description: The ratings lie between 1.0 and 4.0 with 1.0 being inappetizing and 4.0 pleasurable. The mean value is around 3.2, which means that most chocolates are rated as rather tasty overall. Most chocolates are rated with 3.0 and 3.5 and least are rated with 2.0 and 2.25."
    
    #give the mean of all ratings rounded to 3 decimal places 
    s = "mean of ratings: " + str(round(np.mean(df["rating"]),3))

    #plot
    rel = sns.displot(df["rating"], kde=True)

    print(description)
    return rel
    
    
def cocoa_percent(df):
    '''
    Bar chart showing the density of cocoa percent in the chocolates
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            fig(Barplot): density of the cocoa percent
    '''
    #description that is printed to describe what the user sees
    description = "Description: Here you can see that most of the chocolates have a cocoa content of 70-75% with a peak at 70%."
    
    #ax = df["cocoa percent"].value_counts().sort_index()
    number = df["cocoa percent"].value_counts()
    df['number'] = number
    fig = px.bar(df, x = "cocoa percent", y = "number",title = "cocoa percentage")
    print(description)
    return fig
 

def cocoa_percent_rating(df):
    '''
    Box plot(interactive) showing the distribution of cocoa percent per rating. 
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            fig(Boxplot): inner quartiles of the cocoa percent per rating
    '''
    description = "Description: A boxplot is shown for the cocoa percentage as a function of the ratings. For the rating 1, 1.75, and 2.6, there is only one data value, so only one line is shown here for this cocoa percentage. Let's take the 2.5 rating as an example. The maximum value is 100% and the minimum value is 55%. However, these values are outliers. All values below the lower fence and above the upper fence are considered outliers. The fences are 1.5 times the boxes with the median and quantile values we now come to. The median is 71%, which means that 71% is the value that divides all examples in half. The 1st quantile is 70%. 25% of all data points scoring 2.5 are below this quantile, 75% are above. 75% is the percentage of cocoa that makes up the 3rd quantile. Here it is exactly the opposite. 25% are above and 75% below this value. What we can see from this graph is that it does not depend on the cocoa content how the chocolate is rated. Most of the boxes are between 70% and 73%. For rating 1.5 it is different. Here the box ranges from 66% to 86%. Since this plot is interactive, you can move your mouse to any point and the values described will be displayed."

    #create the boxplot
    fig = px.box(df, y="cocoa percent", x="rating", title= "rating ~ cocoa percent")

    print(description)
    return fig
    

def bean_origin_rating(df):
    '''
    Box plot showing the mean rating of the individual countries
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            ax(Axes): inner quartiles of the rating per country
    '''
    #description that is printed to describe what the user sees
    description = "Description: Here we can see the how the different cocoa beans are rated depending on the country of bean origin. Most of the countries are very evenly distributed between 3.0 and 3.5. But we can see one country that is swinging upward. The chocolate with country of bean origin 'Solomon islands'(maybe also the one from Cuba) is rated better in average. The chocolate with bean origin from Puerto Rico is rated the worst. For these two we do not have outliers. This is the case for other countries. Blend, for example has a median of 3.0 but an outlier at 1.0 and 1.5 rating. Contrary, Uganda, where the median is lower at 2.75 but an outlier at 3.75 rating."
    x = df["rating"]
    y = df["country of bean origin"]
    sns.set(rc = {'figure.figsize':(21,8)})
    #create the boxplot
    ax = sns.boxplot(y, x)
    ax.set_xticklabels(ax.get_xticklabels(),rotation = 85) 
    ax.set_title("country of bean origin ~ rating")
    print(description)
    return ax


def company_rating(df):
    '''
    Box plots(interactive) showing the rating per company
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            plot (Boxplot): inner quartiles of the rating per company
    '''
    #description that is printed to describe what the user sees
    description= "Description: Below you can choose for which company (give the first letter of your company) you want to see the average rating. This will help you decide whether you really want to buy chocolate from the company or reconsider your decision. You should prefer companies whose interquartile range (the colored boxes) are further up."
    
    #options used for text box
    criteria_letter = widgets.Dropdown(
        options=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
        description= "First letter of company",
        disabled=False
    )
    

    def plot(criteria):
        '''
        Box plot showing the quartiles of rating per company. The user chooses which companies she wishes to see. 
            Parameters: 
                criteria: first letter of the company the user wishes to be displayed
        '''
        #dataframe with the desired companies
        new_df = df[df["company"].str.startswith(criteria)]
        #create boxplot
        ax = sns.boxplot(x = "company", y = "rating",data = new_df)
        ax.set_title("rating~company")
        ax.set_xticklabels(ax.get_xticklabels(),rotation = 85)


    print(description) 
    return widgets.interact(plot, criteria = criteria_letter)


def company_count(df):
    '''
    Bar chart(interactive) that visualizes how many companies exists per country 
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            fig(Barplot): counts of companies per location
    '''
    #description that is printed to describe what the user sees
    description = "Description: Most chocolate manufacturers come from Thailand with more than 800 companies. There are a lot of countries with less than 100 companies. And three countries(Canada, Germany and Vietnam) with approximately 200 companies."
    #get the counts of companies per country
    df2 = df.groupby("company location")["company"].count().reset_index(name="count")
    #create a bar plot 
    fig = px.bar(df2, x= "company location", y = "count", title= "Companies per company location")
    print(description) 
    return fig




def func(pct, allvals):
    '''
    used by plot_tastes to get the absolute values of the tastes
        Parameters: 
            pct: 
            allvals: tastes we want to display
        Returns: 
            absolute counts of the most common tastes
    '''
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def plot_tastes(df,taste,description):
    '''
    Pie chart with the 5 most common tastes. In the main program we choose for which taste we want to see the most common tastes
        Parameters: 
            df(DataFrame): dateframe used for plotting
            taste(String): name of the column we want the most common tastes from
            description(String): description of the Pie chart
        Returns: 
            plt(Pie chart): Pie chart with the 5 most common tastes
    '''
    #delete those columns with no information
    df2 = df[df[taste] != "no information"] 
    #count per values
    df2 = df2[taste].value_counts()
    #get the 5 most common tastes
    df2 = df2.head(5)
    #label of the tastes
    mylabels = df2.index[:5]
    #create pie chart
    plt.pie(df2, labels = mylabels, autopct=lambda pct: func(pct, df2))
    plt.title("Most " + taste + "s")
    plt.show()
    print(description) 
    return plt


def first_taste_years(df):
    '''
    counts of the first tastes per year that are rated 3.5 or higher
        Parameters: 
            df(DataFrame): dateframe used for plotting
        Returns: 
            fig(Scatterplot): scatter plot for the first tastes per year
    '''

    description = "Description: There is a lot of variety in the first tastes of the chocolates rated 3.5 or higher. A consistent first taste over all years is 'creamy'. Other consistent tastes are 'complex', 'cherry' and 'fatty'. Otherwise the tastes are quite diverse. Feel free to look around with Plotly to get a more detailed view. "

    #select the examples with ratings 3.5 or higher
    highest_rating = df[df["rating"] >= 3.5]
    # group by the years and count the first tastes
    df2 = highest_rating.groupby("review date")["first taste"].value_counts().reset_index(name='counts')

    #create a scatter plot with different colors for different counts
    fig = px.scatter(df2, x = "review date", y = "first taste", color = "counts", width = 1000, height = 1800, title = "The first taste of all chocolates rated 3.5 or higher over the years")

    print(description)
    return fig

