#!/usr/bin/node
import { argv } from 'node:process';

function add(a, b){
    return a+b
}

let a = parseInt(argv[2])
let b = parseInt(argv[3])

console.log(add(a, b))
