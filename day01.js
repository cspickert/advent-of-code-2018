const fs = require("fs");
const path = require("path");
const readline = require("readline");

const getInputReader = () =>
  readline.createInterface({
    input: fs.createReadStream(path.resolve("input/day01.txt")),
  });

const part1 = () => {
  let frequency = 0;
  getInputReader()
    .on("line", (line) => {
      frequency += new Number(line);
    })
    .on("close", () => console.log(frequency));
};

const part2 = () => {
  let frequency = 0;
  const counts = { frequency: 1 };
  let done = false;
  const start = () => {
    const inputReader = getInputReader();
    inputReader
      .on("line", (line) => {
        frequency += new Number(line);
        const count = (counts[frequency] || 0) + 1;
        if (count > 1) {
          done = true;
          console.log(frequency);
          inputReader.close();
          inputReader.removeAllListeners();
        } else {
          counts[frequency] = count;
        }
      })
      .on("close", () => !done && start());
  };
  start();
};

part1();
part2();
