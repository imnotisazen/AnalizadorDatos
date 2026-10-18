
from django.test import TestCase
from django.urls import reverse


class AnalizadorTests(TestCase):

    def convertir(self, numero, base):
        return self.client.post(reverse("inicio"), {
            "accion": "convertir",
            "numero": numero,
            "base": base,
        })

    def test_pagina_principal(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_decimal(self):
        respuesta = self.convertir("255", "10")
        resultado = respuesta.context["resultado"]
        self.assertEqual(resultado["hexadecimal"], "FF")
        self.assertEqual(resultado["binario"], "11111111")

    def test_binario(self):
        respuesta = self.convertir("1010", "2")
        self.assertEqual(
            respuesta.context["resultado"]["decimal"], 10
        )

    def test_octal(self):
        respuesta = self.convertir("377", "8")
        self.assertEqual(
            respuesta.context["resultado"]["decimal"], 255
        )

    def test_hexadecimal(self):
        respuesta = self.convertir("FF", "16")
        self.assertEqual(
            respuesta.context["resultado"]["decimal"], 255
        )

    def test_ajuste_bytes(self):
        respuesta = self.convertir("256", "10")
        resultado = respuesta.context["resultado"]
        self.assertEqual(resultado["bits"], 9)
        self.assertEqual(resultado["bytes"], 2)
        self.assertEqual(
            resultado["binario"], "0000000100000000"
        )

    def test_numero_vacio(self):
        respuesta = self.convertir("", "10")
        self.assertIsNotNone(respuesta.context["error"])

    def test_digitos_invalidos(self):
        respuesta = self.convertir("102", "2")
        self.assertIsNotNone(respuesta.context["error"])

    def test_base_invalida(self):
        respuesta = self.convertir("100", "3")
        self.assertIsNotNone(respuesta.context["error"])

    def test_numero_negativo(self):
        respuesta = self.convertir("-5", "10")
        self.assertIsNotNone(respuesta.context["error"])

    def test_fuera_de_rango(self):
        respuesta = self.convertir("65536", "10")
        self.assertIsNotNone(respuesta.context["error"])

    def test_utf8_con_enie(self):
        respuesta = self.client.post(reverse("inicio"), {
            "accion": "texto",
            "texto": "Año",
        })
        caracteres = respuesta.context["texto_resultado"]
        self.assertEqual(caracteres[1]["decimal"], 241)
        self.assertEqual(caracteres[1]["unicode"], "U+00F1")
        self.assertEqual(caracteres[1]["utf8"], "C3 B1")

    def test_texto_vacio(self):
        respuesta = self.client.post(reverse("inicio"), {
            "accion": "texto",
            "texto": "",
        })
        self.assertIsNotNone(respuesta.context["error_texto"])

    def test_texto_mayor_20(self):
        respuesta = self.client.post(reverse("inicio"), {
            "accion": "texto",
            "texto": "A" * 21,
        })
        self.assertIsNotNone(respuesta.context["error_texto"])
