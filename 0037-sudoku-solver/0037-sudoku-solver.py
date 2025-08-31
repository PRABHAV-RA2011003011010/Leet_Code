from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cells = set()
        emptycells = []

        # build constraints
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cells.add((i, board[i][j]))              # row constraint
                    cells.add((board[i][j], j))              # col constraint
                    cells.add((i // 3, j // 3, board[i][j])) # box constraint
                else:
                    emptycells.append((i, j))

        def backtrack() -> bool:
            if not emptycells:
                return True  # solved

            # --- MRV heuristic: choose cell with fewest valid options ---
            min_cell = min(
                emptycells,
                key=lambda pos: sum(
                    1 for d in map(str, range(1, 10))
                    if (pos[0], d) not in cells and (d, pos[1]) not in cells and (pos[0] // 3, pos[1] // 3, d) not in cells
                )
            )
            r, c = min_cell
            emptycells.remove(min_cell)

            # try possible digits
            for d in map(str, range(1, 10)):
                if (r, d) not in cells and (d, c) not in cells and (r // 3, c // 3, d) not in cells:
                    board[r][c] = d
                    cells.add((r, d))
                    cells.add((d, c))
                    cells.add((r // 3, c // 3, d))

                    if backtrack():
                        return True

                    # undo placement
                    board[r][c] = '.'
                    cells.remove((r, d))
                    cells.remove((d, c))
                    cells.remove((r // 3, c // 3, d))

            # backtrack: put cell back into empty list
            emptycells.append(min_cell)
            return False

        backtrack()




