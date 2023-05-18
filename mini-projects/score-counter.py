teams={
    "group_one":["arg", "aus", "usa"],
    "group_two":["nep", "uk", "ind"],
    "group_three":["jpn", "pak", "slk"],
    "group_four":["can", "esp", "ger"]
}

team_score={
    "nep":[1, 4, 7, 5, 8],
    "uk":[2, 5, 4, 8, 6],
    "ind":[1, 5, 3, 8, 10]
}

user_details=["admin", "12345"]

def groupDetails(group_name):
    if group_name=="group_one":
        return teams[group_name]
    elif group_name=="group_two":
        return teams[group_name]
    elif group_name=="group_three":
        return teams[group_name]
    elif group_name=="group_four":
        return teams[group_name]
    else:
        return None
    
def calculateScore(team_name):
    data=team_score[team_name]
    counter=0
    for val in data:
        counter+=val
    return counter

def teamDetails(group_name, team_name):
    groups=groupDetails(group_name)
    if groups == None:
        print("Invalid details")
    else:   
        for data in groups:
            if team_name==data:
                print("Total score is ",calculateScore(team_name))
                break
        else:
            print("No match found")

def validateLogin():
    username=input("Enter username: ")
    code=input("Enter password: ")
    if username==user_details[0] and code==user_details[1]:
        group_name=input("Enter group name: ")
        team_name=input("Enter team name: ")
        teamDetails(group_name, team_name)
    else:
        print("invalid login credentials")
        validateLogin()

validateLogin()