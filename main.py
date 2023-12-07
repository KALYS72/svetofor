
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

def record(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + '\n')

start = int(input('Write your starting hour: '))
end = int(input('Write your ending hour: '))
starting_hour = hours_to_sec(start)
ending_hour = hours_to_sec(end)

red_bb = 31          #seconds
green_bb =  28   
yellow_bb = 4
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

record("green.txt", green_iter)
record("yellow.txt", yellow_iter)
record("red.txt", red_iter)

with open("iterations.txt", 'w') as file:
    file.write(f"Amount of iterations from {start} to {end} is: {iterations}\n")

green_iter = []
yellow_iter = []
red_iter = []
iterations = 0