class ForLoop:

    @staticmethod
    def printFootballTeams(teams):
        for team in teams:
            print(team)

    @staticmethod
    def splitNames(nameStr):
        names = nameStr.split('-')
        for name in names:
            print(name)

    @staticmethod
    def printSubArray(nameStr):
        names = nameStr.split('-')
        for name in names[1:4]:
            print(name)               

    @staticmethod
    def conditionalLoop(teamArray):
        teams = teamArray.split('-')
        afcEast = ['Buffalo Bills','New York Jets','Miami Dolphins','New England Patriots']
        for team in teams:
            if team in afcEast:
                print('AFC East {}'.format(team))
            else:
                print('Others: {}'.format(team))    


#ForLoop.printFootballTeams(['New England Patriots','Golden State Warriots','49Ers'])
ForLoop.conditionalLoop('New England Patriots-Golden State Warriots-49Ers-Packers-Celtics')            