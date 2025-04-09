def print_board(board):
    """Выводит игровое поле с нумерацией строк и столбцов."""
    print("  1 2 3")  # Заголовок столбцов
    for i, row in enumerate(board, start=1):
        print(i, " ".join(row))  # Вывод строки с нумерацией
    print()


def check_winner(board):
    """Проверяет, есть ли победитель. Возвращает символ победителя или None."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    """Проверяет, заполнено ли игровое поле."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Основная функция игры. Запрашивает имена игроков и запускает игровой процесс."""
    board = [[" "] * 3 for _ in range(3)]

    # Запрос имен игроков
    player1_name = input("Введите имя первого игрока (X): ")
    player2_name = input("Введите имя второго игрока (O): ")

    players = {"X": player1_name, "O": player2_name}
    player = "X"

    while True:
        print_board(board)

        try:
            row, col = map(int, input(f"{players[player]}, введите номер строки и столбца (1-3): ").split())
            if row not in (1, 2, 3) or col not in (1, 2, 3):
                print("Некорректный ввод! Введите числа от 1 до 3.")
                continue

            row -= 1  # Приведение номера строки к индексу (0-2)
            col -= 1  # Приведение номера столбца к индексу (0-2)

            if board[row][col] != " ":
                print("Ячейка уже занята! Попробуйте снова.")
                continue

            board[row][col] = player  # Запись хода игрока
        except ValueError:
            print("Некорректный ввод! Введите два числа, разделенные пробелом.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{players[winner]} победил!")
            break

        if is_full(board):
            print_board(board)
            print("Ничья!")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe()
