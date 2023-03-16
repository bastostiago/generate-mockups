import os
from configparser import ConfigParser


DIR_FILES_TO_PROCESS = os.path.abspath("./../resources/origin_process")
DIR_PROCESSED = os.path.abspath("./../resources/processed")
DIR_PSD_MUGS = os.path.abspath("./../resources/psd/magic_mugs/")
CONFIG = ConfigParser()
CONFIG.read(os.path.abspath("./../config.ini"))


def run_magic_mugs(app, kind_of_m, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = os.listdir(DIR_FILES_TO_PROCESS)

    # progress bar
    files_qty = 6 * len(kind_of_m)
    exported_files = 0

    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            for king_of_mug in kind_of_m:
                # 2 Mugs
                psd_name = '2mugs_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)                                
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # 2 Mugs with coffee
                psd_name = '2mugs_withcoffee_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)                
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # 3 Mugs
                psd_name = '3mugs_transformation_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"                
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)   
                    app.update_layer_image('mug3_image', file_to_process)             
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # Mug 1
                psd_name = 'mug1_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"                
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)                          
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # Mug 2
                psd_name = 'mug2_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)                          
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # Mug center
                psd_name = 'mug_center_magic'
                psd_aux_name = '_glitter' if king_of_mug == '2' else ''
                psd_name = f'{psd_name}{psd_aux_name}'
                psd_file = os.path.join(DIR_PSD_MUGS, f'{psd_name}.psd')
                img_name = f"{file_name}_{psd_name}_.jpg"
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)                          
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            if del_files == 'Y':
                os.remove(file_to_process)
