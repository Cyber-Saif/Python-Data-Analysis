#8th December 2021
def data_analysis():
    file = open("green vancouver.txt")
    total = []
    green_buildings = []
    no_websites = ''
    areas = []
    bikes = []
    
    #this for loop is collecting all the data from the file and spliting them by ';' and
    #stripping out unwanted things like ""or'' and \n from the areas
    for data in file:
        lines = data.split(';')
        for i in range(len(lines)):
            lines[i] = lines[i].strip('""\n')
        total.append(lines)
       
    #this for loop is accessing elements in data which were collected by first for loop
    for j in total:
        #this if statement is extracting Green buildings projects which are in Downtown
        if j[3] == "Green-Buildings":
            if j[10] == "Downtown":
                if len(j[10]) not in green_buildings:
                    green_buildings.append(len(j[10]))
        #this statement is checking which projects does not have website 1 and 2
        if j[5] and j[6] == '':
            no_websites+=j[3]

        #making a list of projects which has 'bike' word in it
        if "Bike" in j[1]:
            if j[1] not in bikes:
                bikes.append(j[1])
        
        #in the end collecting all of local areas 
        if j[10] not in areas:
            areas.append(j[10])
    
    
    print(f'1. ** There are total {green_buildings} Green-Buildings projects in Downtown **\n')
    print(f'2. |  {no_websites} projects does not have 1st and 2nd websites |\n')
    print('3. "projects which contain bike"', *bikes, sep ="\n")
    print('\n 4. Local areas\n',areas)
    
    
        
data_analysis()
