import unittest
from flask import current_app
from app import create_app
from app.models.tipodedicacion import TipoDedicacion
import os

class TipoDedicacionsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_tipodedicacion_creation(self):
        tipo = TipoDedicacion()
        self.assertIsNotNone(TipoDedicacion)

    def test_tipodedicacion_attributes(self):
        tipo = TipoDedicacion()
        tipo.nombre = "Medico"
        tipo.observacion = "Excelente"
        tipo.puntos = "8"
        
        self.assertEqual(tipo.nombre, "Medico")
        self.assertEqual(tipo.observacion, "Excelente")
        self.assertEqual(tipo.puntos, "8")

    def test_tipodedicacion_equality(self):
        td1 = TipoDedicacion()
        td2 = TipoDedicacion()

        td1.nombre = td2.nombre = "ingeniero"
        td1.puntos = td2.puntos = "7"
        
        self.assertEqual(td1, td2)