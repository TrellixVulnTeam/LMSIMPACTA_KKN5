from django.test import TestCase

# Create your tests here.

def calcula_media(self,n1,n2,n3,n4):
    resultado = (n1+n2+n3+n4)/4
    return resultado

def test_metodo01():
  print ('Calcula Média')
  assert calcula_media(5,6,7,8) == '6.5'
  assert calcula_media(10,10,10,10) == '10'
  assert calcula_media(2,5,9,0) == '4'
  assert calcula_media(10,0,0,10) == '5'
  assert calcula_media(5,5,8,2) == '5'

def test_metodo02():
  print ('')


def test_metodo03():
  print ('')


def test_metodo04():
  print ('')
  






