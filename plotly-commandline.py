from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)  # requires version >= 1.9.0

import plotly.graph_objs as go

plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])