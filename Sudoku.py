from PySide2 import QtWidgets as Q
from PySide2 import QtGui
from PySide2.QtCore import Qt


class NumButton(Q.QPushButton):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(40, 40)
        self.val = 0
        self.setSizePolicy(Q.QSizePolicy.Fixed, Q.QSizePolicy.Fixed)
        self.setText("0")
        self.grid_num = 0
        self.position = (x, y)
        self.is_locked = False
        self.button_check = None

    def set_grid_num(self, x):
        self.grid_num = x

    def send_full_pos(self):
        return self, "Grid: "+str(self.grid_num)+" Position: "+str(self.position)

    def mousePressEvent(self, event):
        self.button_check = event.button()
        self.click()

    def increment(self):
        if self.is_locked:
            pass
        else:
            self.val += 1
            if self.val == 10:
                self.val = 1
            self.setText(str(self.val))

    def decrement(self):
        if self.is_locked:
            pass
        else:
            self.val -= 1
            if self.val <= 0:
                self.val = 9
            self.setText(str(self.val))


class SudokuGrid(Q.QWidget):
    def __init__(self, val, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Q.QGridLayout()
        self.setLayout(self.layout)
        self.grid_num = val
        self.buttons = []

    def get_buttons(self, button_list):
        self.buttons += button_list

    def assign_buttons(self):
        x = 0
        for i in range(0, 3):
            for g in range(0, 3):
                btn = self.buttons[x]
                btn.set_grid_num(self.grid_num)
                self.layout.addWidget(btn, i, g)
                self.setLayout(self.layout)
                x += 1


class MainWindow(Q.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Q.QGridLayout()
        self.all_buttons = []
        self.all_grids = []
        self.final_grids = []
        self.source_nums = []
        self.setWindowTitle("Bryce's Sudoku")
        with open('Test.txt') as source:
            for line in source.readlines():
                stripped = line.strip()
                splitted = stripped.split(',')
                self.source_nums += splitted
        count = 0
        for i in range(0, 9):
            for g in range(0, 9):
                btn = NumButton(i, g)
                btn.setText(self.source_nums[count])
                if btn.text() != "0":
                    btn.is_locked = True
                    btn.setStyleSheet('background-color: #00FFFF')
                else:
                    btn.setStyleSheet('background-color: grey')
                self.all_buttons.append(btn)
                count += 1

        for i in range(0, 9):
            grid = SudokuGrid(i)
            self.all_grids.append(grid)

        self.grid1 = self.all_grids[0]
        self.grid2 = self.all_grids[1]
        self.grid3 = self.all_grids[2]
        self.grid4 = self.all_grids[3]
        self.grid5 = self.all_grids[4]
        self.grid6 = self.all_grids[5]
        self.grid7 = self.all_grids[6]
        self.grid8 = self.all_grids[7]
        self.grid9 = self.all_grids[8]

        self.grid1.get_buttons([self.all_buttons[0], self.all_buttons[1], self.all_buttons[2], self.all_buttons[9],
                                self.all_buttons[10],
                                self.all_buttons[11], self.all_buttons[18], self.all_buttons[19], self.all_buttons[20]])

        self.grid2.get_buttons([self.all_buttons[3], self.all_buttons[4], self.all_buttons[5], self.all_buttons[12],
                                self.all_buttons[13],
                                self.all_buttons[14], self.all_buttons[21], self.all_buttons[22], self.all_buttons[23]])

        self.grid3.get_buttons([self.all_buttons[6], self.all_buttons[7], self.all_buttons[8], self.all_buttons[15],
                                self.all_buttons[16],
                                self.all_buttons[17], self.all_buttons[24], self.all_buttons[25], self.all_buttons[26]])

        self.grid4.get_buttons([self.all_buttons[27], self.all_buttons[28], self.all_buttons[29], self.all_buttons[36],
                                self.all_buttons[37],
                                self.all_buttons[38], self.all_buttons[45], self.all_buttons[46], self.all_buttons[47]])

        self.grid5.get_buttons([self.all_buttons[30], self.all_buttons[31], self.all_buttons[32], self.all_buttons[39],
                                self.all_buttons[40], self.all_buttons[41],
                                self.all_buttons[48], self.all_buttons[49], self.all_buttons[50]])

        self.grid6.get_buttons([self.all_buttons[33], self.all_buttons[34], self.all_buttons[35], self.all_buttons[42],
                                self.all_buttons[43],
                                self.all_buttons[44], self.all_buttons[51], self.all_buttons[52], self.all_buttons[53]])

        self.grid7.get_buttons([self.all_buttons[54], self.all_buttons[55], self.all_buttons[56], self.all_buttons[63],
                                self.all_buttons[64],
                                self.all_buttons[65], self.all_buttons[72], self.all_buttons[73], self.all_buttons[74]])

        self.grid8.get_buttons([self.all_buttons[57], self.all_buttons[58], self.all_buttons[59], self.all_buttons[66],
                                self.all_buttons[67],
                                self.all_buttons[68], self.all_buttons[75], self.all_buttons[76], self.all_buttons[77]])

        self.grid9.get_buttons([self.all_buttons[60], self.all_buttons[61], self.all_buttons[62], self.all_buttons[69],
                                self.all_buttons[70],
                                self.all_buttons[71], self.all_buttons[78], self.all_buttons[79], self.all_buttons[80]])

        self.final_grids = [self.grid1, self.grid2, self.grid3, self.grid4, self.grid5, self.grid6, self.grid7,
                            self.grid8, self.grid9]

        clear_button = Q.QPushButton("RESET", self)

        clear_button.move(500, 50)

        x = 0
        for i in range(0, 3):
            for g in range(0, 3):
                grid = self.final_grids[x]
                self.layout.addWidget(grid, i, g)
                self.setLayout(self.layout)
                x += 1

        for i in self.final_grids:
            i.assign_buttons()

        for btn in self.all_buttons:
            btn.clicked.connect(self.checker)

    def checker(self):
        sender = self.sender()
        #Uncomment to see what button is being pressed!
        #print("Button: ", sender, " at postion: ", sender.position, " was pressed!")
        if sender.button_check == Qt.LeftButton:
            sender.increment()
        elif sender.button_check == Qt.RightButton:
            sender.decrement()
        row = self.row_check(sender)
        column = self.column_check(sender)
        grid = self.grid_check(sender)
        win = self.check_win()
        if row or column or grid:
            sender.setStyleSheet('background-color: red')
        elif sender.is_locked:
            sender.setStyleSheet('background-color: #00FFFF')
        elif win:
            for btn in self.all_buttons:
                btn.setStyleSheet('background-color: green')
        else:
            sender.setStyleSheet('background-color: grey')

    def row_check(self, button):
        text = button.text()
        for btn in self.all_buttons:
            if btn.position == button.position:
                pass
            elif btn.position[0] == button.position[0]:
                if btn.text() == text:
                    return True

    def column_check(self, button):
        text = button.text()
        for btn in self.all_buttons:
            if btn.position == button.position:
                pass
            elif btn.position[1] == button.position[1]:
                if btn.text() == text:
                    return True

    def grid_check(self, button):
        text = button.text()
        for btn in self.all_buttons:
            if btn.position == button.position:
                pass
            elif btn.grid_num == button.grid_num:
                if btn.text() == text:
                    return True

    def check_win(self):
        for btn in self.all_buttons:
            column = self.column_check(btn)
            row = self.row_check(btn)
            grid = self.grid_check(btn)
            if column or row or grid:
                return False

        return True


app = Q.QApplication()
main = MainWindow()
main.show()
app.exec_()
