sim_duration = 0
num_inters = 0
num_streets = 0
num_cars = 0
reward = 0
streets = {}
cars = []


def input(dataset_path):  
    global sim_duration, num_inters, num_streets, num_cars, reward, streets, cars
    with open(dataset_path) as infile:
        line = infile.readline()
        line = line.split()
        sim_duration = int(line[0])
        num_inters = int(line[1])
        num_streets = int(line[2])
        num_cars = int(line[3])
        reward = int(line[4])
        for i in range(0, num_streets):
            line = infile.readline()
            line = line.split()
            streets[line[2]] = {}
            streets[line[2]]["start"] = int(line[0])
            streets[line[2]]["end"] = int(line[1])
            streets[line[2]]["time"] = int(line[3])
        for i in range(0, num_cars):
            line = infile.readline()
            line = line.split()
            car = {}
            car["num"] = int(line[0])
            car["path"] = []
            for street_name in line[1:]:
                car["path"].append(street_name)
            cars.append(car)


def outin(dataset_path):
    sched = {}
    with open(dataset_path) as infile:
        num_int = infile.readline()
        num_int = num_int.strip()
        for i in range(int(num_int)):
            line = infile.readline()
            line = int(line.strip())
            # line = [l.strip() for l in line]
            sched[line] = {}

            line2 = infile.readline()
            line2 = int(line2.strip())

            for j in range(line2):
                line3 = infile.readline()
                line3 = line3.split(' ')
                line3 = [l.strip() for l in line3]
                sched[line][line3[0]] = int(line3[1])
    return sched

def eval(sched):
    for 


input('./a.txt')
print(eval(outin('./out.txt')))



