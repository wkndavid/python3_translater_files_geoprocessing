import pandas as pd
import re

#####################################################
# => Traduz os acrônimos                            #
def traduzir_palavra(palavra, dicionario):          #
    return dicionario.get(palavra, palavra)         #
#                                                   #
#####################################################

################################################################################################
# => Traduz a coluna                                                                           # 
def traduzir_colunas(df, colunas, traducoes):                                                  #     
    for coluna in colunas:                                                                     #     
        df[coluna] = df[coluna].apply(lambda x: ' '.join(traduzir_palavra(palavra, traducoes)  #
         for palavra in re.findall(r'\b\w+\b', str(x)))).str.upper()                           #             
    return df                                                                                  # 
################################################################################################
#
#######################################################################################
# => Exemplo de aplicação em diferentes colunas da mesma tabela#                      #  
tabela = pd.read_excel('/home/david/autom/version2/files/setor-teste-dictionary.xlsx')#
#######################################################################################
#
######################################################
# => Substitua com os nomes reais das colunas        #
colunas_a_traduzir = ['se_setor', 'qu_setor', 'nome']# 
#                                                    #
######################################################
#
###################################################################################################
traducoes = {
    'SH' : 'Setor Habitacional',
    'ACR' :'Abrigo Cristo Redentor',
    'ADE' : 'Área de Desenvolvimento Econômico',
    'AE' : 'Área Especial',
    'AeB' : 'Aeroporto de Brasília',
    'AEB' : 'Aeroporto de Brasília',
    'AEMN' : 'Área de Expansão dos Ministérios Norte',
    'SEC' : 'Setor de Expansão Econômica',
    'StEC' : 'Setor de Expansão Econômica',
    'AOS' : 'Área Octogonal Sul',
    'APO' : 'Academia de Polícia',
    'ARIE' : 'Área de Relevante Interesse Ecológico',
    'AVPR' : 'Área Verde de Proteção e Reserva',
    'SHJB' : 'Setor Habitacional Jardim Botânico',
    'BOT' : 'Jardim Botânico',
    'BSB' : 'Brasília',
    'CA' : 'Centro de Atividades - Lago Norte',
    'CADF' : 'Centro Administrativo do Distrito Federal',
    'CCSW' : 'Centro Comercial Sudoeste ',
    'CEN' : 'Cemitério Norte',
    'CES' : 'Cemitério Sul',
    'CE/UNB' : 'Campus Experimental da UnB',
    'CE-UNB' : 'Campus Experimental da UnB',
    'CEUNB' : 'Campus Experimental da UnB',
    'CE' : 'Campus Experimental da UnB',
    'CE/UnB' : 'Campus Experimental da UnB',
    'CE-UnB' : 'Campus Experimental da UnB',
    'CEUnB' : 'Campus Experimental da UnB',
    'CE' : 'Campus Experimental da UnB',
    'CL' : 'Comércio Local',
    'CLN' : 'Comércio Local Norte',
    'CLRN' : 'Comércio Local Residencial Norte',
    'CLS' : 'Comércio Local Sul',
    'CLSW' : 'Comércio Local Sudoeste',
    'CRN' : 'Comércio Residencial Sul',
    'CRS' : 'Comércio Residencial Sul',
    'EMI' : 'Esplanada dos Ministérios',
    'EMO' : 'Eixo Monumental',
    'EM' : 'Eixo Monumental',
    'EPAA' : 'Estrada Parque Armazenamento e Abastecimento (DF–010)',
    'EPAC' : 'Estrada Parque Acampamento (DF–097)',
    'EPAR' : 'Estrada Parque Aeroporto (DF–047)',
    'EPCA' : 'Estrada Parque Centro de Atividades (DF–006)',
    'EPCL' : 'Estrada Parque Ceilândia (DF–095)',
    'EPCT' : 'Estrada Parque Contorno (DF–001)',
    'EPCV' : 'Estrada Parque Cabeça do Veado (DF–035)',
    'EPDB' : 'Estrada Parque Dom Bosco (DF–025)',
    'EPGU' : 'Estrada Parque Guará (DF–051)',
    'EPIA' : 'Estrada Parque Indústria e Abastecimento (DF–003)',
    'EPIB' : 'Estrada Parque Interbairros (DF–081)',
    'EPIG' : 'Estrada Parque Indústrias Gráficas (DF–011)',
    'EPIP' : 'Estrada Parque Ipê (DF–065)',
    'EPJK' : 'Estrada Parque Juscelino Kubitschek (DF–027)',
    'EPNA' : 'Estrada Parque das Nações (DF–004)',
    'EPNB' : 'Estrada Parque Núcleo Bandeirante (DF–075)',
    'EPPN' : 'Estrada Parque Península Norte (DF–009)',
    'EPPR' : 'Estrada Parque Paranoá (DF–005)',
    'EPTG' : 'Estrada Parque Taguatinga (DF–085)',
    'EPTM' : 'Estrada Parque Tamanduá (DF–015)',
    'EPTT' : 'Estrada Parque Torto (DF–007)',
    'EPUB' : 'Estrada Parque Universidade de Brasília (DF–008)',
    'EPVB' : 'Estrada Parque Vargem Bonita (DF–055)',
    'EPVL' : 'Estrada Parque Vale (DF–087)',
    'EPVP' : 'Estrada Parque Vicente Pires (DF–079)',
    'EQN' : 'Entrequadra Norte',
    'EQS' : 'Entrequadra Sul',
    'ERL' : 'Norte – Eixo Rodoviário Leste – Sentido Norte - Eixo L/Eixinho ',
    'ERL' : 'Sul – Eixo Rodoviário Leste – Sentido Sul - Eixo L/Eixinho',
    'ERN' : 'Eixo Rodoviário Norte',
    'ERS' : 'Eixo Rodoviário Sul',
    'ERW' : 'Norte – Eixo Rodoviário Oeste – Sentido Norte  - Eixo W/Eixinho',
    'ERW' : 'Sul – Eixo Rodoviário Oeste – Sentido Sul  - Eixo W/Eixinho',
    'ESAF' : 'Escola de Administração Fazendária',
    'ETO' : 'Esplanada da Torre de Televisão',
    'ML' : 'Mansões do Lago',
    'MI' : 'Mansões do Lago',
    'PCH' : 'Polígono de Captação Hídrica',
    'PFB' : 'Parque Ferroviário de Brasília',
    'PFR' : 'Plataforma Rodoviária',
    'PMU' : 'Praça Municipal',
    'PQEAT' : 'Parque de Exposição Agropecuária do Torto',
    'PQEB' : 'Parque Estação Biológica - Embrapa Asa Norte',
    'PQEN' : 'Parque Ecológico Norte',
    'PQNB' : 'Parque Nacional de Brasília',
    'PqEAT' : 'Parque de Exposição Agropecuária do Torto',
    'PqEB' : 'Parque Estação Biológica - Embrapa Asa Norte',
    'PqEN' : 'Parque Ecológico Norte Burle Marx',
    'PqNB' : 'Parque Nacional de Brasília',
    'PTP' : 'Praça dos Três Poderes',
    'QELC' : 'Quadras Econômicas Lúcio Costa  - Guará',
    'QMSW' : 'Quadra Mista Sudoeste ',
    'QRSW' : 'Quadra Residencial Sudoeste - Sudoeste Econômico',
    'RER-IBGE' : 'Reserva Ecológica do Roncador  - IBGE',
    'RERIBGE' : 'Reserva Ecológica do Roncador  - IBGE',
    'RER/IBGE' : 'Reserva Ecológica do Roncador  - IBGE',
    'RER' : 'Reserva Ecológica do Roncador  - IBGE',
    'SAAN' : 'Setor de Armazenagem e Abastecimento Norte',
    'SAA' : 'Setor de Armazenagem e Abastecimento',
    'SAFN' : 'Setor de Administração Federal Norte ',
    'SAFS' : 'Setor de Administração Federal Sul',
    'SAI' : 'Setor de Áreas Isoladas Sudoeste',
    'SAIN' : 'Setor de Áreas Isoladas Norte',
    'SAIS' : 'Setor de Áreas Isoladas Sul',
    'SAM' : 'Setor de Administração Municipal',
    'SAN' : 'Setor de Autarquias Norte',
    'SAUN' : 'Setor de Autarquias Norte ',
    'SAS' : 'Setor de Autarquias Sul',
    'SAUS' : 'Setor de Autarquias Sul',
    'SBN' : 'Setor Bancário Norte',
    'SBS' : 'Setor Bancário Sul',
    'SPS' : 'Setor Policial Sul',
    'SCEEN' : 'Setor de Clubes Esportivos e Estádios Norte',
    'SCEE' : 'Setor de Clubes Esportivos e Estádios',
    'SCEES' : 'Setor de Clubes Esportivos e Estádios Sul',
    'SCEN' : 'Setor de Clubes Esportivos Norte ',
    'SCES' : 'Setor de Clubes Esportivos Sul',
    'SCIA' : 'Setor Complementar de Indústria e Abastecimento',
    'SCLRN' : 'Setor Comercial Local Residencial Norte',
    'SCRS ' : 'Setor Comercial Residencial Sul',
    'SCN' : 'Setor Comercial Norte',
    'SCLS' : 'Setor Comercial Local Sul',
    'SCLN' : 'Setor Comercial Local Norte',
    'SCS' : 'Setor Comercial Sul',
    'SCTN' : 'Setor Cultural Norte  - Teatro Nacional ',
    'SCTS' : 'Setor Cultural Sul',
    'SDC' : 'Setor de Divulgação Cultural',
    'SDMC' : 'Setor de Materiais de Construção - Ceilândia',
    'SDN' : 'Setor de Diversões Norte',
    'SDS' : 'Setor de Diversões Sul',
    'SEDB' : 'Setor Ermida Dom Bosco',
    'SEN' : 'Setor de Embaixadas Norte',
    'SEPN' : 'Setor de Edifícios de Utilidade Pública Norte',
    'SEPS' : 'Setor de Edifícios de Utilidade Pública Sul',
    'SES' : 'Setor de Embaixadas Sul',
    'SEM' : 'Setor de Embaixadas Norte',
    'SEUPS' : 'Setor de Edifícios e Utilidades Públicas Sul',
    'SEUPN' : 'Setor de Edifícios e Utilidades Públicas Sul',
    'SFA' : 'Zona Funcional-Administrativa',
    'SGA' : 'Setor de Grandes Áreas - Sobradinho',
    'SGAN' : 'Setor de Grandes Áreas Norte',
    'SGAP' : 'Setor de Grandes Áreas Públicas',
    'SGAS' : 'Setor de Grandes Áreas Sul',
    'SGCV' : 'Setor de Garagens e Concessionárias de Veículos - Norte e Sul',
    'SGMN' : 'Setor de Garagens dos Ministérios Norte',
    'SGO' : 'Setor de Garagens Oficiais ou Setor de Gairagens e Oficinas Norte',
    'SGON' : 'Setor de Garagens Oficiais ou Setor de Gairagens e Oficinas Norte',
    'SHA' : 'Setor Habitacional Arniqueiras',
    'SHB' : 'Setor Habitacional Buritis',
    'SHCES' : 'Setor de Habitações Coletivas Econômicas Sul - Cruzeiro Novo',
    'SHCGN' : 'Setor Habitacional Coletivas Geminadas Norte',
    'SHCGS' : 'Setor Habitacional Coletivas Geminadas Sul',
    'SHCN' : 'Setor de Habitações Coletivas Norte',
    'SHCAOS' : 'Setor Habitacional Coletivo Área Octogonal Sul',
    'SHCAO' : 'Setor Habitacional Coletivo Área Octogonal',
    'AOS' : 'Área Octogonal Sul',
    'SHCNW' : 'Setor de Habitações Coletivas Noroeste',
    'SHCS' : 'Setor de Habitações Coletivas Sul',
    'SHCSW' : 'Setor de Habitações Coletivas Sudoeste',
    'SHD' : 'Setor de Hotéis e Diversões - ​Planaltina',
    'SHEP' : 'Setor Habitacional Estrada Parque',
    'SHAL' : 'Setor Habitacional Altiplano Leste',
    'SHIGS' : 'Setor de Habitações Individuais Geminadas Sul',
    'SHIN' : 'Setor de Habitações Individuais Norte',
    'SHIP' : 'Setor Hípico',
    'SHSB' : 'Setor Habitacional São Bartolomeu',
    'SHIS' : 'Setor de Habitações Individuais Sul',
    'SHLN' : 'Setor Hospitalar Local Norte',
    'SHLS' : 'Setor Hospitalar Local Sul',
    'SHLSW' : 'Setor Hospitalar Local Sudoeste',
    'SHMA' : 'Setor Habitacional Jardins Mangueiral',
    'SHN' : 'Setor Hoteleiro Norte',
    'SHS' : 'Setor Hoteleiro Sul',
    'SHPS' : 'Setor Habitacional Por do Sol',
    'SHPB': 'Setor Hospitalar Público de Brasília',
    'SHPT': 'Setor Hospitalar Ponte de Terra',
    'SHSN' : 'Setor Habitacional Sol Nascente',
    'SHTN' : 'Setor de Hotéis e Turismo Norte',
    'SHTO' : 'Setor Habitacional Tororó',
    'SHTQ' : 'Setor Habitacional Taquari',
    'SHAQ' : 'Setor Habitacional Águas Quentes',
    'SHJK' : 'Setor Habitacional Juscelino Kubitschek',    
    'SHTS' : 'Setor de Hotéis e Turismo Sul',
    'SIA' : 'Setor de Indústria e Abastecimento',
    'SIBS' : 'Setor de Indústrias Bernardo Sayão',
    'SIG' : 'Setor de Indústrias Gráficas',
    'SIN' : 'Setor de Inflamáveis',
    'SIT' : 'Setor Invernada do Torto',
    'SPMS' : 'Serviços Partilhados do Ministério da Saúde',
    'FAL' : 'Fonte Água Limpa',
    'SMA' : 'Setor de Múltiplas Atividades do Gama',
    'SMAN' : 'Setor de Múltiplas Atividades Norte',
    'SMAS' : 'Setor de Múltiplas Atividades Sul ',
    'SMC' : 'Setor Militar Complementar',
    'SMDB' : 'Setor de Mansões Dom Bosco',
    'SMHN' : 'Setor Médico Hospitalar Norte',
    'SMHS' : 'Setor Médico Hospitalar Sul',
    'SMIN' : 'Setor de Mansões Isoladas Norte',
    'SMI' : 'Setor de Mansões Isoladas',
    'SMIS' : 'Setor de Mansões Isoladas Sul',
    'SMLN' : 'Setor de Mansões Lago Norte',
    'SML' : 'Setor de Mansões Lago',
    'SMPW' : 'Setor de Mansões Park Way',
    'MSPW' : 'Setor de Mansões Park Way',
    'SMU' : 'Setor Militar Urbano',
    'SO' : 'Setor de Oficinas - Norte e Sul',
    'SOF' : 'Setor de Oficinas - Norte e Sul',
    'SOFN' : 'Setor de Oficinas Norte',
    'SOFS' : 'Setor de Oficinas Sul',
    'SOPI' : 'Setor de Oficinas - Núcleo Bandeirante',
    'SPLM' : 'Setor Placa da Mercedes',
    'SPMN' : 'Setor de Postos e Moteis',
    'SPO' : 'Setor Policial',
    'SPP' : 'Setor Palácio Presidencial',
    'SPVP' : 'Setor de Preservação da Vila Planalto',
    'SQN' : 'Superquadra Norte ',
    'SQNW' : 'Superquadra Noroeste ',
    'SQS' : 'Superquadra Sul',
    'SQSW' : 'Superquadra Sudoeste ',
    'SRES' : 'Setor de Residências Econômicas Sul - Cruzeiro Velho',
    'SRIA' : 'Setor Residencial Indústria e Abastecimento',
    'SRPN' : 'Setor de Recreação Pública Norte - Setor Esportivo – Estádio Mané Garrincha',
    'SRPS' : 'Setor de Recreação Pública Sul - Parque da Cidade Sarah Kubitschek',
    'SRTVN' : 'Setor de Rádio e Televisão Norte',
    'SRTVS' : 'Setor de Rádio e Televisão Sul ',
    'STN' : 'Setor Terminal Norte - Região do Boulevard Shopping',
    'STRC' : 'Setor de Transporte Regional de Cargas ',
    'STS' : 'Setor Terminal Sul',
    'UnB' : 'Universidade de Brasília',
    'UNB' : 'Universidade de Brasília',
    'VPLA' : 'Vila Planalto',
    'ZC' : 'Zona Central',
    'ZCA' : 'Zona Cívico-Administrativa',
    'ZE' : 'Zona Especial',
    'ZfN' : 'Zona Industrial',
    'ZFN' : 'Zona Industrial',
    'ZI' : 'Zona Institucional',
    'ZR' : 'Zona Residencial',
    'ZV' : 'Zona Verde',
    'ZU' : 'Zona Urbana',
    'SHCES' : 'Setor de Habitações Coletivas Econômicas Sul - Cruzeiro Novo',
    'SRES' : 'Setor de Residências Econômicas Sul - Cruzeiro Velho',
    'SRPS' : 'Setor de Recreativo e Parques Sul - Parque da Cidade',
    'SRPN' : 'Setor de Recreativo e Parques Norte - Setor Esportivo - Mané Garrincha, Autódromo, Nilson Nelson, Cláudio Coutinho',
    'SHIGS' : 'Setor de Habitações Individuais Geminadas Sul',
    'CCSW' : 'Centro Comercial Sudoeste',
    'PMU' : 'Praça Municipal',
    'SCES' : 'Setor de Clubes Esportivos Sul',
    'SCRN' : 'Setor Comercial Residencial Norte',
    'SHGC' : 'Setor Habitacional Grande Colorado',
    'SCRS' : 'Setor Comercial Residencial Sul',
    'SHCNW' : 'Setor de Habitações Coletivas Noroeste',
    'SHTQ' : 'Setor Habitacional Taquari - Lago Norte',
    'SHMD' : 'Setor Habitacional Mestre D`Armas',
    'EPAA' : 'Estrada Parque Armazenagem e Abastecimento Plano Piloto',
    'EPAR' : 'Estrada Parque Aeroporto',
    'EPCB' : 'Estrada Parque Contorno do Bosque	Plano Piloto',
    'EPCL' : 'Estrada Parque Ceilândia',
    'EPCT' : 'Estrada Parque Contorno Cerca a bacia de águas do lago Paranoá',
    'EPCV' : 'Estrada Parque Cabeça de Veado',
    'EPDB' : 'Estrada Parque Dom Bosco Lago Sul',
    'EPGU' : 'Estrada Parque Guará',
    'EPIA' : 'Estrada Parque Indústria e Abastecimento Norte-Sul',
    'EPIG' : 'Estrada Parque Indústrias Gráficas',
    'EPNB' : 'Estrada Parque Núcleo Bandeirante',
    'EPPN' : 'Estrada Parque Península Norte Lago Norte - Península',
    'EPPR' : 'Estrada Parque Paranoá',
    'EPTG' : 'Estrada Parque Taguatinga',
    'EPTM' : 'Estrada Parque Tamanduá',
    'ERR' : 'Eixo Rodoviária-Residencial',
    'PEVC' : 'Parque Ecológico e Vivencial da Candangolândia',
    'Q' : 'QUADRA',
    'QD' : 'QUADRA',
    'QI' : 'QUADRA INTERNA',
    'QR' : 'QUADRA RESIDENCIAL',
    'SH' : 'SETOR HABITACIONAL',
    'AC' : 'ÁREA COMPLEMENTAR',
    'GMT' : 'Granja Modelo do Torto',
    'AE': 'Área especial',
    'Ent': 'Entrada',
    'Qd': 'Quadra',
    'Agric': 'Agrícola',
    'EQ': 'Entre quadras',
    'QR': 'Quadra residêncial',
    'AR': 'Área reservada',
    'Est': 'Estrada',
    'Resid': 'Residencial',
    'Av': 'Avenida',
    'Faz': 'Fazenda',
    'Rod': 'Rodovia',
    'Bl': 'Bloco',
    'Gj': 'Granja',
    'SN': 'Sem número',
    'Ch': 'Chácara',
    'Lt': 'Lote',
    'Sl': 'Sala',
    'Col': 'Colônia',
    'Lts': 'Lotes',
    'Slj': 'Sobreloja',
    'Cond': 'Condomínio',
    'Mod': 'Módulo',
    'St': 'Setor',
    'Cj': 'Conjunto',
    'NR': 'Núcleo rural',
    'Tr': 'Trecho',
    'CPC': 'Caixa Postal Comunitária',
    'Pc': 'Praça',
    'Vl': 'Vila',
    'Cs': 'Casa',
    'Prq': 'Parque',
    'Ed': 'Edifício',
    'Proj': 'Projeção',
    'MUDB' : 'Setor de Mansões Urbanas Dom Bosco',
    'smudb' : 'Setor de Mansões Urbanas Dom Bosco',
    'SHBJ' : 'Setor Habitacional Bom Jesus',
    'SHVP' : 'Setor Habitacional Vicente Pires',
    'RCG' : 'Regimento de Cavalaria de Guarda do Exército',
    'PTS' : 'Projeto Técnico Social'
    # Setor Habitacional Contagem Sobradinho - is empty...
}
###########################################################################
#              - Python Translater for geoprocessing files -              #
###########################################################################
# => Aplica a tradução às colunas                                         #
tabela_traduzida = traduzir_colunas(tabela, colunas_a_traduzir, traducoes)#
###########################################################################
#
##################################################################################################
# => Salva o DataFrame atualizado em um novo arquivo xlsx já traduzindo os valores nas células   #
tabela_traduzida.to_excel('/home/david/autom/version2/files/tabela_traduzida.xlsx', index=False) #
##################################################################################################
