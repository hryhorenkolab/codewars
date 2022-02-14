#Function that takes list collection and counts the points of team in the championship
def points(games):
    count = 0
    for score in games:
        res=score.split(':')
        if res[0]==res[1]:
            count +=1
        elif res[0]>res[1]:
            count +=3
        else:
            count +=0
    return count
