from bs4 import BeautifulSoup
import requests
import csv
#allows for opening new files with new  filenames and pairs files from the  same tournament with the same number
with open('counter.txt', 'r') as file:
    count = int(file.read())

count += 1

with open('counter.txt', 'w') as file:
    file.write(str(count))





def team_stats_indiv_game(urlgame):
    outdict = {}
    url = urlgame
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    #FIND THE TEAM NAMES


    header = soup.find('h1')
    #Split the text by the vs. and get r

    print(header.text)
    team1  = header.text.split("vs.")[0]
    #remove white space
   # print(team1)

    team1 = team1[:-1]
   # print(team1)
    team2 = header.text.split("vs.")[1]
    team2 = (team2.split("Match Report")[0])[1:-1]
    #data finding algorithm
    tables = soup.find_all('table')
    table4 = tables[3] # 4th table
    table11 = tables[10] # 11th table

    id4 = table4['id'] # get the ID attribute of the 4th table
    id11 = table11['id'] # get the ID attribute of the 11th table
    #find id of table
    titles1 = soup.find(id=id4)
    #get all table rows
    rows1 = titles1.find_all('tr')
    #get the data of the last row  of table rows
    cols1 = rows1[-1].find_all('td')
    cols1  = cols1[5:]
    # remove empty first 4 data cols  then convert to text
    data1 = [x.text for x in cols1]
    outdict[team1]=data1
    titles2=soup.find(id=id11)
    rows2 = titles2.find_all('tr')
    cols2 = rows2[-1].find_all('td')
    cols2  = cols2[5:]
    data2 = [x.text for x in cols2]
    outdict[team2] = data2
    return  outdict
# must use for two pairs  of teams that play each other
#must be in order  first  game, second game
def team_stats_round(url1,url2):
    round1 = team_stats_indiv_game(url1)
    round2 = team_stats_indiv_game(url2)
    outround={}
    for key,value in round2.items():
        for key2,value2 in round1.items():
            if(key==key2):
                tmp=[]
                tmp.append(round1[key])
                tmp.append(round2[key])
                outround[key]=tmp
    return outround




def knockout_tournament_links(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #names=soup.find_all("div", class_='matchup-team team1 winner')
    #names+=soup.find_all("div", class_='matchup-team team2')
    #names = [x.text.strip().replace('\n','') for x in names]
    #all_the_data = dict.fromkeys(names)
    #for  key in  all_the_data.keys():
        #all_the_data[key]=[]
    with open('links' + f'count' + '.csv', mode='w', newline='') as filelinks:

     span_tag = soup.find_all('span', class_='match-score')
     links=[]

    for span in span_tag:
        small_tag = span.find('small')
        a_tag = small_tag.find('a', href=True)
        #checks that a_tag has an element\
        if a_tag:
            link = a_tag['href']
            links.append("https://fbref.com"+link)


    for i in range(0,len(links),2):
        print(links[i])
        print(links[i+1])


    return links

def linkloader(url):
    #https://fbref.com/en/comps/8/2020-2021/
    name = url[39:]
    s = knockout_tournament_links(url)
    with open(name + '.csv', mode='w', newline='') as fileLink:
        writerlinks = csv.writer(fileLink)
        for link in s:
            writerlinks.writerow([link])
    fileLink.close()
    return



def write_to_csv(url):
    global count

    linkhub = knockout_tournament_links(url)
    with open('Ro16'+f'{count}'+'.csv', mode='w', newline='') as file16:
        writer16 = csv.writer(file16)
        listofgames16 = []
        matches_16_a = team_stats_round(linkhub[12], linkhub[13])
        matches_16_b = team_stats_round(linkhub[14], linkhub[15])
        matches_16_c = team_stats_round(linkhub[16], linkhub[17])
        matches_16_d = team_stats_round(linkhub[18], linkhub[19])
        matches_16_e = team_stats_round(linkhub[20], linkhub[21])
        matches_16_f = team_stats_round(linkhub[22], linkhub[23])
        matches_16_g = team_stats_round(linkhub[24], linkhub[25])
        matches_16_h = team_stats_round(linkhub[26], linkhub[27])
        listofgames16.append(matches_16_a)
        listofgames16.append(matches_16_b)
        listofgames16.append(matches_16_c)
        listofgames16.append(matches_16_d)
        listofgames16.append(matches_16_e)
        listofgames16.append(matches_16_f)
        listofgames16.append(matches_16_g)
        listofgames16.append(matches_16_h)
        writer16.writerow(['Team', 'Goals', 'Assists','PK converted','PK attempted',
                           'Shots','Shots on Target','YCrds','Rcards','Touches','Tackles','Interceptions','BlockedShots'
                              ,'XG','npXG','xAG','SCA','GCA','Cmp','Att','Cmp%','PrgP','Carries','PrgC','AttTakes','ScsflTakes'])  # write header row
        #dictionary pair
        for game in listofgames16:
            for key,value in game.items():
                #write team name then first game stats
                row1 = [key]
                row1.extend(game[key][0])
                #blank  then first game stats
                row2 = [""]
                row2.extend(game[key][1])
                writer16.writerow(row1)
                writer16.writerow(row2)
        file16.close()

    with open('QF'+f'{count}'+'.csv', mode='w', newline='') as fileQF:
        writerQF = csv.writer(fileQF)
        listofgamesQF = []
        matches_QF_a = team_stats_round(linkhub[4],linkhub[5])
        matches_QF_b = team_stats_round(linkhub[6], linkhub[7])
        matches_QF_c = team_stats_round(linkhub[8],linkhub[9])
        matches_QF_d = team_stats_round(linkhub[10],linkhub[11])
        listofgamesQF.append(matches_QF_a)
        listofgamesQF.append(matches_QF_b)
        listofgamesQF.append(matches_QF_c)
        listofgamesQF.append(matches_QF_d)
        writerQF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesQF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerQF.writerow(row1)
                writerQF.writerow(row2)
        fileQF.close()
    with open('SF'+f'{count}'+'.csv', mode='w', newline='') as fileSF:
        writerSF = csv.writer(fileSF)
        listofgamesSF=[]
        matches_SF_a  = team_stats_round(linkhub[0],linkhub[1])
        matches_SF_b = team_stats_round(linkhub[2],linkhub[3])
        listofgamesSF.append(matches_SF_a)
        listofgamesSF.append(matches_SF_b)
        writerSF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesSF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerSF.writerow(row1)
                writerSF.writerow(row2)
        fileSF.close()
#filename should be with a linkhub
def write_to_csv_from_file(filename):
    global count
    linkhub=[]
    with open(filename, mode='r', newline='') as fileLink:
        readerLink = csv.reader(fileLink)
        for row in readerLink:
            linkhub.append(row)
    fileLink.close()
    with open('Ro16'+f'{count}'+'.csv', mode='w', newline='') as file16:
        writer16 = csv.writer(file16)
        listofgames16 = []
        matches_16_a = team_stats_round(linkhub[12][0], linkhub[13][0])
        matches_16_b = team_stats_round(linkhub[14][0], linkhub[15][0])
        matches_16_c = team_stats_round(linkhub[16][0], linkhub[17][0])
        matches_16_d = team_stats_round(linkhub[18][0], linkhub[19][0])
        matches_16_e = team_stats_round(linkhub[20][0], linkhub[21][0])
        matches_16_f = team_stats_round(linkhub[22][0], linkhub[23][0])
        matches_16_g = team_stats_round(linkhub[24][0], linkhub[25][0])
        matches_16_h = team_stats_round(linkhub[26][0], linkhub[27][0])
        listofgames16.append(matches_16_a)
        listofgames16.append(matches_16_b)
        listofgames16.append(matches_16_c)
        listofgames16.append(matches_16_d)
        listofgames16.append(matches_16_e)
        listofgames16.append(matches_16_f)
        listofgames16.append(matches_16_g)
        listofgames16.append(matches_16_h)
        writer16.writerow(['Team', 'Goals', 'Assists','PK converted','PK attempted',
                           'Shots','Shots on Target','YCrds','Rcards','Touches','Tackles','Interceptions','BlockedShots'
                              ,'XG','npXG','xAG','SCA','GCA','Cmp','Att','Cmp%','PrgP','Carries','PrgC','AttTakes','ScsflTakes'])  # write header row
        #dictionary pair
        for game in listofgames16:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writer16.writerow(row1)
                writer16.writerow(row2)
        file16.close()

    with open('QF'+f'{count}'+'.csv', mode='w', newline='') as fileQF:
        writerQF = csv.writer(fileQF)
        listofgamesQF = []
        matches_QF_a = team_stats_round(linkhub[4][0],linkhub[5][0])
        matches_QF_b = team_stats_round(linkhub[6][0], linkhub[7][0])
        matches_QF_c = team_stats_round(linkhub[8][0],linkhub[9][0])
        matches_QF_d = team_stats_round(linkhub[10][0],linkhub[11][0])
        listofgamesQF.append(matches_QF_a)
        listofgamesQF.append(matches_QF_b)
        listofgamesQF.append(matches_QF_c)
        listofgamesQF.append(matches_QF_d)
        writerQF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesQF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerQF.writerow(row1)
                writerQF.writerow(row2)
        fileQF.close()
    with open('SF'+f'{count}'+'.csv', mode='w', newline='') as fileSF:
        writerSF = csv.writer(fileSF)
        listofgamesSF=[]
        matches_SF_a  = team_stats_round(linkhub[0][0],linkhub[1][0])
        matches_SF_b = team_stats_round(linkhub[2][0],linkhub[3][0])
        listofgamesSF.append(matches_SF_a)
        listofgamesSF.append(matches_SF_b)
        writerSF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesSF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerSF.writerow(row1)
                writerSF.writerow(row2)
        fileSF.close()


def write_to_csvSF(SF):
    global count
    linkhub = SF
    with open('SF'+f'count'+'.csv', mode='w', newline='') as fileSF:
        writerSF = csv.writer(fileSF)
        listofgamesSF=[]
        matches_SF_a  = team_stats_round(linkhub[0],linkhub[1])
        matches_SF_b = team_stats_round(linkhub[2],linkhub[3])
        listofgamesSF.append(matches_SF_a)
        listofgamesSF.append(matches_SF_b)
        writerSF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesSF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerSF.writerow(row1)
                writerSF.writerow(row2)
        fileSF.close()
def write_to_csvQF(QF):
    global count
    linkhub = QF
    with open('QF'+f'count'+'.csv', mode='w', newline='') as fileQF:
        writerQF = csv.writer(fileQF)
        listofgamesQF = []
        matches_QF_a = team_stats_round(linkhub[0],linkhub[1])
        matches_QF_b = team_stats_round(linkhub[2], linkhub[3])
        matches_QF_c = team_stats_round(linkhub[4],linkhub[5])
        matches_QF_d = team_stats_round(linkhub[6],linkhub[7])
        listofgamesQF.append(matches_QF_a)
        listofgamesQF.append(matches_QF_b)
        listofgamesQF.append(matches_QF_c)
        listofgamesQF.append(matches_QF_d)
        writerQF.writerow(['Team', 'Goals', 'Assists', 'PK converted', 'PK attempted', 'Shots', 'Shots on Target', 'YCrds', 'Rcards',
             'Touches', 'Tackles', 'Interceptions', 'BlockedShots', 'XG', 'npXG', 'xAG', 'SCA', 'GCA', 'Cmp', 'Att',
             'Cmp%', 'PrgP', 'Carries', 'PrgC', 'AttTakes', 'ScsflTakes'])
        for game in listofgamesQF:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writerQF.writerow(row1)
                writerQF.writerow(row2)
        fileQF.close()
"""def write_to_csv16(R16):
    linkhub  = R16
    with open('Ro16.csv', mode='w', newline='') as file16:
        writer16 = csv.writer(file16)
        listofgames16 = []
        matches_16_a = team_stats_round(linkhub[0], linkhub[1])
        matches_16_b = team_stats_round(linkhub[2], linkhub[3])
        matches_16_c = team_stats_round(linkhub[4], linkhub[5])
        matches_16_d = team_stats_round(linkhub[6], linkhub[7])
        matches_16_e = team_stats_round(linkhub[8], linkhub[9])
        matches_16_f = team_stats_round(linkhub[10], linkhub[11])
        matches_16_g = team_stats_round(linkhub[12], linkhub[13])
        matches_16_h = team_stats_round(linkhub[14], linkhub[15])
        listofgames16.append(matches_16_a)
        listofgames16.append(matches_16_b)
        listofgames16.append(matches_16_c)
        listofgames16.append(matches_16_d)
        listofgames16.append(matches_16_e)
        listofgames16.append(matches_16_f)
        listofgames16.append(matches_16_g)
        listofgames16.append(matches_16_h)
        writer16.writerow(['Team', 'Goals', 'Assists','PK converted','PK attempted',
                           'Shots','Shots on Target','YCrds','Rcards','Touches','Tackles','Interceptions','BlockedShots'
                              ,'XG','npXG','xAG','SCA','GCA','Cmp','Att','Cmp%','PrgP','Carries','PrgC','AttTakes','ScsflTakes'])  # write header row
        #dictionary pair
        for game in listofgames16:
            for key,value in game.items():
                row1 = [key]
                row1.extend(game[key][0])
                row2 = [""]
                row2.extend(game[key][1])
                writer16.writerow(row1)
                writer16.writerow(row2)"""
"""def knockout_tournament_links16(url):
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #names=soup.find_all("div", class_='matchup-team team1 winner')
    #names+=soup.find_all("div", class_='matchup-team team2')
    #names = [x.text.strip().replace('\n','') for x in names]
    #all_the_data = dict.fromkeys(names)
    #for  key in  all_the_data.keys():
        #all_the_data[key]=[]


    span_tag = soup.find_all('span', class_='match-score')
    links=[]

    for span in reversed(span_tag):
        small_tag = span.find('small')
        a_tag = small_tag.find('a', href=True)
        if a_tag:
            link = a_tag['href']
            links.append("https://fbref.com" + link)
            if len(links) == 16:
                break

    for i in range(0,len(links),2):
        tmpdict={}
        print(links[i])
        print(links[i+1])
        tmpdict = team_stats_round(links[i],links[i+1])
        #for key in tmpdict.keys():
         #   if key in all_the_data:
          #      all_the_data[key].append((tmpdict[key]))
    #print(all_the_data)


    return links

















"""
#to prevent excessive webscraping use which could lead to rate limited request linkloader to load  links then load
#example link: https://fbref.com/en/comps/8/2017-2018/2017-2018-Champions-League-Stats
#linkloader('https://fbref.com/en/comps/8/2017-2018/2017-2018-Champions-League-Stats')
#run once then delete
#then call write_to_csv_from_file() with created file
#if you wait sufficiently between linkloads you can create a large database of possibly all champions league knockout tournaments
