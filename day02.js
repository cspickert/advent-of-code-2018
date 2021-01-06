const fs = require("fs");
const path = require("path");

const lines = fs
  .readFileSync(path.resolve("input/day02.txt"), "utf-8")
  .split("\n");

const part1 = () => {
  const letterCounts = {};

  for (const line of lines) {
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
  }

  console.log(letterCounts[2] * letterCounts[3]);
};

const part2 = () => {
  const getDiff = (s1, s2) =>
    Array.from({ length: s1.length }, (_, i) => i).reduce(
      (diffs, i) => (s1[i] === s2[i] ? diffs : [...diffs, i]),
      []
    );

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

part1();
part2();
