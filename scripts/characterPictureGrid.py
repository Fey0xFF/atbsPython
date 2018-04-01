# print grid function
def printGrid(grid):
  for index in grid:
    concatString = ''  
    for item in index:
      concatString += str(item)
    print(concatString)

# pass a list to be drawn into a grid of '.'
def drawGrid(drawnGrid):
  for x in range(0,6,1):
    drawnGrid.insert(x,[])
    for y in range(0,9,1):
      drawnGrid[x].insert(y,'.')
  printGrid(drawnGrid)
  return drawnGrid

# change grid to a heart with '0's
def heartPrinter(rawGrid):
  # 1st row
  rawGrid[0][2] = '0'
  rawGrid[0][3] = '0'
  rawGrid[0][5] = '0'
  rawGrid[0][6] = '0'
  
  # 2nd row
  rawGrid[1][1] = '0'
  rawGrid[1][2] = '0'
  rawGrid[1][3] = '0'
  rawGrid[1][4] = '0'
  rawGrid[1][5] = '0'
  rawGrid[1][6] = '0'
  rawGrid[1][7] = '0'
  
  # 3rd row
  rawGrid[2][1] = '0'
  rawGrid[2][2] = '0'
  rawGrid[2][3] = '0'
  rawGrid[2][4] = '0'
  rawGrid[2][5] = '0'
  rawGrid[2][6] = '0'
  rawGrid[2][7] = '0'
  
  # 4th row
  rawGrid[3][2] = '0'
  rawGrid[3][3] = '0'
  rawGrid[3][4] = '0'
  rawGrid[3][5] = '0'
  rawGrid[3][6] = '0'
  
  # 5th row
  rawGrid[4][3] = '0'
  rawGrid[4][4] = '0'
  rawGrid[4][5] = '0'
  
  # 6th row
  rawGrid[5][4] = '0'

def main():
  grid = []
  grid = drawGrid(grid)
  print('\n\n\n...building heart\n\n\n')
  heartPrinter(grid)
  printGrid(grid)
  
main()  