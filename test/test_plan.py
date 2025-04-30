import unittest
from flask import current_app
from app import create_app
from app.models.plan import Plan
import os

class PlansTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_plan_creation(self):
        plan = Plan()
        self.assertIsNotNone(Plan)

    def test_plan_attributes(self):
        plan = Plan()
        plan.nombre = "pls"
        plan.fechaFin = "07/05"
        plan.fechaInicio = "26/04"

        self.assertEqual(plan.nombre, "pls")
        self.assertEqual(plan.fechaFin, "07/05")
        self.assertEqual(plan.fechaInicio, "26/04")

    def test_plan_equality(self):
        p1 = Plan()
        p2 = Plan()

        p1.nombre = p2.nombre = "lpo"
        p2.fechaFin = p2.fechaFin = "11/11"
        
        self.assertEqual(p1, p2)