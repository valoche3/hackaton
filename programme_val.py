#interface graphique

import flet as ft

# create the widgets ONCE

#carres = [ft.TextField(('1 2 3 4 5 6 7 8 0')) for i in range(9)]

# just a dummy example of some callback you could want to write
# the point is to only CHANGE the widgets, and NOT CREATE them again !

#def reset(board):
   # for i, square in zip(board, squares):
      #  square.value = i

class Board:
    def __init__(self, page):
        self.page = page
        self.squares = self.create_squares()
    def create_squares(self):
        self.squares = [ft.TextField('1 2 3 4 5 6 7 8 0')]
        return self.squares
    def update(self, board):
        for i, square in zip(board, self.squares):
            square.value = str(i)
        # with this approach it is MUCH EASIER to get our hands on the page instance !
        self.page.update()


def main(page : ft.Page):
    board = Board(page)
    page.title = "Puzzle"
    
    #cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    cases = [ft.Container(
            content=ft.Text(f"Case {i+1}"),
            width=100,
            height=100,
            bgcolor=ft.colors.AMBER_300 if i % 2 == 0 else ft.colors.BLUE_300,  # Couleurs alternées
            alignment=ft.alignment.center,
            border_radius=10
        ) 
        for i in range(9)
    ]
    #ligne du dessus
    #ligne_1 = ft.TextField(...)
    #les 9 carrés
    grille = ft.GridView(expand = True, runs_count = 3, max_extent = 150, spacing = 10, run_spacing = 10)
    grille.controls.extend(board.squares)
    #for i in range(9):
        #grille.controls.append(ft.Card(content = ft.Container(squares, a)))
    #boutons en dessous
    
    def shuffle_board(e):
        from random import shuffle
        new_values = list(range(1, 10))  # Valeurs de 1 à 9
        shuffle(new_values)
        board.update(new_values)  # Met à jour les TextFields
        
    boutons = ft.Row([ft.IconButton(icon=ft.icons.REFRESH, on_click=shuffle_board)])
    
    colonne = ft.Column([grille, boutons]) #alignment = ft.MainAxisAlignment.CENTER, spacing = 10)
    page.add(colonne)

ft.app(main)