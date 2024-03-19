import csv
from bs4 import  BeautifulSoup
import requests
import Webscraping as ws
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#https://fbref.com/en/comps/8/2020-2021/2020-2021-Champions-League-Stats
#https://fbref.com/en/comps/8/2019-2020/2019-2020-Champions-League-Stats

def result_assignment(filename):
    df = pd.read_csv(filename)
    scores = df['Goals']
    print(scores)
    results = []
    for i in range(0,len(scores)-4,4):
        if scores[i]>scores[i+2]:
            results.append('W')
        if  scores[i]<scores[i+2]:
            results.append('L')
        if scores[i]==scores[i+2]:
            results.append('D')
        if scores[i+1]>scores[i+3]:
            results.append('W')
        if  scores[i+1]<scores[i+3]:
            results.append('L')
        if scores[i+1]==scores[i+3]:
            results.append('D')
        if scores[i]<scores[i+2]:
            results.append('W')
        if  scores[i]>scores[i+2]:
            results.append('L')
        if scores[i]==scores[i+2]:
            results.append('D')
        if scores[i+1]<scores[i+3]:
            results.append('W')
        if  scores[i+1]>scores[i+3]:
            results.append('L')
        if scores[i+1]==scores[i+3]:
            results.append('D')

    df['Results'] = results
    last_col = 'Results'
    df.columns = list(df.columns[:-1]) + [last_col]
    df.to_csv(filename,index=False)



#only usable with  files that have had results assigned
import pandas as pd

def compare_lead_stats_win_times(filename1, compare_stat):
    df1 = pd.read_csv(filename1)
    print(f"called for {compare_stat}")
    cnt = 0

    for i in range(0, len(df1) - 4, 2):
        stats_team1_game1 = df1.iloc[i][compare_stat]
        stats_team1_game2 = df1.iloc[i + 1][compare_stat]
        stats_team2_game1 = df1.iloc[i + 2][compare_stat]
        stats_team2_game2 = df1.iloc[i + 3][compare_stat]
        result_team1_game1 = df1.iloc[i]['Results']
        result_team1_game2 = df1.iloc[i + 1]['Results']
        result_team2_game1 = df1.iloc[i + 2]['Results']
        result_team2_game2 = df1.iloc[i + 3]['Results']

        # Compare stats of two games for both teams and increment counter
        if ((result_team1_game1 == 'W' or result_team1_game1 == 'D') and stats_team1_game1 >= stats_team2_game1):
            cnt += 1
        elif ((result_team2_game1 == 'W' or result_team2_game1 == 'D') and stats_team2_game1 >= stats_team1_game1):
            cnt += 1
        if ((result_team1_game2 == 'W' or result_team1_game2 == 'D') and stats_team1_game2 >=  stats_team2_game2):
            cnt += 1
        elif ((result_team2_game2 == 'W' or result_team2_game2 == 'D') and stats_team2_game2 >= stats_team1_game2):
            cnt += 1

    return cnt

def compare_all_lead_stats_win_times(filename1):
    df1 = pd.read_csv(filename1)
    headers = list(df1.columns[1:-1])
    list_cnts =[]
    for header in headers:
        list_cnts.append(compare_lead_stats_win_times(filename1,header))

    return list_cnts
def compare_all_lead_stats_win_time_rates_tournament(filename1,filename2,filename3):
    length =4+16+32
    df1 = pd.read_csv(filename1)
    headers = list(df1.columns[1:-1])
    list_cnts1 =[]
    list_cnts2=[]
    list_cnts3 = []
    for header in headers:
        list_cnts1.append(compare_lead_stats_win_times(filename1,header))
        list_cnts2.append(compare_lead_stats_win_times(filename2,header))
        list_cnts3.append(compare_lead_stats_win_times(filename3,header))
    a=np.array(list_cnts1)
    b=np.array(list_cnts2)
    c=np.array(list_cnts3)
    final = (a+b+c)/length

    return final

def compare_all_leaf_stats_win_percentages(filename):
    df1 = pd.read_csv(filename)
    length = len(df1['Goals'])
    list_times  = compare_all_lead_stats_win_times(filename)
    out = [(x/length)*100 for x in  list_times]
    return out
def win_rate_analysis_tournament(filename1,filename2,filename3):
    df1 = pd.read_csv(filename1)
    headers  = list(df1.columns[1:-1])
    analysis = compare_all_lead_stats_win_time_rates_tournament(filename1,filename2,filename3)
    i=2
    for header  in headers[2:]:
        print(f"{analysis[i]*100}%  of teams led in {header} and won their matches")
        i+=1
'''print(compare_all_leaf_stats_win_percentages('QF1.csv'))
print(compare_all_lead_stats_win_time_rates_tournament('Ro161.csv','SF1.csv','QF1.csv'))
print(compare_all_lead_stats_win_times('QF1.csv'))
win_rate_analysis_tournament('Ro161.csv','SF1.csv','QF1.csv')
#advanced stats to focus on XG,npXG,Shots on Target,Successful Takes,Goal Creating Actions
#GCA,npXG,xAG,ScsfulTakes,PrgP'''




















