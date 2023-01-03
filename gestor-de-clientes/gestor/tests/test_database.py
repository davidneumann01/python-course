import copy
import unittest
import database as db
import helpers
import csv
import config


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente('15J', 'Caroline', 'Jons'),
            db.Cliente('34K', 'Juanito', 'Mendoza'),
            db.Cliente('31X', 'Brisa', 'Mandeline')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_no_existente = db.Clientes.buscar('98B')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('91V', 'Rodriguez', 'Antonio')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '91V')
        self.assertEqual(nuevo_cliente.nombre, 'Rodriguez')
        self.assertEqual(nuevo_cliente.apellido, 'Antonio')

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('31X'))
        cliente_modificado = db.Clientes.modificar('31X', 'Josefine', 'Alverdes')
        self.assertEqual(cliente_a_modificar.nombre, 'Brisa')
        self.assertEqual(cliente_modificado.nombre, 'Josefine')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('34K')
        cliente_rebuscado = db.Clientes.buscar('34K')
        self.assertNotEqual(cliente_borrado, cliente_rebuscado)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('20H', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('39137A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('H14', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('34K', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('34K')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('31X', 'Josefine', 'Alverdes')

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader)  # Primera linea del iterador

        self.assertEqual(dni, '31X')
        self.assertEqual(nombre, 'Josefine')
        self.assertEqual(apellido, 'Alverdes')


if __name__ == '__main__':
    unittest.main()
