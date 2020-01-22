import pprint

key_role_dict = dict()
# 016DD4428C2EF04B0E3B17FACAA7D8C2F325BFB0 2009-06-12 10:08:30 Guard
with open("output_consensus_descriptor.txt", "r") as ge:
    lines = ge.readlines()
    for line in lines:
        key, _, _, role = line.rstrip().rsplit(' ')
        if key not in key_role_dict:
            key_role_dict[key] = set()
        key_role_dict[key].add(role)

# B84480B20B37D7052B8A927AE942A811AA9F7975 2013-03-20 05:05:44 107.196.20.189 512000 716800 134144 []
with open("output_server_descriptor.txt", "r") as sd:
    lines = sd.readlines()
    for line in lines:
        key_value = line.rstrip().rsplit(' ')
        try:
            # min_bandwidth is the min of avg, burst and observed bandwidth
            min_bandwidth = min(int(key_value[4]), \
                                 int(key_value[5]), \
                                 int(key_value[6]))
        except ValueError:
            continue
    # pp = pprint.PrettyPrinter(indent=1)
    # pp.pprint(d)
        if key in key_role_dict:
            print("{} {} {}".format(' '.join(key_value), min_bandwidth, role))
        
