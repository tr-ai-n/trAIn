# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class vizualize(object):

    def __init__(self, data):
        '''
        Class to encapsulate the primary
        data-visualization techniques
        ----------Arguements----------
        data:(pd.dataframe) Raw dataframe
        '''

        self.data = data
        self.columns_ = self.data.columns

        # check if `data` is of type `pd.Dataframe`
        if not isinstance(self.data, pd.DataFrame):
            raise Exception('data must be\
             type of pd.DataFrame')
    
    def dist_plot(self, col_tp='_all'):
        '''
        Draws Distribution plots
         for all the numeric column of the Dataframe
        ----------Arguments----------
        col_tp(str) : column name to plot
            default : 'all' plot all columns
        '''
        def check_numeric_type(col):
            '''
            function to check if the column is numeric
            '''
            if pd.api.types.is_numeric_dtype(
                self.data[col].dtype):
                return True
            else:
                return False

        all_numeric_columns = []

        if col_tp=='_all':
            # iterating over the type of each column
            for col in self.data.columns:
                if check_numeric_type(col): # checking if `col` type is numeric
                    all_numeric_columns.append(col) # appending numeric `col`

        else:
            if col_tp not in self.data.columns:
                raise Exception('column',
                col_tp,
                'does not exist in the dataframe.')
            if check_numeric_type(col_tp):
                all_numeric_columns.append(col_tp)

        num_cols = len(all_numeric_columns) # number of numeric oclumns

        # initializing subplot instance
        fig, ax = plt.subplots(num_cols,
                 figsize=(10, (num_cols)*5))

        # enumerating through the numeric cols

        if col_tp=='_all':
            for idx, col in enumerate(all_numeric_columns):  
                sns.distplot(self.data[col].dropna(),
                ax=ax[idx])
        else:
            sns.distplot(self.data[col_tp].dropna(),
                ax=ax)

        # plotting dist_plot
        plt.show()

        return fig, ax

    def null_heat_plot(self):
        '''
        ----------Arguements----------
        data:(pd.dataframe) Raw dataframe
        col:(str)

        '''
        
        fig, ax = plt.subplots(figsize=(10,6))
        sns.heatmap(self.data.isnull(), ax=ax)

        # plotting heat_null_plot
        plt.show()

        return fig, ax

    def class_pie_plot(self, class_col):
        '''
        Pie chart of the Class distribution
        
        '''
        if class_col==None:
            raise Exception('`class_col` \
                needs to be mentioned')
        class_counts = self.data[class_col].value_counts() # count class 
        
        labels = labels = self.data[class_col].unique()
        sizes = np.around((np.array(class_counts)/(np.array(class_counts).sum()))*100, decimals=2)

        fig, ax = plt.subplots()
        ax.pie(sizes,  labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()