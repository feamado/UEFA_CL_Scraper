Fernando  Amado

To Get Results for 2018-19 season
Link:https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats
Firstly use the linkloader function in Webscraping.py with this link 
as such  linkloader(https://fbref.com/en/comps/8/2018-2019/2018-2019-Champions-League-Stats)
once it has been loaded a csv file will pop up in your IDE and/or your files.
This  csv  contains the links that will be used to webscrape the stats, it is done in this manner to slow down rate request limited errors 
Afterwards use the write_to_csv_from_file()function with the filename of the csv link storing file that has just been downloaded (should be something like 2018-2019 Champions League)
This will generate 3 Files with  QF, SF,Ro16 as their titles along  with a number so that the function can be run multiple times to create multiple different files.
You can now look at the team stats in each file for every game in every round from the round of 16 to the semi finals (52 games)
After wards you will use the win_rate_analysis_tournament(filename1,filename2,filename3) with the three filenames that  have been just  generated that  hold the stats in place  of the filenames  in the argument. This will  provide the total times a team leading in a stat other than goals or assists won to show the commanding stats of the tournament
for the 2018-19 edition the  results should be
Team leading in PK converted won or drew 71.15384615384616%  of matches
Team leading in PK attempted won or drew 67.3076923076923%  of matches
Team leading in Shots won or drew 55.769230769230774%  of matches
Team leading in Shots on Target won or drew 65.38461538461539%  of matches
Team leading in YCrds won or drew 51.92307692307693%  of matches
Team leading in Rcards won or drew 69.23076923076923%  of matches
Team leading in Touches won or drew 51.92307692307693%  of matches
Team leading in Tackles won or drew 50.0%  of matches
Team leading in Interceptions won or drew 48.07692307692308%  of matches
Team leading in BlockedShots won or drew 44.230769230769226%  of matches
Team leading in XG won or drew 59.61538461538461%  of matches
Team leading in npXG won or drew 63.46153846153846%  of matches
Team leading in xAG won or drew 63.46153846153846%  of matches
Team leading in SCA won or drew 55.769230769230774%  of matches
Team leading in GCA won or drew 73.07692307692307%  of matches
Team leading in Cmp won or drew 51.92307692307693%  of matches
Team leading in Att won or drew 50.0%  of matches
Team leading in Cmp% won or drew 51.92307692307693%  of matches
Team leading in PrgP won or drew 50.0%  of matches
Team leading in Carries won or drew 51.92307692307693%  of matches
Team leading in PrgC won or drew 48.07692307692308%  of matches
Team leading in AttTakes won or drew 51.92307692307693%  of matches
Team leading in ScsflTakes won or drew 55.769230769230774%  of matches
but these  steps can be repeated to get data for any other edition of the tournament as long as  you use football reference 
here are other links the steps can be repeated for 
https://fbref.com/en/comps/8/2020-2021/2020-2021-Champions-League-Stats
https://fbref.com/en/comps/8/2019-2020/2019-2020-Champions-League-Stats
and  any other main champions league stats page from this website
