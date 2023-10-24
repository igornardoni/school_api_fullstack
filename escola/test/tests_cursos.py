from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_urls = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CT1', descricao='Curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CT2', descricao='Curso teste 2', nivel='I'
        )

    # def test_failed(self):
    #     self.fail('You have failed this city | (Read with Green Arrow voice)')

    def test_get_lista_cursos(self):
        """Teste para verificar a requisição HTTP GET para listar os cursos"""
        response = self.client.get(self.list_urls)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_lista_cursos(self):
        """Teste para verificar a requisição HTTP POST para criar cursos"""
        data = {
             'codigo_curso': 'CT3',
             'descricao': 'Curso teste 3',
             'nivel': 'A'
        }
        response = self.client.post(self.list_urls, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_cursos(self):
        """Teste para verificar a requisição HTTP DELETE -NÃO- permitida, para deletar um curso"""
        response = self.client.delete(reverse('Cursos-detail', args=[self.curso_1.pk]))
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        




