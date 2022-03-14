import os
from photoshopy import Photoshopy


clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
DIR_FILES_TO_PROCESS = os.path.abspath("./../resources/origin_process")
DIR_PROCESSED = os.path.abspath("./../resources/processed")
DIR_PSD_MUGS = os.path.abspath("./../resources/psd/mugs")


def get_files_to_process():
    return os.listdir(DIR_FILES_TO_PROCESS)


def run_mugs(app):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = get_files_to_process()
    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 2 Mugs and Art
            psd_file = os.path.join(DIR_PSD_MUGS, 'mugs_and_art.psd')
            opened = app.openPSD(psd_file)
            if opened:
                img_name = f'{file_name}_1.jpg'
                app.update_layer_image('art_image', file_to_process)
                app.update_layer_image('mug1_image', file_to_process)
                app.update_layer_image('mug2_image', file_to_process)
                app.exportJPEG(img_name, dir_to_save)
                app.closePSD()

            # Mug Side 1
            psd_file = os.path.join(DIR_PSD_MUGS, 'mug1.psd')
            opened = app.openPSD(psd_file)
            if opened:
                img_name = f'{file_name}_2.jpg'
                app.update_layer_image('mug1_image', file_to_process)
                app.exportJPEG(img_name, dir_to_save)
                app.closePSD()

            # Mug Side 2
            psd_file = os.path.join(DIR_PSD_MUGS, 'mug2.psd')
            opened = app.openPSD(psd_file)
            if opened:
                img_name = f'{file_name}_3.jpg'
                app.update_layer_image('mug1_image', file_to_process)
                app.exportJPEG(img_name, dir_to_save)
                app.closePSD()

            # Mug Center
            psd_file = os.path.join(DIR_PSD_MUGS, 'mug_center.psd')
            opened = app.openPSD(psd_file)
            if opened:
                img_name = f'{file_name}_4.jpg'
                app.update_layer_image('mug1_image', file_to_process)
                app.exportJPEG(img_name, dir_to_save)
                app.closePSD()


if __name__ == '__main__':
    option = 99999
    app_obj = None

    while option > 0:
        try:
            clear_console()
            menu = '\n-------------------------\n' \
                   '0 - QUIT \n1 - Generate Mugs \n' \
                   '-------------------------\n' \
                   'Your option (0): '
            option = int(input(menu) or 0)

            if option == 1:
                app_obj = Photoshopy()
                run_mugs(app_obj)

                app_obj.closePhotoshop()

        except Exception as e:
            print(e)
            if app_obj:
                if app_obj.psd_file:
                    app_obj.closePSD()
                app_obj.closePhotoshop()





