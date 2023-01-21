import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
# import hdbscan as hd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import sklearn
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from pyclustertend import hopkins, vat, ivat

plt.rcParams["figure.figsize"] = [16, 9]
DEFAULT_PLOTLY_COLORS = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)',
                         'rgb(44, 160, 44)', 'rgb(214, 39, 40)', 'rgb(148, 103, 189)', 'rgb(140, 86, 75)',
                         'rgb(227, 119, 194)', 'rgb(127, 127, 127)', 'rgb(188, 189, 34)', 'rgb(23, 190, 207)',
                         'rgb(182, 183, 32)', 'rgb(22, 191, 237)', 'rgb(221, 121, 45)', 'rgb(12, 81, 37)']

# Import JHU data
df_confirmed_save = pd.read_csv(
    "csse_covid_19_data/csse_covid_19_time_series/time_series_covid19 _confirmed_global.csv")
df_deaths_save = pd.read_csv("csse_covid_19_data/csse_covid_19_time_series/time_series_covid19 _deaths_global.csv")
df_recovered_save = pd.read_csv(
    "csse_covid_19_data/csse_covid_19_time_series/time_series_covid19 _recovered_global.csv")

