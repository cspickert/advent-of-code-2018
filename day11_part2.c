#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * To compile:
 * $ clang -Ofast -o /tmp/day11 day11.c
 */

int getPowerLevel(int serialNumber, int x, int y)
{
  int rackId = x + 10;
  int powerLevel = rackId * y + serialNumber;
  powerLevel *= rackId;

  char str[10];
  sprintf(str, "%d", powerLevel / 100);

  int len = strlen(str);
  powerLevel = atoi(str + len - 1);

  return powerLevel - 5;
}

int getSum(int **grid, int minX, int minY, int size)
{
  int sum = 0;
  for (int x = minX; x < minX + size; x++)
  {
    for (int y = minY; y < minY + size; y++)
    {
      sum += grid[y][x];
    }
  }
  return sum;
}

int getMaxSum(int **grid, int size, int *outX, int *outY)
{
  int maxSum = 0;
  for (int y = 0; y < 300 - size; y++)
  {
    for (int x = 0; x < 300 - size; x++)
    {
      int sum = getSum(grid, x, y, size);
      if (sum > maxSum)
      {
        maxSum = sum;
        *outX = x;
        *outY = y;
      }
    }
  }
  return maxSum;
}

void initializeGrid(int **grid, int serialNumber)
{
  for (int x = 0; x < 300; x++)
  {
    for (int y = 0; y < 300; y++)
    {
      grid[y][x] = getPowerLevel(serialNumber, x, y);
    }
  }
}

int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    fprintf(stderr, "Usage: %s <serial_number>\n", argv[0]);
    return 1;
  }
  int **grid;
  grid = malloc(sizeof(int *) * 300);
  for (int row = 0; row < 300; row++)
  {
    grid[row] = malloc(sizeof(int) * 300);
  }
  initializeGrid(grid, atoi(argv[1]));
  int resultX = 0;
  int resultY = 0;
  int maxSum = 0;
  int maxSize = 0;
  for (int size = 1; size <= 300; size++)
  {
    int x = 0;
    int y = 0;
    int sum = getMaxSum(grid, size, &x, &y);
    if (sum > maxSum)
    {
      resultX = x;
      resultY = y;
      maxSum = sum;
      maxSize = size;
    }
  }
  for (int row = 0; row < 300; row++)
  {
    free(grid[row]);
  }
  free(grid);
  printf("%d,%d,%d\n", resultX, resultY, maxSize);
  return 0;
}
