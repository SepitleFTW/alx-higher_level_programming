#!/bin/bash
#get byte size of a specific or desired URL
curl -s "$1" | wc -c
