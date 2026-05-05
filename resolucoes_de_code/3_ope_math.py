# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
import math

# ─────────────────────────────────────────────
#  Funções de cálculo
# ─────────────────────────────────────────────

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def exponenciar(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return math.sqrt(a)

def porcentagem(a, b):
    """Calcula quanto por cento 'b' representa de 'a'."""
    if a == 0:
        raise ValueError("O primeiro número não pode ser zero para porcentagem.")
    return (b / a) * 100

# ─────────────────────────────────────────────
#  Exibição
# ─────────────────────────────────────────────

def exibir_menu():
    print("""
╔══════════════════════════════════════╗
║        🧮  CALCULADORA DIO  🧮       ║
╠══════════════════════════════════════╣
║  +   Soma                           ║
║  -   Subtração                      ║
║  *   Multiplicação                  ║
║  /   Divisão                        ║
║  ^   Exponenciação                  ║
║  r   Raiz quadrada                  ║
║  %   Porcentagem (b% de a)          ║
║  h   Ver histórico                  ║
║  l   Limpar histórico               ║
║  s   Sair                           ║
╚══════════════════════════════════════╝""")

def exibir_historico(historico):
    if not historico:
        print("\n📋 Histórico vazio.")
        return
    print("\n📋 Histórico de operações:")
    print("─" * 40)
    for i, entrada in enumerate(historico, 1):
        print(f"  {i}. {entrada}")
    print("─" * 40)

def formatar_numero(n):
    """Remove .0 de inteiros para exibição mais limpa."""
    return int(n) if n == int(n) else round(n, 10)

# ─────────────────────────────────────────────
#  Leitura segura de números
# ─────────────────────────────────────────────

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠️  Entrada inválida. Digite um número válido.")

# ─────────────────────────────────────────────
#  Loop principal
# ─────────────────────────────────────────────

def main():
    historico = []

    print("\n🚀 Bem-vindo à Calculadora DIO!")

    while True:
        exibir_menu()
        operacao = input("\nEscolha uma operação: ").strip().lower()

        # ── Sair ──────────────────────────────
        if operacao == 's':
            print("\n👋 Obrigado por usar a Calculadora DIO. Até logo!")
            break

        # ── Histórico ─────────────────────────
        elif operacao == 'h':
            exibir_historico(historico)
            continue

        # ── Limpar histórico ──────────────────
        elif operacao == 'l':
            historico.clear()
            print("\n🗑️  Histórico limpo com sucesso!")
            continue

        # ── Raiz quadrada (1 número) ──────────
        elif operacao == 'r':
            a = ler_numero("Digite o número: ")
            try:
                resultado = raiz_quadrada(a)
                resultado_fmt = formatar_numero(resultado)
                entrada = f"√{formatar_numero(a)} = {resultado_fmt}"
                print(f"\n✅ Resultado: {entrada}")
                historico.append(entrada)
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        # ── Operações com 2 números ───────────
        elif operacao in ('+', '-', '*', '/', '^', '%'):
            a = ler_numero("Digite o primeiro número:  ")
            b = ler_numero("Digite o segundo número:   ")

            simbolos = {
                '+': '+', '-': '-', '*': '×',
                '/': '÷', '^': '^', '%': '%de'
            }
            operacoes = {
                '+': somar, '-': subtrair,
                '*': multiplicar, '/': dividir,
                '^': exponenciar, '%': porcentagem
            }

            try:
                resultado = operacoes[operacao](a, b)
                resultado_fmt = formatar_numero(resultado)
                a_fmt = formatar_numero(a)
                b_fmt = formatar_numero(b)
                simbolo = simbolos[operacao]

                if operacao == '%':
                    entrada = f"{b_fmt} é {resultado_fmt}% de {a_fmt}"
                else:
                    entrada = f"{a_fmt} {simbolo} {b_fmt} = {resultado_fmt}"

                print(f"\n✅ Resultado: {entrada}")
                historico.append(entrada)

            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        # ── Opção inválida ────────────────────
        else:
            print("\n⚠️  Operação inválida. Escolha uma das opções do menu.")

        input("\nPressione Enter para continuar...")

# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()

