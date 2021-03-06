import unittest
from src.logica.Suma import Suma

class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma = Suma()

    def tearDown(self):
        self.suma=None

    def test_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        # Arrange
        self.sumando1=19
        self.sumando2=50
        self.resultadoesperado=69

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)

    def test_operacionSuma_dosNumerosNegativos_retornaSuma(self):
        # Arrange
        self.sumando1=-3
        self.sumando2=-7
        self.resultadoesperado=-10

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.sumando1,self.sumando2)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)

    def test_operacionResta_dosNumerosPositivos_retornaResta(self):
        # Arrange
        self.minuendo=50
        self.sustraendo=30
        self.resultadoesperado=20

        # Do
        self.resultadoActual=self.suma.operacionResta(self.minuendo,self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)
