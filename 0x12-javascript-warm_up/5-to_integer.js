#!/usr/bin/node
import { argv } from 'node:process';

try
{
    let count = parseInt(argv[2])
    console.log(`My number:${count}`)
}catch
{
    console.log("Not a number")
}
