#!/bin/bash

# download consensuses
wget --recursive --no-parent -nH --cut-dirs=2 https://collector.torproject.org/archive/relay-descriptors/consensuses/

# download server-descriptors
wget --recursive --no-parent -nH --cut-dirs=2 https://collector.torproject.org/archive/relay-descriptors/server-descriptors/
