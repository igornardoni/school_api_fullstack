import os
import django
import random
from faker import Faker
from validate_docbr import CPF
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Aluno, Curso, Matricula


def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999),
                               random.randrange(100, 999), random.randrange(0, 9))
        cpf = cpf.generate()
        data_nascimento = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80)
        a = Aluno(nome=nome, rg=rg, cpf=cpf, data_nascimento=data_nascimento)
        a.save()


def criando_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    Faker.seed(10)

    # Lista de descrições disponíveis para cursos
    descs = ['Python Fundamentos', 'Python intermediário', 'Python Avançado',
             'Python para Data Science', 'Django/React', 'Django/Angular', 'Django REST',
             'Automações RPA em Python', 'C# básico', 'C# intermediário', 'C++ básico',
             'C++ intermediário', 'Unity Game/C#', 'Unreal Game Engine/C++']

    for _ in range(quantidade_de_cursos):
        codigo_curso = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),
                                        random.randrange(1, 9))
        if descs:
            descricao = random.choice(descs)
            descs.remove(descricao)
        else:
            # Se a lista de descrições acabar, reinicie com descrições aleatórias
            descricao = fake.sentence()

        nivel = random.choice("BIA")
        c = Curso(codigo_curso=codigo_curso, descricao=descricao, nivel=nivel)
        c.save()


# criando_alunos(200)
criando_cursos(14)
print('Executou!')
