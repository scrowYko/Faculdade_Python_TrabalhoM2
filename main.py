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
        print("Matrícula inválida! Deve ter 7 dígitos, ex: 2025001.")
        return

    if matricula in alunos:
        print("Matrícula já cadastrada!")
        return

    nome = input("Digite o nome do aluno: ").strip()
    alunos[matricula] = {"nome": nome}
    print(f"Aluno {nome} cadastrado com sucesso!")


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
        print("Aluno não encontrado.")


def menu_alunos() -> None:
    """Menu de gestão de alunos."""
    while True:
        print("""
==-== Gestão de Diciplinas ==-==
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

# ==================== Gestão de Disciplinas ====================

def menu_disciplinas() -> None:
    gestao_diciplinas_ops()
    escolha = input(">>> ")
    match escolha:
        case '1':
            cadastrar_disciplina()
        case '2':
            listar_diciplinas()
        case '3':
            print("Digite o código da disciplina desejada:")
            codigo = input(">> ")
            buscar_disciplina(codigo)

def gestao_diciplinas_ops() -> None:
    print("==-== Gestão de Diciplinas ==-==")
    print("[1] Cadastrar Disciplina")
    print("[2] Listar Diciplinas")
    print("[3] Buscar Diciplina por Código")
    print("[4] Voltar ao Menu Principal")

def cadastrar_disciplina():
    print("Digite o código da diciplina (AAxxx):")
    codigo = adicionar_codigo()
    print("Digite o nome da diciplina:")
    nome = adicionar_nome_dis()
    print("Digite o número de vagas: ")
    vagas = adicionar_numero()

    disciplina = {
        "nome" : nome,
        "vagas": vagas
    }
    disciplinas[codigo] = disciplina
    return

def adicionar_codigo() -> str:
    codigo = ""
    while True:
        codigo = input(">> ")
        valido = True
        if len(codigo) == 5:
            for i in range(2, 5):
                valido = valido and codigo[i].isdigit()            
            for i in range(2):
                valido = valido and codigo[i].isalpha() and codigo[i].isupper()
            if codigo in disciplinas.keys():
                print("Esse código de disciplina já está registrado")
                continue
    
            if valido:
                return codigo
            print("Este código é inválido")

def adicionar_nome_dis() -> str:
    nome = ""
    while True:
        nome = input(">> ")
        valido = True

        if len(nome) > 0:
            for diciplina in disciplinas.values():
                if nome == diciplina['nome']:
                    valido = False
            if valido:
                return nome
            print("Este nome já foi registrado")

def adicionar_numero() -> int:
    numero = ""
    while not numero.isdigit():
        numero = input(">> ")
    return int(numero)

def listar_diciplinas() -> None:
    if len(disciplinas) == 0:
        print("Não existe nenhuma disciplina")
    else:
        print("==~== Lista de Disciplinas ==~==")
        for codigo, disciplina in disciplinas.items():
            print(f"{codigo}: {disciplina['nome']}")
            print(f"Vagas: {disciplina['vagas']}\n")
        pausar()

def buscar_disciplina(codigo) -> None:
    if codigo in disciplinas.keys():
        disciplina = disciplinas[codigo]
        print(f"{codigo}: {disciplina['nome']}")
        print(f"Vagas: {disciplina['vagas']}\n")
        return
    print("Este código não está registrado")

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
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")
        pausar()


# ==================== Execução ====================
if __name__ == "__main__":
    menu_principal()
