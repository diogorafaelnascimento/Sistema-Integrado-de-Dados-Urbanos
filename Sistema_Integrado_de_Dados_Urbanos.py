print('*-' * 16)
print('SISTEMA INTEGRADO DE DADOS URBANOS')
print('*-' * 16)
largura_via = float(input('\nLargura aproximada da parte analisada da via de estudo em metros (inclui calçada): '))
comprimento_via = float(input('Comprimento aproximado da parte analisada da via de estudo em metros: '))
area_via = comprimento_via * largura_via
pavimentacao = {
    'A': 'Pavimentação asfáltica',
    'P': 'Pavimentação drenante com pedras de granito ou basalto',
    'C': 'Pavimentação drenante com blocos ou lajotas de concreto',
    'T': 'Rua não pavimentada'
}
while True:
    tipo_input = input('''\nTIPO DE PAVIMENTAÇÃO:
[A] Asfaltada
[P] Pedras de granito ou basalto
[C] Blocos ou lajotas de concreto
[T] Não pavimentada
''').strip().upper()
    if not tipo_input:
        print('Digite uma opção válida.')
        continue
    tipo_via = tipo_input[0]
    if tipo_via in pavimentacao:
        break
    else:
        print('Opção inválida.')
while True:
    esgoto_input = input('\nA rua possui coleta de esgoto pública? [S/N]' ).strip().upper()
    if not esgoto_input:
        print('Digite uma opção válida.')
        continue
    esgoto = esgoto_input [0]
    if esgoto in ('S', 'N'):
        break
    else:
        print('Opção inválida.')
while True:
    rampa_input = input('Existem rampas de acessibilidade que permitam o trânsito de cadeira de rodas por toda a via? [S/N]' ).strip().upper()
    if not rampa_input:
        print('Digite uma opção válida.')
        continue
    rampa = rampa_input [0]
    if rampa in ('S', 'N'):
        break
    else:
        print('Opção inválida.')
arvore_total = piso_tatil_total = soma_lotes = soma_construida = soma_permeavel = l = tot_morador = 0
contagem_tipos = {
    'U': 0,
    'M': 0,
    'C': 0,
    'I': 0,
    'P': 0
}
while True:
    tipo_input = input('''\nTIPO DE OCUPAÇÃO DO LOTE: 
[U] Residência Unifamiliar
[M] Residência Multifamiliar
[C] Comercial
[I] Industrial
[P] Área pública/Institucional
    ''').strip().upper()
    if not tipo_input:
        print("Digite uma opção válida.")
        continue
    tipo = tipo_input[0]
    if tipo in ('U', 'M'):
        contagem_tipos[tipo] += 1
        lote = float(input('Qual o tamanho do lote (m²)? '))
        soma_lotes += lote
        l += 1
        unidade = float(input('Qual a área construída da(s) edificação(ções) (m²)? '))
        soma_construida += unidade
        permeavel = float(input('Qual a área permeável? '))
        soma_permeavel += permeavel
        morador = float(input('Quantos moradores moram na residência? '))
        tot_morador += morador
        piso_tatil = input('Existe piso tátil na calçada? [S/N]' )
        if piso_tatil.strip().upper() == 'S':
            piso_tatil_total += 1
        arvore = int(input('Quantas árvores estão plantadas na calçada? '))
        arvore_total += arvore
    elif tipo in ('C', 'I', 'P'):
        contagem_tipos[tipo] += 1
        lote = float(input('Qual o tamanho do lote (m²)? '))
        soma_lotes += lote
        l += 1
        unidade = float(input('Qual a área construída da(s) edificação(ções) (m²)? '))
        soma_construida += unidade
        permeavel = float(input('Qual a área permeável? '))
        soma_permeavel += permeavel
        piso_tatil = input('Existe piso tátil na calçada? [S/N]')
        if piso_tatil.strip().upper() == 'S':
            piso_tatil_total += 1
        arvore = int(input('Quantas árvores estão plantadas na calçada? '))
        arvore_total += arvore
    else:
        print('Opção inválida!')
    proximo_input = input('Deseja continuar? [S/N]').strip().upper()
    if not proximo_input:
        print("Digite S ou N.")
        continue
    proximo = proximo_input[0]
    if proximo == 'N':
        break
if soma_lotes > 0:
    ca = soma_construida / soma_lotes
    to = (soma_lotes - soma_permeavel) / soma_lotes * 100
    ip = soma_permeavel / soma_lotes
    print(f'\nQuantidade de lotes da análise = {l}')
    print('\nÍNDICES URBANÍSTICOS (MÉDIA PONDERADA):')
    print(f'Índice de aproveitamento médio da área estudada = {ca:.2f}')
    print(f'Taxa de ocupação média da área estudada = {to:.2f}%')
    print(f'Índice de permeabilidade média da área estudada = {ip:.2f}')
    print('\nCOMPOSIÇÃO DA VIA:')
    nomes = {
        'U': 'Edificações Residenciais Unifamiliares',
        'M': 'Edificações Residenciais Multifamiliares',
        'C': 'Edificações Comerciais',
        'I': 'Edificações Industriais',
        'P': 'Edificações Públicas/Institucionais'
    }
    for chave in contagem_tipos:
        if contagem_tipos[chave] > 0:
            print(f'{nomes[chave]}')
else:
    print('Nenhum lote foi inserido.')
print(f'Cobertura da via: {pavimentacao[tipo_via]}')
print(f'A via contempla {arvore_total} árvores')
if l > 0:
    percentual_piso_tatil = int((piso_tatil_total / l) * 100)
else:
    percentual_piso_tatil = 0
print(f'{percentual_piso_tatil} % dos lotes possuem piso tátil')
if esgoto == 'S':
    print('A via possui coleta de esgoto pública')
else:
    print('A via não possui coleta de esgoto pública')
if rampa == 'S':
    print('A via possui rampas de acessibilidade que permitam o trânsito de cadeira de rodas por toda sua extensão')
else:
    print('A via não possui rampas de acessibilidade que permitam o trânsito de cadeira de rodas por toda sua extensão')
print('\nDENSIDADE POPULACIONAL:')
print(f'A área total (vias + lotes): {area_via + soma_lotes:.2f}m²')
print(f'A área dos lotes do estudo possuem {soma_lotes:.2f} m² e {int(tot_morador)} moradores')
if soma_lotes > 0:
    densidade = tot_morador * 1_000_000 / soma_lotes
else:
    densidade = 0
print(f'A densidade populacional do objeto de estudo é de {densidade:.2f} hab/km²')
classificacao = ''
if l == 0:
    classificacao = 'Sem dados suficientes'
else:
    tipo_predominante = max(contagem_tipos, key=contagem_tipos.get)
    if contagem_tipos[tipo_predominante] / l >= 0.6:
        if tipo_predominante == 'U':
            classificacao = 'Tecido residencial horizontal predominante'
        elif tipo_predominante == 'M':
            classificacao = 'Tecido residencial verticalizado'
        elif tipo_predominante == 'C':
            classificacao = 'Eixo comercial estruturado'
        elif tipo_predominante == 'I':
            classificacao = 'Zona de predominância industrial'
        elif tipo_predominante == 'P':
            classificacao = 'Zona institucional predominante'
    else:
        classificacao = 'Tecido urbano de uso misto'
print('\nCLASSIFICAÇÃO MORFOLÓGICA:')
print(classificacao)
if densidade < 2000:
    classe_densidade = 'Baixa densidade urbana'
elif densidade < 8000:
    classe_densidade = 'Média densidade urbana'
else:
    classe_densidade = 'Alta densidade urbana'
print(f'Classe: {classe_densidade}')