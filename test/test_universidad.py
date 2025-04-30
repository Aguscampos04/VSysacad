import unittest
from flask import current_app
from app import create_app
from app.models.universidad import Universidad
import os

class UniversidadsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_universidad_creation(self):
        universidad = Universidad()
        self.assertIsNotNone(Universidad)

    def test_universidad_attributes(self):
        universidad = Universidad()
        universidad.nombre = "Universidad nacional"
        universidad.abreviatura = "utn"
        universidad.codigoPostal="5600"

        self.assertEqual(universidad.nombre, "Universidad nacional")
        self.assertEqual(universidad.abreviatura, "utn")
        self.assertEqual(universidad.codigoPostal, "5600")

    def test_universidad_equality(self):
        u1 = Universidad()
        u2 = Universidad()

        u1.nombre = u2.nombre = "UM"
        u1.codigoPostal = u2.codigoPostal = "5300"
        
        self.assertEqual(u1, u2)