import pandas as pd
import numpy as np
from bokeh.io import show
from pandas import DataFrame
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.io import export_png
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.models import Title


from bokeh.layouts import gridplot
# Use this to output in Jupyter notebook
p = figure(plot_width=400, plot_height=400)

# show(p) # show the results
df = pd.DataFrame.from_csv("DATAset/HSall_members.csv")
state_df = df.loc[df["chamber"]=="House"]
state_df = state_df.groupby(["state_abbrev"]).size().reset_index(name = "number")
print(list(state_df))
state = state_df["state_abbrev"].tolist()
count = state_df["number"].tolist()
source = ColumnDataSource(data=dict(state = state,count=count))

# Set the x_range to the list of categories above
p = figure(x_range=state,plot_width=1500, plot_height=250, title="member in state")

# Categorical values can also be used as coordinates
p.vbar(x=state, top=count, width=0.9)

# Set some properties to make the plot look better
p.xgrid.grid_line_color = None
p.y_range.start = 0
show(p)
export_png(p, filename=str(1)+"image.png")
age_df = df.dropna(subset=["born","died"])
age_df = age_df.loc[age_df["chamber"]=="House"]
output = []
for index,row in age_df.iterrows():
    age = row["died"]-row["born"]
    output.append(age)
age_df["aveage"] = output

age_df = age_df.groupby(["state_abbrev"]).mean().reset_index()
state_age = []
ave_age = []
for index,row in age_df.iterrows():
    state_age.append(row["state_abbrev"])
    ave_age.append(row["aveage"])

source  = ColumnDataSource(data=dict(state = state_age, ave_age = ave_age))
p1 = figure(x_range = state, plot_width = 1500, plot_height=250, title="the age of member in state")
p1.vbar(x=state, top = ave_age, width = 0.9)
# show(p1)
export_png(p1, filename=str(2)+"image.png")
state_df = state_df.sort_values(by = "number",ascending=False)

state_df = state_df[0:10]
state = state_df["state_abbrev"].tolist()
count = state_df["number"].tolist()
source = ColumnDataSource(data=dict(state = state,count=count))

# Set the x_range to the list of categories above
p2 = figure(x_range=state,plot_width=500, plot_height=250, title="top 10 numbers of member in different state")

# Categorical values can also be used as coordinates
p2.vbar(x=state, top=count, width=0.9)
# show(p2)
export_png(p2, filename=str(3)+"image.png")
age_df = age_df.sort_values(by = "aveage",ascending=False)
age_df = age_df[0:10]
state_age = []
ave_age = []
for index,row in age_df.iterrows():
    state_age.append(row["state_abbrev"])
    ave_age.append(row["aveage"])

source  = ColumnDataSource(data=dict(state = state_age, ave_age = ave_age))
p3 = figure(x_range = state, plot_width = 500, plot_height=250, title="the oldest 10 members in different state")
p3.vbar(x=state, top = ave_age, width = 0.9)
# show(p3)
export_png(p3, filename=str(4)+"image.png")
