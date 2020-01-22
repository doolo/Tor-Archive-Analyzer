# Tor-Archive-Analyzer

## Usage

### Download and extract Tor consensus archive

``` bash
cd archive

# Download
bash -x download_archive.sh

# Extract
bash -x extract_one_consensus_per_day.sh
```

### Parse and join the consensus

``` bash
# Extract consensus info 
python3.5 consensus_descriptor.py > output_consensus_descriptor.txt

# Extract server descriptor info
python3.5 server_descriptor.py > output_server_descriptor.txt

# Join GE bandwidth
python3.5 join_GE_bandwidth.py > GE_bandwidth.txt
```

### Output

The final output is in GE_bandwidth.txt:

	ID Date Time IPv4 Average_Bandwidth Burst_Bandwidth Observed_Bandwidth IPv6 Min_Bandwidth Role
	B28AE4CEF59F492765E0938A8AA500C6D6DA42F2 2015-12-06 15:37:01 104.131.28.54 153600 307200 119808 ['2604:a880:800:10::53:b001'] 119808 Guard

## Dependencies

stem: https://stem.torproject.org/download.html
