dataset_path = './a.txt'

sim_duration = 0
num_inters = 0
num_streets = 0
num_cars = 0
reward = 0

streets = {}
cars = []


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


print(streets)
print(cars)
