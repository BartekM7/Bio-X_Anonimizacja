import dearpygui.dearpygui as dpg

from dialogues import input_dialogue, output_dialogue
from callbacks import  start_callback
from windows import main_window, error_window, success_window

def gui():
    start_callback()

    dpg.create_context()

    main_window()
    input_dialogue()
    output_dialogue()

    error_window()
    success_window()

    dpg.create_viewport(title='Anonimizacja', width=700, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()