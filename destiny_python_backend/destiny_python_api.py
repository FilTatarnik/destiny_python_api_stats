import requests
import pprint as pprint
import json
import config


    
def search_destiny_player():
    #----------------Asking user for Acc name via input()----------------
        print('Input your Bungie Acc name:')
    
    #----------------Getting Players Bungie account name----------------
        search_destiny_player_input = input()
    
    #----------------Printing user input----------------
        print('Searching for: ', search_destiny_player_input)
    
    #----------------Requests to get JSON data from Bungie API----------------
    
        #----------------Parsing through JSON object from Bungie API----------------
        #----------------Search For Player----------------
        # https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/...
        search_player = requests.get(f'https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/3/{search_destiny_player_input}', headers={"X-API-KEY": config.api_key})
        
        #----------------Display Name----------------
        display_name = search_player.json()['Response'][0]['displayName']
        #----------------Membership ID----------------
        membership_id = search_player.json()['Response'][0]['membershipId']
        
    #----------------Get Profile...Gets Bungie Account Info----------------
        get_profile = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{membership_id}/?components=100', headers={"X-API-KEY": config.api_key})
        #----------------Get Character Ids..Classes..Titan..Warlock..Hunter----------------
        character_ids = get_profile.json()['Response']['profile']['data']['characterIds']
        
        #----------------Get Specific Character Info----------------
        character_info = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{membership_id}/Character/{character_ids}/?components=200')
        #----------------Character Equipment----------------
        character_equipment = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Profile/{membership_id}/Character/2305843009300787626/?components=205')
        
    #----------------Get Destiny PVP Stats----------------
        #https://www.bungie.net/Platform/Destiny2/3/Account/4611686018467419826/Stats/
        get_stats = requests.get(f'https://www.bungie.net/Platform/Destiny2/3/Account/{membership_id}/Stats/', headers={"X-API-KEY": config.api_key})
    #----------------PVP Stats----------------
        #----------------Write a function that loops through the json object until the allTime and then print them out after that? I'm not sure. I just know that this what's going on below isn't efficient.----------------
        #----------------Total Kills----------------
        kills = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['kills']['basic']['displayValue']
        #----------------Kill Death Ratio----------------
        kd = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['killsDeathsRatio']['basic']['displayValue']
        #----------------Assists----------------
        assists = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['assists']['basic']['displayValue']
        #----------------Activities Entered----------------
        activities_entered = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['activitiesEntered']['basic']['displayValue']
        #----------------Activities Won----------------
        activities_won = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['activitiesWon']['basic']['displayValue']
        #----------------Average Kill Distance----------------
        average_kill_distance = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['averageKillDistance']['basic']['displayValue']
        #----------------Seconds Played----------------
        seconds_played = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['secondsPlayed']['basic']['displayValue']
        #----------------Deaths----------------
        deaths = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['deaths']['basic']['displayValue']
        #----------------Suicides----------------   
        suicides = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['suicides']['basic']['displayValue']
        #----------------Average Lifespan----------------
        average_lifespan = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['averageLifespan']['basic']['displayValue']
        #----------------Best Single Game Kills----------------
        best_single_game_kills = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['bestSingleGameKills']['basic']['displayValue']
        #----------------Resurrections Performed----------------
        resurections_performed = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['resurrectionsPerformed']['basic']['displayValue']
        #----------------Resurrections Recieved----------------
        resurrections_recieved = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['resurrectionsReceived']['basic']['displayValue']
        #----------------Score----------------
        score = get_stats.json()['Response']['mergedAllCharacters']['results']['allPvP']['allTime']['score']['basic']['displayValue']
        #----------------Assists----------------

        #----------------Activities Won Ratio Variable----------------
        activity_win_ratio = (int(activities_entered) / int(activities_won))
        
        #----------------Printing Bungie Data that was queried to command line----------------
        #----------------------------------------------------------------
        pprint.pprint('Your classes : ' + str(character_ids))
        #----------------------------------------------------------------
        pprint.pprint('The Bungie Account you searched for is: ' + str(display_name))
        pprint.pprint('Your Membership ID is: ' + str(membership_id))
        pprint.pprint('You have : ' + str(kills) + ' kills in total.')
        pprint.pprint('YOUR KD IS : ' + str(kd))
        pprint.pprint('Your score is : ' + str(score))
        pprint.pprint('You have : ' + str(assists) + ' assists.')
        pprint.pprint('Activities Entered is: ' + str(activities_entered))
        pprint.pprint('Activities Won is: ' + str(activities_won))
        pprint.pprint('Your Activity Win Ratio is: ' + str(activity_win_ratio))
        pprint.pprint('Your Average Kill Distance is : ' + str(average_kill_distance) + ' meters.')
        pprint.pprint('You have played : ' + str(seconds_played))
        pprint.pprint('You have died : ' + str(deaths) + ' times.')
        pprint.pprint('Your Average Lifespan in a Single Game is : ' + str(average_lifespan))
        pprint.pprint('Your Best Single Game Kill number is : ' + str(best_single_game_kills))
    #----------------Asking user if they'd like to get Class specific stats----------------
    

#----------------Running search player function----------------
search_destiny_player()

#Navigate to your folder where destiny_python_api.py is located and type it out. This will run the program.