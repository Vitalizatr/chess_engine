from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

console = Console()
title ='''
# ШАХМАТЫ
'''
md = Markdown(title)
console.print(md)
board = [
    ["2" , None, "2", "2", "2","2", None, "3"],
    [None, None, "1", "1", "1","1", None, None],
    ["1" , "1", ".", ".", ".",".", "1", "1"],
    ["." , ".", ".", ".", ".",".", ".", "."],
    ["." , ".", ".", ".", ".",".", ".", "."],
    ["1" , "1", ".", ".", ".",".", "1", "1"],
    [None, None, "1", "1", "1","1", None, None],
    ["3" , None, "2", "2", "2","2", None, "2"],
]

def out_board(board):
    table = Table(show_header=False, box=None, padding=(0, 0), pad_edge=False)

    k=0
    style="[black on white]"
    for i in board:
        k+=1
        render_row =[]
        for ceil in i:
            k+=1
            s=""
            if k%2==0:
                s+=style
            if ceil != None:
                render_row.append(f"{s}-{ceil}-")
            else:   
                render_row.append(f"{s}   ")
        table.add_row(*render_row)
    console.print(table)
