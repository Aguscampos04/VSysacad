import unittest
from flask import current_app
from app import create_app
from app.models.departamento import Departamento
import os

class DepartamentosTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_departamento_creation(self):
        departamento = Departamento()
        self.assertIsNotNone(Departamento)

    def test_departamento_attributes(self):
        departamento = Departamento()
        departamento.nombre = "Economia"
        
        self.assertEqual(departamento.nombre, "Economia")

    def test_departamento_equality(self):
        d1 = Departamento()
        d2 = Departamento()

        d1.nombre = d2.nombre = "quimica"
        
        self.assertEqual(d1, d2)