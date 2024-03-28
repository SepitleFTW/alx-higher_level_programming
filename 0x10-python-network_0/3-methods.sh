#!/bin/bash
#display all http method of a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
