def hours_to_sec(hours):
    hours *= 60 * 60
    return hours

def time(sec):
    all = {
    "sec":sec % 60,
    "min":sec // 60 % 60,
    "h":sec // 60 // 60 % 24
    }
    return all

def clock(sec):
    main = time(sec)
    return f"{main['h']:02d}:{main['min']:02d}:{main['sec']:02d}"
def svetofor(g, y, r):
    import time
    import os

    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = '\033[33m'
    RESET = "\033[0;0m"

    start_g = g
    start_y = y
    start_r = r

    seconds_in_iteration = 0
    iter = 0
    circle = 0

    while circle != 1:
        if iter == 0:
            print(GREEN + str(g) + RESET + "\n")
            g -= 1
            if g == 0:
                iter = 1

        elif iter == 1:
            print(YELLOW + '~' + "\n")
            y -= 1
            if y == 0:
                iter = 2

        elif iter == 2:
            print(RED + str(r) + RESET + "\n")
            r -= 1
            if r == 0:
                iter = 0
                g = start_g
                y = start_y
                r = start_r
                circle+=1

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        seconds_in_iteration += 1

    return f"Seconds in one iteration: {seconds_in_iteration}"


def record(filename, title, data):
    import csv
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            existing_data = list(reader)
    except FileNotFoundError:
        existing_data = []
        
    existing_data.append([title])

    existing_data.extend(data)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(existing_data)





start = int(input('Write your starting hour: '))
end = int(input('Write your ending hour: '))
starting_hour = hours_to_sec(start)
ending_hour = hours_to_sec(end)

red_bb = 28    #seconds
green_bb = 31
yellow_bb = 3
t_iteration = red_bb + green_bb + yellow_bb



green_iter = []
yellow_iter = []
red_iter = []
iterations = 0
cur_time = starting_hour
while (time(cur_time))["h"] != end:
    start_g = cur_time
    cur_time += green_bb
    green_iter.append(clock(start_g) + " - " + clock(cur_time))
    start_y = cur_time
    cur_time += yellow_bb
    yellow_iter.append(clock(start_y) + " - " + clock(cur_time))
    start_r = cur_time
    cur_time += red_bb
    red_iter.append(clock(start_r) + " - " + clock(cur_time))
    iterations += 1

record("color.csv", "Green", green_iter)
record("color.csv", "Yellow", yellow_iter)
record("color.csv", "Red", red_iter)

with open("iterations.txt", 'w') as file:
    file.write(f"Amount of iterations from {start} to {end} is: {iterations}\n")

print(svetofor(green_bb, yellow_bb, red_bb))


green_iter = []
yellow_iter = []
red_iter = []
iterations = 0