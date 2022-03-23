from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models
from django.urls import reverse
import uuid


class WebPassword(models.Model):
    password = models.CharField(
        max_length=50, help_text='Introduce la contraseña para el sitio web', verbose_name='Contraseña')
    is_required = models.BooleanField(
        default=False, help_text='¿Quieres que la web tenga contraseña?', verbose_name='Activada')

    class Meta:
        verbose_name = ("Contraseña")
        verbose_name_plural = ("Contraseña Global")

    def __str__(self):
        return "Contraseña"


class Cancion(models.Model):
    nombre = models.CharField(
        max_length=50, help_text='¡Escribe una canción que quieres que suene en la fiesta!', verbose_name='Canción')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID única asociada a la canción")

    class Meta:
        verbose_name = ("Canción")
        verbose_name_plural = ("Canciones")

    def __str__(self):
        return "Cancion"


class Confirmacion(models.Model):
    ASISTIRAS = (
        (None, ''),
        (True, '¡Sí!, contad conmigo'),
        (False, 'No voy a poder asistir')
    )
    NUMERO_ACOMPANANTES = (
        ('0', 'Iré solo'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                           help_text="ID única asociada a la confirmación")
    asistiras = models.BooleanField(
        default=None, help_text='¿Asistirás?', verbose_name='Asistirás', choices=ASISTIRAS, null=False)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(
        max_length=50, help_text='Introduce tu nombre', verbose_name='Nombre')
    surname = models.CharField(
        max_length=50, help_text='Introduce tu apellido', verbose_name='Apellido')
    bus_ida = models.BooleanField(
        default=False, help_text='¿Necesitarás autobús de ida?', verbose_name='Autobús de ida')
    bus_vuelta = models.BooleanField(
        default=False, help_text='¿Necesitarás autobús de vuelta?', verbose_name='Autobús de vuelta')
    acompanantes = models.CharField(
        max_length=1, help_text='Número de acompañantes', verbose_name='Número', default='', choices=NUMERO_ACOMPANANTES)
    nombres_acompanantes = models.TextField(max_length=500, help_text='Escribe los nombres de los acompañantes, uno por línea.',
                                            verbose_name='Información acompañantes', blank=True, null=True)
    nombre_cancion = models.CharField(max_length=50, help_text='¡Introduce una canción que quieres que suene durante la fiesta!',
                                      verbose_name='Canción', blank=True, null=True)
    nombre_grupo = models.CharField(max_length=50, help_text='¡Introduce el grupo de la canción que quieres que suene durante la fiesta!',
                                    verbose_name='Grupo', blank=True, null=True)
    food_restrictions = models.BooleanField(
        default=False, help_text='¿Tienes especificaciones alimentarias? (Alergias, vegetariano, no como carne...)', verbose_name='Alergias alimentarias / Otros')
    food_restrictions_especificaciones = models.TextField(max_length=500, help_text='Especifica, en caso de tener acompañante, quién tiene la alergia/otro (Por ejemplo: "Ana no come carne")',
                                                          verbose_name='Alergias alimentarias / Otros', blank=True, default='')

    class Meta:
        verbose_name = ("confirmación")
        verbose_name_plural = ("Confirmaciones")

    def __str__(self):
        return self.name


class Autobus(models.Model):
    TIPO_BUS = (
        ('i', 'Ida'),
        ('v', 'Vuelta')
    )
    site_type = models.CharField(
        max_length=1,
        choices=TIPO_BUS,
        blank=False,
        default='',
        help_text='Escoge el tipo de viaje',
        verbose_name='Tipo de viaje'
    )
    origen = models.CharField(
        max_length=50, help_text='Introduce el nombre del origen', verbose_name='Origen', primary_key=True)
    destino = models.CharField(
        max_length=50, help_text='Introduce el nombre del sitio', verbose_name='Destino')
    time = models.TimeField(
        verbose_name="Hora de salida", help_text="Introduce la hora de salida")

    class Meta:
        verbose_name = "autobús"
        verbose_name_plural = "Autobuses"

    def __str__(self):
        return self.origen + " -> " + self.destino


class Itinerario(models.Model):
    name = models.CharField(
        max_length=200, help_text="Introduce el nombre del evento (p.e Salida autobus Pamplona)", verbose_name="Nombre")
    description = models.TextField(
        max_length=1000, help_text="Introduce una descripción para el evento", verbose_name="Descripción del evento", blank=True)
    start_time = models.TimeField(
        verbose_name="Hora inicio", help_text="Introduce la hora de inicio")
    end_time = models.TimeField(
        verbose_name="Hora fin", help_text="Introduce la hora de finalización", blank=True, null=True)
    location_name = models.CharField(
        max_length=50, help_text='Introduce el nombre de la localización', verbose_name='Nombre localización', blank=True)
    location_url = models.URLField(help_text='Introduce el enlace a google maps',
                                   verbose_name="Enlace a Google Maps", max_length=2000, default="", blank=True)
    image = models.URLField(help_text='Introduce el enlace de la fotografía',
                            verbose_name="Enlace a la imagen", max_length=2000, default="")

    class Meta:
        verbose_name = ("evento")
        verbose_name_plural = ("Itinerario")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Itinerario_detail", kwargs={"pk": self.pk})


class LugarDeLaBoda(models.Model):
    name = models.CharField(max_length=40, verbose_name="Lugar de la boda",
                            help_text="Este es el texto que aparecerá en la página principal")
    mensaje = models.CharField(max_length=100, verbose_name="Mensaje",
                               help_text="Este es el texto que aparecerá en la página principal p.e.\"¡Estás invitado a la boda!\" ")
    location_url = models.URLField(help_text='Introduce el enlace a google maps',
                                   verbose_name="Enlace a Google Maps", max_length=2000, default="", blank=True)

    class Meta:
        verbose_name = ("Lugar de la boda")
        verbose_name_plural = ("_Lugar de la boda")

    def __str__(self):
        return self.name


class NombresPareja(models.Model):
    novio = models.CharField(
        max_length=50, verbose_name="Nombre novio", help_text="Introduce el nombre del novio")
    novia = models.CharField(max_length=50, verbose_name="Nombre novia",
                             help_text="Introduce el nombre de la novia")
    descripcion_novio = models.TextField(max_length=400, verbose_name="Descripción novio",
                                         help_text="Introduce descripción del novio (déjalo en blanco si no quieres que aparezca nada)", blank=True, default="")
    descripcion_novia = models.TextField(max_length=400, verbose_name="Descripción novia",
                                         help_text="Introduce descripción de la novia (déjalo en blanco si no quieres que aparezca nada)", blank=True, default="")

    class Meta:
        verbose_name = ("Nombre")
        verbose_name_plural = ("_Nombres pareja")

    def __str__(self):
        return self.novio

    def get_absolute_url(self):
        return reverse("NombresPareja_detail", kwargs={"pk": self.pk})


class FechaDeBoda(models.Model):
    fecha = models.DateTimeField(
        verbose_name="Fecha de la boda", help_text="Introduce la fecha y hora de la boda")

    class Meta:
        verbose_name = ("Fecha de la boda")
        verbose_name_plural = ("_Fecha de la boda")

    def __str__(self):
        return "Fecha boda"

    def get_year(self):
        return self.fecha.year

    def get_month(self):
        return self.fecha.month

    def get_day(self):
        return self.fecha.day


class ItinerarioHeader(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre header",
                            help_text="Este es el texto que aparecerá en la página principal")
    description = models.CharField(max_length=150, verbose_name="Descripcion header",
                                   help_text="Esta es la descripcion que aparecerá debajo del título en la página principal")

    class Meta:
        verbose_name = ("Titulo Itinerario")
        verbose_name_plural = ("_Titulo Itinerario")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ItinerarioHeader_detail", kwargs={"pk": self.pk})
