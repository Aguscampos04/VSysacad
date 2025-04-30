import unittest
from flask import current_app
from app import create_app
from app.models.area import Area
import os

class AreasTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_area_creation(self):
        area = Area()
        self.assertIsNotNone(Area)

    def test_area_attributes(self):
        area = Area()
        area.nombre = "matematica"
        
        self.assertEqual(area.nombre, "matematica")

    def test_area_equality(self):
        a1 = Area()
        a2 = Area()

        a1.nombre = a2.nombre = "Lengua"
        
        self.assertEqual(a1, a2)