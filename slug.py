import re
import unicodedata

def slugify(texto: str) -> str:
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    texto = texto.lower()
    texto = re.sub(r'[^a-z0-9\s-]', '', texto)
    texto = re.sub(r'[\s-]+', '-', texto).strip('-')
    return texto


def slugificar_lista(lista_textos):
    slugs = []
    
    for texto in lista_textos:
        slug = slugify(texto)
        slugs.append(slug)
    
    return slugs

textos = ["xxxx","yyyy","zzzz"]

resultado = slugificar_lista(textos)

#Resultado:
# Título: Curso de Engenharia de Software
# Slug: curso-de-engenharia-de-software

print(resultado)