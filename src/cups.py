import os
from configparser import ConfigParser


DIR_FILES_TO_PROCESS = os.path.abspath("./../resources/origin_process")
DIR_PROCESSED = os.path.abspath("./../resources/processed")
DIR_PSD_CUPS = os.path.abspath("./../resources/psd/cups/")
CONFIG = ConfigParser()
CONFIG.read(os.path.abspath("./../config.ini"))


def run_cups(app, kind_of_c, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = os.listdir(DIR_FILES_TO_PROCESS)

    # progress bar
    files_qty = 0
    if kind_of_c == 1:
        files_qty += 3
        if CONFIG['DEFAULT']['GenerateNoBackgroundImages'] == 'yes':
            files_qty += 2
    else:
        files_qty += 1
    exported_files = 0

    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 2 Cups and Art
            if kind_of_c in (1, 2):
                psd_file = os.path.join(DIR_PSD_CUPS, 'white_cups_art.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('art_image', file_to_process)
                    app.update_layer_image('cup1_image', file_to_process)
                    app.update_layer_image('cup2_image', file_to_process)
                    img_name = f"{file_name}_1_white_cup.jpg"
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            if kind_of_c == 1:

                # Cup Side 1
                psd_file = os.path.join(DIR_PSD_CUPS, 'white_cup_1.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('cup1_image', file_to_process)
                    img_name = f"{file_name}_2_white_cup.jpg"
                    app.exportJPEG(img_name, dir_to_save)
                    if CONFIG['DEFAULT']['GenerateNoBackgroundImages'] == 'yes':
                        img_name = f"{file_name}_2_white_cup.png"
                        app.update_layer_visibility(f'bg1', False)
                        app.exportPNG(img_name, dir_to_save)
                        exported_files += 1
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # Cup Side 2
                psd_file = os.path.join(DIR_PSD_CUPS, 'white_cup_2.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('cup2_image', file_to_process)
                    img_name = f"{file_name}_3_white_cup.jpg"
                    app.exportJPEG(img_name, dir_to_save)
                    if CONFIG['DEFAULT']['GenerateNoBackgroundImages'] == 'yes':
                        img_name = f"{file_name}_3_white_cup.png"
                        app.update_layer_visibility(f'bg2', False)
                        app.exportPNG(img_name, dir_to_save)
                        exported_files += 1
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            if del_files == 'Y':
                os.remove(file_to_process)
