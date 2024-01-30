# Função para geração de um dataframe de metadados

def gerar_metadados(dataframe):
    '''
    Gera um dataframe contendo metadados das colunas do dataframe fornecido.

    :param dataframe: Dataframe
        DataFrame para o qual os metadados serão gerados.
    :return: DataFrame
        DataFrame contendo os metadados.
    '''
    import pandas as pd
    metadados = pd.DataFrame({
        'Variável': dataframe.columns,
        'Tipo': dataframe.dtypes,
        'Qtde de nulos': dataframe.isnull().sum(),
        '% de nulos': round((dataframe.isnull().sum()/len(dataframe))*100, 2),
        'Cardinalidade': dataframe.nunique(),
    })
    metadados = metadados.reset_index(drop=True)
    return metadados


# Função para geração de gráfico de variáveis com dados nulos

def grafico_bar_valores_nulos(dataframe):
    '''
    Gera um gráfico de barras das variáveis destacando os dados nulos/ausentes

    :param coluna: Dataframe
        Dataframe ser analisado.
    '''
    import matplotlib.pyplot as plt
    import missingno as msno
    plt.figure(figsize=(10, 5))
    ax = plt.subplot()
    msno.bar(dataframe, color='dodgerblue', fontsize=8, ax=ax)
    plt.title('Visualização das variáveis com dados nulos/ausentes\n')
    plt.tight_layout()


# Função para exibição dos valores únicos dos outliers

def valores_outliers(dataframe, coluna, limite, sinal):
    '''
    Exibe os valores únicos dos outliers

    :param col: Column Dataframe
        Dataframe e coluna a ser analisado.
    :param lim: int
        Valor do limite inferior ou superior.
    :param sinal: str
        Símbolo de maior(>) ou menor(<).
    :return: None
    '''
    import numpy as np
    arr = np.array(dataframe[coluna])
    if sinal == '>':
        val = arr[np.where(arr > limite)[0]]
    else:
        val = arr[np.where(arr < limite)[0]]
    print(f'\n{coluna.upper()}: {np.unique(val)}')


# Função para exibição da quantidade de valores nulos

def exibe_quantidade_nulos(dataframe, coluna):
    '''
    Exibe a quantidade e percentual de valores nulos de uma coluna específica

    :param df: Dataframe
        DataFrame a ser analisado.
    :param coluna: Column Dataframe
        Coluna do dataframe a ser analisado.
    :return: None
    '''
    try:
        qtde_nulos = dataframe[coluna].isnull().sum()
        perc_nulos = round((dataframe[coluna].isnull().sum()/len(dataframe[coluna]))*100, 2)
        print(f'\nQuantidade de registros nulos na coluna {coluna}: {qtde_nulos} ({perc_nulos} %)')
    except:
        print(f'\nColuna {coluna} não existe ou foi apagada.')


# Função para geração de gráfico countplot     

def graf_countplot(dataframe, x, hue=None, rotation=0):
    '''
    Função para gerar um gráfico countplot.

    :param data: DataFrame
        DataFrame contendo os dados.
    :param x: str
        Nome da coluna a ser plotada no eixo x.
    :param hue: str, opcional
        Nome da coluna usada para distinguir subcategorias no eixo x.
    :param rotation: int, opcional
        Grau de rotação dos valores das barras do eixo x.
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns
    # Plotar o gráfico
    plt.figure(figsize=(12, 5))
    ax = sns.countplot(data=dataframe, x=x, palette='Set2', hue=hue)
    
    # Adiciona título ao gráfico
    ax.set_title(f'Countplot da variável categórica: {x}', loc='left')
    # Remover rótulos dos eixos
    ax.set(xlabel='', ylabel='')
    # Ajusta o tamanho dos rótulos
    ax.tick_params(labelsize=10)
    # Exibe rótulos sem formatação especial
    ax.ticklabel_format(style='plain', axis='y')
    
    # Adiciona rótulos (valores) nas barras
    for container in ax.containers:
        ax.bar_label(container, size=8, rotation=rotation)

    # Ajusta o layout para evitar sobreposição
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.15, hspace=0.2)
    plt.show()
