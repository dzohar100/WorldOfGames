# The method gets the points the user got, open the score file and add the score to the current score in the file.
def add_score(points):
    try:
        file = open("/Users/DorZohar 1/PycharmProjects/WorldOfGames/Scores.txt", "r+", encoding='utf-8')
        value_as_int = 0
        for line in file:
            splitted_line = line.split(' ')
            for values in splitted_line:
                value_as_int = int(values)
        result = value_as_int + points
        file.seek(0)
        file.write(str(result))
        print(result)
        file.close()
    except IOError:
        print("Couldn't reach file...")