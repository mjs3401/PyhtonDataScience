"""
Testing out pandas features using example datasets
"""

import pandas as pd


def main():
    # Get sample dataset from R
    df = pd.read_csv( 'https://raw.githubusercontent.com/mwaskom/seaborn'
                      '-data/master/iris.csv')

    # Sort datafrems
    # Sort values ascending (default)
    df_sort_asc = df.sort_values('sepal_length')
    # Sort value descending
    df_sort_des = df.sort_values('sepal_length', ascending=False)
    # Sort multiple columns
    df_sort_multi = df.sort_values(['species','sepal_length'])

    # Rename columns
    df_rename = df.rename(columns = {'species':'name'})

    # Remove columns
    df_drop = df.drop(columns=['sepal_length','petal_width'])

    # Reshaping dataframes
    # Melt: Gather columns into rows. Rename new columns.
    df_melt = pd.melt(df).rename(columns={'variable':'var', 'value':'val'})


    return


if __name__ == '__main__':
    main()
