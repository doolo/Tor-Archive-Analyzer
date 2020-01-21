# Tor-Archive-Analyzer

## Usage

### Download and extract Tor consensus archive

``` bash
cd archive

# Download
bash -x download_archive.sh

# Extract
bash -x extract_one_consensus_per_month.sh
```

### Parse and join the ceonsensus

``` bash
# Extract consensus info 
python3.5 consensus_descriptor.py > output_consensus_descriptor.txt

# Extract server descriptor info
python3.5 server_descriptor.py > output_server_descriptor.txt

# Join GE bandwidth
python3.5 join_GE_bandwidth.py > GE_bandwidth.txt
```

## Dependencies

stem: https://stem.torproject.org/download.html
