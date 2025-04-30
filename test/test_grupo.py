import unittest
from flask import current_app
from app import create_app
from app.models.grupo import Grupo
import os

class GruposTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_grupo_creation(self):
        grupo = Grupo()
        self.assertIsNotNone(Grupo)

    def test_grupo_attributes(self):
        grupo = Grupo()
        grupo.nombre = "c06"
        
        self.assertEqual(grupo.nombre, "c06")

    def test_grupo_equality(self):
        g1 = Grupo()
        g2 = Grupo()

        g1.nombre = g2.nombre = "c05"
        
        self.assertEqual(g1, g2)