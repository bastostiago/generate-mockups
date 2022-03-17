import os
from photoshopy import Photoshopy
from configparser import ConfigParser
from definitions import COLOR_OF_MUGS

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
DIR_FILES_TO_PROCESS = os.path.abspath("./../resources/origin_process")
DIR_PROCESSED = os.path.abspath("./../resources/processed")
DIR_PSD_MUGS = os.path.abspath("./../resources/psd/mugs")
CONFIG = ConfigParser()
CONFIG.read(os.path.abspath("./../config.ini"))


def get_files_to_process():
    return os.listdir(DIR_FILES_TO_PROCESS)


def run_mugs(app, kind_of_m, color_of_m):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    #progress bar
    files_qty = 0
    if kind_of_m == 1:
        files_qty += 5
    elif kind_of_m == 4:
        files_qty += 3
    else:
        files_qty += 1
    files_qty = files_qty * len(color_of_m)
    exported_files = 0

    files_to_process = get_files_to_process()
    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 2 Mugs and Art
            if kind_of_m in (1, 2):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mugs_and_art.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('art_image', file_to_process)
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_1_{COLOR_OF_MUGS[color].get('color')}.jpg"
                        app.update_layer_color('mug2_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug2_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug2_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Side 1
            if kind_of_m in (1, 4):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug1.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_2_{COLOR_OF_MUGS[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Side 2
            if kind_of_m in (1, 4):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug2.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_3_{COLOR_OF_MUGS[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Center
            if kind_of_m in (1, 4):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug_center.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_4_{COLOR_OF_MUGS[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # 3 Mugs
            if kind_of_m in (1, 3):
                psd_file = os.path.join(DIR_PSD_MUGS, '3mugs.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)
                    app.update_layer_image('mug3_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_0_{COLOR_OF_MUGS[color].get('color')}.jpg"
                        app.update_layer_color('mug2_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug2_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug2_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug3_color_inside', COLOR_OF_MUGS[color].get('rgb'))
                        app.update_layer_color('mug3_color_triminside', COLOR_OF_MUGS[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            if CONFIG['DEFAULT']['DeleteOriginFiles'] == 'yes':
                os.remove(file_to_process)


if __name__ == '__main__':
    option = 99999
    app_obj = None

    while option > 0:
        try:
            print('')
            clear_console()
            menu = '-------------------------\n' \
                   '0 - QUIT \n1 - Generate Mugs\n' \
                   '-------------------------\n' \
                   'Your option (0): '
            option = int(input(menu) or 0)

            if option == 1:

                # build kind of mugs menu
                clear_console()
                menu = '-------------------------\n' \
                       'What KIND OF MUGS do you need? \n' \
                       '1 - ALL\n' \
                       '2 - Art and Two Mugs\n' \
                       '3 - Tree Mugs Together\n' \
                       '4 - Tree Mugs Apart\n' \
                       '-------------------------\n' \
                       'Your option (1): '
                kind_of_mugs = int(input(menu) or 1)

                # build colors of mugs menu
                clear_console()
                menu = '-------------------------\n' \
                       'What COLORS OF MUGS do you need? \n'
                for key, value in COLOR_OF_MUGS.items():
                    menu += f"{key} - {value.get('color')}\n"
                menu += '-------------------------\n' \
                        'Your options (1): '
                color_of_mugs = input(menu) or '1'
                color_of_mugs = color_of_mugs.split(',')
                color_of_mugs = [x.strip() for x in color_of_mugs]

                app_obj = Photoshopy()
                run_mugs(app_obj, kind_of_mugs, color_of_mugs)
                app_obj.closePhotoshop()

        except Exception as e:
            print(e)
            if app_obj:
                if app_obj.psd_file:
                    app_obj.closePSD()
                app_obj.closePhotoshop()





