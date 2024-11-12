import os
import glob

def replace_tg_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace("\\tg", "\\mathrm{tg}")
    content = content.replace("\\ctg", "\\mathrm{ctg}")
    content = content.replace("\\operatorname{tg}", "\\mathrm{tg}")
    content = content.replace("\\operatorname{ctg}", "\\mathrm{ctg}")
    content = content.replace("\\Z", "\\mathbb{Z}")
    content = content.replace("\\R", "\\mathbb{R}")

    with open(file_path, 'w') as file:
        file.write(content)

def replace_tg_in_folder(folder_path):
    for file_path in glob.glob(os.path.join(folder_path, '**', '*.*'), recursive=True):
        if file_path.endswith('.md'):
            replace_tg_in_file(file_path)

if __name__ == "__main__":
    replace_tg_in_folder(os.path.dirname(os.path.abspath(__file__)))