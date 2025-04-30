import unittest
from flask import current_app
from app import create_app
from app.models.tipoespecialidad import TipoEspecialidad
import os

class TipoEspecialidadsTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_tipoespecialidad_creation(self):
        tipoe = TipoEspecialidad()
        self.assertIsNotNone(TipoEspecialidad)

    def test_tipoespecialidad_attributes(self):
        tipoe = TipoEspecialidad()
        tipoe.nombre = "ciber"
        tipoe.nivel = "medio"
        tipoe.observacion = "bueno"
        
        self.assertEqual(tipoe.nombre, "ciber")
        self.assertEqual(tipoe.nivel, "medio")
        self.assertEqual(tipoe.observacion, "bueno")

    def test_tipoespecialidad_equality(self):
        te = TipoEspecialidad()
        te1= TipoEspecialidad()

        te.nombre = te1.nombre = "encodear"
        te.sigla = te1.sigla = "enc"
        
        self.assertEqual(te ,te1)