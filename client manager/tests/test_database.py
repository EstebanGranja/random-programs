import unittest
import copy
import helpers
import database as db
import config
import csv

class TestDataBase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente("40154711", "Chino", "Maidana"),
            db.Cliente("34221409", "Marta", "Tarot"),
            db.Cliente("29605755", "Ricardo", "Fort"),
            ]
    

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("40154711")
        cliente_inexistente = db.Clientes.buscar("12442711")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)


    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear("45555741", "Jose", "Manolo")
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "45555741")
        self.assertEqual(nuevo_cliente.nombre, "Jose")
        self.assertEqual(nuevo_cliente.apellido, "Manolo")


    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar("40154711"))
        cliente_modificado = db.Clientes.modificar("40154711", "Carlos", "Maidana")
        self.assertEqual(cliente_a_modificar.nombre, "Chino")
        self.assertEqual(cliente_modificado.nombre, "Carlos")

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("40154711")
        cliente_rebuscar = db.Clientes.buscar("40154711")
        self.assertEqual(cliente_borrado.dni, "40154711")
        self.assertIsNone(cliente_rebuscar) 

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('12345678', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('0000', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F1234567', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('40154711', db.Clientes.lista))


    def test_escritura_csv(self):
        db.Clientes.borrar('40154711')
        db.Clientes.borrar('29605755')
        db.Clientes.modificar('34221409', 'Ricardo', 'Montaner')

        nombre, apellido, dni = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            nombre, apellido, dni = next(reader)

        self.assertEqual(nombre, 'Ricardo')
        self.assertEqual(apellido, 'Montaner')
        self.assertEqual(dni, '34221409')