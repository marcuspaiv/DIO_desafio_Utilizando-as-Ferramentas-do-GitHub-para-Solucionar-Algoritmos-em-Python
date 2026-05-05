# Verificando Palíndromos
# Desafio DIO - Etapa 6

def normalizar(texto):
    """Remove espaços e converte para minúsculas para comparação justa."""
    return texto.replace(" ", "").lower()

def eh_palindromo(texto):
    """Verifica se o texto é um palíndromo."""
    texto_normalizado = normalizar(texto)
    texto_invertido   = texto_normalizado[::-1]   # fatiamento reverso
    return texto_normalizado == texto_invertido, texto_normalizado, texto_invertido

# ── Programa principal ──────────────────────────────────

print("=" * 45)
print("   🔄  Verificador de Palíndromos")
print("=" * 45)

palavra = input("\nDigite uma palavra ou frase: ").strip()

if not palavra:
    print("⚠️  Nenhum texto foi digitado.")
else:
    resultado, normalizada, invertida = eh_palindromo(palavra)

    print("\n" + "─" * 45)
    print(f"  Original:  {palavra}")
    print(f"  Invertida: {normalizada[::-1]}")
    print("─" * 45)

    if resultado:
        print(f'  ✅ "{palavra}" É um palíndromo!')
    else:
        print(f'  ❌ "{palavra}" NÃO é um palíndromo.')

    print("=" * 45)

    # ── Explicação didática ─────────────────────
    print("\n📚 Como funciona?")
    print(f'  Texto normalizado:  "{normalizada}"')
    print(f'  Texto invertido:    "{invertida}"')
    print(f'  São iguais?         {"Sim ✅" if resultado else "Não ❌"}')
    print("\n💡 Dica: usamos fatiamento reverso [::-1] para inverter a string.")