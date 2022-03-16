import sys, os
import unittest
from photoshopy import Photoshopy


class TestPhotoshopy(unittest.TestCase):
    def setUp(self) -> None:
        self.psd_origin = os.path.abspath("./resources/my_tests.psd")
        self.jpeg_path = os.path.abspath("./resources/tmp")
        self.jpeg_name = "my_tests.jpg"
        self.jpeg_full_path = os.path.join(self.jpeg_path, self.jpeg_name)
        self.image_to_replace_full_path = os.path.abspath("./resources/chris.jpg")

        if not os.path.exists(self.jpeg_path):
            os.mkdir(self.jpeg_path)

        self.app = Photoshopy()

    def tearDown(self) -> None:
        self.app.closePhotoshop()

        if os.path.exists(self.jpeg_full_path):
            os.remove(self.jpeg_full_path)

        if os.path.exists(self.jpeg_path):
            os.rmdir(self.jpeg_path)

    def test_OpenPSD(self):
        opened = self.app.openPSD(self.psd_origin)
        if opened:
            self.app.closePSD()
        self.assertTrue(opened)

    def test_update_layer_text(self):
        updated_1 = False
        updated_2 = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            updated_1 = self.app.update_layer_text('Texto 1', 'Tiago')
            updated_2 = self.app.update_layer_text('Texto 2', 'Bastos')
            self.app.closePSD()

        self.assertTrue(updated_1)
        self.assertTrue(updated_2)

    def test_exportJPEG(self):
        exported = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            self.app.update_layer_text('Texto 1', 'Tiago')
            self.app.update_layer_text('Texto 2', 'Bastos')

            exported = self.app.exportJPEG(self.jpeg_name, self.jpeg_path)
            self.app.closePSD()

        self.assertTrue(exported)

    def test_update_layer_image(self):
        updated = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            updated = self.app.update_layer_image('foto', self.image_to_replace_full_path)
            self.app.closePSD()

        self.assertTrue(updated)

    def test_update_layer_color(self):
        updated = False

        opened = self.app.openPSD(self.psd_origin)
        if opened:
            updated = self.app.update_layer_color('bg_color_2', (0,255,0))
            self.app.closePSD()

        self.assertTrue(updated)

if __name__ == '__main__':
    unittest.main()