from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64
import dash_bootstrap_components as dbc
from PIL import Image





image_path ="assests/gif.gif"

def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df_line = pd.read_csv("assests/quarterly_combined_data_avg.csv")


df_line['region_id']=df_line['region_id'].astype(str)
df_line['year_quarter']=df_line['year_quarter'].astype(str)

df_line.rename(columns={'avg_med_house_price':'Average House Price','avg_rent_index':'Average Rent Price','region_desc':'Location','year_quarter':'Year/Quarter'}, inplace=True)

fig1 = px.line(df_line, title='Housing Prices Over Time', x="Year/Quarter", y="Average House Price", color="Location",markers=True)

fig2 = px.line(df_line, title='Rent Cost Over Time',x="Year/Quarter", y="Average Rent Price", color="Location", markers=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
pil_img = Image.open("assests/feature_importance_w_pricecut.jpg")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#










app.layout = html.Div(children=[
    # All elements from the top of the page
    html.H4("Relationship with Rent Costs (Left) | 3D Model of top 2 features to Median Home Price (Right)"),

        html.Img(src=pil_img,  style={'display':'inline-block', 'margin-left':'20px'}),

        html.Img(src=b64_image(image_path),  style={'display':'inline-block', 'margin-left':'305px','margin-bottom':'55px'}),
    
    
    
    html.Div([

        dcc.Graph(
            id='graph1',
            figure=fig1,
            style={'display':'inline-block'}
        ),
        
        dcc.Graph(
            id='graph2',
            figure=fig2,
            style={'display':'inline-block'}
        ),
        ]),



    
    
]) 
if __name__ == '__main__':
    app.run_server(debug=True) 
