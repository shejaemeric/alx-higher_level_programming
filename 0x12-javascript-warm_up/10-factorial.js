#!/usr/bin/node
import { argv } from 'node:process';

function fact(n)
{
    return n*factorial(n-1)
}
let n = parseInt(argv[0])
console.log(fact(n))