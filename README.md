# 🐍 DIO Desafio — Utilizando as Ferramentas do GitHub para Solucionar Algoritmos em Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces-181717?style=for-the-badge&logo=github&logoColor=white)
![DIO](https://img.shields.io/badge/DIO-Desafio-E91E63?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-00C851?style=for-the-badge)

*Desafio prático da [DIO](https://www.dio.me/) para explorar o GitHub Codespaces e o GitHub Copilot na resolução de algoritmos em Python.*

</div>

---

## 📋 Sobre o Projeto

Este repositório contém as soluções dos 6 desafios de algoritmos em Python propostos pela DIO, desenvolvidos diretamente no **GitHub Codespaces** com o apoio do **GitHub Copilot** como ferramenta de IA.

O objetivo foi praticar conceitos fundamentais de programação Python — desde manipulação de strings até condicionais e operações matemáticas — utilizando o ambiente de desenvolvimento na nuvem do GitHub.

---

## 🗂️ Estrutura do Projeto

```
DIO_desafio_Utilizando-as-Ferramentas-do-GitHub-para-Solucionar-Algoritmos-em-Python/
│
├── 📁 resolucoes_de_code/
│   ├── 🐾 1_concat_dados.py
│   ├── ✏️ 2_repet_txt.py
│   ├── 📐 3_ope_math.py
│   ├── 🧮 4_verificar_par_impar.py
│   ├── 📚 5_medias_de_notas.py
│   └── 🔄 6_verificando_palindromos.py
│
└── 📄 README.md
```

---

## 🚀 Etapas do Desafio

### 🐾 Etapa 1 — Concatenando Dados

**Descrição:** Receber dois dados diferentes do usuário e concatená-los em uma única string.

**Conceitos praticados:**
- Manipulação de Strings
- Concatenação com operador `+`
- Entrada de dados com `input()`

```python
variavel1 = input("Digite a primeira informação:")
variavel2 = input("Digite a segunda informação:")

variavel_concatenada = variavel1 + " " + variavel2

print("As variaveis concatenadas são: ", variavel_concatenada)
```

---

### ✏️ Etapa 2 — Repetindo Textos

**Descrição:** Solicitar uma string e um número inteiro e retornar a string repetida o número de vezes informado.

**Conceitos praticados:**
- Manipulação de Strings
- Números Inteiros (`int`)
- Multiplicação de strings com operador `*`
- Entrada de dados

```python
string = input("Digite uma string: ")
numero = int(input("Digite um numero: "))

print((string + " ") * numero)
```

---

### 📐 Etapa 3 — Operações Matemáticas Simples

**Descrição:** Receber dois números como entrada e realizar operações matemáticas entre eles.

**Conceitos praticados:**
- Operações Matemáticas Básicas (`+`, `-`, `*`, `/`, `**`)
- Entrada de dados
- Funções e modularização do código
- Tratamento de erros com `try/except`

> 💡 *Código otimizado com o apoio do GitHub Copilot, incluindo menu interativo, histórico de operações e suporte a raiz quadrada e porcentagem.*

---

### 🧮 Etapa 4 — Verificando Números Pares e Ímpares

**Descrição:** Receber um número inteiro e verificar se ele é par ou ímpar.

**Conceitos praticados:**
- Condicionais `if` / `else`
- Operador de módulo `%`
- Expressão ternária (otimização com IA)

```python
def verificar_par_impar(numero):
    return "par" if numero % 2 == 0 else "ímpar"
```

> 💡 *A lógica foi condensada em uma linha com expressão ternária — sugestão típica do GitHub Copilot para código mais pythônico.*

---

### 📚 Etapa 5 — Calculando Média de Notas

**Descrição:** Calcular a média de três notas fornecidas pelo usuário.

**Conceitos praticados:**
- Uso de variáveis para armazenar dados
- Operadores aritméticos `+` e `/`
- Validação de entrada do usuário
- Classificação de resultado com condicionais

| Média | Situação |
|:-----:|:--------:|
| ≥ 9.0 | 🏆 Excelente |
| ≥ 7.0 | ✅ Aprovado |
| ≥ 5.0 | ⚠️ Recuperação |
| < 5.0 | ❌ Reprovado |

```python
def calcular_media(notas):
    return sum(notas) / len(notas)
```

---

### 🔄 Etapa 6 — Verificando Palíndromos

**Descrição:** Verificar se uma palavra ou frase é um palíndromo.

**Conceitos praticados:**
- Manipulação e inversão de strings
- Fatiamento reverso com `[::-1]`
- Normalização de texto (`.lower()`, `.replace()`)
- Comparação de strings

```python
def eh_palindromo(texto):
    texto_normalizado = texto.replace(" ", "").lower()
    texto_invertido   = texto_normalizado[::-1]
    return texto_normalizado == texto_invertido
```

> 💡 *A normalização do texto permite detectar palíndromos em frases como "Amor à Roma", não apenas em palavras simples.*

---

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.x instalado **ou** acesso ao GitHub Codespaces

### Rodando no GitHub Codespaces

1. Acesse o repositório no GitHub
2. Clique em **Code → Codespaces → Create codespace on main**
3. No terminal do Codespace, acesse a pasta de soluções:

```bash
cd resolucoes_de_code
```

4. Execute o script desejado:

```bash
python 1_concat_dados.py
python 2_repet_txt.py
python 3_ope_math.py
python 4_verificar_par_impar.py
python 5_medias_de_notas.py
python 6_verificando_palindromos.py
```

### Rodando localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/DIO_desafio_Utilizando-as-Ferramentas-do-GitHub-para-Solucionar-Algoritmos-em-Python.git

# Acesse a pasta
cd DIO_desafio_.../resolucoes_de_code

# Execute qualquer script
python nome_do_arquivo.py
```

---

## 🤖 Ferramentas Utilizadas

| Ferramenta | Uso |
|:---:|:---|
| ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white) | Versionamento e hospedagem do código |
| ![Codespaces](https://img.shields.io/badge/-Codespaces-181717?logo=github&logoColor=white) | Ambiente de desenvolvimento na nuvem |
| ![Copilot](https://img.shields.io/badge/-GitHub%20Copilot-181717?logo=github&logoColor=white) | Assistente de IA para otimização do código |
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Linguagem de programação utilizada |

---

## 👨‍💻 Autor

<div align="center">

**Marcus Paiva**

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/marcuspaiv)

*Desenvolvido durante o curso Formação Github Certification da [DIO](https://www.dio.me/) 🚀*

</div>

---

<div align="center">

⭐ *Se este projeto foi útil para você, deixe uma estrela!* ⭐

</div>
