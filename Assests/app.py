from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

df_line = pd.read_csv("Assests/quarterly_combined_data_avg.csv")


df_line['region_id']=df_line['region_id'].astype(str)
df_line['year_quarter']=df_line['year_quarter'].astype(str)

df_line.rename(columns={'avg_med_house_price':'Average House Price','avg_rent_index':'Average Rent Price','region_desc':'Location','year_quarter':'Year/Quarter'}, inplace=True)



fig1 = px.line(df_line, x="Year/Quarter", y="Average House Price", color="Location", width=2000, height=400, markers=True)

fig2 = px.line(df_line, x="Year/Quarter", y="Average Rent Price", color="Location", width=2000, height=400, markers=True)

app.layout = html.Div(children=[
    # All elements from the top of the page

    html.Div([
        html.H1(children='Housing Prices Over Time'),

        html.Div(children='''
            The cost of housing from 2018-2022
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),
        
    ]),
    

    html.Div([
        html.H1(children='Rent Cost Over Time'),
        

        html.Div(children='''
            The cost of rent from 2018-2022
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)