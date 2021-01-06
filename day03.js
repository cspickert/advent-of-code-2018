const fs = require("fs");
const path = require("path");
const readline = require("readline");

const LINE_RE = /^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$/;

const getInputReader = () =>
  readline.createInterface({
    input: fs.createReadStream(path.resolve("input/day03.txt")),
  });

const forEachLocation = (startX, startY, w, h, callback) => {
  for (let x = startX; x < startX + w; x++) {
    for (let y = startY; y < startY + h; y++) {
      callback(x + "," + y);
    }
  }
};

const part1 = () => {
  const covered = {};

  getInputReader()
    .on("line", (line) => {
      const match = LINE_RE.exec(line);
      const [_line, _id, startX, startY, w, h] = match.map(Number);
      forEachLocation(startX, startY, w, h, (key) => {
        covered[key] = (covered[key] || 0) + 1;
      });
    })
    .on("close", () => {
      const result = Object.entries(covered).reduce(
        (count, [_, v]) => (v > 1 ? count + 1 : count),
        0
      );
      console.log(result);
    });
};

const part2 = () => {
  const claims = [];
  const claimLocations = {};

  getInputReader()
    .on("line", (line) => {
      const match = LINE_RE.exec(line);
      const [_, id, startX, startY, w, h] = match.map(Number);
      claims.push([id, startX, startY, w, h]);
      forEachLocation(startX, startY, w, h, (key) => {
        claimLocations[key] = (claimLocations[key] || []).concat([id]);
      });
    })
    .on("close", () => {
      for (const [id, startX, startY, w, h] of claims) {
        let unique = true;
        forEachLocation(startX, startY, w, h, (key) => {
          const claimsAtLocation = claimLocations[key];
          unique =
            unique &&
            claimsAtLocation.length === 1 &&
            claimsAtLocation[0] === id;
        });
        if (unique) {
          console.log(id);
          break;
        }
      }
    });
};

part1();
part2();
