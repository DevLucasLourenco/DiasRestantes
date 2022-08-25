from datetime import datetime
from dateutil.relativedelta import relativedelta


def identificar_formatacao(item):
    try:
        data_limite = datetime.strptime(item, '%d/%m/%Y')
    except:
        data_limite = datetime.strptime(item, '%d/%m/%y')
        
    return data_limite


def adaptacao():
    
    if diferenca.hours and diferenca.minutes < 0:
        hoje_str = datetime.strftime(hoje, '%d/%m/%Y')
        return f'O dia da entrega é hoje, {hoje_str}'

    elif  diferenca.months > 0:
        return f'Faltam {diferenca.months} meses e {diferenca.days} dias'
        
    elif diferenca.days == 1:
        return f'Falta {diferenca.days} dia e {diferenca.hours}hrs'

    elif diferenca.days == 0:
        if diferenca.hours == 0:
            return f'Faltam {diferenca.minutes} minutos'
        return f'Faltam {diferenca.hours}hrs e {diferenca.minutes} minutos'

    elif diferenca.days > 1:
        return f'Faltam {diferenca.days} dias e {diferenca.hours}hrs'

    else:
        return f'Passaram-se {diferenca.days} dias do prazo'.replace('-', '')



if __name__ == '__main__':
    hoje = datetime.today()
    
    input_data_limite = input('informe a data limite:')
    data_limite = identificar_formatacao(input_data_limite)

    diferenca = relativedelta(data_limite, hoje)
    
    print(adaptacao())

    