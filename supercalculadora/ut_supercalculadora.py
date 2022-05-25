import unittest
import supercalculadora
import expr_aritmetica
import ut_calculadora
import ut_expr_aritmetica


# class TestsSupercalculadora(unittest.TestCase):
#     def test_sumar(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("4", sc.calcular("2 + 2"))

#     def test_restar(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("0", sc.calcular("2 - 2"))

#     def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("6", sc.calcular("5 + 4 - 3"))

#     def test_expresion_compleja_sin_parentesis_con_precedencia(self):
#         sc = supercalculadora.Supercalculadora(
#             expr_aritmetica.ExprAritmetica())
#         self.assertEqual("3", sc.calcular("5 + 4 / 2 - 4"))


class TestsSupercalculadora(unittest.TestCase):
    """_summary_
        Clase TestsSupercalculadora
    Args:
        unittest (module): Modulo de test unitarios, importa la alse TestCase
    """
    def setUp(self):
        """_summary_
            Funcion setUp
            Crear un objeto supercalculadora con parametro objeto ExprAritmetica
        """
        "añadido setup y teardown debajo"
        self.sc = supercalculadora.Supercalculadora(
            expr_aritmetica.ExprAritmetica())

    def tearDown(self):
        """_summary_
            Funcion tearDown
        """
        pass

    def test_sumar(self):
        """_summary_
            Funcion test_sumar
            Hace un test unitario de suma mediante un assertEqual con valores "4", metodo calcular de objeto sccon valores "2+2"
        """
        self.assertEqual("4", self.sc.calcular("2 + 2"))

    def test_restar(self):
        """_summary_
            Funcion test_restar
            Hace un test unitario de resta mediante un assertEqual con valores "0", sc con metodo calcular valores("2-2")
        """
        self.assertEqual("0", self.sc.calcular("2 - 2"))

    def test_expresion_compleja_sin_parentesis_sin_precedencia(self):
        """_summary_
            Funcion test_expresion_compleja_sin_parentesis_sin_precedencia
            Hace un test unitario de expresion compleja sin parentesis, mediante un assertEqual con valores "6" y metodo calcular valores "5+4-3"
        """
        self.assertEqual("6", self.sc.calcular("5 + 4 - 3"))

# añade función de simplificar
    def test_expresion_compleja_sin_parentesis_con_precedencia(self):
        """_summary_
            Funcion test_expresion_compleja_sin_parentesis_con_precedencia
            Realiza 4 test unitarios con la funcion con distintos valores vara verificar que tiene precedencia
        """
        self.assertEqual("3", self.sc.calcular("5 + 4 / 2 - 4"))
        self.assertEqual("-1", self.sc.calcular("4 / 2 - 3"))
        self.assertEqual("1", self.sc.calcular("4 / 2 - 3 + 1 + 6 / 3 - 1"))
        self.assertEqual(
            "-8", self.sc.calcular("4 / -2 + 3 + -1 + -6 / -3 - 10"))
