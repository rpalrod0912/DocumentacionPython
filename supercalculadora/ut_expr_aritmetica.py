import unittest
import expr_aritmetica

#Clase TestsExprAritmetica() que hereda de la clase unitttest.TestCase
#Funcion setUp-->El valor de expresion = funcion ExprAritemcia de la clase expr_aritmetica
#Funcion

class TestsExprAritmetica(unittest.TestCase):
    """_summary_
        Clase TestsExprAritmetica
    Args:
        unittest (module): importa clase TestCase de el modulo unittest
    """
    def setUp(self):
        """_summary_
            Funcion setUp
            esta expresion igual objeto ExprAritmetica()
        """
        self.expresion = expr_aritmetica.ExprAritmetica()

    def tearDown(self):
        """_summary_
            Funcion tearDown
        """
        pass

    def test_extraer_operandos_y_operadores_en_2_mas_2(self):
        """_summary_
            Funcion test_extrar_operando_y_operadores_en_2_mas_2
            Llama a la funcion assertEqual  con parametros introducidos de diccionario{'Operandos:[2,2],'Operadores:[+]'}
             y como segundo valor estra expresion con funcion parse("2+2")
        """
        self.assertEqual({'Operandos': [2, 2],
                          'Operadores': ['+']},
                         self.expresion.parse("2 + 2"))

    def test_extraer_operandos_y_operadores_en_10_entre_menos_5(self):
        """_summary_
            Funcion test_extraer_operandos_y_operadores_en_10_entre_menos_5
            Realiza la funcion assertEqual extrayendo del diccionario clave operandos los valores 10-5, clave operadores /
            y como segundo valor funcion parse a  expresion con valor "10 /-5"
        """
        self.assertEqual({'Operandos': [10, -5],
                          'Operadores': ['/']},
                         self.expresion.parse("10 / -5"))

    def test_extraer_operandos_y_operadores_en_expr_sin_ptsis(self):
        """_summary_
            Funcion test_extraer_operandos_y_operadores_en_expr_sin_ptsis
            Realiza assert Equal diccionario operandos valores [5,4,2,2], operadores ['+','*','/']
            y segundo parametro expresion.parse ("5+4 * 2 / 2")
        """
        self.assertEqual({'Operandos': [5, 4, 2, 2],
                          'Operadores': ['+', '*', '/']},
                         self.expresion.parse("5 + 4 * 2 / 2"))
