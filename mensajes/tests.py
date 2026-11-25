from django.template import Context, Template
from django.test import TestCase
from django.urls import reverse

from .models import Mensaje


class PruebasMensaje(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mensaje = Mensaje.objects.create(texto="Esta es una prueba.")

    def test_contenido_modelo(self):
        self.assertEqual(self.mensaje.texto, "Esta es una prueba.")

    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/", secure=True)
        self.assertEqual(respuesta.status_code, 200)

    def test_pagina_inicio(self):
        respuesta = self.client.get(reverse("inicio"), secure=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "inicio.html")
        self.assertContains(respuesta, "Esta es una prueba.")

    def test_str_modelo(self):
        self.assertEqual(str(self.mensaje), "Esta es una prueba.")

    def test_muestra_fecha_en_inicio(self):
        fecha_formateada = Template('{{ fecha|date:"j \\d\\e F, H:i" }}').render(
            Context({"fecha": self.mensaje.fecha})
        )
        respuesta = self.client.get(reverse("inicio"), secure=True)
        self.assertContains(respuesta, fecha_formateada)


class PruebasTableroVacio(TestCase):
    def test_tablero_vacio_muestra_mensaje(self):
        respuesta = self.client.get(reverse("inicio"), secure=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Todavía no hay mensajes.")
