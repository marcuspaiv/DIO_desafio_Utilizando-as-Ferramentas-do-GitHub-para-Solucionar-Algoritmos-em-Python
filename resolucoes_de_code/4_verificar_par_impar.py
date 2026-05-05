# Verificando Números Pares e Ímpares
# Desafio DIO - Etapa 4

def verificar_par_impar(numero):
    """Verifica se um número inteiro é par ou ímpar."""
    return "par" if numero % 2 == 0 else "ímpar"

def ler_inteiro(mensagem):
    """Lê um número inteiro com tratamento de erro."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️  Entrada inválida! Digite apenas números inteiros.")

# ── Programa principal ──────────────────────────────────

print("=" * 40)
print("   🔢  Verificador de Par ou Ímpar")
print("=" * 40)

numero = ler_inteiro("\nDigite um número inteiro: ")

resultado = verificar_par_impar(numero)

print(f"\n✅ O número {numero} é {resultado}!")

# Explicação do conceito para fins didáticos
print(f"\n📚 Por quê? {numero} % 2 = {numero % 2}", end=" → ")
if numero % 2 == 0:
    print("resto zero significa PAR.")
else:
    print("resto um significa ÍMPAR.")

print("=" * 40)