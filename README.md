
# Team D: Rising Home Prices
## Overview of Project

Our team wanted to answer a very relevant question for many americans, including ourselves: **Is there an increase in the housing prices for our top five major cities** ? We are confident we can answer this question. With that being said, below we provided our process of aquiring the informaion, our database, and our machine learning model(s). 


<img src="https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/pexels-jeffrey-czum-2904142.jpg" width="400" height="400">


## Communication Roles

While the team will collaborate on all roles, the following responsibilities are as follows:

<img src="https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/team_roles.png" width="400" height="200">

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


Based off our research we have come to the conclusion that these cities provide the most useful informaiton in answering our question. Our research revoles around investigating what is the **average cost of living** based off the ten years. We will also be analyzing the **housing prices** in the desired locations. 




<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/pexels-karolina-grabowska-4506270.jpg width="400" height="400">

## Machine Learning 


After reviewing machine learning models, we believe that a **Supervised Linear Regression Model** will benefit our project the most by giving us the most accurate output. The primary directive of our model is to make a projection for 2-5 years out. We believe that it will be a sufficent time interval. **Our model should predict a linear trend**. 


<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/pexels-gustavo-fring-6285130.jpg width="400" height="200">


## Dashboard 
<img src=https://github.com/NortonAAA/Team_D_Final_Project/blob/main/images/Housing%20Price%20Dashboard/Slide1.PNG width="400" height="200">