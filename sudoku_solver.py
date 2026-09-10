from typing import List, Optional, Tuple


def read_board(filename: str) -> List[List[int]]:
    """
    从文本文件读取数独。

    文件格式：
    每行 9 个数字，用空格分隔；
    0 表示空格。
    """
    board = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # 跳过空行
            if not line:
                continue

            row = list(map(int, line.split()))
            board.append(row)

    # 检查是否为 9×9
    if len(board) != 9:
        raise ValueError("数独必须有 9 行")

    for row in board:
        if len(row) != 9:
            raise ValueError("数独每一行必须有 9 个数字")

    return board


class SudokuSolver:
    def __init__(self, board: List[List[int]]):

        self.board = [row[:] for row in board]

        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        self._init_constraints()

    def _box_id(self, row: int, col: int) -> int:
        """计算某个格子属于哪个九宫格"""
        return (row // 3) * 3 + col // 3

    def _init_constraints(self):
        """初始化约束，并检查输入数独是否存在冲突"""

        for r in range(9):
            for c in range(9):

                num = self.board[r][c]

                # 0 表示空格
                if num == 0:
                    continue

                if num < 1 or num > 9:
                    raise ValueError(
                        f"非法数字：第 {r + 1} 行，第 {c + 1} 列"
                    )

                box = self._box_id(r, c)

                # 检查行、列、九宫格中是否存在重复数字
                if (
                    num in self.rows[r]
                    or num in self.cols[c]
                    or num in self.boxes[box]
                ):
                    raise ValueError(
                        f"初始数独存在冲突："
                        f"第 {r + 1} 行，第 {c + 1} 列，数字 {num}"
                    )

                self.rows[r].add(num)
                self.cols[c].add(num)
                self.boxes[box].add(num)

    def _get_candidates(self, row: int, col: int) -> set:
        """计算某个空格可以填写哪些数字"""

        box = self._box_id(row, col)

        used = (
            self.rows[row]
            | self.cols[col]
            | self.boxes[box]
        )

        return set(range(1, 10)) - used

    def _find_best_cell(self) -> Optional[Tuple[int, int, set]]:
        """
        找到候选数字最少的空格。
        """

        best = None
        min_candidates = 10

        for r in range(9):
            for c in range(9):

                # 已经填过的格子跳过
                if self.board[r][c] != 0:
                    continue

                candidates = self._get_candidates(r, c)

                # 没有任何候选数字，说明当前路径错误
                if len(candidates) == 0:
                    return r, c, candidates

                # 找候选数字最少的格子
                if len(candidates) < min_candidates:

                    min_candidates = len(candidates)
                    best = (r, c, candidates)

                    # 只有一个候选数字，不可能找到更优情况
                    if min_candidates == 1:
                        return best

        return best

    def _backtrack(self) -> bool:
        """使用回溯算法求解"""

        cell = self._find_best_cell()

        # 没有空格了，说明求解完成
        if cell is None:
            return True

        row, col, candidates = cell

        # 没有候选数字，说明当前选择错误
        if not candidates:
            return False

        box = self._box_id(row, col)

        # 尝试所有候选数字
        for num in sorted(candidates):

            # 填入数字
            self.board[row][col] = num

            self.rows[row].add(num)
            self.cols[col].add(num)
            self.boxes[box].add(num)

            # 递归解决剩余数独
            if self._backtrack():
                return True

            # 当前选择错误，撤销
            self.board[row][col] = 0

            self.rows[row].remove(num)
            self.cols[col].remove(num)
            self.boxes[box].remove(num)

        return False

    def solve(self) -> Optional[List[List[int]]]:
        """求解数独"""

        if self._backtrack():
            return self.board

        return None


def print_board(board: List[List[int]]):
    """打印数独"""

    for r in range(9):

        if r > 0 and r % 3 == 0:
            print("-" * 21)

        for c in range(9):

            if c > 0 and c % 3 == 0:
                print("|", end=" ")

            print(board[r][c], end=" ")

        print()


if __name__ == "__main__":

    # 从 sudoku.txt 读取数独
    board = read_board("sudoku.txt")

    print("输入的数独：")
    print_board(board)

    solver = SudokuSolver(board)

    result = solver.solve()

    if result is None:
        print("\n这个数独无解")
    else:
        print("\n求解结果：")
        print_board(result)