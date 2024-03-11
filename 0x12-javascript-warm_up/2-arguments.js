#!/usr/bin/node
/*
this script will print a message
depending onb the number of arguments*/

const argCount = process.argv.length - 2;

if (argCount === 0) {
    console.log("No argument");
} else if (argCount === 1) {
    consol.log("Argument found");
} else {
    console.log("Arguments found");
}
