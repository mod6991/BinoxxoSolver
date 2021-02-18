"""
Binoxxo solver
Josué Clément (2021)
"""

import arcade
from BinoxxoSolver import Binoxxo

BORDER_WIDTH = 1
CELL_SIZE = 50
ROWS, COLS = 10, 10
SCREEN_WIDTH = (11 * BORDER_WIDTH) + (10 * CELL_SIZE)
SCREEN_HEIGHT = (11 * BORDER_WIDTH) + (10 * CELL_SIZE)
SCREEN_TITLE = "Binoxxo solver"

LINES_POSITIONS = \
[
    BORDER_WIDTH // 2,
    (1 * BORDER_WIDTH) + (1 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (2 * BORDER_WIDTH) + (2 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (3 * BORDER_WIDTH) + (3 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (4 * BORDER_WIDTH) + (4 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (5 * BORDER_WIDTH) + (5 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (6 * BORDER_WIDTH) + (6 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (7 * BORDER_WIDTH) + (7 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (8 * BORDER_WIDTH) + (8 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (9 * BORDER_WIDTH) + (9 * CELL_SIZE) + (BORDER_WIDTH // 2),
    (10 * BORDER_WIDTH) + (10 * CELL_SIZE) + (BORDER_WIDTH // 2)
]

CELLS_START_POSITIONS = \
[
    (1 * BORDER_WIDTH),
    (2 * BORDER_WIDTH) + (1 * CELL_SIZE),
    (3 * BORDER_WIDTH) + (2 * CELL_SIZE),
    (4 * BORDER_WIDTH) + (3 * CELL_SIZE),
    (5 * BORDER_WIDTH) + (4 * CELL_SIZE),
    (6 * BORDER_WIDTH) + (5 * CELL_SIZE),
    (7 * BORDER_WIDTH) + (6 * CELL_SIZE),
    (8 * BORDER_WIDTH) + (7 * CELL_SIZE),
    (9 * BORDER_WIDTH) + (8 * CELL_SIZE),
    (10 * BORDER_WIDTH) + (9 * CELL_SIZE)
]


def change_coords(x, y):
    return x, SCREEN_HEIGHT - y


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.binoxxo = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.cell_row = 0
        self.cell_col = 0

    def setup(self):
        """Set up the game variables. Call to re-start the game."""
        self.binoxxo = Binoxxo()
        self.mouse_x = 0
        self.mouse_y = 0
        self.cell_row = 0
        self.cell_col = 0

    def on_draw(self):
        """Render the screen."""
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.draw_gameboard()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        val = None
        update_val = False
        if key == arcade.key.X:
            val = 'X'
            update_val = True
        elif key == arcade.key.O:
            val = 'O'
            update_val = True
        elif key == arcade.key.DELETE:
            val = None
            update_val = True
        elif key in (arcade.key.SPACE, arcade.key.ENTER):
            self.try_to_solve()

        if update_val:
            self.binoxxo.gb[self.cell_row][self.cell_col] = val

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.mouse_x, self.mouse_y = change_coords(x, y)
        self.cell_row = self.get_cell(self.mouse_y)
        self.cell_col = self.get_cell(self.mouse_x)

    def _draw_horizontal_lines(self):
        for i in range(11):
            sx, sy = change_coords(0, LINES_POSITIONS[i])
            ex, ey = change_coords(SCREEN_HEIGHT, LINES_POSITIONS[i])
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BORDER_WIDTH)

    def _draw_vertical_lines(self):
        for i in range(11):
            sx, sy = change_coords(LINES_POSITIONS[i], 0)
            ex, ey = change_coords(LINES_POSITIONS[i], SCREEN_HEIGHT)
            arcade.draw_line(sx, sy, ex, ey, arcade.color.BLACK, BORDER_WIDTH)

    def draw_gameboard(self):
        self._draw_horizontal_lines()
        self._draw_vertical_lines()

        for row_i in range(10):
            for col_i in range(10):
                tx, ty = change_coords(CELLS_START_POSITIONS[col_i] + (CELL_SIZE // 2),
                                       CELLS_START_POSITIONS[row_i] + (CELL_SIZE // 2))
                arcade.draw_text(self.get_cell_str(row_i, col_i), tx, ty, arcade.color.BLACK, 32,
                                 width=40, align='center', anchor_x='center', anchor_y='center')

    def get_cell_str(self, row_i, col_i):
        cell_value = self.binoxxo.gb[row_i][col_i]
        if not cell_value:
            return ' '
        return cell_value

    def get_cell(self, pos):
        """Get the current cell from mouse position."""
        for i in range(1, 10):
            if pos < CELLS_START_POSITIONS[i]:
                return i - 1
        return 9

    def try_to_solve(self):
        while True:
            s1 = self.binoxxo.solve_surrounded()
            s2 = self.binoxxo.solve_twins()
            s3 = self.binoxxo.solve_full()
            s4 = self.binoxxo.solve_4lt4()
            s5 = self.binoxxo.solve_no_duplicates()

            if not s1 and not s2 and not s3 and not s4 and not s5:
                print('solve ended')
                break


def main():
    """Main method"""
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
