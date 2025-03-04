import dearpygui.dearpygui as dpg
from TestName.windows import main_window, error_window, success_window
from TestName.dialogues import input_dialogue, output_dialogue

def gui_setup():
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
