---
layout: post
title: "Top 100 universities in India - Analyze using pandas"
date: 2017-04-05
tags: [tips]
comments: true
---

&nbsp;

Yesterday, I saw this year's top 100 Indian university ranking list. You can view the [ranking methodology here](https://www.nirfindia.org/Docs/Ranking_Methodology_And_Metrics_2017.pdf). I thought to plot simple histogram using this data. Which state is more frequent in the list? You can view the data from this web page [National Institutional Ranking Framework](https://www.nirfindia.org/univ).

&nbsp;

<img src="/images/nirfindia.png?raw=true" style="width: 1600px;"/>

&nbsp;

We are going to use pandas library in python. You can read [pandas from here](http://pandas.pydata.org/pandas-docs/stable/). The definition is from the above link.

>pandas is a Python package providing fast, flexible, and expressive data structures designed to make working >with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level >building block for doing practical, real world data analysis in Python. 

I use "python version 3.6.0". You can find using the command "python -V" or "python --version" in terminal (GNU/Linux). And, I use "pandas version 0.19.2". Use these below commands. 

    import pandas as pd
    print(pd.__version__)

In case, if you do not have python pandas, google for pandas installations.


To read an html link

    india_rank = pd.read_html("https://www.nirfindia.org/univ")[0]
    print(india_rank)

See the printed results below.

&nbsp;

<img src="/images/nirfindia1.png?raw=true" style="width: 600px;"/>

&nbsp;

<img src="/images/nirfindia2.png?raw=true" style="width: 600px;"/>

&nbsp;

<img src="/images/nirfindia3.png?raw=true" style="width: 600px;"/>

&nbsp;

The results are messy, and surprisingly there are "300 rows x 16 columns". I guess due to the table inside the table pandas read it differently (see first figure). 

Let us drop the "Nan" datas from the table.

    india_rank = india_rank.dropna()

See the present table size

    print(india_rank.shape)

The result is (100, 16). 

Print the table now

    print(india_rank)

&nbsp;

<img src="/images/nirfindia4.png?raw=true" style="width: 600px;"/>

&nbsp;

You can view a small table inside the column index "Name" (see first figure). We will drop the unwanted columns. I counted the column by index number and found 11 [2,3,4,5,6,7,8,9,10,11,12] columns have to be removed.

    columns_to_drop = [2,3,4,5,6,7,8,9,10,11,12]
    india_rank = india_rank.drop(india_rank.columns[columns_to_drop], axis=1)
    print(india_rank)

&nbsp;

<img src="/images/nirfindia5.png?raw=true" style="width: 600px;"/>

&nbsp;

Now, you can see only the required column names"INSTITUTE ID, Name, Unnamed: 13, Unnamed: 14, and Unnamed: 15"
We can change column name as follows

    Unnamed: 12    =  City
    Unnamed: 13    =  State
    Unnamed: 14    =  Score
    Unnamed: 15    =  Rank

&nbsp;

<img src="/images/nirfindia6.png?raw=true" style="width: 600px;"/>

&nbsp;

Use the commands to groupby 'State' and a new column "count"

    india_rank_state = india_rank.groupby(["State"])["City"].count().reset_index(name="State_count")

&nbsp;

<img src="/images/nirfindia7.png?raw=true" style="width: 600px;"/>

&nbsp;

Use matplotlib to plot and the following command to show the plot figure

    import matplotlib.pyplot as plt
    india_rank_state.plot(x='State', y='State_count', kind='bar', legend=False)
    india_rank_state.to_csv("india_rank_list.csv", sep=',')
    plt.show()

&nbsp;

<img src="/images/ranking_university_state.png?raw=true" style="width: 1600px;"/>

&nbsp;

You can download the [file here](/data/india_rank_list.csv) and the full script is below.

&nbsp;

    import pandas as pd
    import matplotlib.pyplot as plt

    india_rank = pd.read_html("https://www.nirfindia.org/univ")[0]
    india_rank = india_rank.dropna()

    columns_to_drop = [2,3,4,5,6,7,8,9,10,11]
    india_rank = india_rank.drop(india_rank.columns[columns_to_drop], axis=1)
    india_rank = india_rank.rename(columns={'Unnamed: 12': 'City', 'Unnamed: 13': 'State', 'Unnamed: 14': 'Score', 'Unnamed: 15': 'Rank'})

    india_rank_state = india_rank.groupby(["State"])["City"].count().reset_index(name="State_count")

    india_rank_state.plot(x='State', y='State_count', kind='bar', legend=False)
    india_rank_state.to_csv("india_rank_list.csv", sep='\t')
    plt.show()
