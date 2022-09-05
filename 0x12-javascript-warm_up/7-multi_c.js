#!/usr/bin/node
import { argv } from 'node:process';

try
{
    let arg = parseInt(argv[2])
}catch{
    console.log('Missing number of occurrences')
}

for(let x=0; x<=arg; x++)
{
    console.log("C is fun\n")
}
