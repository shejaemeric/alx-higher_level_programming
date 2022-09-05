#!/usr/bin/node
import { argv } from 'node:process';

try
{
    let arg = parseInt(argv[2])
}catch{
    console.log('Missing size')
}

for(let x=0;x<arg;x++)
{
    for(let y=0;y<arg;y++)
    {
        console.log("X")
    }
    console.log('\n')
}
