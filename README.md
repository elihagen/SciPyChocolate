All you have to do to see our results is to run the MainProject.ipynb file. There you will be guided through our project.
Make sure you have the preprocessing.py, plot.py, and playfile.py available for the MainProject.ipynp.

Project requirement list
libraries:
- numpy (for math functions, working with arrays)
- math(for math functions)
- scipy (for statistics, integration)
- pandas (for grouping, combining, filtering, time-series)
- matplotlib (for data visualization)
- seaborn (for plotting (random distributions, uses matplotlib underneath)
- plotly (for interactive plotting)
- ipywidgets (for interactive widgets like sliders,...)

project description & goal:
Our aim is to visualize some interesting relationships in the Chocolate dataset.
Where do the most popular chocolate varieties come from? Which ingredients are the most popular? Is there a change in tastes?
Here the user can select which information he wishes to see.
We also want to try to give you the best matches by entering your preferences for cocoa content or place of origin.


Preprocessing.py:
(input: cvs file path, output: modified data frames)
This file is used to preprocess the data.
There are 3 possible outputs in this file: preprocessed data (preprocessing()), summary statistics (statistics()), list of all companies (get_list_company()) and a list of all countries (get_list_countries()). Choose an option and you will get the result.
You do not need a parameter for these methods.

Plot.py:
(input: df and constraints, output: plot is shown)
This file is intended for data analysis and visualisation. You can freely choose which data you are interested in and this plot will be the output. Decide between review_dates, overall ratings (ratings), overall cocoa percent (cocoa_percent), cocoa_percent_rating, bean_origin_rating, company_rating, company_count, most common first_tastes, second or third tastes (plot_tastes) and the count of first tastes of popular chocolates over the years (first_taste_years). These methods require the method name as stated here and the preprocessed data as parameter. Below each graph is a short description. This will help you to understand the graphs and describes what you can see and what conclusions you can draw.
Some plots are interactive. For company_rating, you can choose which data you are particularly interested in. For cocoa_percent, cocoa_percent_rating, company_rating and first_taste_years, you can move the mouse over the graph and see the more precise values for the individual data points.

Play.py:  
input: df and constraints
output: chocolate that meets your needs :)
The file is already imported and ready for use.
This file should help you to find your dream chocolate. Specify allergies, the region from which you want chocolate, the cocoa content and the ingredients that should not be missing. The right chocolate will be displayed.
