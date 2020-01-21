from stem.descriptor.reader import DescriptorReader
import stem.descriptor.remote

my_descriptors = [
    #'./archive/server-descriptors/server-descriptors-2018-02.tar.xz',
    './archive/server-descriptors/',
]

# try:
#     processed_files = load_processed_files('/home/user/research/consensus/consensuses/server-descriptors/used_descriptors')
#     reader.set_processed_files(processed_files)
# except:
#     pass # could not load, maybe this is the first run

#start_time = time.time()

with DescriptorReader(my_descriptors) as reader:
    for descriptor in reader:
        # print(descriptor)
        # for all attributes: https://stem.torproject.org/api/descriptor/server_descriptor.html
        # nickname (str) -- * relay's nickname
        # fingerprint (str) -- identity key fingerprint
        # published (datetime) -- * time in UTC when this descriptor was made
        # address (str) -- * IPv4 address of the relay
        # average_bandwidth (int) -- * average rate it's willing to relay in bytes/s
        # burst_bandwidth (int) -- * burst rate it's willing to relay in bytes/s
        # observed_bandwidth (int) -- * estimated capacity based on usage in bytes/s
        # total_bw += min(desc.average_bandwidth, desc.burst_bandwidth, desc.observed_bandwidth)
        # or_addresses (list) -- * alternative for our address/or_port attributes, each entry is a tuple of the form (address (str), port (int), is_ipv6 (bool))

#        if len(descriptor.or_addresses) == 0:
#            continue
        
        IPv6 = []
        for address in descriptor.or_addresses:
            if address[2] is True:
                IPv6.append(address[0])

        print(descriptor.fingerprint, \
              descriptor.published, \
              descriptor.address, \
              descriptor.average_bandwidth, \
              descriptor.burst_bandwidth, \
              descriptor.observed_bandwidth, \
              IPv6)

#reader.save_processed_files('/home/user/research/consensus/consensuses/server-descriptors/used_descriptors', reader.get_processed_files())

