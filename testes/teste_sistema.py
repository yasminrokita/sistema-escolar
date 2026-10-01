from src.sistema import cadastrar_aluno, verificar_situacao


def test_cadastrar_aluno():
    aluno = cadastrar_aluno("Ana", 8)

    assert aluno["nome"] == "Ana"
    assert aluno["nota"] == 8


def test_verificar_situacao():
    assert verificar_situacao(8) == "Aprovado"
    assert verificar_situacao(4) == "Reprovado"
