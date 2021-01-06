#!/usr/bin/env node

import { readFileSync } from "fs";
import { resolve } from "path";
import { argv, exit } from "process";

if (argv.length < 3) {
  console.error(`Usage: node run.js day01`);
  exit(1);
}

const dayName = argv.slice(2)[0];
const dayInput = readFileSync(resolve(`input/${dayName}.txt`), "utf-8");
const { loadData, part1, part2 } = await import(resolve(`${dayName}.js`));

const data = loadData ? loadData(dayInput) : dayInput.split("\n");
console.log(part1(data));
console.log(part2(data));
