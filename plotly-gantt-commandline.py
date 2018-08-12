# new test 

import platform
import IPython
import pandas as pd
import numpy as np  
import plotly
import datetime

from plotly import __version__
import plotly.figure_factory as ff

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
print(__version__) 

import plotly.graph_objs as go

#plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])

# displays  in  notebook -  WORKED  
init_notebook_mode(connected=True)
iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])


print("Loaded a few libraries ...")
print("python  version " + platform.python_version())
print("IPython version is {} -> okay".format(IPython.version_info))
print("Plotly  version: " + __version__)
print("Pandas  version: " + pd.__version__)
print("Numpy   version: " + np.__version__)

t1 = datetime.datetime.now()
print("Loading Project Catalog using Excel")
#  path to file . 
excel_file = "/devel/py35-work/data/scenario-inputs2.xlsx"
movies_sheet1 = pd.read_excel(excel_file, sheet_name="ProjectCatalog", index_col=0)
movies_sheet1.head()
t2 = datetime.datetime.now()
print("Loaded Project Catalog in " + str((t2-t1).total_seconds()) +  " seconds" ) 

df = [dict(Task="Job A1", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B1", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C1", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
iplot(fig, filename='gantt-simple-gantt-chart', world_readable=True)


print("\n** See Chart At https://plot.ly/~mbisignani/0\n" )


