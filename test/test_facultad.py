import unittest
from flask import current_app
from app import create_app
from app.models.facultad import Facultad
import os

class FacultadsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_facultad_creation(self):
        facultad = Facultad()
        self.assertIsNotNone(facultad)

    def test_facultad_attributes(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ingeniería"
        facultad.sigla = "FI"
        facultad.ciudad = "Córdoba"
        
        self.assertEqual(facultad.nombre, "Facultad de Ingeniería")
        self.assertEqual(facultad.sigla, "FI")
        self.assertEqual(facultad.ciudad, "Córdoba")

    def test_facultad_equality(self):
        f1 = Facultad()
        f2 = Facultad()

        f1.nombre = f2.nombre = "Facultad de Derecho"
        f1.sigla = f2.sigla = "FD"
        
        self.assertEqual(f1, f2)