import unittest
from flask import current_app
from app import create_app
from app.models.especialidad import Especialidad
import os

class EspecialidadsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_especialidad_creation(self):
        especialidad = Especialidad()
        self.assertIsNotNone(Especialidad)

    def test_especialidad_attributes(self):
        especialidad = Especialidad()
        especialidad.nombre = "sistemas"
        especialidad.letra = "S"
        especialidad.observacion = "buenos"
        
        self.assertEqual(especialidad.nombre, "sistemas")
        self.assertEqual(especialidad.letra, "S")
        self.assertEqual(especialidad.observacion, "buenos")

    def test_especialidad_equality(self):
        e1 = Especialidad()
        e2 = Especialidad()

        e1.nombre = e2.nombre = "Rata"
        e1.letra = e2.letra = "R"
        
        self.assertEqual(e1, e2)