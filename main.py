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


# Estruturas de dados principais
alunos: Dict[str, Dict[str, str]] = {}
disciplinas: Dict[str, Dict[str, str | int]] = {}
matriculas: List[Dict[str, str]] = []


# ==================== Funções utilitárias ====================

def validar_matricula(matricula: str) -> bool:
    """Valida se a matrícula tem o formato correto (AAAA###)."""
    return len(matricula) == 7 and matricula.isdigit() and matricula[:4].isdigit()


def validar_codigo_disciplina(codigo: str) -> bool:
    """Valida se o código da disciplina segue o formato LLNNN."""
    return (
        len(codigo) == 5
        and codigo[:2].isalpha()
        and codigo[:2].isupper()
        and codigo[2:].isdigit()
    )


def pausar() -> None:
    """Aguarda o usuário pressionar Enter para continuar."""
    input("\nPressione ENTER para continuar...")


# ==================== Gestão de Alunos ====================

def cadastrar_aluno() -> None:
    """Cadastra um novo aluno, validando formato e duplicidade."""
    matricula = input("Digite a matrícula (AAAA###): ").strip()
    if not validar_matricula(matricula):
        print("❌ Matrícula inválida! Deve ter 7 dígitos, ex: 2025001.")
        return

    if matricula in alunos:
        print("❌ Matrícula já cadastrada!")
        return

    nome = input("Digite o nome do aluno: ").strip()
    alunos[matricula] = {"nome": nome}
    print(f"✅ Aluno {nome} cadastrado com sucesso!")


def listar_alunos() -> None:
    """Exibe todos os alunos cadastrados."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for matr, dados in alunos.items():
            print(f"{matr} - {dados['nome']}")


def buscar_aluno() -> None:
    """Busca e exibe dados de um aluno pela matrícula."""
    matricula = input("Digite a matrícula: ").strip()
    aluno = alunos.get(matricula)
    if aluno:
        print(f"Aluno encontrado: {aluno['nome']}")
    else:
        print("❌ Aluno não encontrado.")


def menu_alunos() -> None:
    """Menu de gestão de alunos."""
    while True:
        print("""
====== Gestão de Alunos ======
[1] Cadastrar Aluno
[2] Listar Alunos
[3] Buscar Aluno
[4] Voltar
""")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
        pausar()


# ==================== Menu Principal ====================

def menu_principal() -> None:
    """Menu principal do sistema."""
    while True:
        print("""
====== Sistema de Gestão Acadêmica - Universidade Python ======
[1] Gestão de Alunos
[2] Gestão de Disciplinas
[3] Gestão de Matrículas
[4] Geração de Relatórios
[5] Sair
===============================================================
""")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_disciplinas()
        elif opcao == "3":
            menu_matriculas()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "5":
            print("Encerrando o sistema... 👋")
            break
        else:
            print("Opção inválida.")
        pausar()


# ==================== Execução ====================
if __name__ == "__main__":
    menu_principal()