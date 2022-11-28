import os
import base64
import warnings
warnings.filterwarnings('ignore')
from IPython.display import display,Markdown
import matplotlib.pyplot as plt
import matplotlib.image as img
import seaborn as sns

import pandas as pd

table_section=''
plot_section=''
metric_section=''



def printmd(string):
    display(Markdown(string))

project_name=os.listdir(os.getcwd())[0]
path=os.getcwd()

project_folder=path+"\\"+project_name

for i in os.listdir(project_folder+'//Datasets'):
    table_name=i[:-4]
    table_html=pd.read_csv(project_folder+'//Datasets//'+i).to_html(index=False, na_rep='No Value',)
    section=f''' 
    <div class='table-sec'>
    <h1 class='table-name'>
    {i[:-4]}
    </h1>
    <div class='tab'>
    {table_html}
    </div>
    </div>
    '''
    table_section+=section
    # print(table_name)
    
    
for i in os.listdir(project_folder+'//Plots'):
    table_name=i[:-4]
    # print(project_folder+'//Plots//'+i)
    with open(project_folder+'//Plots//'+i, "rb") as img_file:
        base = base64.b64encode(img_file.read())
    # print(base[2:-1])
    

    section=f''' 
    <div class='plot-sec'>
    <h1 class='plot-name'>
    {i[:-4]}
    </h1>
    <div class='plot'>
    <img src="data:image/png;base64,{ str(base)[2:-1] }">
    </div>
    </div>
    '''
    plot_section+=section
    # print(i)
    
    
for i in os.listdir(project_folder+'//Metrics'):
    table_name=i[:-4]
    print(i)
    with open(project_folder+'//Metrics//'+i, "rb") as img_file:
        base = base64.b64encode(img_file.read())
        # print(base[2:-1])
        

    section=f''' 
        <div class='plot-sec'>
        <h1 class='plot-name'>
        {i[:-4]}
        </h1>
        <div class='plot'>
        <img src="data:image/png;base64,{ str(base)[2:-1] }">
        </div>
        </div>
        '''
    metric_section+=section
    
    
    
    
html=f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    table {{
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}}
.table-sec {{
    margin: 50px 50px;
}}
    
.table-name {{
    text-transform: capitalize;
}}
 td, #customers th {{
 text-overflow: ellipsis;
  border: 1px solid #ddd;
  padding: 8px;
    white-space: nowrap;
  overflow: hidden;
    max-width: 200px;
}}
.tab {{
    overflow-x: scroll;
}}
 tr:nth-child(even){{background-color: #f2f2f2;}}
 tr:hover {{background-color: #ddd;}}
 th {{
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}}
 
 
 .{{
    margin: 50px 0;
}}
 
h1.project-name {{
    text-align: center;
    font-size: 70px;
    color: cadetblue;
}}
 
.plot-section {{
    display: flex;
    flex-direction: column;
    align-items: stretch;
    padding:100px;
}}
.metrics-section {{
    display: flex;
    flex-direction: column;
    align-items: stretch;
    padding:100px;
}}
.plot > img {{
    width: 100%;
    padding:50px;
}}
 
 
</style>
</head>
<body>
<h1 class='project-name' >{project_name}</h1>
<div class="table-section">
{table_section}
</div>
<div class='plot-section'>
{plot_section}
</div>
<div class='metrics-section'>
{metric_section}
</div> 
</body>
</html>
'''


with open('report.html', 'w',encoding="utf-8") as f:
    f.write(html)
