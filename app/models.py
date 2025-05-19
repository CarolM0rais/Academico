from django.db import models


class UF(models.Model):
    sigla = models.CharField(max_length=2, unique=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, related_name="cidades")

    def __str__(self):
        return f"{self.nome} - {self.uf.sigla}"



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    nome_do_pai = models.CharField(max_length=100, null=True, blank=True)
    nome_da_mae = models.CharField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField(unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class Estudante(Pessoa):
    ocupacao     = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Professor(Pessoa):
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class AreaDoSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome



class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(AreaDoSaber, on_delete=models.SET_NULL, null=True, blank=True)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome



class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area_saber = models.ForeignKey(AreaDoSaber, on_delete=models.SET_NULL, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.nome



class Turno(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



class Matricula(models.Model):
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE, null = True, blank = True)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.estudante} - {self.curso}"



class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.SET_NULL, null=True, blank=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Avaliação: {self.descricao}"



class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"



class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Estudante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ocorrência: {self.descricao}"
