
# Team D: Rising Home Prices
## Overview of Project

Our team wanted to answer a very relevant question for many americans, including ourselves: **Is there an increase in the housing prices for our top five major cities** ? We are confident we can answer this question. With that being said, below we provided our process of aquiring the informaion, our database, and our machine learning model(s). 


<img src="https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/pexels-jeffrey-czum-2904142.jpg" width="400" height="400">


## Communication Roles

While the team will collaborate on all roles, the following responsibilities are as follows:

<img src="https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/team_roles.png" width="800" height="400">

## Data Integration 


We decide to utilize the Postgres data base system. Our data will primarily be focused on five major cities in America. The following is the list of major cities:

1. Chicago
2. Austin
3. Houston 
4. Nashville 
5. Charlotte

Our datasets are sourced from Zillow, Zillow Group, Federal Housing Finance Agency, Online Data Robert Shiller, and University of Chicago Library. 
For our datasets we will be the main metric we will be using is “Metropolitan Statistical Area” or MSA. MSA focuses on population core that has community with a high concentration of economic and social integration.  
We will be utilizing Amazon’s Amazon Web Services. AWS is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.
Now, we moved the following metrics to the ASW instance
- Median home price/MSA
-	Unemployment/MSA 
-	MSA Table
All metrics will be moved to Postgres to be cleaned, organized, and preform our data analysis. 

#### Update 11/10

From the above data sources, we pulled from 6 data tables to combine into one .csv file called combined_data. This was refined to the 5 focus MSA areas. This was all done and transformed within our SQL database in Postgres. The file was loaded to our GitHub repository to be pulled into the Machine Learning model. Once in model, we removed any NaN's from the most recently data set.


Based off our research we have come to the conclusion that these cities provide the most useful informaiton in answering our question. Our research revoles around investigating what is the **average cost of living** based off the ten years. We will also be analyzing the **housing prices** in the desired locations. 

#### Update 11/17
We have added additional data for Price Cut table from Zillow to test the additional accuracy.


<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/pexels-karolina-grabowska-4506270.jpg width="400" height="400">

## Machine Learning

After reviewing machine learning models, we believe that a **Supervised Linear Regression Model** will benefit our project the most by giving us the most accurate output. The primary directive of our model is to make a projection for 2-5 years out. We believe that it will be a sufficent time interval. **Our model should predict a linear trend**. 

#### Update 11/10
The initial Machine Learning model is based on the Combined_Data.csv created in the ETL portion of the data integration. Since the target variable of Med_Home_Price is a continuous variable without classification, we used the Naive Random Oversampling. Performing a accuracy check, the model is currently at 65%. We will look for possible different sampling techniques but also additional data.



#### Update 11/17
Machine model was further tested by looking at importance of the features. The resulting bar chart represents those features. The strongest relationship is with Rent cost.

<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/feature_importances.png width="400" height="200">


## Dashboard 

#### Update 11/17
For our dashboard, we will be using Python Dash, Plotly, and Flask (located in Assets folder) in repository host on local server.
<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/dashboard_example.png width="400" height="200">

Now, "Dash" is a Python framework that is designed for building web applications. It builds on top of Flask, Plotly. It gives the user the ability to build dashboards using pure Python. 

 