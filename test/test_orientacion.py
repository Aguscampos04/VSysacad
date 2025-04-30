import unittest
from flask import current_app
from app import create_app
from app.models.orientacion import Orientacion
import os

class OrientacionsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_orientacion_creation(self):
        orientacion = Orientacion()
        self.assertIsNotNone(Orientacion)

    def test_orientacion_attributes(self):
        orientacion = Orientacion()
        orientacion.nombre = "nose"
        
        self.assertEqual(orientacion.nombre, "nose")

    def test_orientacion_equality(self):
        o1 = Orientacion()
        o2 = Orientacion()

        o1.nombre = o2.nombre = "nose2"
        
        self.assertEqual(o1, o2)