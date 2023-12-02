from input import parse_buses, buses, sbuses, timestamp, stimestamp, buses2, sbuses2

# part1


def find_time(timestamp, buses):
    buses = dict(zip([int(bus) for bus in buses], [int(bus) for bus in buses]))
    while any(time < timestamp for time in buses.values()):
        for bus, time in buses.items():
            if time < timestamp:
                buses[bus] += bus
    bus, time = min(buses.items(), key=lambda pair: pair[1])
    print(buses)
    return (time-timestamp)*bus


def part2(buses):
    """buses = List[Tuple[str,int]], (bus#,offset)"""
    timetable = {bus: 100000000000000 for bus in [pair[0] for pair in buses]}
    timestamp = 100000000000000
    found = False
    while not found:
        print(timetable)
        for bus in buses:
            bus_no = bus[0]
            while timetable[bus_no] < timestamp:
                timetable[bus_no] += int(bus_no)
            if timetable[bus_no] != timestamp+bus[1]:
                timestamp += int(buses[0][0])
                break
        if all(timetable[bus[0]] == timestamp+bus[1] for bus in buses):
            found = True
    return timetable


def ft(buses, start, step=1):
    g = start
    found = False
    while not found:
        print(g)
        if all((g+bus[1]) % int(bus[0]) == 0 for bus in buses):
            found = True
        else:
            g = g+step
    return g


sbuses2 = [(int(pair[0]), pair[1]) for pair in sbuses2]
buses2 = [(int(pair[0]), pair[1]) for pair in buses2]


# this version actually runs quickly, ~175μs, unlike the brute force versions above
def part22(buses):
    """buses = List[Tuple[int,int]], (bus#,offset)"""
    lcm = 1
    time = 0
    for i in range(len(buses)-1):
        bus_no = buses[i+1][0]
        offset = buses[i+1][1]
        lcm *= buses[i][0]
        while (time + offset) % bus_no != 0:
            time += lcm
    return time
