from django.db import models

class Receituario(models.Model):
    paciente_nome = models.CharField(max_length=100)
    medico_nome = models.CharField(max_length=100)
    medicamentos = models.TextField()
    data_prescricao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Receituário para {self.paciente_nome}"
