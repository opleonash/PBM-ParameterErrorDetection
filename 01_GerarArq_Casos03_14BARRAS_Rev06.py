# -*- coding: utf-8 -*-
"""
01 - Gerar os arquivos de Lote para simulação para rodar o ANATEM.
Na versão A, para um erro no gerador X, são aplicados degraus em todas as barras para treinamento da ML.
Na versão B, para cada erro em um gerador, são aplicados degraus somente na barra em questão.
Após gerar os casos, rodar o ANATEM em Lote
Rev04: Somente degraus de tensão. Além de erro de ka, erro de H
Em versões futuras:
    - colocar o valor de ka errado ou H errado aleatório (por isso, importante mudar a estrutura)
#Não esquecer de abrir no lote do ANATEM tanto os casos sem erro, quanto os casos com erro de parâmetro.
"""
import numpy as np
import shutil
from ANATEMstb import STB, CDU, BLT
import matplotlib.pyplot as plt

#Retorna um vetor de valores aleatórios com distribuição uniforme entre valor min e valor max excluindo-se um % em TORNO do valor escolhido.
#Por exemplo: 
#x_exato  = 100
#x_min = 10% de 100 = 10
#x_max = 500% de 100 = 500
#x_perc = 2%
# ele vai gerar pontos entre 10 e 100, excluindo-se valores entre 98 e 102.

def rdmValErroPar(qtde, x_exato, x_min, x_max, x_perc):
    
    x = [] 
    np.random.seed(10) 
    for i in range(qtde): 
        num_aleatorio = np.random.uniform(x_min, x_max)
        
    
        if (1 - x_perc)*x_exato <= num_aleatorio < (1 + x_perc)*x_exato: #se o valor estiver dentro da faixa
            #se o valor for maior que o valor correto, ele joga para a faixa de cima:
            if(num_aleatorio > x_exato):    
                num_aleatorio = np.random.uniform((1 + x_perc)*x_exato, x_max)
            #senão na faixa de baixo
            else:
                num_aleatorio = np.random.uniform(x_min, (1 - x_perc)*x_exato)
        
        x.append(num_aleatorio)
    
    return x


# x = rdmValErroPar(1000, 100, 0.1*100, 5*100, 0.02)
# indices = np.arange(1000)

# plt.figure(figsize=(10, 6))
# plt.scatter(indices, x, label='Vetor de 1000 elementos', color='b', s=10)
# plt.xlabel('Índice')
# plt.ylabel('Valor')
# plt.title('Gráfico do Vetor de 1000 Elementos')
# plt.legend()
# plt.grid(True)
# plt.show()



#Utiliza como base para gerar os arquivos STB, CDU o BLT os arquivos na pasta "ArqANATEMOrig"

#Gerar degraus em diferentes barras, curto-circuitos em diversos pontos, retirar e colocar gerador no sistema.

#NÃO PRECISO CRIAR TANTAS CLASSES
#Instâncias de Classes:
Blt1 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb1 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu1 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt2 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb2 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu2 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt3 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb3 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu3 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt4 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb4 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu4 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt5 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb5 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu5 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt6 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb6 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu6 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt7 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb7 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu7 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt8 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb8 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu8 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt9 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb9 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu9 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt10 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb10 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu10 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt11 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb11 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu11 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt12 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb12 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu12 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt13 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb13 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu13 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt14 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb14 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu14 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt15 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb15 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu15 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt16 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb16 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu16 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt17 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb17 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu17 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt18 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb18 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu18 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt19 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb19 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu19 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt20 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb20 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu20 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt21 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb21 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu21 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt22 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb22 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu22 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt23 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb23 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu23 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt24 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb24 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu24 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')

Blt25 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\16GENERATOR.blt')
Stb25 = STB(NameFileStbOrig= 'ArqANATEMOrig\\68bus_ANATEM_modificado.stb') 
Cdu25 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\16GENERATOR.cdu')



# Blt20 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb20 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu20 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt51 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb51 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu51 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt52 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb52 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu52 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt53 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb53 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu53 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt54 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb54 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu54 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt55 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb55 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu55 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt56 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb56 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu56 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')

# Blt57 = BLT(NameFileBltOrig= 'ArqANATEMOrig\\SIS14B.BLT')
# Stb57 = STB(NameFileStbOrig= 'ArqANATEMOrig\\SIS14B_2.STB') 
# Cdu57 = CDU(NameFileCduOrig= 'ArqANATEMOrig\\SIS14B.CDU')






#Parâmetros de Simulação:
TempoSimul = 40 #tempo de simulação deve ser igual ao que à RNA foi gerada!
#TempoSimul = 200 #tempo de simulação deve ser igual ao que à RNA foi gerada!
NumSimul = 100
DegrauMaxPerc = 0.20 
#DegrauMaxPerc = 0.05 
DegrauMinPerc = 0
TempoIniDeg = 1
TempoFimDeg = 20
#TempoFimDeg = 100

#Quantidade de casos de fluxo de potência:
StartCaso = 1
NumCasosFluxPot = 1

#Perturbação natural: degraus de tensão
degrau = [] 
np.random.seed(10) #degraus de tensão sejam os mesmos
for i in range(NumSimul): 
    degrau.append(np.random.uniform(DegrauMinPerc, DegrauMaxPerc))


#Valores de Erros de Parâmetros Aleatórios 
ValMinPerc = 0.1 #10% do valor real
faixaPerc = 0.01 #faixa em torno de 2% (dentro os valores de parâmetros estão ok) (tinha testado inicialmente com 2%)
ValMaxPerc = 5.00 #500% é o erro máximo do parâmetro


#ValErroKp_1001_AVRG1_B01 = rdmValErroPar(NumSimul, 200, ValMinPerc*200, ValMaxPerc*200, faixaPerc) #Erro 1
ValErroKa_1006_AVR_G6_B06 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 1
ValErroKa_1001_AVR_G1_B01 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 2
ValErroKa_1004_AVR_G4_B04 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 3
ValErroKa_1002_AVR_G2_B02 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 4
ValErroKa_1003_AVR_G3_B03 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 5
ValErroKa_1008_AVR_G8_B08 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 6
ValErroKa_1012_AVR_G12_B12 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 7
ValErroKp_1008_AVR_G8_B08 = rdmValErroPar(NumSimul, 200, ValMinPerc*200, ValMaxPerc*200, faixaPerc) #Erro 8
ValErroTr_1009_AVR_G9_B09 = rdmValErroPar(NumSimul, 0.01, ValMinPerc*0.01, ValMaxPerc*0.01, faixaPerc) #Erro 9
ValErroAex_1001_AVR_G1_B01 = rdmValErroPar(NumSimul, 0.0000319, ValMinPerc*0.0000319, ValMaxPerc*0.0000319, faixaPerc) #Erro 10
ValErroKe_1006_AVR_G6_B06 = rdmValErroPar(NumSimul, 1, ValMinPerc*1, ValMaxPerc*1, faixaPerc) #Erro 11
ValErroTe_1007_AVR_G7_B07 = rdmValErroPar(NumSimul, 0.785, ValMinPerc*0.785, ValMaxPerc*0.785, faixaPerc) #Erro 12
ValErroK_1102_PSS_G2_B02 = rdmValErroPar(NumSimul, 20, ValMinPerc*20, ValMaxPerc*20, faixaPerc) #Erro 13
ValErroT1_1112_PSS_G12_B12 = rdmValErroPar(NumSimul, 0.15, ValMinPerc*0.15, ValMaxPerc*0.15, faixaPerc) #Erro 14
ValErroT2_1105_PSS_G5_B05 = rdmValErroPar(NumSimul, 0.04, ValMinPerc*0.04, ValMaxPerc*0.04, faixaPerc) #Erro 15
ValErroTW_1102_PSS_G2_B02 = rdmValErroPar(NumSimul, 15, ValMinPerc*15, ValMaxPerc*15, faixaPerc) #Erro 16
ValErroT3_1109_PSS_G9_B09 = rdmValErroPar(NumSimul, 0.09, ValMinPerc*0.09, ValMaxPerc*0.09, faixaPerc) #Erro 17
ValErroT4_1107_PSS_G7_B07 = rdmValErroPar(NumSimul, 0.04, ValMinPerc*0.04, ValMaxPerc*0.04, faixaPerc) #Erro 18

ValErroH_blt_0006_B06 = rdmValErroPar(NumSimul, 34.8, ValMinPerc*34.8, ValMaxPerc*34.8, faixaPerc) #Erro 19
ValErroH_blt_0010_B10 = rdmValErroPar(NumSimul, 31.0, ValMinPerc*31.0, ValMaxPerc*31.0, faixaPerc) #Erro 20
ValErroLd_blt_0012_B12 = rdmValErroPar(NumSimul, 10.1, ValMinPerc*10.1, ValMaxPerc*10.1, faixaPerc) #Erro 21
ValErroTld_blt_0011_B11 = rdmValErroPar(NumSimul, 4.1, ValMinPerc*4.1, ValMaxPerc*4.1, faixaPerc) #Erro 22
ValErroTlld_blt_0008_B08 = rdmValErroPar(NumSimul, 0.05, ValMinPerc*0.05, ValMaxPerc*0.05, faixaPerc) #Erro 23
ValErroLl_blt_0004_B04 = rdmValErroPar(NumSimul, 2.95, ValMinPerc*2.95, ValMaxPerc*2.95, faixaPerc) #Erro 24
ValErroTllq_blt_0009_B09 = rdmValErroPar(NumSimul, 0.035, ValMinPerc*0.035, ValMaxPerc*0.035, faixaPerc) #Erro 25


# ValErroKa_23_RGT_MAQ_B06 = rdmValErroPar(NumSimul, 408, ValMinPerc*408, ValMaxPerc*408, faixaPerc) #Erro 1
# ValErroKa_20_RGT_MAQ_B01 = rdmValErroPar(NumSimul, 408, ValMinPerc*408, ValMaxPerc*408, faixaPerc) #Erro 2
# ValErroKa_31_RGT_MAQ_B14 = rdmValErroPar(NumSimul, 25, ValMinPerc*25, ValMaxPerc*25, faixaPerc) #Erro 3
# ValErroKa_21_RGT_MAQ_B02 = rdmValErroPar(NumSimul, 408, ValMinPerc*408, ValMaxPerc*408, faixaPerc) #Erro 4
# ValErroKa_22_RGT_MAQ_B03 = rdmValErroPar(NumSimul, 408, ValMinPerc*408, ValMaxPerc*408, faixaPerc) #Erro 5
# ValErroKa_11_RGT_MAQ_B08 = rdmValErroPar(NumSimul, 300, ValMinPerc*300, ValMaxPerc*300, faixaPerc) #Erro 6
# ValErroKa_12_RGT_MAQ_B12 = rdmValErroPar(NumSimul, 300, ValMinPerc*300, ValMaxPerc*300, faixaPerc) #Erro 7
# ValErroH_Modelo202 = rdmValErroPar(NumSimul, 3.588, ValMinPerc*3.588, ValMaxPerc*3.588, faixaPerc) #Erro 8 e 9
# ValErroH_Modelo201 = rdmValErroPar(NumSimul, 2.474, ValMinPerc*2.474, ValMaxPerc*2.474, faixaPerc) #Erro 10
# ValErroKe_23_RGT_MAQ_B06 = rdmValErroPar(NumSimul, 1.0, ValMinPerc*1.0, ValMaxPerc*1.0, faixaPerc) #Erro 11
# ValErroR_40_RGV_MAQ_B01 = rdmValErroPar(NumSimul, 0.05, ValMinPerc*0.05, ValMaxPerc*0.05, faixaPerc) #Erro 12
# ValErroTw_40_RGV_MAQ_B01 = rdmValErroPar(NumSimul, 1.5, ValMinPerc*1.5, ValMaxPerc*1.5, faixaPerc) #Erro 13
# ValErroR_41_RGV_MAQ_B02 = rdmValErroPar(NumSimul, 0.05, ValMinPerc*0.05, ValMaxPerc*0.05, faixaPerc) #Erro 14
# ValErroTw_41_RGV_MAQ_B02 = rdmValErroPar(NumSimul, 1.5, ValMinPerc*1.5, ValMaxPerc*1.5, faixaPerc) #Erro 15
# ValErroAt_42_RGV_MAQ_B06 = rdmValErroPar(NumSimul, 1.2, ValMinPerc*1.2, ValMaxPerc*1.2, faixaPerc) #Erro 16
# ValErroD_43_RGV_MAQ_B14 = rdmValErroPar(NumSimul, 1.0, ValMinPerc*1.0, ValMaxPerc*1.0, faixaPerc) #Erro 17
# ValErroAex_11_RGT_MAQ_B08 = rdmValErroPar(NumSimul, 0.0147, ValMinPerc*0.0147, ValMaxPerc*0.0147, faixaPerc) #Erro 18
# ValErroLq_Modelo201 = rdmValErroPar(NumSimul, 59.9, ValMinPerc*59.9, ValMaxPerc*59.9, faixaPerc) #Erro 19
# ValErroT2d_Modelo202 = rdmValErroPar(NumSimul, 0.048, ValMinPerc*0.048, ValMaxPerc*0.048, faixaPerc) #Erro 20

# ValErroBex_21_RGT_MAQ_B02 = rdmValErroPar(NumSimul, 1.36, ValMinPerc*1.36, ValMaxPerc*1.36, faixaPerc) #Erro 51
# ValErroKf_20_RGT_MAQ_B01 = rdmValErroPar(NumSimul, 0.1046, ValMinPerc*0.1046, ValMaxPerc*0.1046, faixaPerc) #Erro 52
# ValErroTe_22_RGT_MAQ_B03 = rdmValErroPar(NumSimul, 1.0, ValMinPerc*1.0, ValMaxPerc*1.0, faixaPerc) #Erro 53
# ValErroTf_23_RGT_MAQ_B06 = rdmValErroPar(NumSimul, 3.17, ValMinPerc*3.17, ValMaxPerc*3.17, faixaPerc) #Erro 54
# ValErroTf_11_RGT_MAQ_B08 = rdmValErroPar(NumSimul, 3.0, ValMinPerc*3.0, ValMaxPerc*3.0, faixaPerc) #Erro 55
# ValErroBex_12_RGT_MAQ_B12 = rdmValErroPar(NumSimul, 1.206, ValMinPerc*1.206, ValMaxPerc*1.206, faixaPerc) #Erro 56
# ValErroTa_31_RGT_MAQ_B14 = rdmValErroPar(NumSimul, 0.2, ValMinPerc*0.2, ValMaxPerc*0.2, faixaPerc) #Erro 57





    
#Barras de Geração ou compensador síncrono para degraus (número dos CDUs dos RTs onde serão aplicados degraus, não os CDUs com erros de parãmetros):
#nCDU_DegV = [11, 12, 20, 21, 22, 31, 23] 
nCDU_DegV = [1006, 1001, 1004, 1002, 1003, 1008, 1012, 1007, 1010, 1009, 1011, 1005] 






#Linhas para curto circuito
  
#Arquivos e parâmetros Sem erros:
FileStbSEM = []      #Nome do arquivo .stb novo a ser gerado
FileCduSEM = []      #Nome do arquivo .cdu novo a ser gerado
FileBltSEM = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltSEM = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduSEM = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltSEM = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutSEM = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogSEM = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro1:
FileStbErro1 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro1 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro1 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro1 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro1 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro1 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro1 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro1 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro2:
FileStbErro2 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro2 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro2 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro2 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro2 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro2 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro2 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro2 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro3:
FileStbErro3 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro3 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro3 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro3 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro3 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro3 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro3 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro3 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro4:
FileStbErro4 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro4 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro4 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro4 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro4 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro4 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro4 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro4 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro5:
FileStbErro5 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro5 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro5 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro5 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro5 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro5 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro5 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro5 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro6:
FileStbErro6 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro6 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro6 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro6 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro6 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro6 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro6 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro6 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro7:
FileStbErro7 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro7 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro7 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro7 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro7 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro7 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro7 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro7 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro8:
FileStbErro8 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro8 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro8 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro8 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro8 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro8 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro8 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro8 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro8:
FileStbErro9 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro9 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro9 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro9 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro9 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro9 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro9 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro9 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Arquivos e parâmetros com Erro8:
FileStbErro10 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro10 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro10 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro10 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro10 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro10 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro10 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro10 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro11 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro11 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro11 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro11 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro11 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro11 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro11 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro11 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro12 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro12 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro12 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro12 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro12 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro12 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro12 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro12 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro13 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro13 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro13 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro13 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro13 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro13 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro13 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro13 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro14 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro14 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro14 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro14 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro14 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro14 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro14 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro14 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro15 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro15 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro15 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro15 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro15 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro15 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro15 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro15 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro16 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro16 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro16 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro16 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro16 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro16 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro16 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro16 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro17 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro17 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro17 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro17 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro17 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro17 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro17 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro17 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro18 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro18 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro18 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro18 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro18 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro18 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro18 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro18 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro19 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro19 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro19 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro19 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro19 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro19 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro19 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro19 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro20 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro20 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro20 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro20 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro20 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro20 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro20 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro20 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro21 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro21 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro21 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro21 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro21 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro21 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro21 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro21 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro22 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro22 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro22 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro22 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro22 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro22 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro22 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro22 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro23 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro23 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro23 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro23 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro23 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro23 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro23 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro23 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro24 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro24 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro24 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro24 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro24 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro24 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro24 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro24 = []  #Nome do parâmetro LOG dentro do arquivo STB

FileStbErro25 = []      #Nome do arquivo .stb novo a ser gerado
FileCduErro25 = []      #Nome do arquivo .cdu novo a ser gerado
FileBltErro25 = []      #Nome do arquivo .blt novo a ser gerado
NameFilePltErro25 = []  #Nome do parâmetro PLT dentro do arquivo STB
NameFileCduErro25 = []  #Nome do parâmetro CDU dentro do arquivo STB
NameFileBltErro25 = []  #Nome do parâmetro BLT dentro do arquivo STB
NameFileOutErro25 = []  #Nome do parâmetro OUT dentro do arquivo STB
NameFileLogErro25 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro51 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro51 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro51 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro51 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro51 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro51 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro51 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro51 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro52 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro52 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro52 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro52 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro52 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro52 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro52 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro52 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro53 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro53 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro53 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro53 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro53 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro53 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro53 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro53 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro54 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro54 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro54 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro54 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro54 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro54 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro54 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro54 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro55 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro55 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro55 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro55 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro55 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro55 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro55 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro55 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro56 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro56 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro56 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro56 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro56 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro56 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro56 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro56 = []  #Nome do parâmetro LOG dentro do arquivo STB

# FileStbErro57 = []      #Nome do arquivo .stb novo a ser gerado
# FileCduErro57 = []      #Nome do arquivo .cdu novo a ser gerado
# FileBltErro57 = []      #Nome do arquivo .blt novo a ser gerado
# NameFilePltErro57 = []  #Nome do parâmetro PLT dentro do arquivo STB
# NameFileCduErro57 = []  #Nome do parâmetro CDU dentro do arquivo STB
# NameFileBltErro57 = []  #Nome do parâmetro BLT dentro do arquivo STB
# NameFileOutErro57 = []  #Nome do parâmetro OUT dentro do arquivo STB
# NameFileLogErro57 = []  #Nome do parâmetro LOG dentro do arquivo STB

#Diretórios de Arquivos para serem processados em lote:
dirSem   = 'LOTE-Sem\\'
dirErro1 = 'LOTE-Erro_01\\'
dirErro2 = 'LOTE-Erro_02\\'
dirErro3 = 'LOTE-Erro_03\\'
dirErro4 = 'LOTE-Erro_04\\'
dirErro5 = 'LOTE-Erro_05\\'
dirErro6 = 'LOTE-Erro_06\\'
dirErro7 = 'LOTE-Erro_07\\'
dirErro8 = 'LOTE-Erro_08\\'
dirErro9 = 'LOTE-Erro_09\\'
dirErro10 = 'LOTE-Erro_10\\'
dirErro11 = 'LOTE-Erro_11\\'
dirErro12 = 'LOTE-Erro_12\\'
dirErro13 = 'LOTE-Erro_13\\'
dirErro14 = 'LOTE-Erro_14\\'
dirErro15 = 'LOTE-Erro_15\\'
dirErro16 = 'LOTE-Erro_16\\'
dirErro17 = 'LOTE-Erro_17\\'
dirErro18 = 'LOTE-Erro_18\\'
dirErro19 = 'LOTE-Erro_19\\'
dirErro20 = 'LOTE-Erro_20\\'
dirErro21 = 'LOTE-Erro_21\\'
dirErro22 = 'LOTE-Erro_22\\'
dirErro23 = 'LOTE-Erro_23\\'
dirErro24 = 'LOTE-Erro_24\\'
dirErro25 = 'LOTE-Erro_25\\'

# dirErro51 = 'LOTE-Erro_51\\'
# dirErro52 = 'LOTE-Erro_52\\'
# dirErro53 = 'LOTE-Erro_53\\'
# dirErro54 = 'LOTE-Erro_54\\'
# dirErro55 = 'LOTE-Erro_55\\'
# dirErro56 = 'LOTE-Erro_56\\'
# dirErro57 = 'LOTE-Erro_57\\'





#Continuo usando a estrutura de lote para gerar os casos de simulação. Mas somente altera os eventos

#Nome de Arquivo Padrão: Erro_01_Rest_1_ncdu_01_DegrV_01

#Nome do Arquivo de Histórico de Fluxo de potência (gerado pelo ANAREDE):
arqSAV = 'NETS_NYPS_VB.HIS'

#Copiar o arquivo .SAV para os diretórios anteriores (necessário para carregar casos de fluxo de pot no ANATEM)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirSem + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro1 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro2 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro3 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro4 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro5 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro6 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro7 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro8 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro9 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro10 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro11 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro12 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro13 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro14 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro15 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro16 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro17 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro18 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro19 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro20 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro21 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro22 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro23 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro24 + arqSAV)
shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro25 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro51 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro52 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro53 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro54 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro55 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro56 + arqSAV)
# shutil.copy('ArqANATEMOrig\\' + arqSAV, dirErro57 + arqSAV)



#manter a geração de vários arquivos BLTs ou CDUs para gerar erros aleatorios neles tbm. Fazer um "for" por fora para grupo de erro em %.
#Assim a gente consegue avaliar qual % de erro ele consegue classificar bem



#Casos sem erro: 
for j in range(StartCaso, NumCasosFluxPot+1):
    
    for k in nCDU_DegV: #no caso sem erro, são gerados degraus DE TENSÃO em todas as barras. São cdus do RT correspondente
    
        for i in range(NumSimul):
    
            #Arquivo .stb a ser gerado        
            FileStbSEM.append(dirSem + 'Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
            
            #Nomes dos Parâmetros ULOG dentro do arquivo STB
            NameFilePltSEM.append('PLT\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
            NameFileCduSEM.append('CDU\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
            NameFileBltSEM.append('BLT\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
            #NameFileOutSEM.append('(OUT\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
            #NameFileLogSEM.append('(LOG\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
            Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbSEM[-1],
                                      NameFilePlotNew=NameFilePltSEM[-1],
                                      NameFileCduNew=NameFileCduSEM[-1],
                                      NameFileBltNew=NameFileBltSEM[-1],
                                      #NameFileOutNew=NameFileOutSEM[-1],
                                      #NameFileLogNew=NameFileLogSEM[-1],
                                      Rest = j,
                                      ABS_DEVT_TCDUNew=degrau[i],
                                      ncduNew=k,
                                      timeIniDegNew=TempoIniDeg,
                                      timeFinDegNew=TempoFimDeg,
                                      timeSimulNew=TempoSimul
                                      )
            
            #Arquivo .cdu a ser gerado        
            FileCduSEM.append(dirSem + 'CDU\\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
            Cdu1.CreateNewCduNewParam(NameFileCduNew=FileCduSEM[-1])
            
            #Arquivo .blt a ser gerado        
            FileBltSEM.append(dirSem + 'BLT\\Sem_00_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
            Blt1.CreateNewBltNewParam(NameFileBltNew= FileBltSEM[-1])
            
            
       
#Casos com erro 1: Ka = valor orig.=1  (    1006 AVR_G6 ) - barra 06  Ncdu = 1006
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1006 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro1.append(dirErro1 + 'Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro1.append('PLT\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro1.append('CDU\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro1.append('BLT\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro1.append('(OUT\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro1.append('(LOG\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro1[-1],
                                  NameFilePlotNew=NameFilePltErro1[-1],
                                  NameFileCduNew=NameFileCduErro1[-1],
                                  NameFileBltNew=NameFileBltErro1[-1],
                                  #NameFileOutNew=NameFileOutErro1[-1],
                                  #NameFileLogNew=NameFileLogErro1[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro1.append(dirErro1 + 'CDU\\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu1.CreateNewCduNewParam(NameFileCduNew=FileCduErro1[-1],
                                  Ka_1006_AVR_G6_New=ValErroKa_1006_AVR_G6_B06[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro1.append(dirErro1 + 'BLT\\Erro_01_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt1.CreateNewBltNewParam(NameFileBltNew= FileBltErro1[-1])
                
# # #---------------------------------------------------------------------------------------
#Casos com erro 2: Ka = valor orig.=1  (    1001 AVR_G1 ) - barra 01  Ncdu = 1001
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1001 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro2.append(dirErro2 + 'Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro2.append('PLT\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro2.append('CDU\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro2.append('BLT\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro2.append('(OUT\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro2.append('(LOG\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro2[-1],
                                  NameFilePlotNew=NameFilePltErro2[-1],
                                  NameFileCduNew=NameFileCduErro2[-1],
                                  NameFileBltNew=NameFileBltErro2[-1],
                                 # NameFileOutNew=NameFileOutErro2[-1],
                                  #NameFileLogNew=NameFileLogErro2[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro2.append(dirErro2 + 'CDU\\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu2.CreateNewCduNewParam(NameFileCduNew=FileCduErro2[-1],
                                  Ka_1001_AVR_G1_New=ValErroKa_1001_AVR_G1_B01[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro2.append(dirErro2 + 'BLT\\Erro_02_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt2.CreateNewBltNewParam(NameFileBltNew= FileBltErro2[-1])
        
        
# # #---------------------------------------------------------------------------------------
#Casos com erro 03: Ka = valor orig.=1  (    1004 AVR_G1 ) - barra 4  Ncdu = 1004
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1004 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro3.append(dirErro3 + 'Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro3.append('PLT\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro3.append('CDU\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro3.append('BLT\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro3.append('(OUT\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro3.append('(LOG\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro3[-1],
                                  NameFilePlotNew=NameFilePltErro3[-1],
                                  NameFileCduNew=NameFileCduErro3[-1],
                                  NameFileBltNew=NameFileBltErro3[-1],
                                  #NameFileOutNew=NameFileOutErro3[-1],
                                  #NameFileLogNew=NameFileLogErro3[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro3.append(dirErro3 + 'CDU\\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu3.CreateNewCduNewParam(NameFileCduNew=FileCduErro3[-1],
                                  Ka_1004_AVR_G4_New=ValErroKa_1004_AVR_G4_B04[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro3.append(dirErro3 + 'BLT\\Erro_03_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt3.CreateNewBltNewParam(NameFileBltNew= FileBltErro3[-1])
        
# # #--------------------------------------------------------------------------------------        
#Casos com erro 04: Ka = valor orig.=1  (    1002 AVR_G2 ) - barra 0  Ncdu = 1002
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1002 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro4.append(dirErro4 + 'Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro4.append('PLT\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro4.append('CDU\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro4.append('BLT\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro4.append('(OUT\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro4.append('(LOG\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro4[-1],
                                  NameFilePlotNew=NameFilePltErro4[-1],
                                  NameFileCduNew=NameFileCduErro4[-1],
                                  NameFileBltNew=NameFileBltErro4[-1],
                                  #NameFileOutNew=NameFileOutErro4[-1],
                                  #NameFileLogNew=NameFileLogErro4[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro4.append(dirErro4 + 'CDU\\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu4.CreateNewCduNewParam(NameFileCduNew=FileCduErro4[-1],
                                  Ka_1002_AVR_G2_New=ValErroKa_1002_AVR_G2_B02[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro4.append(dirErro4 + 'BLT\\Erro_04_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt4.CreateNewBltNewParam(NameFileBltNew= FileBltErro4[-1])
        
# # #------------------------------------------------------------------------------------        
#Casos com erro 05:  Ka = valor orig.=1  (    1003 AVR_G3 ) - barra 3  Ncdu = 1003
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1003 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro5.append(dirErro5 + 'Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro5.append('PLT\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro5.append('CDU\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro5.append('BLT\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro5.append('(OUT\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro5.append('(LOG\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro5[-1],
                                  NameFilePlotNew=NameFilePltErro5[-1],
                                  NameFileCduNew=NameFileCduErro5[-1],
                                  NameFileBltNew=NameFileBltErro5[-1],
                                  #NameFileOutNew=NameFileOutErro5[-1],
                                  #NameFileLogNew=NameFileLogErro5[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro5.append(dirErro5 + 'CDU\\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu5.CreateNewCduNewParam(NameFileCduNew=FileCduErro5[-1],
                                  Ka_1003_AVR_G3_New=ValErroKa_1003_AVR_G3_B03[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro5.append(dirErro5 + 'BLT\\Erro_05_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt5.CreateNewBltNewParam(NameFileBltNew= FileBltErro5[-1])
        
# # #------------------------------------------------------------------------------
#Casos com erro 06: Ka = valor orig.=1  (    1008 AVR_G8 ) - barra 8  Ncdu = 1008
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1008 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro6.append(dirErro6 + 'Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro6.append('PLT\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro6.append('CDU\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro6.append('BLT\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro6.append('(OUT\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro6.append('(LOG\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro6[-1],
                                  NameFilePlotNew=NameFilePltErro6[-1],
                                  NameFileCduNew=NameFileCduErro6[-1],
                                  NameFileBltNew=NameFileBltErro6[-1],
                                  #NameFileOutNew=NameFileOutErro6[-1],
                                  #NameFileLogNew=NameFileLogErro6[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro6.append(dirErro6 + 'CDU\\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu6.CreateNewCduNewParam(NameFileCduNew=FileCduErro6[-1],
                                  Ka_1008_AVR_G8_New=ValErroKa_1008_AVR_G8_B08[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro6.append(dirErro6 + 'BLT\\Erro_06_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt6.CreateNewBltNewParam(NameFileBltNew= FileBltErro6[-1])

# # #-----------------------------------------------------------------------------
#Casos com erro 07: Ka = valor orig.=1  (    1012 AVR_G12 ) - barra 12  Ncdu = 1012
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1012 #Ncdu
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro7.append(dirErro7 + 'Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro7.append('PLT\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro7.append('CDU\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro7.append('BLT\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro7.append('(OUT\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out') 
        #NameFileLogErro7.append('(LOG\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro7[-1],
                                  NameFilePlotNew=NameFilePltErro7[-1],
                                  NameFileCduNew=NameFileCduErro7[-1],
                                  NameFileBltNew=NameFileBltErro7[-1],
                                  #NameFileOutNew=NameFileOutErro7[-1],
                                  #NameFileLogNew=NameFileLogErro7[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro7.append(dirErro7 + 'CDU\\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu7.CreateNewCduNewParam(NameFileCduNew=FileCduErro7[-1],
                                  Ka_1012_AVR_G12_New=ValErroKa_1012_AVR_G12_B12[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro7.append(dirErro7 + 'BLT\\Erro_07_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt7.CreateNewBltNewParam(NameFileBltNew= FileBltErro7[-1])
        
#Casos com erro 8: Kp = valor orig.=200  (    1008 AVR_G8 ) - barra 8  Ncdu = 1008

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1008 #Ncdu 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro8.append(dirErro8 + 'Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro8.append('PLT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro8.append('CDU\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro8.append('BLT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro8.append('(OUT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro8.append('(LOG\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb8.CreateNewStbNewParam(NameFileStbNew=FileStbErro8[-1],
                                  NameFilePlotNew=NameFilePltErro8[-1],
                                  NameFileCduNew=NameFileCduErro8[-1],
                                  NameFileBltNew=NameFileBltErro8[-1],
                                  #NameFileOutNew=NameFileOutErro8[-1],
                                  #NameFileLogNew=NameFileLogErro8[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro8.append(dirErro8 + 'CDU\\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu8.CreateNewCduNewParam(NameFileCduNew=FileCduErro8[-1],
                                  Kp_1008_AVR_G8_New= ValErroKp_1008_AVR_G8_B08[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro8.append(dirErro8 + 'BLT\\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt8.CreateNewBltNewParam(NameFileBltNew= FileBltErro8[-1])
                                  
        

# # #Casos com erro 9: Tr = valor orig.=0.01  (    1009 AVR_G9 ) - barra 9  Ncdu = 1009
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1009 #Ncdu (degrau de tensão na barra 14)
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro9.append(dirErro9 + 'Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro9.append('PLT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro9.append('CDU\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro9.append('BLT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro9.append('(OUT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro9.append('(LOG\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb9.CreateNewStbNewParam(NameFileStbNew=FileStbErro9[-1],
                                  NameFilePlotNew=NameFilePltErro9[-1],
                                  NameFileCduNew=NameFileCduErro9[-1],
                                  NameFileBltNew=NameFileBltErro9[-1],
                                  #NameFileOutNew=NameFileOutErro9[-1],
                                  #NameFileLogNew=NameFileLogErro9[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul)
        
        #Arquivo .cdu a ser gerado        
        FileCduErro9.append(dirErro9 + 'CDU\\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu9.CreateNewCduNewParam(NameFileCduNew=FileCduErro9[-1],
                                  Tr_1009_AVR_G9_New=ValErroTr_1009_AVR_G9_B09[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro9.append(dirErro9 + 'BLT\\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt9.CreateNewBltNewParam(NameFileBltNew= FileBltErro9[-1])
        
str_Erro = 'Erro_10'        
#Casos com erro 10: Aex = valor orig.= 0.0000319  (1001 AVR_G1 ) - barra   Ncdu = 1001
for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1001 #Ncdu (degrau de tensão na barra 2)
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro10.append(dirErro10 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro10.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro10.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro10.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro10.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro10.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb10.CreateNewStbNewParam(NameFileStbNew=FileStbErro10[-1],
                                  NameFilePlotNew=NameFilePltErro10[-1],
                                  NameFileCduNew=NameFileCduErro10[-1],
                                  NameFileBltNew=NameFileBltErro10[-1],
                                  #NameFileOutNew=NameFileOutErro10[-1],
                                  #NameFileLogNew=NameFileLogErro10[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro10.append(dirErro10 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu10.CreateNewCduNewParam(NameFileCduNew=FileCduErro10[-1],
                                   Aex_1001_AVR_G1_New=ValErroAex_1001_AVR_G1_B01[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro10.append(dirErro10 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt10.CreateNewBltNewParam(NameFileBltNew= FileBltErro10[-1])     

                                  
str_Erro = 'Erro_11'

# #Casos com erro 11: Ke = (valor orig.=1)  (1006 AVR_G6  ) - barra 06  Ncdu = 1006

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1006 #Ncdu (degrau de tensão na barra 6)
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro11.append(dirErro11 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro11.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro11.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro11.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro11.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro11.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb11.CreateNewStbNewParam(NameFileStbNew=FileStbErro11[-1],
                                  NameFilePlotNew=NameFilePltErro11[-1],
                                  NameFileCduNew=NameFileCduErro11[-1],
                                  NameFileBltNew=NameFileBltErro11[-1],
                                  #NameFileOutNew=NameFileOutErro11[-1],
                                  #NameFileLogNew=NameFileLogErro11[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro11.append(dirErro11 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu11.CreateNewCduNewParam(NameFileCduNew=FileCduErro11[-1],
                                   Ke_1006_AVR_G6_New=ValErroKe_1006_AVR_G6_B06[i])
                                
        
        #Arquivo .blt a ser gerado        
        FileBltErro11.append(dirErro11 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt11.CreateNewBltNewParam(NameFileBltNew= FileBltErro11[-1])
        
str_Erro = 'Erro_12'

# #Casos com erro 12: Te = (valor orig.=0.785)  (1007 AVR_G7  ) - barra 07  Ncdu = 1007

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1007 #Ncdu 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro12.append(dirErro12 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro12.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro12.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro12.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro12.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro12.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb12.CreateNewStbNewParam(NameFileStbNew=FileStbErro12[-1],
                                  NameFilePlotNew=NameFilePltErro12[-1],
                                  NameFileCduNew=NameFileCduErro12[-1],
                                  NameFileBltNew=NameFileBltErro12[-1],
                                  #NameFileOutNew=NameFileOutErro12[-1],
                                  #NameFileLogNew=NameFileLogErro12[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro12.append(dirErro12 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu12.CreateNewCduNewParam(NameFileCduNew=FileCduErro12[-1],
                                   Te_1007_AVR_G7_New=ValErroTe_1007_AVR_G7_B07[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro12.append(dirErro12 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt12.CreateNewBltNewParam(NameFileBltNew= FileBltErro12[-1])



str_Erro = 'Erro_13'

# #Casos com erro 13:  K = (valor orig.=20)  (1102  PSS_G2  ) - barra 02  Ncdu = 1002 (degrau no RT, não no PSS!!)

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1002 #Ncdu (degrau de tensão na barra 02) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro13.append(dirErro13 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro13.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro13.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro13.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro13.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro13.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb13.CreateNewStbNewParam(NameFileStbNew=FileStbErro13[-1],
                                  NameFilePlotNew=NameFilePltErro13[-1],
                                  NameFileCduNew=NameFileCduErro13[-1],
                                  NameFileBltNew=NameFileBltErro13[-1],
                                  #NameFileOutNew=NameFileOutErro13[-1],
                                  #NameFileLogNew=NameFileLogErro13[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro13.append(dirErro13 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu13.CreateNewCduNewParam(NameFileCduNew=FileCduErro13[-1],
                                   K_1102_PSS_G2_New=ValErroK_1102_PSS_G2_B02[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro13.append(dirErro13 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt13.CreateNewBltNewParam(NameFileBltNew= FileBltErro13[-1])

# #-------------------------------------------------------------------------------

str_Erro = 'Erro_14'

# #Casos com erro 14: T1 = (valor orig.=0.15)  (1112  PSS_G12  ) - barra 12  Ncdu = 1012 (degrau no RT, não no PSS!!)

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1012 #Ncdu (degrau de tensão na barra 12) - observação: não degrau de em wref!
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro14.append(dirErro14 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro14.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro14.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro14.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro14.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro14.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb14.CreateNewStbNewParam(NameFileStbNew=FileStbErro14[-1],
                                  NameFilePlotNew=NameFilePltErro14[-1],
                                  NameFileCduNew=NameFileCduErro14[-1],
                                  NameFileBltNew=NameFileBltErro14[-1],
                                  #NameFileOutNew=NameFileOutErro14[-1],
                                  #NameFileLogNew=NameFileLogErro14[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro14.append(dirErro14 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu14.CreateNewCduNewParam(NameFileCduNew=FileCduErro14[-1],
                                   T1_1112_PSS_G12_New=ValErroT1_1112_PSS_G12_B12[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro14.append(dirErro14 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt14.CreateNewBltNewParam(NameFileBltNew= FileBltErro14[-1])
        
        
# #-------------------------------------------------------------------------------

str_Erro = 'Erro_15'

# #Casos com erro 15:  T2 = (valor orig.=0.04)  (1112  PSS_G5  ) - barra 5  Ncdu = 1005 (degrau no RT, não no PSS!!)

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1005 #Ncdu (degrau de tensão na barra 05) - observação: não degrau de em wref!
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro15.append(dirErro15 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro15.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro15.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro15.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        NameFileOutErro15.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        NameFileLogErro15.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb15.CreateNewStbNewParam(NameFileStbNew=FileStbErro15[-1],
                                  NameFilePlotNew=NameFilePltErro15[-1],
                                  NameFileCduNew=NameFileCduErro15[-1],
                                  NameFileBltNew=NameFileBltErro15[-1],
                                  NameFileOutNew=NameFileOutErro15[-1],
                                  NameFileLogNew=NameFileLogErro15[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro15.append(dirErro15 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu15.CreateNewCduNewParam(NameFileCduNew=FileCduErro15[-1],
                                   T2_1105_PSS_G5_New=ValErroT2_1105_PSS_G5_B05[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro15.append(dirErro15 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt15.CreateNewBltNewParam(NameFileBltNew= FileBltErro15[-1])
                

#--------------------------------------------------------------------------------

str_Erro = 'Erro_16'

# #Casos com erro 16: TW = (valor orig.=15)  (1102  PSS_G2) - barra 02  Ncdu = 1002

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1002 #Ncdu (degrau de tensão na barra 02) - 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro16.append(dirErro16 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro16.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro16.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro16.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro16.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro16.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb16.CreateNewStbNewParam(NameFileStbNew=FileStbErro16[-1],
                                  NameFilePlotNew=NameFilePltErro16[-1],
                                  NameFileCduNew=NameFileCduErro16[-1],
                                  NameFileBltNew=NameFileBltErro16[-1],
                                  #NameFileOutNew=NameFileOutErro16[-1],
                                  #NameFileLogNew=NameFileLogErro16[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro16.append(dirErro16 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu16.CreateNewCduNewParam(NameFileCduNew=FileCduErro16[-1],
                                   TW_1102_PSS_G2_New=ValErroTW_1102_PSS_G2_B02[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro16.append(dirErro16 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt16.CreateNewBltNewParam(NameFileBltNew= FileBltErro16[-1])
        
# #--------------------------------------------------------------------------------

str_Erro = 'Erro_17'

#Casos com erro 17: T3 = (valor orig.=0.09)  (1109_PSS_G9) - barra 09  Ncdu = 1009

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1009 #Ncdu (degrau de tensão na barra 06) - observação: não degrau de em wref!
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro17.append(dirErro17 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro17.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro17.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro17.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro17.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro17.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb17.CreateNewStbNewParam(NameFileStbNew=FileStbErro17[-1],
                                  NameFilePlotNew=NameFilePltErro17[-1],
                                  NameFileCduNew=NameFileCduErro17[-1],
                                  NameFileBltNew=NameFileBltErro17[-1],
                                  #NameFileOutNew=NameFileOutErro17[-1],
                                  #NameFileLogNew=NameFileLogErro17[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro17.append(dirErro17 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu17.CreateNewCduNewParam(NameFileCduNew=FileCduErro17[-1],
                                   T3_1109_PSS_G9_New=ValErroT3_1109_PSS_G9_B09[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro17.append(dirErro17 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt17.CreateNewBltNewParam(NameFileBltNew= FileBltErro17[-1])
        
        
#--------------------------------------------------------------------------------

str_Erro = 'Erro_18'

#Casos com erro 18: T4 = (valor orig.=0.04)  (1107_PSS_G7) - barra 07  Ncdu = 1007

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1007 #Ncdu (degrau de tensão na barra 08) - observação: não degrau de em wref! (aqui coincidiu ser igual)
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro18.append(dirErro18 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro18.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro18.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro18.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro18.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro18.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb18.CreateNewStbNewParam(NameFileStbNew=FileStbErro18[-1],
                                  NameFilePlotNew=NameFilePltErro18[-1],
                                  NameFileCduNew=NameFileCduErro18[-1],
                                  NameFileBltNew=NameFileBltErro18[-1],
                                  #NameFileOutNew=NameFileOutErro18[-1],
                                  #NameFileLogNew=NameFileLogErro18[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro18.append(dirErro18 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu18.CreateNewCduNewParam(NameFileCduNew=FileCduErro18[-1],
                                   T4_1107_PSS_G7_New=ValErroT4_1107_PSS_G7_B07[i])
        
        #Arquivo .blt a ser gerado        
        FileBltErro18.append(dirErro18 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt18.CreateNewBltNewParam(NameFileBltNew= FileBltErro18[-1])
        
#---------------------------------------------------------------------------------


str_Erro = 'Erro_19'

#Casos com erro 19: H = (valor orig.=34.8)  - barra 06  Ncdu = 1006

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1006 #Ncdu (degrau de tensão na barra 02) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro19.append(dirErro19 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro19.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro19.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro19.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro19.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro19.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb19.CreateNewStbNewParam(NameFileStbNew=FileStbErro19[-1],
                                  NameFilePlotNew=NameFilePltErro19[-1],
                                  NameFileCduNew=NameFileCduErro19[-1],
                                  NameFileBltNew=NameFileBltErro19[-1],
                                  #NameFileOutNew=NameFileOutErro19[-1],
                                  #NameFileLogNew=NameFileLogErro19[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro19.append(dirErro19 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu19.CreateNewCduNewParam(NameFileCduNew=FileCduErro19[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro19.append(dirErro19 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt19.CreateNewBltNewParam(NameFileBltNew= FileBltErro19[-1],
                                   H_blt_0006 = ValErroH_blt_0006_B06[i])
        

str_Erro = 'Erro_20'

#Casos com erro 20: H = (valor orig.=31)  - barra 10  Ncdu = 1010

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1010 #Ncdu (degrau de tensão na barra 10) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro20.append(dirErro20 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro20.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro20.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro20.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro20.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro20.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb20.CreateNewStbNewParam(NameFileStbNew=FileStbErro20[-1],
                                  NameFilePlotNew=NameFilePltErro20[-1],
                                  NameFileCduNew=NameFileCduErro20[-1],
                                  NameFileBltNew=NameFileBltErro20[-1],
                                  #NameFileOutNew=NameFileOutErro20[-1],
                                  #NameFileLogNew=NameFileLogErro20[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro20.append(dirErro20 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu20.CreateNewCduNewParam(NameFileCduNew=FileCduErro20[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro20.append(dirErro20 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt20.CreateNewBltNewParam(NameFileBltNew= FileBltErro20[-1],
                                   H_blt_0010=ValErroH_blt_0010_B10[i])  
        
        
        

str_Erro = 'Erro_21'

#Casos com erro 21: Ld = (valor orig.=10.1)  - barra 12  Ncdu = 1012

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1012 #Ncdu (degrau de tensão na barra 02) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro21.append(dirErro21 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro21.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro21.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro21.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro21.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro21.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb21.CreateNewStbNewParam(NameFileStbNew=FileStbErro21[-1],
                                  NameFilePlotNew=NameFilePltErro21[-1],
                                  NameFileCduNew=NameFileCduErro21[-1],
                                  NameFileBltNew=NameFileBltErro21[-1],
                                  #NameFileOutNew=NameFileOutErro21[-1],
                                  #NameFileLogNew=NameFileLogErro21[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro21.append(dirErro21 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu21.CreateNewCduNewParam(NameFileCduNew=FileCduErro21[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro21.append(dirErro21 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt21.CreateNewBltNewParam(NameFileBltNew= FileBltErro21[-1],
                                   Ld_blt_0012 = ValErroLd_blt_0012_B12[i])
        
        
str_Erro = 'Erro_22'

#Casos com erro 22: T'd = (valor orig.=4.1)  - barra 11  Ncdu = 1011
    

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1011 #Ncdu (degrau de tensão na barra 02) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro22.append(dirErro22 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro22.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro22.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro22.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro22.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro22.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb22.CreateNewStbNewParam(NameFileStbNew=FileStbErro22[-1],
                                  NameFilePlotNew=NameFilePltErro22[-1],
                                  NameFileCduNew=NameFileCduErro22[-1],
                                  NameFileBltNew=NameFileBltErro22[-1],
                                  #NameFileOutNew=NameFileOutErro22[-1],
                                  #NameFileLogNew=NameFileLogErro22[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro22.append(dirErro22 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu22.CreateNewCduNewParam(NameFileCduNew=FileCduErro22[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro22.append(dirErro22 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt22.CreateNewBltNewParam(NameFileBltNew= FileBltErro22[-1],
                                   Tld_blt_0011 = ValErroTld_blt_0011_B11[i])
                                  
        
        
str_Erro = 'Erro_23'

#Casos com erro 23:  T"d = (valor orig.=0.05)  - barra 08  Ncdu = 1008

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1008 #Ncdu (degrau de tensão na barra 09) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro23.append(dirErro23 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro23.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro23.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro23.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro23.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro23.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb23.CreateNewStbNewParam(NameFileStbNew=FileStbErro23[-1],
                                  NameFilePlotNew=NameFilePltErro23[-1],
                                  NameFileCduNew=NameFileCduErro23[-1],
                                  NameFileBltNew=NameFileBltErro23[-1],
                                  #NameFileOutNew=NameFileOutErro23[-1],
                                  #NameFileLogNew=NameFileLogErro23[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro23.append(dirErro23 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu23.CreateNewCduNewParam(NameFileCduNew=FileCduErro23[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro23.append(dirErro23 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt23.CreateNewBltNewParam(NameFileBltNew= FileBltErro23[-1],
                                   Tlld_blt_0008 = ValErroTlld_blt_0008_B08[i])

str_Erro = 'Erro_24'

#Casos com erro 24: Ll = (valor orig.=2.95)  - barra 04  Ncdu = 1004

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1004 #Ncdu (degrau de tensão na barra 4) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro24.append(dirErro24 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro24.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro24.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro24.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro24.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro24.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb24.CreateNewStbNewParam(NameFileStbNew=FileStbErro24[-1],
                                  NameFilePlotNew=NameFilePltErro24[-1],
                                  NameFileCduNew=NameFileCduErro24[-1],
                                  NameFileBltNew=NameFileBltErro24[-1],
                                  #NameFileOutNew=NameFileOutErro24[-1],
                                  #NameFileLogNew=NameFileLogErro24[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro24.append(dirErro24 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu24.CreateNewCduNewParam(NameFileCduNew=FileCduErro24[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro24.append(dirErro24 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt24.CreateNewBltNewParam(NameFileBltNew= FileBltErro24[-1],
                                   Ll_blt_0004=ValErroLl_blt_0004_B04[i])
                                   
        
        

str_Erro = 'Erro_25'

#Casos com erro 25: T"q = (valor orig.=0.035)  - barra 09  Ncdu = 1009
   

for j in range(StartCaso, NumCasosFluxPot+1):
    
    k = 1009 #Ncdu (degrau de tensão na barra 09) 
    
    for i in range(NumSimul):

        #Arquivo .stb a ser gerado        
        FileStbErro25.append(dirErro25 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
        #Nomes dos Parâmetros ULOG dentro do arquivo STB
        NameFilePltErro25.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
        NameFileCduErro25.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
        NameFileBltErro25.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
        #NameFileOutErro25.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
        #NameFileLogErro25.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
        Stb25.CreateNewStbNewParam(NameFileStbNew=FileStbErro25[-1],
                                  NameFilePlotNew=NameFilePltErro25[-1],
                                  NameFileCduNew=NameFileCduErro25[-1],
                                  NameFileBltNew=NameFileBltErro25[-1],
                                  #NameFileOutNew=NameFileOutErro25[-1],
                                  #NameFileLogNew=NameFileLogErro25[-1],
                                  Rest = j,
                                  ABS_DEVT_TCDUNew=degrau[i],
                                  ncduNew=k,
                                  timeIniDegNew=TempoIniDeg,
                                  timeFinDegNew=TempoFimDeg,
                                  timeSimulNew=TempoSimul
                                  )
        
        #Arquivo .cdu a ser gerado        
        FileCduErro25.append(dirErro25 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
        Cdu25.CreateNewCduNewParam(NameFileCduNew=FileCduErro25[-1])
                                   
        
        #Arquivo .blt a ser gerado        
        FileBltErro25.append(dirErro25 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
        Blt25.CreateNewBltNewParam(NameFileBltNew= FileBltErro25[-1],
                                   Tllq_blt_0009=ValErroTllq_blt_0009_B09[i])
                                  
#---------------------------------------------------------------------------------                                   


# str_Erro = 'Erro_20'
# #modelo202
# #Casos com erro 20: T''D = (valor orig.=0.048)  

# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 20 #Ncdu (degrau de tensão na barra 01) 
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro20.append(dirErro20 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro20.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro20.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro20.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro20.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro20.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb20.CreateNewStbNewParam(NameFileStbNew=FileStbErro20[-1],
#                                   NameFilePlotNew=NameFilePltErro20[-1],
#                                   NameFileCduNew=NameFileCduErro20[-1],
#                                   NameFileBltNew=NameFileBltErro20[-1],
#                                   NameFileOutNew=NameFileOutErro20[-1],
#                                   NameFileLogNew=NameFileLogErro20[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro20.append(dirErro20 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu20.CreateNewCduNewParam(NameFileCduNew=FileCduErro20[-1])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro20.append(dirErro20 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt20.CreateNewBltNewParam(NameFileBltNew= FileBltErro20[-1],
#                                    T2d_Modelo202 = ValErroT2d_Modelo202[i])
        
# #---------------------------------------------------------------------------------        

#Os erros 51 a 57 são para classes não definidas no modelo:
#Um erro por barra onde tiver gerador ou compensador



# #Erro no RT da barra 02
# #Casos com erro 51: Bex (valor orig.=1.36)  (21 RGT_MAQ_B02) - barra 02  Ncdu = 21
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 21 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro51.append(dirErro51 + 'Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro51.append('PLT\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro51.append('CDU\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro51.append('BLT\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro51.append('(OUT\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro51.append('(LOG\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro51[-1],
#                                   NameFilePlotNew=NameFilePltErro51[-1],
#                                   NameFileCduNew=NameFileCduErro51[-1],
#                                   NameFileBltNew=NameFileBltErro51[-1],
#                                   NameFileOutNew=NameFileOutErro51[-1],
#                                   NameFileLogNew=NameFileLogErro51[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro51.append(dirErro51 + 'CDU\\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu51.CreateNewCduNewParam(NameFileCduNew=FileCduErro51[-1],
#                                   Bex_21_RGT_MAQ_B02New=ValErroBex_21_RGT_MAQ_B02[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro51.append(dirErro51 + 'BLT\\Erro_51_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt51.CreateNewBltNewParam(NameFileBltNew= FileBltErro51[-1])
        
#-------------------------------------------------------------------------------------------------------------------------


# #Erro no RT da barra 01
# #Casos com erro 52: Kf = valor orig.=0.1046  (20 RGT_MAQ_B01) - barra 01  Ncdu = 20
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 20 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro52.append(dirErro52 + 'Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro52.append('PLT\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro52.append('CDU\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro52.append('BLT\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro52.append('(OUT\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro52.append('(LOG\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro52[-1],
#                                   NameFilePlotNew=NameFilePltErro52[-1],
#                                   NameFileCduNew=NameFileCduErro52[-1],
#                                   NameFileBltNew=NameFileBltErro52[-1],
#                                   NameFileOutNew=NameFileOutErro52[-1],
#                                   NameFileLogNew=NameFileLogErro52[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro52.append(dirErro52 + 'CDU\\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu52.CreateNewCduNewParam(NameFileCduNew=FileCduErro52[-1],
#                                     Kf_20_RGT_MAQ_B01New=ValErroKf_20_RGT_MAQ_B01[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro52.append(dirErro52 + 'BLT\\Erro_52_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt52.CreateNewBltNewParam(NameFileBltNew= FileBltErro52[-1])
        
#-------------------------------------------------------------------------------------------------------------------------        


# #Erro no RT da barra 03      
# #Casos com erro 53: Te (valor orig.=1)  (22 RGT_MAQ_B03) - barra 03  Ncdu = 22
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 22 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro53.append(dirErro53 + 'Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro53.append('PLT\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro53.append('CDU\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro53.append('BLT\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro53.append('(OUT\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro53.append('(LOG\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro53[-1],
#                                   NameFilePlotNew=NameFilePltErro53[-1],
#                                   NameFileCduNew=NameFileCduErro53[-1],
#                                   NameFileBltNew=NameFileBltErro53[-1],
#                                   NameFileOutNew=NameFileOutErro53[-1],
#                                   NameFileLogNew=NameFileLogErro53[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro53.append(dirErro53 + 'CDU\\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu53.CreateNewCduNewParam(NameFileCduNew=FileCduErro53[-1],
#                                   Te_22_RGT_MAQ_B03New=ValErroTe_22_RGT_MAQ_B03[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro53.append(dirErro53 + 'BLT\\Erro_53_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt53.CreateNewBltNewParam(NameFileBltNew= FileBltErro53[-1])
    

#-------------------------------------------------------------------------------------------------------------------------        


# #Erro no RT da barra 06
# #Casos com erro 54: Tf: (valor orig.=3.17)  (23 RGT_MAQ_B06) - barra 06  Ncdu = 23
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 23 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro54.append(dirErro54 + 'Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro54.append('PLT\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro54.append('CDU\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro54.append('BLT\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro54.append('(OUT\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro54.append('(LOG\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb54.CreateNewStbNewParam(NameFileStbNew=FileStbErro54[-1],
#                                   NameFilePlotNew=NameFilePltErro54[-1],
#                                   NameFileCduNew=NameFileCduErro54[-1],
#                                   NameFileBltNew=NameFileBltErro54[-1],
#                                   NameFileOutNew=NameFileOutErro54[-1],
#                                   NameFileLogNew=NameFileLogErro54[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro54.append(dirErro54 + 'CDU\\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu54.CreateNewCduNewParam(NameFileCduNew=FileCduErro54[-1],
#                                   Tf_23_RGT_MAQ_B06New=ValErroTf_23_RGT_MAQ_B06[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro54.append(dirErro54 + 'BLT\\Erro_54_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt54.CreateNewBltNewParam(NameFileBltNew= FileBltErro54[-1])
        
#-------------------------------------------------------------------------------------------------------------------------        


# # #Erro no RT da barra 08

# #Casos com erro 55: Tf :valor orig.=3.0  (11 RGT_MAQ_B08) - barra 08  Ncdu = 11
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 11 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro55.append(dirErro55 + 'Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro55.append('PLT\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro55.append('CDU\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro55.append('BLT\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro55.append('(OUT\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro55.append('(LOG\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro55[-1],
#                                   NameFilePlotNew=NameFilePltErro55[-1],
#                                   NameFileCduNew=NameFileCduErro55[-1],
#                                   NameFileBltNew=NameFileBltErro55[-1],
#                                   NameFileOutNew=NameFileOutErro55[-1],
#                                   NameFileLogNew=NameFileLogErro55[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro55.append(dirErro55 + 'CDU\\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu55.CreateNewCduNewParam(NameFileCduNew=FileCduErro55[-1],
#                                   Tf_11_RGT_MAQ_B08New=ValErroTf_11_RGT_MAQ_B08[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro55.append(dirErro55 + 'BLT\\Erro_55_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt55.CreateNewBltNewParam(NameFileBltNew= FileBltErro55[-1])

#-------------------------------------------------------------------------------------------------------------------------        


# # #Erro no RT da barra 12

# #Casos com erro 56: Bex valor orig.=1.206)  (12 RGT_MAQ_B12) - barra 12  Ncdu = 12
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 12 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro56.append(dirErro56 + 'Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro56.append('PLT\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro56.append('CDU\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro56.append('BLT\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro56.append('(OUT\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out') 
#         NameFileLogErro56.append('(LOG\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro56[-1],
#                                   NameFilePlotNew=NameFilePltErro56[-1],
#                                   NameFileCduNew=NameFileCduErro56[-1],
#                                   NameFileBltNew=NameFileBltErro56[-1],
#                                   NameFileOutNew=NameFileOutErro56[-1],
#                                   NameFileLogNew=NameFileLogErro56[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro56.append(dirErro56 + 'CDU\\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu56.CreateNewCduNewParam(NameFileCduNew=FileCduErro56[-1],
#                                   Bex_12_RGT_MAQ_B12New=ValErroBex_12_RGT_MAQ_B12[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro56.append(dirErro56 + 'BLT\\Erro_56_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt56.CreateNewBltNewParam(NameFileBltNew= FileBltErro56[-1])
        
#-------------------------------------------------------------------------------------------------------------------------        


# # #Erro no RT da barra 14       

# #Casos com erro 57: Ta = valor orig.=0.2  (31 RGT_MAQ_B14) - barra 014  Ncdu = 31
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 31 #Ncdu
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro57.append(dirErro57 + 'Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro57.append('PLT\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro57.append('CDU\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro57.append('BLT\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro57.append('(OUT\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro57.append('(LOG\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb1.CreateNewStbNewParam(NameFileStbNew=FileStbErro57[-1],
#                                   NameFilePlotNew=NameFilePltErro57[-1],
#                                   NameFileCduNew=NameFileCduErro57[-1],
#                                   NameFileBltNew=NameFileBltErro57[-1],
#                                   NameFileOutNew=NameFileOutErro57[-1],
#                                   NameFileLogNew=NameFileLogErro57[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro57.append(dirErro57 + 'CDU\\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu57.CreateNewCduNewParam(NameFileCduNew=FileCduErro57[-1],
#                                   Ta_31_RGT_MAQ_B14New=ValErroTa_31_RGT_MAQ_B14[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro57.append(dirErro57 + 'BLT\\Erro_57_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt57.CreateNewBltNewParam(NameFileBltNew= FileBltErro57[-1])
        

           
# #-----------------------------------------------------------------------------------
# #Para os erros de BLT (H, Ld, etc.) tem dois modelos de Geradores:
# #modelo 201: barra 2, 3, 6, 8, 12 
# #modelo 202: barra 1 e 14
# #Ou seja, mudando o valor de um parâmetro de um modelo de um gerador, alterar o valor do parâmetro dos geradores das barras que tem o mesmo modelo!

# #Casos com erro 8: H = 5 (valor orig.=3.588) nos geradores das barras 1 e/ou 14. Observação: aplico degrau de tensão somente na barra 1 (maior P)
# #Depois fazer com erro 9 = erro nos geradores 2,3 etc.. (se não, vou ter que separar)
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 20 #Ncdu (degrau de tensão na barra 1)
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro8.append(dirErro8 + 'Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro8.append('PLT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro8.append('CDU\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro8.append('BLT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro8.append('(OUT\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro8.append('(LOG\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb8.CreateNewStbNewParam(NameFileStbNew=FileStbErro8[-1],
#                                   NameFilePlotNew=NameFilePltErro8[-1],
#                                   NameFileCduNew=NameFileCduErro8[-1],
#                                   NameFileBltNew=NameFileBltErro8[-1],
#                                   NameFileOutNew=NameFileOutErro8[-1],
#                                   NameFileLogNew=NameFileLogErro8[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro8.append(dirErro8 + 'CDU\\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu8.CreateNewCduNewParam(NameFileCduNew=FileCduErro8[-1])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro8.append(dirErro8 + 'BLT\\Erro_08_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt8.CreateNewBltNewParam(NameFileBltNew= FileBltErro8[-1],
#                                   H_Modelo202=ValErroH_Modelo202[i])
# #---------------------------------------------------------------------------------------        

# # #Casos com erro 9: H = 6 (valor orig.=3.588) nos geradores das barras . Observação: aplico degrau de tensão somente na barra 14 neste caso;
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 31 #Ncdu (degrau de tensão na barra 14)
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro9.append(dirErro9 + 'Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro9.append('PLT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro9.append('CDU\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro9.append('BLT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro9.append('(OUT\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro9.append('(LOG\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb9.CreateNewStbNewParam(NameFileStbNew=FileStbErro9[-1],
#                                   NameFilePlotNew=NameFilePltErro9[-1],
#                                   NameFileCduNew=NameFileCduErro9[-1],
#                                   NameFileBltNew=NameFileBltErro9[-1],
#                                   NameFileOutNew=NameFileOutErro9[-1],
#                                   NameFileLogNew=NameFileLogErro9[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro9.append(dirErro9 + 'CDU\\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu9.CreateNewCduNewParam(NameFileCduNew=FileCduErro9[-1])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro9.append(dirErro9 + 'BLT\\Erro_09_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt9.CreateNewBltNewParam(NameFileBltNew= FileBltErro9[-1],
#                                   H_Modelo202=ValErroH_Modelo202[i])
# #---------------------------------------------------------------------------------------    
# #A moral da história acima é que, ao aplicarmos degrau na barra 1 ou 14 (ou nas duas), o modelo identifica que tem erro na barra 1 e 14 (mas não diz em qual especificamente)

# str_Erro = 'Erro_10'
             
# #Casos com erro 10: H = (valor orig.=2.474) nos geradores das barras 2 (28,3 MW), 3 (CS), 6 (19,3 MW), 8 (CS) e 12 (CS). Observação: aplico degrau de tensão somente na barra 2 neste caso;
# #Neste caso, para um degrau na barra 2, no caso do erro10, indica erro no parâmetro H das barras 2, 3, 6, 8 ou 12
# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 21 #Ncdu (degrau de tensão na barra 2)
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro10.append(dirErro10 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro10.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro10.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro10.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro10.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro10.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb10.CreateNewStbNewParam(NameFileStbNew=FileStbErro10[-1],
#                                   NameFilePlotNew=NameFilePltErro10[-1],
#                                   NameFileCduNew=NameFileCduErro10[-1],
#                                   NameFileBltNew=NameFileBltErro10[-1],
#                                   NameFileOutNew=NameFileOutErro10[-1],
#                                   NameFileLogNew=NameFileLogErro10[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro10.append(dirErro10 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu10.CreateNewCduNewParam(NameFileCduNew=FileCduErro10[-1])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro10.append(dirErro10 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt10.CreateNewBltNewParam(NameFileBltNew= FileBltErro10[-1],
#                                   H_Modelo201=ValErroH_Modelo201[i])        


#-------------------------------------------------------------------------------

# str_Erro = 'Erro_11'

# # #Casos com erro 11: Ke = (valor orig.=1)  (23 RGT_MAQ_B06) - barra 06  Ncdu = 23

# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 23 #Ncdu (degrau de tensão na barra 6)
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro11.append(dirErro11 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro11.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro11.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro11.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro11.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro11.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb11.CreateNewStbNewParam(NameFileStbNew=FileStbErro11[-1],
#                                   NameFilePlotNew=NameFilePltErro11[-1],
#                                   NameFileCduNew=NameFileCduErro11[-1],
#                                   NameFileBltNew=NameFileBltErro11[-1],
#                                   NameFileOutNew=NameFileOutErro11[-1],
#                                   NameFileLogNew=NameFileLogErro11[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro11.append(dirErro11 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu11.CreateNewCduNewParam(NameFileCduNew=FileCduErro11[-1],
#                                    Ke_23_RGT_MAQ_B06New=ValErroKe_23_RGT_MAQ_B06[i]
#                                    )
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro11.append(dirErro11 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt11.CreateNewBltNewParam(NameFileBltNew= FileBltErro11[-1])
        
# #-------------------------------------------------------------------------------

# str_Erro = 'Erro_12'

# # #Casos com erro 11: R = (valor orig.=0.05)  (40 RGV_MAQ_B01) - barra 01  Ncdu = 40

# for j in range(StartCaso, NumCasosFluxPot+1):
    
#     k = 20 #Ncdu (degrau de tensão na barra 01) - observação: não degrau de em wref!
    
#     for i in range(NumSimul):

#         #Arquivo .stb a ser gerado        
#         FileStbErro12.append(dirErro12 + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.STB')
        
#         #Nomes dos Parâmetros ULOG dentro do arquivo STB
#         NameFilePltErro12.append('PLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.plt')
#         NameFileCduErro12.append('CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.cdu')
#         NameFileBltErro12.append('BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.blt')
#         NameFileOutErro12.append('(OUT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.out')
#         NameFileLogErro12.append('(LOG\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.log')
#         Stb12.CreateNewStbNewParam(NameFileStbNew=FileStbErro12[-1],
#                                   NameFilePlotNew=NameFilePltErro12[-1],
#                                   NameFileCduNew=NameFileCduErro12[-1],
#                                   NameFileBltNew=NameFileBltErro12[-1],
#                                   NameFileOutNew=NameFileOutErro12[-1],
#                                   NameFileLogNew=NameFileLogErro12[-1],
#                                   Rest = j,
#                                   ABS_DEVT_TCDUNew=degrau[i],
#                                   ncduNew=k,
#                                   timeIniDegNew=TempoIniDeg,
#                                   timeFinDegNew=TempoFimDeg,
#                                   timeSimulNew=TempoSimul
#                                   )
        
#         #Arquivo .cdu a ser gerado        
#         FileCduErro12.append(dirErro12 + 'CDU\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.CDU')
#         Cdu12.CreateNewCduNewParam(NameFileCduNew=FileCduErro12[-1],
#                                    R_40_RGV_MAQ_B01New=ValErroR_40_RGV_MAQ_B01[i])
        
#         #Arquivo .blt a ser gerado        
#         FileBltErro12.append(dirErro12 + 'BLT\\' + str_Erro + '_Rest_' + str(j) + '_ncdu_' + str(k) + '_DegV_' + str(i) + '.BLT')
#         Blt12.CreateNewBltNewParam(NameFileBltNew= FileBltErro12[-1])


#-------------------------------------------------------------------------------