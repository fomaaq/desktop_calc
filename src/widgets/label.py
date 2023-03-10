'''
The module contains classes and methods for configuring the text label widget
'''

import tkinter as tk


class Label:
    '''
    The class is responsible for creating and placing a text label, as well as for updating it
    '''
    def __init__(self, initial_text: str):
        '''
        :param str initial_text: text displayed at startup
        '''
        self.label_text = tk.Label(anchor='e',
                                   text=initial_text,
                                   font=('Segoe', 27, 'bold'),
                                   bg='#666666',
                                   fg='white',
                                   width=20,
                                   height=3)

        # Placement of a text label
        self.label_text.pack()

    def update_text(self, new_text: str):
        '''
        Updates the text in the text label

        :param str new_text: the text that should be after the update
        '''
        self.label_text.configure(text=new_text)
