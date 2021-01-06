export function part1(lines) {
  return lines.reduce((frequency, line) => frequency + Number(line), 0);
}

export function part2(lines) {
  let frequency = 0;
  const counts = { frequency: 1 };
  while (true) {
    for (const line of lines) {
      frequency += new Number(line);
      const count = (counts[frequency] || 0) + 1;
      if (count > 1) {
        return frequency;
      }
      counts[frequency] = count;
    }
  }
}
