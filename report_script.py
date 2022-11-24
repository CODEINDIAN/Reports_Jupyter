# Importing libraries
import os
import warnings
warnings.filterwarnings('ignore')
from IPython.display import display,Markdown
import matplotlib.pyplot as plt
import matplotlib.image as img
import seaborn as sns
import pandas as pd


def printmd(string):
    display(Markdown(string))

project_name=os.listdir(os.getcwd()+'//Source')[0]
path=os.getcwd()

project_folder=path+"\\Source\\"+project_name

section_list=os.listdir(project_folder)

# print(section_list)

# Section _1
printmd(f'''# <h1 style='text-align:center;color:#8c2fde;'> {project_name}</h1>''')
printmd('<br><br><br>')
printmd('# Plots')

datasets_path=project_folder+'\\Datasets'
for i in os.listdir(datasets_path):
    printmd(f''' # DatasetName: {i[:-4]} <br>''')
    display(pd.read_csv(datasets_path+'\\'+i))
printmd('<br><br><br>')
printmd('# Plots')
# Section 2
plots_path=project_folder+'\\Plots'
for i in os.listdir(plots_path):
    printmd(f''' # Plots: {i[:-4]} <br>''')
    plt.figure(figsize=(20,10),dpi=200)
    im = img.imread(plots_path+'\\'+i)
    plt.imshow(im)
    plt.show()



