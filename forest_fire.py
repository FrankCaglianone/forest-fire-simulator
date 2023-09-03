import random
import time

# start the simulation initialize all prob and create canvas
def start():
    # ----- CREATE THE GRID --------
    A1: I30.set_background_color(38, 194, 129)

    # ------ GET MAIN 4 FACTORS ------
    # rain; in mm/h ; + rain - probability
    rain = random.randint(1, 6)
    rainString = str(rain)
    K4 = "Rain is : " + rainString
    # humidity; in % ; + humi - probability
    humidity = random.randint(1, 100)
    humiString = str(humidity)
    K5 = "Humidity is : " + humiString
    # temperature; in celsius ; + temp + probability
    temperature = random.randint(1, 40)
    tempString = str(temperature)
    K6 = "Temperature is :" + tempString
    # wind; in km/h ; + wind + probability
    wind = random.randint(1, 61)
    windString = str(wind)
    k7 = "Wind is : " + windString
    # wind direction
    windDirection = windDir()
    K8 = "Wind directions is " + windDirection
    # flammability depending on the tree type
    flammability = tree_flammability()
    strFlam = str(flammability)
    K9 = "Tree flammability is: " + strFlam

    # ------ CALCULATE THE PROBABILITIES ------
    # ~ spread
    p_spread = temperature * wind / rain / humidity
    strSpread = str(p_spread)
    K13 = "p_spread is: " + strSpread
    spread_time = 1 / p_spread
    sprtime_str = str(spread_time)
    K16 = "Spreading time is: " + sprtime_str
    # ~ out
    p_out = tree_flammability()
    strOut = str(p_out)
    K14 = "p_out is: " + strOut
    timeOut = 1 / p_out
    timeOut_str = str(timeOut)
    K17 = "Burning time is: " + timeOut_str

    # ----- PICK RANDOM TREE TO SET ON FIRE ------
    tree0 = E15
    tree0.set_background_color(255, 0, 0)

    # -------- START THE TIMER -------
    timer(tree0, windDirection)


# reset the game
def reset():
    A1: I30.set_background_color(38, 194, 129)


# Create timer and burn the trees
def timer(cell, dir):
    t = 0
    cell.set_background_color(100, 0, 0)
    if dir == "north":
            for x in range(t, 5):
                for row in E1:E15:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)
    elif dir == "south":
        for x in range(t, 5):
                for row in E30:E15:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)
    elif dir == "north-east":
        for x in range(t, 5):
                for row in I1:F15:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)
    elif dir == "north-ovest":
        for x in range(t, 5):
                for row in A1:D15:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)
    elif dir == "south-east":
        for x in range(t, 5):
                for row in F15:I30:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)
    else:
        for x in range(t, 5):
                for row in D15:A30:
                    t += 1
                    timer = str(t)
                    K11 = "TIMER: " + timer
                    row.set_background_color(100, 0, 0)
                    time.sleep(1)


# random wind direction
def windDir():
    x = random.randint(0, 6)
    if x == 0:
        direction = "north"
    elif x == 1:
        direction = "south"
    elif x == 2:
        direction = "north-east"
    elif x == 3:
        direction = "north-ovest"
    elif x == 4:
        direction = "south-east"
    else:
        direction = "south-ovest"
    return direction


# random tree type
def tree_flammability():
    x = random.randint(0, 3)
    # "single-stem" # high flammability
    if x == 0:
        flamma = random.randint(76, 100)
    # "cluster"  # medium-high flammability
    elif x == 1:
        flamma = random.randint(51, 75)
    # "stand" # medium flammability
    elif x == 2:
        flamma = random.randint(26, 50)
    # "woodland" # low flammability
    else:
        flamma = random.randint(1, 25)
    return flamma