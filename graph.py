# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:11:41 2022

@author: Vikas Reddy karkala
"""

import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def update_graph(data):
    axes=fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y,'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()    
tablevalues=[]
sg.theme('DarkTeal6')
layout=[
        [sg.Table(headings=['Observation','Result'], values=tablevalues,hide_vertical_scroll=True,
                  key='-TABLE-',expand_x=True)],
        [sg.Input(key='-INPUT-'),sg.Button('Submit')],
        [sg.Canvas(key='-CANVAS-')]
        ]
window=sg.Window('Graph App',layout,finalize=True)

fig=matplotlib.figure.Figure(figsize=(5,4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig,window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()
# window=sg.Window('Graph App',layout,finalize=True)
while True:
    events,values=window.read(timeout=0)
    if events==sg.WIN_CLOSED:break
    if events=='Submit':
        new_val=values['-INPUT-']
        if new_val.isnumeric():
            tablevalues.append([len(tablevalues)+1,float(new_val)])
            window['-TABLE-'].update(tablevalues)
            window['-INPUT-'].update('')
            update_graph(tablevalues)
            
            
window.close()            