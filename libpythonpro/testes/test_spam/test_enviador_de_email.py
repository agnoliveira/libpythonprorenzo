import pytest


from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'agnoliveira@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'agnoliveira@gmail.com',
        'Cursos Python Pro',
        'Turma Jessica Ferrari'
    )
    assert destinatario in resultado
