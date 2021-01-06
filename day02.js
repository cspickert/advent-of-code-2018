const fs = require("fs");
const path = require("path");
const readline = require("readline");

const getInputReader = () =>
  readline.createInterface({
    input: fs.createReadStream(path.resolve("input/day02.txt")),
  });

const part1 = () => {
  const letterCounts = {};
  getInputReader()
    .on("line", (line) => {
      const charCounts = line
        .split("")
        .reduce((counts, c) => ({ ...counts, [c]: (counts[c] || 0) + 1 }), {});
      const uniqueCharCounts = Object.entries(charCounts).reduce(
        (counts, [_, count]) => ({ ...counts, [count]: 1 }),
        {}
      );
      Object.entries(uniqueCharCounts).forEach(
        ([count, _]) => (letterCounts[count] = (letterCounts[count] || 0) + 1)
      );
    })
    .on("close", () => console.log(letterCounts[2] * letterCounts[3]));
};

const part2 = () => {
  const getDiff = (s1, s2) =>
    Array.from({ length: s1.length }, (_, i) => i).reduce(
      (diffs, i) => (s1[i] === s2[i] ? diffs : [...diffs, i]),
      []
    );

  const processLines = (lines) => {
    for (let i = 0; i < lines.length; i++) {
      for (let j = i + 1; j < lines.length; j++) {
        const [k, ...rest] = getDiff(lines[i], lines[j]);
        if (rest.length === 0) {
          console.log(lines[i].slice(0, k) + lines[i].slice(k + 1));
          break;
        }
      }
    }
  };

  const lines = [];
  getInputReader()
    .on("line", (line) => lines.push(line))
    .on("close", () => processLines(lines));
};

part1();
part2();
