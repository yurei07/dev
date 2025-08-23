class cheessboard():
    
    n_rows = n_cols = 8 
    table = []

    for y in range(n_rows):
        row = []
        for x in range(n_cols):
            row.append((x + y + 1) % 2)
        table.append(row)

    for row in table:
       print(*row)
cheessboard()

class knight():
    def __init__(self) -> None:
        self.knight = knight

