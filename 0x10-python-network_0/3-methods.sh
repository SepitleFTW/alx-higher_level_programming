#!/bin/bash
#display all http method of a given URL
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
