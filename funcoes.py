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


# Função para exibir a quantidade de valores únicos

def exibe_valores_unicos(coluna):
    '''
    Exibe a quantidade de valores únicos de coluna(s) específica(s)

    :param coluna: Column Dataframe
        Dataframe e coluna a ser analisado.
    :return: Dataframe
        DataFrame contendo os nome e quantidade.
    '''
    import pandas as pd
    coluna_qtde = pd.DataFrame(coluna.value_counts().sort_index())
    coluna_qtde = coluna_qtde.rename(columns={'count': 'Quantidade'})
    coluna_qtde = coluna_qtde.T
    return coluna_qtde

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
    '''
    import pandas as pd
    import numpy as np
    arr = np.array(dataframe[coluna])
    if sinal == '>':
        val = arr[np.where(arr > limite)[0]]
    else:
        val = arr[np.where(arr < limite)[0]]
    print(f'\n{coluna.upper()}: {np.unique(val)}')
    