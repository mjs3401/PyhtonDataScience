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

    # Concat dataframes
    # Concat two
    df_concat = pd.concat([df,df])

    # Subset rows
    # Select rows
    df_rows = df[df.sepal_length > 5]
    # Select sample of rows
    df_sample = df.sample(frac=0.5)
    # Select 10 largest
    df_largest = df.nlargest(10,'sepal_length')
    # Select 10 smallest
    df_smallest = df.nsmallest(10, 'sepal_length')
    # First n rows
    df_head = df.head(25)
    # Select last n rows
    df_tail = df.tail(25)

    # Subset columns
    # Select subset of mulitple columns
    df_subcol = df[['species', 'sepal_length']]
    # Select single column
    df_onecol = df['species']
    # Other way to do this
    df_onecol = df.species
    # Select column names that match regex
    df_regex_col = df.filter(regex='.*\width$')



    return


if __name__ == '__main__':
    main()
