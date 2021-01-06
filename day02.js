export function part1(lines) {
  const letterCounts = {};

  for (const line of lines) {
    const charCounts = line
      .split("")
      .reduce((counts, c) => ({ ...counts, [c]: (counts[c] || 0) + 1 }), {});
    const uniqueCharCounts = Object.entries(charCounts).reduce(
      (counts, [_, count]) => ({ ...counts, [count]: 1 }),
      {}
    );
    for (const [count, _] of Object.entries(uniqueCharCounts)) {
      letterCounts[count] = (letterCounts[count] || 0) + 1;
    }
  }

  return letterCounts[2] * letterCounts[3];
}

export function part2(lines) {
  const getDiff = (s1, s2) =>
    Array.from({ length: s1.length }, (_, i) => i).reduce(
      (diffs, i) => (s1[i] === s2[i] ? diffs : [...diffs, i]),
      []
    );

  for (let i = 0; i < lines.length; i++) {
    for (let j = i + 1; j < lines.length; j++) {
      const diff = getDiff(lines[i], lines[j]);
      if (diff.length === 1) {
        return lines[i].slice(0, diff[0]) + lines[i].slice(diff[0] + 1);
      }
    }
  }
}
