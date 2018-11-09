import pprint

d = dict()

with open("14_15_server_descriptors.txt", "r") as sd:
    lines = sd.readlines()
    for line in lines:
        key_value = line.rstrip().rsplit(' ', 4)
        try:
            # real_bandwidth is the min of avg, burst and observed bandwidth
            real_bandwidth = min(int(key_value[2]), \
                                 int(key_value[3]), \
                                 int(key_value[4]))
            d[key_value[0]] = key_value[1:]
        except ValueError:
            continue
        d[key_value[0]].append(str(real_bandwidth))
    # pp = pprint.PrettyPrinter(indent=1)        
    # pp.pprint(d)

with open("GE.txt", "r") as ge:
    lines = ge.readlines()
    for line in lines:
        key_value = line.rstrip().rsplit(' ', 1)
        key = key_value[0]
        role = key_value[1]
        if key in d:
            print("{} {} {}".format( key , ' '.join(map(str, d[key])), role))

