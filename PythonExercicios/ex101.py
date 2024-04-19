def voto(ano):
    from datetime import date
    ano = date.today().year - ano
    if ano < 16:
        return f'Com {ano} anos não vota.'
    elif ano > 70 or ano < 18:
        return f'Com {ano} anos o voto é opcional.'
    else:
        return f'Com {ano} anos o voto é obrigatório.'
print(voto(int(input('Em que ano você nasceu? '))))