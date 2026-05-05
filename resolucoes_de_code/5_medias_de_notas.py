# Calculando Média de Notas
# Desafio DIO - Etapa 5

def ler_nota(mensagem):
    """Lê uma nota entre 0 e 10 com tratamento de erro."""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("⚠️  A nota deve estar entre 0 e 10.")
        except ValueError:
            print("⚠️  Entrada inválida! Digite apenas números.")

def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)

def classificar_media(media):
    """Retorna a situação do aluno com base na média."""
    if media >= 9:
        return "🏆 Excelente"
    elif media >= 7:
        return "✅ Aprovado"
    elif media >= 5:
        return "⚠️  Recuperação"
    else:
        return "❌ Reprovado"

# ── Programa principal ──────────────────────────────────

print("=" * 40)
print("   📚  Calculadora de Média de Notas")
print("=" * 40)

nota1 = ler_nota("\nDigite a nota 1 (0 a 10): ")
nota2 = ler_nota("Digite a nota 2 (0 a 10): ")
nota3 = ler_nota("Digite a nota 3 (0 a 10): ")

notas = [nota1, nota2, nota3]
media = calcular_media(notas)
situacao = classificar_media(media)

print("\n" + "─" * 40)
print(f"  Nota 1:  {nota1:.1f}")
print(f"  Nota 2:  {nota2:.1f}")
print(f"  Nota 3:  {nota3:.1f}")
print("─" * 40)
print(f"  Média:   {media:.2f}")
print(f"  Situação: {situacao}")
print("=" * 40)

# Explicação didática do cálculo
print(f"\n📐 Cálculo: ({nota1} + {nota2} + {nota3}) / 3 = {media:.2f}")