from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# This tool will require to first create a list of all the MATCH_IDs the user wants to get the data from.

# Insert the date of the events you will be scraping.
DATE_NAME = 'INSERT_DATE_HERE'

# Insert the MATCH_ID of the first match of the list.
lst_first = ['INSERT_FIRST_MATCH_ID_HERE']

# Insert the rest of the MATCH_IDs here.
lst_rest = ['INSERT_REST_MATCH_ID_HERE']

# # Replace this path with the path you want the .csv with data to be saved into.
# data_csv_path = '/Users/YOUR_USER/YOUR_FOLDER/'

# Loop through the lst_first list (this will only contain one match).
# Then replace "lst_first" with "lst_rest" to loop though the rest of the matches.
for match in lst_first:
    browser = webdriver.Chrome()
    browser.get(f'https://www.flashscore.co.uk/match/{match}/#/match-summary')

    time.sleep(4)
    browser.maximize_window()
    window_before = browser.window_handles[0]
    print('browser.title ' + browser.title)

    time.sleep(4)

    # Hide cookies banner
    browser.execute_script("document.getElementById('onetrust-banner-sdk').style.display='none';")

    # Define Team Home and Team Away
    team_home = browser.find_element("css selector",
            '.duelParticipant__home .participant__participantName .participant__overflow').get_attribute('innerHTML')

    team_away = browser.find_element("css selector",
            '.duelParticipant__away .participant__participantName .participant__overflow').get_attribute('innerHTML')

    time.sleep(4)

    # Get Standings positions
    browser.find_element("xpath", "//button[text()='Standings']").click()
    time.sleep(4)

    home_standings = browser.find_element("css selector", f"[title^='{team_home}']") \
                    .find_element("xpath", './../../../..').find_element("css selector", '.tableCellRank').get_attribute('innerHTML').replace('.','')

    away_standings = browser.find_element("css selector", f"[title^='{team_away}']") \
                    .find_element("xpath", './../../../..').find_element("css selector", '.tableCellRank').get_attribute('innerHTML').replace('.','')

    last_list_positions = browser.find_elements("css selector", '.ui-table__row')[-1]

    tot_pos = last_list_positions.find_element("css selector", '.table__cell .tableCellRank').get_attribute('innerHTML').replace('.','')

    # Click H2H
    browser.find_element("xpath", "//button[text()='H2H']").click()
    time.sleep(3)

    # team_home - Home
    browser.find_element("xpath", f"//button[text()='{team_home} - Home']").click()
    time.sleep(3)

    # home first
    home_first = browser.find_element("css selector",'.h2h .h2h__row:first-child .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if home_first != ['']:
        home_first = home_first + home_first

    else:
        home_first = browser.find_element("css selector",'.h2h .h2h__row:first-child .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # home second
    home_second = browser.find_element("css selector",'.h2h .h2h__row:nth-child(2) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if home_second != ['']:
        home_second = home_second + home_second

    else:
        home_second = browser.find_element("css selector",'.h2h .h2h__row:nth-child(2) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # home third
    home_third = browser.find_element("css selector",'.h2h .h2h__row:nth-child(3) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if home_third != ['']:
        home_third = home_third + home_third

    else:
        home_third = browser.find_element("css selector",'.h2h .h2h__row:nth-child(3) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # home fourth
    home_fourth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(4) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if home_fourth != ['']:
        home_fourth = home_fourth + home_fourth

    else:
        home_fourth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(4) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # home fifth
    home_fifth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(5) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if home_fifth != ['']:
        home_fifth = home_fifth + home_fifth

    else:
        home_fifth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(5) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')


    # team_away - Away
    browser.find_element("xpath", f"//button[text()='{team_away} - Away']").click()
    time.sleep(3)

    # away first
    away_first = browser.find_element("css selector",'.h2h .h2h__row:first-child .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if away_first != ['']:
        away_first = away_first + away_first

    else:
        away_first = browser.find_element("css selector",'.h2h .h2h__row:first-child .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # away second
    away_second = browser.find_element("css selector",'.h2h .h2h__row:nth-child(2) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if away_second != ['']:
        away_second = away_second + away_second

    else:
        away_second = browser.find_element("css selector",'.h2h .h2h__row:nth-child(2) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # away third
    away_third = browser.find_element("css selector",'.h2h .h2h__row:nth-child(3) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if away_third != ['']:
        away_third = away_third + away_third

    else:
        away_third = browser.find_element("css selector",'.h2h .h2h__row:nth-child(3) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # away fourth
    away_fourth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(4) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if away_fourth != ['']:
        away_fourth = away_fourth + away_fourth

    else:
        away_fourth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(4) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # away fifth
    away_fifth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(5) .h2h__result__fulltime .h2h__regularTimeResult') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')
    if away_fifth != ['']:
        away_fifth = away_fifth + away_fifth

    else:
        away_fifth = browser.find_element("css selector",'.h2h .h2h__row:nth-child(5) .h2h__result') \
                            .get_attribute('innerHTML').replace('</span><span>', ',') \
                            .replace('<span>', '').replace('</span>', '').split(',')

    # Date
    match_date = browser.find_element("xpath", '//*[@id="detail"]/div[4]/div[1]/div').get_attribute('innerHTML').split()[0]

    temp_df = {'Date': match_date,'TeamHome': team_home, 'TeamAway': team_away,
            'pos_home': home_standings, 'pos_away': away_standings, 'tot_pos': tot_pos,
            'home_1_h': home_first[0], 'home_1_a': home_first[1],
            'home_2_h': home_second[0], 'home_2_a': home_second[1],
            'home_3_h': home_third[0], 'home_3_a': home_third[1],
            'home_4_h': home_fourth[0], 'home_4_a': home_fourth[1],
            'home_5_h': home_fifth[0], 'home_5_a': home_fifth[1],
            'away_1_h': away_first[0], 'away_1_a': away_first[1],
            'away_2_h': away_second[0], 'away_2_a': away_second[1],
            'away_3_h': away_third[0], 'away_3_a': away_third[1],
            'away_4_h': away_fourth[0], 'away_4_a': away_fourth[1],
            'away_5_h': away_fifth[0], 'away_5_a': away_fifth[1]}

    df = pd.DataFrame([temp_df])

    df.to_csv(f'/Users/YOUR_USER/{DATE_NAME}_DATA.csv', mode='a')

    browser.close()

    time.sleep(2)
