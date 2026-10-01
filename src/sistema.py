def cadastrar_aluno(nome, nota):
    aluno = {
        "nome": nome,
        "nota": nota
    }
    return aluno


def verificar_situacao(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"
