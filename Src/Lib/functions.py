import numpy
import pandas

import seaborn as sns
import matplotlib.pyplot as plt

def correlation(df, target = -1, threshold=0.75):
    '''Checks for correlation between a target column and the rest,
    drops columns that are below the threshold.
    
    Parameters: dataframe, target (column index, default = -1), threshold (default = 0.75)
    Returns: dataframe with columns above the threshold, displays Seaborn Heatmap'''
    
    df2 = df.copy()
	
    corr_matrix = df2.corr().abs()
	
    for i in range(len(corr_matrix.columns)):
        if (corr_matrix.iloc[i,target] < threshold):
            df2 = df2.drop(columns = corr_matrix.columns[i])
			
    sns.heatmap(df2.corr(), annot=True)
	
    return df2

def plot_maker(df, plot = sns.histplot, figsize_x = 20, figsize_y = 10):
	'''Returns a plot (default Seaborn histplot) in a single fig for each column of a given DataFrame
    
    Input: DataFrame, plot (default = sns.histplot), figsize_x (default = 20), figsize_y (default = 10)
    Output: Plots of all the columns'''

	cols = list(df.columns)
	fig_cols = len(cols)
	fig, ax = plt.subplots(1, fig_cols, figsize = (figsize_x, figsize_y))
        
	for col in cols:
		plot(data=df, x=col, ax = ax[cols.index(col)])
		ax[cols.index(col)].set_title(col)

	return


if __name__ == "__main__":
	correlation()
	plot_maker()