const LINE_RE = /^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$/;

const forEachLocation = (startX, startY, w, h, callback) => {
  for (let x = startX; x < startX + w; x++) {
    for (let y = startY; y < startY + h; y++) {
      callback([x, y].join(","));
    }
  }
};

export function part1(lines) {
  const covered = {};

  for (const line of lines) {
    const match = LINE_RE.exec(line);
    const [startX, startY, w, h] = match.slice(2).map(Number);
    forEachLocation(startX, startY, w, h, (key) => {
      covered[key] = (covered[key] || 0) + 1;
    });
  }

  return Object.entries(covered).reduce(
    (count, [_, v]) => (v > 1 ? count + 1 : count),
    0
  );
}

export function part2(lines) {
  const claims = [];
  const claimLocations = {};

  for (const line of lines) {
    const match = LINE_RE.exec(line);
    const [id, startX, startY, w, h] = match.slice(1).map(Number);
    claims.push([id, startX, startY, w, h]);
    forEachLocation(startX, startY, w, h, (key) => {
      claimLocations[key] = (claimLocations[key] || []).concat([id]);
    });
  }

  for (const [id, startX, startY, w, h] of claims) {
    let unique = true;
    forEachLocation(startX, startY, w, h, (key) => {
      unique =
        unique &&
        claimLocations[key].length === 1 &&
        claimLocations[key][0] === id;
    });
    if (unique) {
      return id;
    }
  }
}
