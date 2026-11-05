'''
Initialize a 2D list using the specified number of rows and columns.



Initialize every cell with EMPTY = -1.



Implement a method to retrieve a tile.



Implement a method to change a tile.



Implement a method to return the entire map.
'''
class MapData:
    EMPTY = -1
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.map = [[self.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
    def get_tile(self,row,col):
        return self.map[row][col]
    def set_tile(self,row,col,tile):
        # how to prevent index out of range error when setting a tile in the map
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        self.map[row][col] = tile
    def get_map(self):
        #prevent the map from being modified by returning a copy of the map
        return [row.copy() for row in self.map]
    
