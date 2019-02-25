import viz
import pandas as pd

# sample data
df_tmp = pd.read_csv('sample_data/titanic/train.csv')

v1 = viz.vizualize(df_tmp)

v1.dist_plot(col_tp='_all')
v1.null_heat_plot()
v1.class_pie_plot('Survived')