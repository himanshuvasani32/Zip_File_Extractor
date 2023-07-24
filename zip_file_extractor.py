import PySimpleGUI as sg
from zip_extractor_function import zip_extractor

sg.theme('Black')

zip_file_label = sg.Text("Select a compressed file:")
zip_file_input = sg.Input()
zip_file_choose_button = sg.FileBrowse("Choose", key="zipfile")

dest_path_label = sg.Text("Select a destination path:")
dest_path_input = sg.Input()
dest_choose_button = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key='output', text_color='green')

window = sg.Window("Zip File Extractor",
                   layout=[[zip_file_label, zip_file_input, zip_file_choose_button],
                           [dest_path_label, dest_path_input, dest_choose_button],
                           [extract_button, output_label]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    compressed_filepath = values["zipfile"]
    dest_path = values["folder"]
    zip_extractor(compressed_filepath, dest_path)
    window['output'].update(value="Extraction Successfully Completed!")

window.close()

