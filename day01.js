const fs = require("fs");
const path = require("path");

const lines = fs
  .readFileSync(path.resolve("input/day01.txt"), "utf-8")
  .split("\n");

const part1 = () =>
  console.log(lines.reduce((frequency, line) => frequency + Number(line), 0));

const part2 = () => {
  let frequency = 0;
  const counts = { frequency: 1 };
  let done = false;

  while (!done) {
    for (const line of lines) {
      frequency += new Number(line);
      const count = (counts[frequency] || 0) + 1;
      if (count > 1) {
        done = true;
        break;
      }
      counts[frequency] = count;
    }
  }

  console.log(frequency);
};

part1();
part2();
