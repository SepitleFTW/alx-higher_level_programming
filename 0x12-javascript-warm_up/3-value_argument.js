#!/usr/bin/node

/*
this script will print the first argument passed to it
 */

const arg = process.argv[2];

if (arg === undefined) {
    console.log("no argument");
} else {
    console.log(arg);
}

