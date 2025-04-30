import unittest
from flask import current_app
from app import create_app
from app.models.grado import Grado
import os

class GradosTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_grado_creation(self):
        grado = Grado()
        self.assertIsNotNone(Grado)

    def test_grado_attributes(self):
        grado = Grado()
        grado.nombre = "com9"
        
        self.assertEqual(grado.nombre, "com9")

    def test_grado_equality(self):
        g1 = Grado()
        g2 = Grado()

        g1.nombre = g2.nombre = "com2"
        
        self.assertEqual(g1, g2)