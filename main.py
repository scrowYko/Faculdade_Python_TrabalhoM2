"""
Projeto M2 - Sistema de Gestão Acadêmica
Disciplina: Introdução à Programação em Python
Professor: Evandro Chagas Ribeiro da Rosa
Universidade do Vale do Itajaí (UNIVALI)

Integrantes:
- Davi Henry Morel Pintos - 8491445
- Maria Eduarda - 8480087
- Erik Von Wangenheim - 7817720
"""

from typing import Dict, List

# ==================== Estruturas de Dados ====================

alunos: Dict[str, Dict[str, str]] = {}
disciplinas: Dict[str, Dict[str, str | int]] = {}
matriculas: List[Dict[str, str]] = []

# ==================== Funções Utilitárias ====================

def validar_matricula(matricula: str) -> bool:
    """Valida se a matrícula tem o formato correto (AAAA###)."""
    return len(matricula) == 7 and matricula.isdigit()

def validar_codigo_disciplina(codigo: str) -> bool:
    """Valida se o código da disciplina segue o formato LLNNN."""
    return (
        len(codigo) == 5
        and codigo[:2].isalpha()
        and codigo[:2].isupper()
        and codigo[2:].isdigit()
    )

def pausar() -> None:
    input("\nPressione ENTER para continuar...")

# ==================== Gestão de Alunos ====================

def cadastrar_aluno() -> None:
    matricula = input("Digite a matrícula (AAAA###): ").strip()
    if not validar_matricula(matricula):
        print("Matrícula inválida! Exemplo: 2025001")
        return

    if matricula in alunos:
        print("Matrícula já cadastrada!")
        return

    nome = input("Digite o nome do aluno: ").strip()
    alunos[matricula] = {"nome": nome}
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar_alunos() -> None:
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for m, dados in alunos.items():
            print(f"{m} - {dados['nome']}")

def buscar_aluno() -> None:
    matricula = input("Digite a matrícula: ").strip()
    aluno = alunos.get(matricula)
    if aluno:
        print(f"Aluno encontrado: {aluno['nome']}")
    else:
        print("Aluno não encontrado.")

def menu_alunos() -> None:
    while True:
        print("""
====== Gestão de Alunos ======
[1] Cadastrar Aluno
[2] Listar Alunos
[3] Buscar Aluno
[4] Voltar
""")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_aluno()
        elif op == "2":
            listar_alunos()
        elif op == "3":
            buscar_aluno()
        elif op == "4":
            break
        else:
            print("Opção inválida.")
        pausar()

# ==================== Gestão de Disciplinas ====================

def cadastrar_disciplina() -> None:
    codigo = input("Código (LLNNN): ").strip()
    if not validar_codigo_disciplina(codigo):
        print("Código inválido! Exemplo: SI100")
        return

    if codigo in disciplinas:
        print("Código já cadastrado!")
        return

    nome = input("Nome da disciplina: ").strip()
    try:
        vagas = int(input("Número de vagas: ").strip())
    except ValueError:
        print("Número de vagas inválido.")
        return

    disciplinas[codigo] = {"nome": nome, "vagas": vagas}
    print(f"Disciplina {nome} cadastrada com sucesso!")

def listar_disciplinas() -> None:
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
    else:
        print("\n--- Disciplinas ---")
        for cod, d in disciplinas.items():
            print(f"{cod} - {d['nome']} ({d['vagas']} vagas)")

def buscar_disciplina() -> None:
    codigo = input("Digite o código da disciplina: ").strip().upper()
    d = disciplinas.get(codigo)
    if d:
        print(f"{codigo} - {d['nome']} ({d['vagas']} vagas)")
    else:
        print("Disciplina não encontrada.")

def menu_disciplinas() -> None:
    while True:
        print("""
====== Gestão de Disciplinas ======
[1] Cadastrar Disciplina
[2] Listar Disciplinas
[3] Buscar Disciplina
[4] Voltar
""")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_disciplina()
        elif op == "2":
            listar_disciplinas()
        elif op == "3":
            buscar_disciplina()
        elif op == "4":
            break
        else:
            print("Opção inválida.")
        pausar()

# ==================== Gestão de Matrículas ====================

def realizar_matricula() -> None:
    matr = input("Matrícula do aluno: ").strip()
    cod = input("Código da disciplina: ").strip().upper()

    if matr not in alunos:
        print("Aluno não encontrado.")
        return
    if cod not in disciplinas:
        print("Disciplina não encontrada.")
        return

    for m in matriculas:
        if m["matricula"] == matr and m["codigo"] == cod:
            print("Aluno já inscrito nessa disciplina.")
            return

    if disciplinas[cod]["vagas"] <= 0:
        print("Sem vagas disponíveis.")
        return

    matriculas.append({"matricula": matr, "codigo": cod})
    disciplinas[cod]["vagas"] -= 1
    print("Matrícula realizada com sucesso!")

def listar_matriculas() -> None:
    if not matriculas:
        print("Nenhuma matrícula registrada.")
    else:
        print("\n--- Matrículas ---")
        for m in matriculas:
            nome_aluno = alunos[m["matricula"]]["nome"]
            nome_disc = disciplinas[m["codigo"]]["nome"]
            print(f"{nome_aluno} -> {nome_disc}")

def menu_matriculas() -> None:
    while True:
        print("""
====== Gestão de Matrículas ======
[1] Realizar Inscrição
[2] Listar Inscrições
[3] Voltar
""")
        op = input("Escolha: ").strip()
        if op == "1":
            realizar_matricula()
        elif op == "2":
            listar_matriculas()
        elif op == "3":
            break
        else:
            print("Opção inválida.")
        pausar()

# ==================== Relatórios ====================

def relatorio_alunos_por_disciplina() -> None:
    cod = input("Código da disciplina: ").strip().upper()
    if cod not in disciplinas:
        print("Disciplina não encontrada.")
        return

    alunos_disc = [m["matricula"] for m in matriculas if m["codigo"] == cod]

    if not alunos_disc:
        print("Nenhum aluno matriculado nessa disciplina.")
    else:
        print(f"\n--- Alunos em {disciplinas[cod]['nome']} ---")
        for matr in alunos_disc:
            print(f"{matr} - {alunos[matr]['nome']}")

def relatorio_disciplinas_por_aluno() -> None:
    matr = input("Matrícula do aluno: ").strip()
    if matr not in alunos:
        print("Aluno não encontrado.")
        return

    disc_aluno = [m["codigo"] for m in matriculas if m["matricula"] == matr]

    if not disc_aluno:
        print("Aluno não está matriculado em nenhuma disciplina.")
    else:
        print(f"\n--- Disciplinas de {alunos[matr]['nome']} ---")
        for cod in disc_aluno:
            print(f"{cod} - {disciplinas[cod]['nome']}")

def relatorio_disciplinas_sem_vagas() -> None:
    esgotadas = [c for c, d in disciplinas.items() if d["vagas"] == 0]
    if not esgotadas:
        print("Nenhuma disciplina com vagas esgotadas.")
    else:
        print("\n--- Disciplinas sem vagas ---")
        for cod in esgotadas:
            print(f"{cod} - {disciplinas[cod]['nome']}")

def menu_relatorios() -> None:
    while True:
        print("""
====== Relatórios ======
[1] Alunos por Disciplina
[2] Disciplinas por Aluno
[3] Disciplinas com Vagas Esgotadas
[4] Voltar
""")
        op = input("Escolha: ").strip()
        if op == "1":
            relatorio_alunos_por_disciplina()
        elif op == "2":
            relatorio_disciplinas_por_aluno()
        elif op == "3":
            relatorio_disciplinas_sem_vagas()
        elif op == "4":
            break
        else:
            print("Opção inválida.")
        pausar()

# ==================== Menu Principal ====================

def menu_principal() -> None:
    while True:
        print("""
====== Sistema de Gestão Acadêmica - Universidade Python ======
[1] Gestão de Alunos
[2] Gestão de Disciplinas
[3] Gestão de Matrículas
[4] Relatórios
[5] Sair
===============================================================
""")
        op = input("Escolha: ").strip()
        if op == "1":
            menu_alunos()
        elif op == "2":
            menu_disciplinas()
        elif op == "3":
            menu_matriculas()
        elif op == "4":
            menu_relatorios()
        elif op == "5":
            print("Encerrando o sistema... 👋")
            break
        else:
            print("Opção inválida.")
        pausar()

# ==================== Execução ====================

if __name__ == "__main__":
    menu_principal()
