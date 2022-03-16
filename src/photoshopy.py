import win32com.client
import os
from pathvalidate import sanitize_filename


class Photoshopy:
    app = None
    psd_file = None

    def __init__(self):
        self.app = win32com.client.Dispatch("Photoshop.Application")
        # self.app.Visible = False

    def closePhotoshop(self):
        self.app.Quit()

    def openPSD(self, filename):
        if os.path.isfile(filename) == False:
            self.closePhotoshop()
            return False

        self.app.Open(filename)
        self.psd_file = self.app.Application.ActiveDocument
        return True

    def closePSD(self):
        if self.psd_file is None:
            raise Exception(FileNotFoundError)

        self.app.Application.ActiveDocument.Close(2)
        self.psd_file = None

        return True

    def update_layer_text(self, layer_name, text):
        if not self.psd_file:
            raise Exception(FileNotFoundError)
        layer = self.psd_file.ArtLayers[layer_name]
        layer_text = layer.TextItem
        layer_text.contents = text
        return True

    def update_layer_image(self, layer_name, full_path_image):
        if not self.psd_file:
            raise Exception(FileNotFoundError)
        layer = self.psd_file.ArtLayers[layer_name]
        self.psd_file.ActiveLayer = layer

        # edit content command - open psb file
        type_id = self.app.Application.StringIDToTypeID("placedLayerEditContents")
        action_descriptor = win32com.client.Dispatch("Photoshop.ActionDescriptor")
        self.app.Application.ExecuteAction(type_id, action_descriptor, 1)

        # replace content
        type_id = self.app.Application.StringIDToTypeID("placedLayerReplaceContents")
        id_null = self.app.Application.CharIDToTypeID("null")
        action_descriptor = win32com.client.Dispatch("Photoshop.ActionDescriptor")
        action_descriptor.PutPath(id_null, full_path_image)
        idPgNm = self.app.Application.CharIDToTypeID("PgNm")
        action_descriptor.PutInteger(idPgNm, 1)
        self.app.Application.ExecuteAction(type_id, action_descriptor, 2)

        # close psb file
        self.app.Application.ActiveDocument.Close(1)

        return True

    def update_layer_color(self, layer_name, color):
        if not self.psd_file:
            raise Exception(FileNotFoundError)
        layer = self.psd_file.ArtLayers[layer_name]
        self.psd_file.ActiveLayer = layer

        fill_color = win32com.client.Dispatch("Photoshop.SolidColor")
        fill_color.rgb.red = 0
        fill_color.rgb.green = 255
        fill_color.rgb.blue = 0
        sel = self.app.Application.ActiveDocument.Selection
        sel.Fill(fill_color, 2, 100, False)

        return True

    def exportJPEG(self, filename, folder='', quality=80):
        if not self.psd_file:
            raise Exception(FileNotFoundError)
        filename = sanitize_filename(filename)
        full_path = os.path.join(folder, filename)

        options = win32com.client.Dispatch("Photoshop.ExportOptionsSaveForWeb")
        # jpg
        options.Format = 6
        options.Quality = quality

        self.psd_file.Export(ExportIn=full_path, ExportAs=2, Options=options)

        return os.path.isfile(full_path)

