import unittest
from flask import current_app
from app import create_app
from app.models.materia import Materia
import os

class MateriasTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_materia_creation(self):
        materia = Materia()
        self.assertIsNotNone(Materia)

    def test_materia_attributes(self):
        materia= Materia()
        materia.nombre = "desarrollo"
        materia.codigo = "459"
        materia.observacion = "compleja"
        
        self.assertEqual(materia.nombre, "desarrollo")
        self.assertEqual(materia.codigo, "459")
        self.assertEqual(materia.observacion, "compleja")

    def test_materia_equality(self):
        m1 = Materia()
        m2 = Materia()

        m1.nombre = m2.nombre = "Derecho"
        m1.codigo = m2.codigo = "457"
        
        self.assertEqual(m1, m2)