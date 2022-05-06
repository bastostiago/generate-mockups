import os
from photoshopy import Photoshopy
from configparser import ConfigParser
from definitions import COLOR_OF_MUGS, COLOR_OF_BOTTLES, COLOR_OF_MUGS_HEART, COLOR_OF_NECESSAIRE_ZIPPER

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
DIR_FILES_TO_PROCESS = os.path.abspath("./../resources/origin_process")
DIR_PROCESSED = os.path.abspath("./../resources/processed")
DIR_PSD_MUGS = os.path.abspath("./../resources/psd/mugs")
DIR_PSD_BOTTLES = os.path.abspath("./../resources/psd/bottles/")
DIR_PSD_NECESSAIRES = os.path.abspath("./../resources/psd/necessaires/")
CONFIG = ConfigParser()
CONFIG.read(os.path.abspath("./../config.ini"))


def get_files_to_process():
    return os.listdir(DIR_FILES_TO_PROCESS)


def run_mugs(app, kind_of_m, color_of_m, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = get_files_to_process()

    # progress bar
    files_qty = 0
    if kind_of_m == 1:
        files_qty += 5
    elif kind_of_m == 4:
        files_qty += 3
    else:
        files_qty += 1
    files_qty = files_qty * len(color_of_m) * len(files_to_process)
    exported_files = 0

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

            if del_files == 'Y':
                os.remove(file_to_process)


def run_bottles(app, kind_of_b, color_of_b, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = get_files_to_process()

    # progress bar
    files_qty = 0
    if kind_of_b == 1:
        files_qty += 3
    else:
        files_qty += 1
    files_qty = files_qty * len(color_of_b) * len(files_to_process)
    exported_files = 0

    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 750 Aluminum
            if kind_of_b == 1:
                # 2 bottles
                psd_file = os.path.join(DIR_PSD_BOTTLES, 'aluminum_750_2bottles.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('bottle1_image', file_to_process)
                    app.update_layer_image('bottle2_image', file_to_process)
                    for color in color_of_b:
                        color_value = COLOR_OF_BOTTLES[str(kind_of_b)][color].get('value')
                        img_name = f"{file_name}_1_{color_value}.jpg"
                        app.update_layer_visibility(f'bottle1_color_{color_value}', True)
                        app.update_layer_visibility(f'bottle2_color_{color_value}', True)
                        app.exportJPEG(img_name, dir_to_save)
                        app.update_layer_visibility(f'bottle1_color_{color_value}', False)
                        app.update_layer_visibility(f'bottle2_color_{color_value}', False)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

                # bottle 1
                psd_file = os.path.join(DIR_PSD_BOTTLES, 'aluminum_750_bottle1.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('bottle1_image', file_to_process)
                    for color in color_of_b:
                        color_value = COLOR_OF_BOTTLES[str(kind_of_b)][color].get('value')
                        img_name = f"{file_name}_2_{color_value}.jpg"
                        app.update_layer_visibility(f'bottle1_color_{color_value}', True)
                        app.exportJPEG(img_name, dir_to_save)
                        app.update_layer_visibility(f'bottle1_color_{color_value}', False)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...",
                              end='')
                    app.closePSD()

                # bottle 2
                psd_file = os.path.join(DIR_PSD_BOTTLES, 'aluminum_750_bottle2.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('bottle1_image', file_to_process)
                    for color in color_of_b:
                        color_value = COLOR_OF_BOTTLES[str(kind_of_b)][color].get('value')
                        img_name = f"{file_name}_3_{color_value}.jpg"
                        app.update_layer_visibility(f'bottle1_color_{color_value}', True)
                        app.exportJPEG(img_name, dir_to_save)
                        app.update_layer_visibility(f'bottle1_color_{color_value}', False)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...",
                              end='')
                    app.closePSD()

            if del_files == 'Y':
                os.remove(file_to_process)


def run_mugs_heart(app, kind_of_m, color_of_m, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = get_files_to_process()

    # progress bar
    files_qty = 0
    if kind_of_m == 1:
        files_qty += 4
    elif kind_of_m == 3:
        files_qty += 3
    else:
        files_qty += 1
    files_qty = files_qty * len(color_of_m) * len(files_to_process)
    exported_files = 0

    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 2 Mugs and Art
            if kind_of_m in (1, 2):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mugs_and_art_heart.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('art_image', file_to_process)
                    app.update_layer_image('mug1_image', file_to_process)
                    app.update_layer_image('mug2_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_heart_1_{COLOR_OF_MUGS_HEART[color].get('color')}.jpg"
                        app.update_layer_color('mug2_color_inside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug2_color_handle', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Side 1
            if kind_of_m in (1, 3):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug1_heart.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_heart_2_{COLOR_OF_MUGS_HEART[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Side 2
            if kind_of_m in (1, 3):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug2_heart.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_heart_3_{COLOR_OF_MUGS_HEART[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug1_color_handle', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            # Mug Center
            if kind_of_m in (1, 3):
                psd_file = os.path.join(DIR_PSD_MUGS, 'mug_center_heart.psd')
                opened = app.openPSD(psd_file)
                if opened:
                    app.update_layer_image('mug1_image', file_to_process)
                    for color in color_of_m:
                        img_name = f"{file_name}_heart_4_{COLOR_OF_MUGS_HEART[color].get('color')}.jpg"
                        app.update_layer_color('mug1_color_inside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.update_layer_color('mug1_color_triminside', COLOR_OF_MUGS_HEART[color].get('rgb'))
                        app.exportJPEG(img_name, dir_to_save)
                        exported_files += 1
                        print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                    app.closePSD()

            if del_files == 'Y':
                os.remove(file_to_process)


def run_necessaires(app, color_of_n, del_files='Y'):
    if not os.path.isdir(DIR_FILES_TO_PROCESS):
        os.mkdir(DIR_FILES_TO_PROCESS)

    if not os.path.isdir(DIR_PROCESSED):
        os.mkdir(DIR_PROCESSED)

    files_to_process = get_files_to_process()

    # progress bar
    files_qty = 1
    files_qty = files_qty * len(color_of_n) * len(files_to_process)
    exported_files = 0

    if files_to_process:
        for file_to_process in files_to_process:
            file_name = os.path.splitext(file_to_process)[0]
            file_to_process = os.path.join(DIR_FILES_TO_PROCESS, file_to_process)

            dir_to_save = os.path.join(DIR_PROCESSED, file_name)
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)

            # 2 necessaires
            psd_file = os.path.join(DIR_PSD_NECESSAIRES, '2necessaires.psd')
            opened = app.openPSD(psd_file)
            if opened:
                app.update_layer_image('necessaire1_image', file_to_process)
                app.update_layer_image('necessaire2_image', file_to_process)
                for color in color_of_n:
                    img_name = f"{file_name}_1_zipper_{COLOR_OF_NECESSAIRE_ZIPPER[color].get('color')}.jpg"
                    app.update_layer_color('zipper1_color', COLOR_OF_NECESSAIRE_ZIPPER[color].get('rgb'))
                    app.update_layer_color('zipper2_color', COLOR_OF_NECESSAIRE_ZIPPER[color].get('rgb'))
                    app.exportJPEG(img_name, dir_to_save)
                    exported_files += 1
                    print("\r", "{:.2f}".format(exported_files / files_qty * 100), " percent complete...", end='')
                app.closePSD()

            if del_files == 'Y':
                os.remove(file_to_process)


if __name__ == '__main__':
    option = 99999
    app_obj = None
    app_visible = CONFIG['DEFAULT']['AppVisible']
    close_photoshop = CONFIG['DEFAULT']['ClosePhotoshop']
    if CONFIG['DEFAULT']['DeleteOriginFiles'] == 'no':
        delete_origin_files = 'N'
    else:
        delete_origin_files = 'Y'
    last_option = None
    run_last_option = False

    while option != 99:
        try:
            print('')
            clear_console()

            if CONFIG['DEFAULT']['DeleteOriginFiles'] == 'inquire':
                delete_origin_files = (input('Would you like to DELETE the original files? Y or N: (Y)') or 'Y').upper()

            menu = '-------------------------\n'
            if last_option:
                menu += '0 - PREVIOUS SETUP \n'
            else:
                last_option = [0, 0, 0]

            menu += '1 - Generate Mugs\n' \
                    '2 - Generate Bottles\n' \
                    '3 - Generate Heart Mugs\n' \
                    '4 - Necessaires\n' \
                    '-------------------------\n' \
                    'Your option (0): '

            option = int(input(menu) or 0)

            if option == 0:
                option = last_option[0]
                run_last_option = True
            else:
                last_option[0] = option
                run_last_option = False

            if option in (1, 3):

                # build kind of mugs menu
                clear_console()
                if run_last_option:
                    kind_of_mugs = last_option[1]
                else:
                    if option == 1:
                        menu = '-------------------------\n' \
                               'What KIND OF MUGS do you need? \n' \
                               '1 - ALL\n' \
                               '2 - Art and Two Mugs\n' \
                               '3 - Tree Mugs Together\n' \
                               '4 - Tree Mugs Apart\n' \
                               '-------------------------\n' \
                               'Your option (1): '
                    if option == 3:
                        menu = '-------------------------\n' \
                               'What KIND OF MUGS do you need? \n' \
                               '1 - ALL\n' \
                               '2 - Art and Two Mugs\n' \
                               '3 - Tree Mugs Apart\n' \
                               '-------------------------\n' \
                               'Your option (1): '
                    kind_of_mugs = int(input(menu) or 1)
                last_option[1] = kind_of_mugs

                # build colors of mugs menu
                clear_console()
                if run_last_option:
                    color_of_mugs = last_option[2]
                else:
                    menu = '-------------------------\n' \
                           'What COLORS OF MUGS do you need? \n'
                    for key, value in (COLOR_OF_MUGS if option == 1 else COLOR_OF_MUGS_HEART).items():
                        menu += f"{key} - {value.get('color')}\n"
                    menu += '-------------------------\n' \
                            'Your options (1): '
                    color_of_mugs = input(menu) or '1'
                    color_of_mugs = color_of_mugs.split(',')
                    color_of_mugs = [x.strip() for x in color_of_mugs]

                last_option[2] = color_of_mugs

                app_obj = Photoshopy(app_visible)
                if option == 1:
                    run_mugs(app_obj, kind_of_mugs, color_of_mugs, delete_origin_files)
                if option == 3:
                    run_mugs_heart(app_obj, kind_of_mugs, color_of_mugs, delete_origin_files)
                if close_photoshop == 'yes':
                    app_obj.closePhotoshop()

            elif option == 2:

                # build kind of bottles
                clear_console()
                if run_last_option:
                    kind_of_bottles = last_option[1]
                else:
                    menu = '-------------------------\n' \
                           'What KIND OF BOTTLES do you need? \n' \
                           '1 - Aluminum 750 ML\n' \
                           '-------------------------\n' \
                           'Your option (1): '
                    kind_of_bottles = int(input(menu) or 1)

                last_option[1] = kind_of_bottles

                # build colors of bottles menu
                clear_console()
                if run_last_option:
                    color_of_bottles = last_option[2]
                else:
                    menu = '-------------------------\n' \
                           'What COLORS OF BOTTLES do you need? \n'
                    for key, value in COLOR_OF_BOTTLES[str(kind_of_bottles)].items():
                        menu += f"{key} - {value.get('color')}\n"
                    menu += '-------------------------\n' \
                            'Your options (1): '
                    color_of_bottles = input(menu) or '1'
                    color_of_bottles = color_of_bottles.split(',')
                    color_of_bottles = [x.strip() for x in color_of_bottles]

                last_option[2] = color_of_bottles

                app_obj = Photoshopy(app_visible)
                run_bottles(app_obj, kind_of_bottles, color_of_bottles, delete_origin_files)
                if close_photoshop == 'yes':
                    app_obj.closePhotoshop()

            elif option == 4:

                # build colors of necessaires
                clear_console()
                if run_last_option:
                    color_of_necessaire_zipper = last_option[2]
                else:
                    menu = '-------------------------\n' \
                           'What COLORS OF NECESSAIRE ZIPPERS do you need? \n'
                    for key, value in COLOR_OF_NECESSAIRE_ZIPPER.items():
                        menu += f"{key} - {value.get('color')}\n"
                    menu += '-------------------------\n' \
                            'Your options (1): '
                    color_of_necessaire_zipper = input(menu) or '1'
                    color_of_necessaire_zipper = color_of_necessaire_zipper.split(',')
                    color_of_necessaire_zipper = [x.strip() for x in color_of_necessaire_zipper]

                last_option[2] = color_of_necessaire_zipper

                app_obj = Photoshopy(app_visible)
                run_necessaires(app_obj, color_of_necessaire_zipper, delete_origin_files)
                if close_photoshop == 'yes':
                    app_obj.closePhotoshop()

        except Exception as e:
            print(e)
            if app_obj:
                if app_obj.psd_file:
                    app_obj.closePSD()
                if close_photoshop == 'yes':
                    app_obj.closePhotoshop()





