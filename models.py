from django.db import models

class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    nombre_idioma = models.CharField(max_length=50)
    familia_linguistica = models.CharField(max_length=50)
    nivel_dificultad_promedio = models.CharField(max_length=20)
    num_hablantes_estimado = models.BigIntegerField()
    es_popular = models.BooleanField()

    def __str__(self):
        return self.nombre_idioma

class CursoIdioma(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    nivel_curso = models.CharField(max_length=50)
    duracion_semanas = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cupo_maximo = models.IntegerField()
    horario_clase = models.CharField(max_length=100)
    material_incluido = models.TextField()
    fecha_inicio_oferta = models.DateField()

    def __str__(self):
        return self.nombre_curso

class EstudianteIdioma(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    idioma_nativo = models.CharField(max_length=50)
    fecha_inscripcion = models.DateField()
    nivel_conocimiento_idioma = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ProfesorIdioma(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    idioma_enseñanza = models.CharField(max_length=50)
    nivel_dominio = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario_hora = models.DecimalField(max_digits=5, decimal_places=2)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class InscripcionIdioma(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(EstudianteIdioma, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(CursoIdioma, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado_inscripcion = models.CharField(max_length=50)
    nota_final_curso = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_finalizacion = models.DateField(null=True, blank=True)
    id_profesor_asignado = models.ForeignKey(ProfesorIdioma, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inscripción {self.id_inscripcion}"

class MaterialDidactico(models.Model):
    id_material = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=255)
    tipo_material = models.CharField(max_length=50)
    descripcion = models.TextField()
    editorial = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    id_idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    nivel_asociado = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    es_obligatorio = models.BooleanField()

    def __str__(self):
        return self.nombre_material

class EvaluacionIdioma(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    id_inscripcion = models.ForeignKey(InscripcionIdioma, on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(max_length=50)
    fecha_evaluacion = models.DateField()
    puntaje_obtenido = models.DecimalField(max_digits=5, decimal_places=2)
    ponderacion = models.DecimalField(max_digits=3, decimal_places=2)
    comentarios_profesor = models.TextField()
    habilidades_evaluadas = models.TextField()

    def __str__(self):
        return f"Evaluación {self.id_evaluacion}"
