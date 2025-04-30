import unittest
from flask import current_app
from app import create_app
from app.models.alumno import Alumno
import os

class AlumnosTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_alumno_creation(self):
        alumno = Alumno()
        self.assertIsNotNone(Alumno)

    def test_alumno_attributes(self):
        alumno = Alumno()
        alumno.nombre = "Nacho"
        alumno.apellido = "Peña"
        alumno.nrodocumento = "45719602"
        
        self.assertEqual(alumno.nombre, "Nacho")
        self.assertEqual(alumno.apellido, "Peña")
        self.assertEqual(alumno.nrodocumento, "45719602")

    def test_alumno_equality(self):
        a1 = Alumno()
        a2 = Alumno()

        a1.nombre = a2.nombre = "Loana"
        a1.apellido = a2.apellido = "Vargas"
        
        self.assertEqual(a1, a2)