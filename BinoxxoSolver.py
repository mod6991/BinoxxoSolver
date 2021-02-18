class Binoxxo:
    def __init__(self):
        self.gb = []
        for row_i in range(10):
            self.gb.append([])
            for col_i in range(10):
                self.gb[row_i].append(None)

    @staticmethod
    def get_opposite(val):
        if val == 'X':
            return 'O'
        return 'X'

    def get_row(self, row_i):
        return self.gb[row_i]

    def get_col(self, col_i):
        col = []
        for row in self.gb:
            col.append(row[col_i])
        return col

    def solve_surrounded(self):
        solved_anything = False

        solved_hor = self.solve_surrounded_hor()
        solved_ver = self.solve_surrounded_ver()

        if solved_hor or solved_ver:
            solved_anything = True

        return solved_anything

    def solve_surrounded_hor(self):
        solved_anything = False

        for row_i in range(10):
            for col_i in range(1, 9):
                cell_val = self.gb[row_i][col_i]
                left_val = self.gb[row_i][col_i - 1]
                right_val = self.gb[row_i][col_i + 1]
                if not cell_val and left_val and right_val:
                    if left_val == right_val:
                        self.gb[row_i][col_i] = Binoxxo.get_opposite(left_val)
                        print(f'({row_i}, {col_i}) was surrounded horizontally')
                        solved_anything = True

        return solved_anything

    def solve_surrounded_ver(self):
        solved_anything = False

        for row_i in range(1, 9):
            for col_i in range(10):
                cell_val = self.gb[row_i][col_i]
                left_val = self.gb[row_i - 1][col_i]
                right_val = self.gb[row_i + 1][col_i]
                if not cell_val and left_val and right_val:
                    if left_val == right_val:
                        self.gb[row_i][col_i] = Binoxxo.get_opposite(left_val)
                        print(f'({row_i}, {col_i}) was surrounded vertically')
                        solved_anything = True

        return solved_anything

    def solve_twins(self):
        solved_anything = False

        solved_hor = self.solve_twins_hor()
        solved_ver = self.solve_twins_ver()

        if solved_hor or solved_ver:
            solved_anything = True

        return solved_anything

    def solve_twins_hor(self):
        solved_anything = False

        for row_i in range(10):
            for col_i in range(1, 9):
                cell_val = self.gb[row_i][col_i]
                left_val = self.gb[row_i][col_i - 1]
                right_val = self.gb[row_i][col_i + 1]

                if cell_val and left_val and cell_val == left_val and not right_val:
                    self.gb[row_i][col_i + 1] = Binoxxo.get_opposite(cell_val)
                    print(f'({row_i}, {col_i + 1}) has twins on the left')
                    solved_anything = True
                elif cell_val and right_val and cell_val == right_val and not left_val:
                    self.gb[row_i][col_i - 1] = Binoxxo.get_opposite(cell_val)
                    print(f'({row_i}, {col_i - 1}) has twins on the right')
                    solved_anything = True

        return solved_anything

    def solve_twins_ver(self):
        solved_anything = False

        for row_i in range(1, 9):
            for col_i in range(10):
                cell_val = self.gb[row_i][col_i]
                top_val = self.gb[row_i - 1][col_i]
                bot_val = self.gb[row_i + 1][col_i]

                if cell_val and top_val and cell_val == top_val and not bot_val:
                    self.gb[row_i + 1][col_i] = Binoxxo.get_opposite(cell_val)
                    print(f'({row_i + 1}, {col_i}) has twins on the top')
                    solved_anything = True
                elif cell_val and bot_val and cell_val == bot_val and not top_val:
                    self.gb[row_i - 1][col_i] = Binoxxo.get_opposite(cell_val)
                    print(f'({row_i - 1}, {col_i}) has twins on the bottom')
                    solved_anything = True

        return solved_anything

    @staticmethod
    def count(lst):
        count_o, count_x = 0, 0
        for item in lst:
            if item == 'O':
                count_o += 1
            elif item == 'X':
                count_x += 1
        return count_o, count_x

    def solve_full(self):
        solved_anything = False

        solved_hor = self.solve_full_hor()
        solved_ver = self.solve_full_ver()

        if solved_hor or solved_ver:
            solved_anything = True

        return solved_anything

    def solve_full_hor(self):
        solved_anything = False

        for row_i in range(10):
            row = self.get_row(row_i)
            count_o, count_x = Binoxxo.count(row)

            if count_o == 5 and count_x < 5:
                for col_i in range(10):
                    if not self.gb[row_i][col_i]:
                        self.gb[row_i][col_i] = 'X'
                print(f'fill row {row_i} with X because 5 O were found')
                solved_anything = True

            if count_x == 5 and count_o < 5:
                for col_i in range(10):
                    if not self.gb[row_i][col_i]:
                        self.gb[row_i][col_i] = 'O'
                print(f'fill row {row_i} with O because 5 X were found')
                solved_anything = True

        return solved_anything

    def solve_full_ver(self):
        solved_anything = False

        for col_i in range(10):
            col = self.get_col(col_i)
            count_o, count_x = Binoxxo.count(col)

            if count_o == 5 and count_x < 5:
                for row_i in range(10):
                    if not self.gb[row_i][col_i]:
                        self.gb[row_i][col_i] = 'X'
                print(f'fill col {col_i} with X because 5 O were found')
                solved_anything = True

            if count_x == 5 and count_o < 5:
                for row_i in range(10):
                    if not self.gb[row_i][col_i]:
                        self.gb[row_i][col_i] = 'O'
                print(f'fill col {col_i} with O because 5 X were found')
                solved_anything = True

        return solved_anything

    @staticmethod
    def get_risk(lst, risk_val):
        risk_lst = []
        tmp_lst = []

        for i in range(10):
            item = lst[i]
            if not item or item == risk_val:
                if len(tmp_lst) == 3:
                    risk_lst.append(tmp_lst)
                    tmp_lst = [i]
                else:
                    tmp_lst.append(i)
            else:
                if tmp_lst:
                    risk_lst.append(tmp_lst)
                    tmp_lst = []

        if tmp_lst:
            risk_lst.append(tmp_lst)

        return risk_lst

    @staticmethod
    def is_risky(lst):
        for sub_lst in lst:
            if len(sub_lst) == 3:
                return True
        return False

    def solve_4lt4(self):
        solved_anything = False

        solved_hor = self.solve_4lt4_hor()
        solved_ver = self.solve_4lt4_ver()

        if solved_hor or solved_ver:
            solved_anything = True

        return solved_anything

    def solve_4lt4_hor(self):
        solved_anything = False

        for row_i in range(10):
            row = self.get_row(row_i)
            count_o, count_x = Binoxxo.count(row)

            if count_o == 4 and count_x < 4:
                lst = Binoxxo.get_risk(row, 'X')
                is_risky = Binoxxo.is_risky(lst)
                if is_risky:
                    for sub_lst in lst:
                        if len(sub_lst) < 3:
                            for col_i in sub_lst:
                                if not self.gb[row_i][col_i]:
                                    self.gb[row_i][col_i] = 'X'
                                    print(f'({row_i}, {col_i}) can only be X on the row')
                                    solved_anything = True

            elif count_x == 4 and count_o < 4:
                lst = Binoxxo.get_risk(row, 'O')
                is_risky = Binoxxo.is_risky(lst)
                if is_risky:
                    for sub_lst in lst:
                        if len(sub_lst) < 3:
                            for col_i in sub_lst:
                                if not self.gb[row_i][col_i]:
                                    self.gb[row_i][col_i] = 'O'
                                    print(f'({row_i}, {col_i}) can only be O on the row')
                                    solved_anything = True

        return solved_anything

    def solve_4lt4_ver(self):
        solved_anything = False

        for col_i in range(10):
            col = self.get_col(col_i)
            count_o, count_x = Binoxxo.count(col)

            if count_o == 4 and count_x < 4:
                lst = Binoxxo.get_risk(col, 'X')
                is_risky = Binoxxo.is_risky(lst)
                if is_risky:
                    for sub_lst in lst:
                        if len(sub_lst) < 3:
                            for row_i in sub_lst:
                                if not self.gb[row_i][col_i]:
                                    self.gb[row_i][col_i] = 'X'
                                    print(f'({row_i}, {col_i}) can only be X on the col')
                                    solved_anything = True

            elif count_x == 4 and count_o < 4:
                lst = Binoxxo.get_risk(col, 'O')
                is_risky = Binoxxo.is_risky(lst)
                if is_risky:
                    for sub_lst in lst:
                        if len(sub_lst) < 3:
                            for row_i in sub_lst:
                                if not self.gb[row_i][col_i]:
                                    self.gb[row_i][col_i] = 'O'
                                    print(f'({row_i}, {col_i}) can only be O on the col')
                                    solved_anything = True

        return solved_anything

    @staticmethod
    def get_empty(lst):
        lst_empty = []

        for i in range(10):
            if not lst[i]:
                lst_empty.append(i)

        return lst_empty

    def check_duplicates_row(self, given_row_i, given_row, lst_empty):
        solved_anything = False

        for row_i in range(10):
            if row_i == given_row_i:
                continue

            row = self.get_row(row_i)
            count_o, count_x = self.count(row)

            if count_o == 5 and count_x == 5:
                same = True
                for i in range(10):
                    if i in lst_empty:
                        continue
                    if row[i] != given_row[i]:
                        same = False

                if same:
                    a, b = lst_empty
                    self.gb[given_row_i][a] = self.gb[row_i][b]
                    self.gb[given_row_i][b] = self.gb[row_i][a]
                    print(f'completed row {given_row_i} by swapping with full row {row_i}')

        return solved_anything

    def check_duplicates_col(self, given_col_i, given_col, lst_empty):
        solved_anything = False

        for col_i in range(10):
            if col_i == given_col_i:
                continue

            col = self.get_col(col_i)
            count_o, count_x = self.count(col)

            if count_o == 5 and count_x == 5:
                same = True
                for i in range(10):
                    if i in lst_empty:
                        continue
                    if col[i] != given_col[i]:
                        same = False

                if same:
                    a, b = lst_empty
                    self.gb[a][given_col_i] = self.gb[b][col_i]
                    self.gb[b][given_col_i] = self.gb[a][col_i]
                    print(f'completed col {given_col_i} by swapping with full col {col_i}')

        return solved_anything

    def solve_no_duplicates(self):
        solved_anything = False

        # horizontal check
        for row_i in range(10):
            row = self.get_row(row_i)
            count_o, count_x = Binoxxo.count(row)

            if count_o == 4 and count_x == 4:
                lst_empty = self.get_empty(row)
                duplicate_row = self.check_duplicates_row(row_i, row, lst_empty)
                if duplicate_row:
                    solved_anything = True

        # vertical check
        for col_i in range(10):
            col = self.get_col(col_i)
            count_o, count_x = Binoxxo.count(col)

            if count_o == 4 and count_x == 4:
                lst_empty = self.get_empty(col)
                duplicate_col = self.check_duplicates_col(col_i, col, lst_empty)
                if duplicate_col:
                    solved_anything = True

        return solved_anything
