import math
def solution(a, b):
    hrA, minA = map(int, a.split(":"))  # Convert split parts to integers
    hrB, minB = map(int, b.split(":"))
    if hrB < hrA: #means they played overnight
        hrB += 24

    remainder = minA % 15
    if remainder != 0:
        minA = minA + (15 -remainder) #find next possible starting time
    start = hrA* 60 + minA
    stop = hrB * 60 + minB
    total = stop - start #total time the player was online
    games = math.floor(total/ 15) #maximum games possible
    return games
print(solution("20:00", "06:00")) 