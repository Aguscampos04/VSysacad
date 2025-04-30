import unittest
from flask import current_app
from app import create_app
from app.models.categoriacargo import CategoriaCargo
import os

class CategoriacargosTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_categoriacargo_creation(self):
        categoria = CategoriaCargo()
        self.assertIsNotNone(CategoriaCargo)

    def test_categoriacargo_attributes(self):
        categoria = CategoriaCargo()
        categoria.nombre = "alto"
        
        self.assertEqual(categoria.nombre, "alto")

    def test_categoriacargo_equality(self):
        cc1 = CategoriaCargo()
        cc2 = CategoriaCargo()

        cc1.nombre = cc2.nombre = "medio"
        
        self.assertEqual(cc1, cc2)