def notas(*val, sit=False):
    """
    --> Função para analisar situação e notas de vários alunos.
    :param val: uma ou mais notas dos alunos.
    :param sit: valor opcional, dizendo se deve ou não adicionar situação.
    :return: dicionário com várias informções sobre a situação da turma.
    """
    no = dict()
    no['total'] = len(val)
    no['maior'] = max(val)
    no['menor'] = min(val)
    no['media'] = sum(val)/len(val)
    if sit:
        if no['media'] >= 7:
            no['situação'] = 'BOA'
        elif no['media'] >= 5:
            no['situação'] = 'RAZOAVEL'
        else:
            no['situação'] = 'RUIM'
    return no
resp = notas(5, 6, 8, sit=True)
print(resp)
help(notas)