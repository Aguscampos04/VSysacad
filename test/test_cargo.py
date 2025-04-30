import unittest
from flask import current_app
from app import create_app
from app.models.cargo import Cargo
import os

class CargosTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo()
        self.assertIsNotNone(Cargo)

    def test_cargo_attributes(self):
        cargo = Cargo()
        cargo.nombre = "profesor"
        cargo.puntos = "10"
        
        self.assertEqual(cargo.nombre, "profesor")
        self.assertEqual(cargo.puntos, "10")
       

    def test_cargo_equality(self):
        c1 = Cargo()
        c2 = Cargo()

        c1.nombre = c2.nombre = "alumno"
        c1.puntos = c2.puntos = "9"
        
        self.assertEqual(c1, c2)