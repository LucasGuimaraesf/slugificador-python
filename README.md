# Slugificador em Python

Utilitário em Python para converter textos em slugs amigáveis para URL, tratando acentos, caracteres especiais e duplicidade.
Este projeto é um utilitário simples em Python para transformar textos em **slugs amigáveis para URL**.

## Funcionalidades

- Remove acentos automaticamente
- Converte para letras minúsculas
- Remove caracteres especiais
- Substitui espaços por hífens
- Suporte para listas de textos
- Geração de slugs únicos (evita duplicados)

---

## Exemplo

Entrada:
```python
[
    "Curso de Engenharia de Software",
    "Python é incrível!!! 🐍",
    "Curso de Python",
    "Curso de Python"
]
