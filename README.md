# Suduko 9×9 Solver

A simple Sudoku solver written in Python using the backtracking algorithm.

The program reads a Sudoku puzzle from a text file, validates the input, and automatically finds a solution.

---

## Features

* Read a Sudoku puzzle from `sudoku.txt`
* Validate the input puzzle
* Solve Sudoku using a backtracking algorithm
* Choose the cell with the fewest candidates first to improve efficiency
* Display the original puzzle and the solved puzzle in the terminal
* No third-party libraries required

---

## Project Structure

```text
.
├── sudoku_solver.py
└── sudoku.txt
```

* `sudoku_solver.py`: Sudoku solver program
* `sudoku.txt`: Input Sudoku puzzle

---

## Input Format

The input file should contain a $9\times9$ Sudoku puzzle.

Here, $9\times9$ means that the Sudoku board contains 9 rows and 9 columns.

Each row should contain 9 numbers separated by spaces.

Use `0` to represent an empty cell.

Example:

```text
0 0 0 5 0 2 0 0 1
1 0 7 0 0 0 0 9 0
6 9 0 0 0 8 5 0 0
5 0 1 8 4 0 0 0 0
0 0 6 0 7 0 0 8 0
0 4 0 0 0 0 1 5 0
0 0 0 4 8 1 0 0 5
4 0 3 0 0 0 0 0 9
0 1 0 0 0 6 8 0 0
```

---

## Usage

Make sure Python 3 is installed.

Run the following command in the project directory:

```bash
python sudoku_solver.py
```

The program will first display the input Sudoku puzzle and then print the solution.

---

## Algorithm

This project uses a **backtracking algorithm** to solve Sudoku.

For each empty cell, the program calculates all possible candidate numbers according to the current row, column, and $3\times3$ box.

Here, $3\times3$ represents one of the nine sub-grids in a standard Sudoku board.

To reduce unnecessary searches, the solver chooses the empty cell with the fewest candidate numbers first.

If a candidate causes a conflict, the program restores the previous state and tries another candidate until a solution is found.

---

## Requirements

* Python 3
* No third-party libraries required

---

## License

This project is created for learning and practice.

---

# 数独求解器

这是一个使用 Python 编写的简单数独求解器，采用回溯算法自动完成数独求解。

程序会从文本文件中读取数独，检查输入是否合法，并自动寻找数独的解。

---

## 功能

* 从 `sudoku.txt` 文件读取数独
* 自动检查输入的数独是否合法
* 使用回溯算法求解数独
* 优先选择候选数字最少的空格，提高搜索效率
* 在终端显示原始数独和求解结果
* 无需安装第三方库

---

## 项目结构

```text
.
├── sudoku_solver.py
└── sudoku.txt
```

* `sudoku_solver.py`：数独求解程序
* `sudoku.txt`：待求解的数独文件

---

## 输入格式

输入文件需要包含一个 $9\times9$ 的数独。

其中， $9\times9$ 表示数独包含 9 行和 9 列。

每一行包含 9 个数字，并使用空格分隔。

使用 `0` 表示空格。

示例：

```text
0 0 0 5 0 2 0 0 1
1 0 7 0 0 0 0 9 0
6 9 0 0 0 8 5 0 0
5 0 1 8 4 0 0 0 0
0 0 6 0 7 0 0 8 0
0 4 0 0 0 0 1 5 0
0 0 0 4 8 1 0 0 5
4 0 3 0 0 0 0 0 9
0 1 0 0 0 6 8 0 0
```

---

## 使用方法

首先确保电脑已经安装 Python 3。

然后在项目目录中运行：

```bash
python sudoku_solver.py
```

程序会首先显示输入的数独，然后输出求解结果。

---

## 算法

本项目使用**回溯算法**求解数独。

对于每一个空格，程序会根据当前所在的行、列以及 $3\times3$ 九宫格计算所有可以填写的候选数字。

其中， $3\times3$ 表示标准数独中的一个九宫格区域，即 3 行和 3 列组成的子区域。

为了减少不必要的搜索，程序会优先选择候选数字最少的空格进行尝试。

如果当前填写的数字导致冲突，程序会撤销当前选择，并继续尝试其他候选数字，直到找到一个完整的解。

---

## 环境要求

* Python 3
* 无需安装第三方库

---

## 许可证

本项目主要用于学习和练习。
