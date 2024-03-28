#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and get the response body size in bytes
response_size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}')

# Display the response body size
echo "Response body size for $url: $response_size bytes"
