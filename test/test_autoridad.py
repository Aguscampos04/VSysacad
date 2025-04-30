import unittest
from flask import current_app
from app import create_app
from app.models.autoridad import Autoridad
import os

class AutoridadsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_autoridad_creation(self):
        autoridad = Autoridad()
        self.assertIsNotNone(Autoridad)

    def test_autoridad_attributes(self):
        autoridad = Autoridad()
        autoridad.nombre = "autor1"
        autoridad.cargo = "administrador"
        autoridad.telefono = "2604028628"
        
        self.assertEqual(autoridad.nombre, "autor1")
        self.assertEqual(autoridad.cargo, "administrador")
        self.assertEqual(autoridad.telefono, "2604028628")

    def test_autoridad_equality(self):
        a1 = Autoridad()
        a2 = Autoridad()

        a1.nombre = a2.nombre = "autor2"
        a2.cargo = a2.cargo = "admin"
        
        self.assertEqual(a1, a2)