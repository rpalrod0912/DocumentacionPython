import unittest
import calculadora


class TestCalculadora(unittest.TestCase):
    """_summary_
        Clase TestCalculadora
    Args:
        unittest (module): Sacamos un TestCase del modulo unittest
    """
    def setUp(self):
        """_summary_
            Funcion setUp
            inicializa self.calc como un objeto Calculadora del modulo calculadora
            Returns:
                _type_:None
        """
        self.calc = calculadora.Calculadora()

    def tearDown(self):
        """_summary_
            Funcion tearDown
            pass
        """
        pass

    def test_sumar_2_y_2(self):
        """_summary_
            Funcion test_sumar_2_y_2
            Realiza un assertEqual(4, sel.calc.sumar(2,2))
        """
        self.assertEqual(4, self.calc.sumar(2, 2))

    def test_sumar_5_y_7(self):
        """_summary_
            Funcion test_sumar_5_y_7
            Realiza assertEqual(12, self.calc.sumar(5,7))
        """
        self.assertEqual(12, self.calc.sumar(5, 7))

    def test_sumar_propiedad_conmutativa(self):
        """_summary_
            Funcion test_sumar_propiedad_conmutativas
            Realiza un assertEqual(self.calc.sumar(5,7),self.calc.sumar(7,5))
        """
        self.assertEqual(self.calc.sumar(5, 7),
                         self.calc.sumar(7, 5))

    def test_restar_5_y_3(self):
        """_summary_
            Funcion test_restar_5_y_3
            Realiza un assertEqual(2,self.calc.restar(5,3))
        """
        self.assertEqual(2, self.calc.restar(5, 3))

    def test_restar_2_y_3(self):
        """_summary_
            Funcion test_restar_2_y_3
            Realiza un assertEqual(-1,self.cal.restar(2,3))
        """
        self.assertEqual(-1, self.calc.restar(2, 3))

    def test_restar_no_propiedad_conmutativa(self):
        """_summary_
            test_restar_no_propiedad_conmutativa
            Verifica que la resta sigue propiedad conmutativa
            Realiza un assertNotEqual(self.calc.restar(5,3),self.calc.restar(3,5))
        """
        self.assertNotEqual(self.calc.restar(5, 3),
                            self.calc.restar(3, 5))

    def test_sumar_numeros_negativos(self):
        """_summary_
            Funcion test_sumar_numeros_negativos
            Realiza un assertEqual(0,self.calc.sumar(2,-2))
        """
        self.assertEqual(0, self.calc.sumar(2, -2))

    def test_restar_numeros_negativos(self):
        """_summary_
            Funcion test_restar_numeros_negativos
            Realiza un assertEqual(-7,self.calc.restar(-5,2))
            Lo mismo pero -5 ,(-7,-2)
        """
        self.assertEqual(-7, self.calc.restar(-5, 2))
        self.assertEqual(-5, self.calc.restar(-7, -2))

    def test_division_exacta(self):
        """_summary_
            Funcion test_division_exacta
            Realiza assertEqual(1,self.calc.dividir(2,2))
            Lo mismo pero 2, (10,5)
        """
        self.assertEqual(1, self.calc.dividir(2, 2))
        self.assertEqual(2, self.calc.dividir(10, 5))

    def test_division_exacta_negativa(self):
        """_summary__summary_
            Funcion test_division_exacta_negativa
            Realiza assertEqual(-2,self.calc.dividir(10,-5))
            Realiza assertEqual 2, (-10,-5)

        """
        self.assertEqual(-2, self.calc.dividir(10, -5))
        self.assertEqual(2, self.calc.dividir(-10, -5))

    def test_division_no_entera_da_excepcion(self):
        """_summary_
            Funcion test_division_no_entera_da_excepcion
            Realiza un assertEqual(Value,Error, y divide calc valores(3,2))
        """
        self.assertEqual(ValueError, self.calc.dividir(3, 2))

    def test_division_por_0(self):
        """_summary_
            Funcion test_division_por_0s:
            Verificia que no se divide por 0s
        """
        self.assertEqual(ZeroDivisionError, self.calc.dividir(3, 0))
