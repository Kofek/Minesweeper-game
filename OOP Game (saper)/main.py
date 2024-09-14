from tkinter import *
from cell import Cell
import settings
import utilities
import ctypes
# podstawowe ustawienia okna
root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Saper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(100),
    height=utilities.height_percentage(20)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg = "black",
    fg = "white",
    text = ("Minesweeper Game"),
    font = ("", 48)
)
game_title.place(
    x = utilities.width_percentage(25),
    y = 0
)

left_frame = Frame(
    root,
    bg='black', # change later for black
    width=utilities.width_percentage(20),
    height=utilities.height_percentage(80)
)
left_frame.place(x=0, y=utilities.height_percentage(20))

center_frame = Frame(
    root,
    bg='black', # change later for black
    width=utilities.width_percentage(80),
    height=utilities.height_percentage(80)
)
center_frame.place(x=utilities.width_percentage(20), y=utilities.height_percentage(20))

for x in range(settings.button_rows):
    for y in range(settings.button_columns):
        button = Cell(x,y)
        button.create_btn_object(
            center_frame,
            height = settings.button_height,
            width = settings.button_width
            )
        button.cell_btn_object.grid(column=x, row=y)

Cell.randomize_mines()
Cell.create_cell_count_label(left_frame)
Cell.create_mines_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.mines_count_label_object.place(x=0, y=50)

# uruchomienie okna
root.mainloop()
