# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:01:37 2023
Manipular arquivos ANATEM no formato STB
@author: SQ4083
"""
import chardet


class STB:
    def __init__(self,
                 NameFileStbOrig):
        
        self.NameFileStbOrig = NameFileStbOrig
        self.NameFilePlotOrig = 'mbinf_pss.plt'
        self.NameFileOutOrig = 'mbinf_pss.out'
        self.NameFileLogOrig = 'mbinf_pss.log'

        #self.ContentFileStbOrig = self._ReadFileStb()

        #Ler arquivo .stb -> self.ContentFileStbOrig tem o conteúdo do arquivo original (cada linha do arquivo é um array)
        self.ContentFileStbOrig = ''
        self._ReadFileStb()
        
        
    def _ReadFileStb(self):
        #with open(self.NameFileStbOrig, 'r') as file:
        #with open(self.NameFileStbOrig, 'r', encoding='windows-1252') as file:
        #    self.ContentFileStbOrig = file.readlines()
        #    file.close()
    
        with open(self.NameFileStbOrig, 'rb') as file:  # Ler como bytes
            raw_data = file.read()

        detected_encoding = chardet.detect(raw_data)['encoding']  # Detectar a codificação
        if detected_encoding is None:
            detected_encoding = 'utf-8'  # Fallback para UTF-8 se não for detectado

        with open(self.NameFileStbOrig, 'r', encoding=detected_encoding, errors='replace') as file:
            self.ContentFileStbOrig = file.readlines()

        
    #def _ReadFileStb(self):
    #    with open(self.NameFileStbOrig, 'r') as file:
    #        LinesFromFile = file.readlines()
    #        #file.close()
    #    return LinesFromFile
        
            
    #Criar um novo arquivo STB com parâmetros diferentes do arquivo original
    #Para a linha onde encontra-se o parâmetro (array), altera-se o valor da string antiga pela nova (o valor do parâmetro default)        
    #A função somente cria os arquivos .stb. 
    def CreateNewStbNewParam(self, NameFileStbNew = None,
                             NameFilePlotNew = None,
                             NameFileCduNew = None,
                             NameFileBltNew = None,
                             NameFileOutNew = None,
                             NameFileLogNew = None,
                             Rest = 1,
                             HNew=4.938,
                             p1_AVRNew=100.0,
                             ABS_DEVT_TCDUNew=0.01,
                             ncduNew=31,
                             timeIniDegNew=1.0,
                             timeFinDegNew=8.0,
                             timeSimulNew=30.0):
                             #DPLT_DELT=True,
                             #DPLT_FMAQ=True,
                             #DPLT_PELE=True,
                             #DPLT_QELE=True,
                             #DPLT_VOLT=True,
                             #DPLT_CDU_1=True,
                             #DPLT_CDU_2=True,
                             #DPLT_CDU_3=True,
                             #DPLT_CDU_4=True,
                             #DPLT_CDU_5=True,
                             #DPLT_CDU_6=True):
        
        #Copia o conteúdo do arquivo original para uma vaviável nova
        #ContentFileStbNew = self.ContentFileStbOrig
        
        #Lê o arquivo Original direto do arquivo. Forçar a leitura do arquivo original
        self._ReadFileStb()
        ContentFileStbNew = self.ContentFileStbOrig
        
        
        
        #Nas linhas a seguir, realiza a alteração de algumas linhas
        
        #Altera o nome do arquivo de Plot (linha 30 do arquivo stb)
        #ContentFileStbNew[29] = self.ContentFileStbOrig[29].replace(self.NameFilePlotOrig, NameFilePlotNew)
        if NameFilePlotNew is not None:
            ContentFileStbNew[31-1] = NameFilePlotNew + '\n'
        
        #Altera o nome do arquivo de Out 
        if NameFileOutNew is not None:
            ContentFileStbNew[24-1] = NameFileOutNew + '\n'
        
        #Altera o nome do arquivo de Log
        #if NameFileLogNew is not None:
        #    ContentFileStbNew[39-1] = NameFileLogNew  + '\n'
        
        #Altera o nome do arquivo de Blt
        if NameFileBltNew is not None:
            ContentFileStbNew[58-1] = NameFileBltNew  + '\n'
        
        #Altera o nome do arquivo de Cdu
        if NameFileCduNew is not None:
            ContentFileStbNew[62-1] = NameFileCduNew  + '\n'

        #Altera o número de caso do restabelecimento do fluxo de potência:
        #ContentFileStbNew[17-1] = str(Rest) + '\n' 
            
        #Altera o valor de H (linha 60 do arquivo stb, 5 caracteres):
        #ContentFileStbNew[59] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[59], HNew, 13, 17)
        
        #Altera o parâmetro p1 do Regulador de tensão (linha 87, 6 caracteres)
        #ContentFileStbNew[86] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[86], p1_AVRNew, 34, 39)
            
        #Altera o valor de degrau de entrada do regulador (up e down, linhas 151 e 152)
        ContentFileStbNew[97-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[97-1], ABS_DEVT_TCDUNew, 39, 44)
        ContentFileStbNew[98-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[98-1], -ABS_DEVT_TCDUNew, 39, 44)
        
        #Altera o tempo para início e final do degrau
        ContentFileStbNew[97-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[97-1], timeIniDegNew, 6, 13)
        ContentFileStbNew[98-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[98-1], timeFinDegNew, 6, 13)
        
        #Altera o ncdu a ser aplicado o degrau
        ContentFileStbNew[97-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[97-1], ncduNew, 14, 19, integer=True)
        ContentFileStbNew[98-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[98-1], ncduNew, 14, 19, integer=True)
        
        
        #Altera o tempo total de simulação:
        ContentFileStbNew[161-1] = self.WriteValueInColumnANAT(self.ContentFileStbOrig[161-1], timeSimulNew, 1, 8)    
        
        #Altera as linhas (comenta) que não serão plotadas:
        # if DPLT_DELT is False:
        #     ContentFileStbNew[164] = '(' + self.ContentFileStbOrig[164]
        # if DPLT_FMAQ is False:
        #     ContentFileStbNew[165] = '(' + self.ContentFileStbOrig[165] 
        # if DPLT_PELE is False:
        #     ContentFileStbNew[166] = '(' + self.ContentFileStbOrig[166] 
        # if DPLT_QELE is False:
        #     ContentFileStbNew[167] = '(' + self.ContentFileStbOrig[167] 
        # if DPLT_VOLT is False:
        #     ContentFileStbNew[168] = '(' + self.ContentFileStbOrig[168] 
        # if DPLT_CDU_1 is False:
        #     ContentFileStbNew[169] = '(' + self.ContentFileStbOrig[169] 
        # if DPLT_CDU_2 is False:
        #     ContentFileStbNew[170] = '(' + self.ContentFileStbOrig[170] 
        # if DPLT_CDU_3 is False:
        #     ContentFileStbNew[171] = '(' + self.ContentFileStbOrig[171] 
        # if DPLT_CDU_4 is False:
        #     ContentFileStbNew[172] = '(' + self.ContentFileStbOrig[172] 
        # if DPLT_CDU_5 is False:
        #     ContentFileStbNew[173] = '(' + self.ContentFileStbOrig[173] 
        # if DPLT_CDU_6 is False:
        #     ContentFileStbNew[174] = '(' + self.ContentFileStbOrig[174] 

        #Escreve o conteúdo em novo arquivo
        with open(NameFileStbNew, 'w') as FileStbNew:
            fileStbNew = open(NameFileStbNew, 'w')
            fileStbNew.writelines(ContentFileStbNew)
            print('Arquivo ' + str(NameFileStbNew) + ' criado.')                

        return 
    
   

    #altera o valor de um campo (coluna) no .stb
    #posColIni e posColFim são índices de ínicio e fim de coluna de acordo com o manual do ANATEM
    #lineANAT é uma string de uma linha do arquivo .stb
    def WriteValueInColumnANAT(self, strlineANAT, valor, posColIni, posColFim, integer = False):
        posColIni = posColIni - 1 #posColFim não tem alteração de índice
        
        #caso seja um número:
        if integer == True:
            if isinstance(valor, (int, float)):
                #converte em inteiro
                intValor = int(valor)
                #capturar somente os n caracteres para caber na coluna
                strValorComNCaracteres = str(intValor).rjust(posColFim - posColIni)
        else:    
            if isinstance(valor, (int, float)):
                #converte em string com 20 números decimais (força ponto decimal)
                strValorDec = "{:.20f}".format(valor)
                #capturar somente os n caracteres para caber na coluna
                strValorComNCaracteres = strValorDec[:(posColFim - posColIni)]
            if isinstance(valor, str): 
                strValorComNCaracteres = valor
            
        #substitui a string na linha do arquivo .stb na posição da coluna
        return strlineANAT[:posColIni] + strValorComNCaracteres + strlineANAT[posColFim:] 
    
    
    
    
    
#Classe para tratar de um arquivo PLT
#Se onlyData:
#   - None: preserva a estrutura original do arquivo
#   - t: mostra somente valores das variáveis no domínio do tempo (excluí header e coluna do tempo)
#   - f: mostra somente valores das variáveis no domínio da frequencia (excluí header e coluna do tempo)

class PLT():
    def __init__(self, NameFilePLTOrig, onlyData = None):
        
        self.NameFilePLTOrig = NameFilePLTOrig
        self.ContentFilePltOrig = self._ReadFilePLT()
        self.NumVariaveis = self._GetNumVariaveis()
        self.NumLinesHeader = self._GetNumLinesHeader()
        self.Header = self._GetHeader()
        self.HasExcludedHeader = False
        self.HasExcludedTimeColumn = False
        self.TAmost = self._GetTAmost()
    #     self.DataTable = self.GetDataTable()
    #     self.temp = None
        
        
    #     if onlyData == 't':
    #         self.HasExcludedHeader = self.ExcludeHeader()
    #         self.HasExcludedTimeColumn = self.ExcludeTimeColumn()
            
    #     if onlyData == 'f':
    #         self.HasExcludedHeader = self.ExcludeHeader()
           
    #         self.temp = self.GetDataIdx(2)
            
    #         self.HasExcludedTimeColumn = self.ExcludeTimeColumn()
            
            
            


            
    # #Ler dados do arquivo e armazenar como tabela 
    # def GetDataTable(self):
    #     #ver o que ocorre se não excluir o cabeçalho
    #     tabela = []
    #     with open(self.NameFilePLTOrig, 'r') as arquivo:
    #         for linha in arquivo:
    #             tabela.append(linha.strip().split())
    #         print(tabela)
    #     return tabela
    

    # #Obter dados de uma variável (idx é um inteiro que identifica a coluna, usar a info do header como referência)
    # def GetDataIdx(self, idx):
    #     data = []
    #     with open(self.NameFilePLTOrig, 'r') as arquivo:
    #         for linha in arquivo:
    #             valores = linha.strip().split()
    #             data.append(valores[idx])
    #     return data

            
         
        
        

    #Ler arquivo PLT
    def _ReadFilePLT(self):
        with open(self.NameFilePLTOrig, 'r') as file:
            LinesFromFile = file.readlines()
            file.close()
        return LinesFromFile
    
    #Obtem o número de variáveis (linha 0 contém o número de variáveis, incluindo tempo)
    def _GetNumVariaveis(self):
        str1 = self.ContentFilePltOrig[0]
        return int(str1) - 1
    
    #Obtem o número de linhas de cabeçalho (depende do número de variáveis, inclui tempo)
    def _GetNumLinesHeader(self):
        str1 = self.ContentFilePltOrig[0]
        return int(str1)
    

    
    #Obter Cabeçalho
    def _GetHeader(self):
        LineStart = 1
        LineEnd = self.NumLinesHeader + 1
        str1 = self.ContentFilePltOrig[LineStart:LineEnd]
        
        return str1
    
    #Obter o período de amostragem:
    def _GetTAmost(self):
        penult_linha = self.ContentFilePltOrig[-2]
        penult_tempo = float(penult_linha.split()[0])
        
        ult_linha = self.ContentFilePltOrig[-1]
        ult_tempo = float(ult_linha.split()[0])
        
        TAmost = ult_tempo - penult_tempo
        
        return TAmost

    #Excluir o cabeçalho:
    def ExcludeHeader(self):
        #obtem da linha lineStart até o último array
        lineStart = self.NumLinesHeader + 1 
        LinesContentNew = self.ContentFilePltOrig[lineStart:]
        
        #Atualiza ContentFilePltOrig sem header:
        self.ContentFilePltOrig = LinesContentNew   
        
        with open(self.NameFilePLTOrig, 'w') as fileW:
            for line in LinesContentNew:
                fileW.write(line)
        return True
    

        
    #Exclui coluna do tempo. colTime é a coluna que termina o caracter de tempo
    def ExcludeTimeColumn(self, colTime=13):
        tempContentFilePlt = self.ContentFilePltOrig
        #para cada linha, exclui os n primeiros caracteres (coluna de tempo, colTime)
        for i in range(len(tempContentFilePlt)):
            str1 = tempContentFilePlt[i]
            str2 = str1[colTime:]
            tempContentFilePlt[i] = str2
            
        #Atualiza ContentFilePltOrig sem coluna do tempo:
        self.ContentFilePltOrig = tempContentFilePlt  

        with open(self.NameFilePLTOrig, 'w') as fileW:
            for line in tempContentFilePlt:
                fileW.write(line)
        
        return True
    
    #

    #Mudar a extensão do arquivo
    #def RenamePltTo(self, NewExt = 'txt'):
    #    NomeSemExt, Extens = self.NameFilePLTOrig
    #    
    #    return NomeSemExt


class CDU:
    def __init__(self,
                 NameFileCduOrig):
        
        self.NameFileCduOrig = NameFileCduOrig

        #Ler arquivo .cdu -> self.ContentFileStbOrig tem o conteúdo do arquivo original (cada linha do arquivo é um array)
        self.ContentFileCduOrig = ''
        self._ReadFileCdu()
        
        
    def _ReadFileCdu(self):
        #with open(self.NameFileCduOrig, 'r') as file:
        #    self.ContentFileCduOrig = file.readlines()
        #    file.close()
            
        with open(self.NameFileCduOrig, 'rb') as file:  # Ler como bytes
            raw_data = file.read()

        detected_encoding = chardet.detect(raw_data)['encoding']  # Detectar a codificação
        if detected_encoding is None:
            detected_encoding = 'utf-8'  # Fallback para UTF-8 se não for detectado

        with open(self.NameFileCduOrig, 'r', encoding=detected_encoding, errors='replace') as file:
            self.ContentFileCduOrig = file.readlines()  
            
            
    #Criar um novo arquivo Cdu com parâmetros diferentes do arquivo original
    def CreateNewCduNewParam(self, 
                             NameFileCduNew,
                             # Ka_23_RGT_MAQ_B06New = 408,
                             # Ka_20_RGT_MAQ_B01New = 408,
                             # Ka_31_RGT_MAQ_B14New = 25,
                             # Ka_21_RGT_MAQ_B02New = 408,
                             # Ka_22_RGT_MAQ_B03New = 408,
                             # Ka_11_RGT_MAQ_B08New = 300,
                             # Ka_12_RGT_MAQ_B12New = 300,
                             # Ke_23_RGT_MAQ_B06New = 1,
                             # R_40_RGV_MAQ_B01New = 0.05,
                             # Tw_40_RGV_MAQ_B01New = 1.5,
                             # R_41_RGV_MAQ_B02New = 0.05,
                             # Tw_41_RGV_MAQ_B02New = 1.5,
                             # At_42_RGV_MAQ_B06New = 1.2,
                             # D_43_RGV_MAQ_B14New = 1.0,
                             # Aex_11_RGT_MAQ_B08New = 0.0147,
                             # Bex_21_RGT_MAQ_B02New = 1.36,
                             # Kf_20_RGT_MAQ_B01New = 0.1046,
                             # Te_22_RGT_MAQ_B03New = 1.0,
                             # Tf_23_RGT_MAQ_B06New = 3.17,
                             # Tf_11_RGT_MAQ_B08New = 3.0,
                             # Bex_12_RGT_MAQ_B12New = 1.206,
                             # Ta_31_RGT_MAQ_B14New = 0.2):
                             #Kp_1001_AVRG1_New = 200,
                             Ka_1006_AVR_G6_New = 1,
                             Ka_1001_AVR_G1_New = 1,
                             Ka_1004_AVR_G4_New = 1,
                             Ka_1002_AVR_G2_New = 1,
                             Ka_1003_AVR_G3_New = 1,
                             Ka_1008_AVR_G8_New = 1,
                             Ka_1012_AVR_G12_New = 1,
                             Kp_1008_AVR_G8_New = 200,
                             Tr_1009_AVR_G9_New = 0.01,
                             Aex_1001_AVR_G1_New = 0.0000319,
                             Ke_1006_AVR_G6_New = 1,
                             Te_1007_AVR_G7_New = 0.785,
                             K_1102_PSS_G2_New = 20,
                             T1_1112_PSS_G12_New = 0.15,
                             T2_1105_PSS_G5_New = 0.04,
                             TW_1102_PSS_G2_New = 15,
                             T3_1109_PSS_G9_New = 0.09,
                             T4_1107_PSS_G7_New = 0.04):
        
       
        #Lê o arquivo Original direto do arquivo. Forçar a leitura do arquivo original
        self._ReadFileCdu()
        ContentFileCduNew = self.ContentFileCduOrig
        
        #Realiza alteração de Parâmetros:
        
        #Altera o valor de Ka_23_RGT_MAQ_B06 
        # ContentFileCduNew[233-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[233-1], Ka_23_RGT_MAQ_B06New, 15, 32)
        
        # #Altera o valor de Ka_20_RGT_MAQ_B01 
        # ContentFileCduNew[104-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[104-1], Ka_20_RGT_MAQ_B01New, 15, 32)
        
        # #Altera o valor de Ka_31_RGT_MAQ_B14:
        # ContentFileCduNew[276-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[276-1], Ka_31_RGT_MAQ_B14New, 15, 32)
        
        # #Altera o valor de Ka_21_RGT_MAQ_B02:
        # ContentFileCduNew[147-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[147-1], Ka_21_RGT_MAQ_B02New, 15, 32)    
        
        # #Altera o valor de ka_22 RGT_MAQ_B03:
        # ContentFileCduNew[190-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[190-1], Ka_22_RGT_MAQ_B03New, 15, 32)    
        
        # #Altera o valor de Ka_11_RGT_MAQ_B08:
        # ContentFileCduNew[13-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[13-1], Ka_11_RGT_MAQ_B08New, 15, 32)    
         
        # #Altera o valor de Ka_12_RGT_MAQ_B12:
        # ContentFileCduNew[59-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[59-1], Ka_12_RGT_MAQ_B12New, 15, 32)    
        
        # #Altera o valor de Ke_23_RGT_MAQ_B06: 
        # ContentFileCduNew[234-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[234-1], Ke_23_RGT_MAQ_B06New, 15, 32)
        
        # #Altera o valor de R_40_RGV_MAQ_B01: 
        # ContentFileCduNew[327-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[327-1], R_40_RGV_MAQ_B01New, 15, 32)
            
        # #Altera o valor de Tw_40_RGV_MAQ_B01: 
        # ContentFileCduNew[332-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[332-1], Tw_40_RGV_MAQ_B01New, 15, 32)
            
        # #Altera o valor de R_41_RGV_MAQ_B02: 
        # ContentFileCduNew[388-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[388-1], R_41_RGV_MAQ_B02New, 15, 32)
            
        # #Altera o valor de Tw_41_RGV_MAQ_B02: 
        # ContentFileCduNew[393-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[393-1], Tw_41_RGV_MAQ_B02New, 15, 32)
            
        # #Altera o valor de At_42_RGV_MAQ_B06: 
        # ContentFileCduNew[443-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[443-1], At_42_RGV_MAQ_B06New, 15, 32)
            
        # #Altera o valor de D_43_RGV_MAQ_B14: 
        # ContentFileCduNew[505-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[505-1], D_43_RGV_MAQ_B14New, 15, 32)
            
        # #Altera o valor de Aex_11_RGT_MAQ_B08: 
        # ContentFileCduNew[11-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[11-1], Aex_11_RGT_MAQ_B08New, 15, 32)
        
        # #Altera o valor de Bex_21_RGT_MAQ: 
        # ContentFileCduNew[146-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[146-1], Bex_21_RGT_MAQ_B02New, 15, 32)
        
        # #Altera o valor de Kf_20_RGT_MAQ_B01:
        # ContentFileCduNew[106-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[106-1], Kf_20_RGT_MAQ_B01New, 15, 32)    
            
        # #Altera o valor de Te_22_RGT_MAQ_B03New:
        # ContentFileCduNew[195-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[195-1], Te_22_RGT_MAQ_B03New, 15, 32)        
            
        
        # #Altera o valor de Tf_23_RGT_MAQ_B06New:
        # ContentFileCduNew[239-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[239-1], Tf_23_RGT_MAQ_B06New, 15, 32)  
        
        # #Altera o valor de Tf_11_RGT_MAQ_B08New:
        # ContentFileCduNew[20-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[20-1], Tf_11_RGT_MAQ_B08New, 15, 32)   
        
        # #Altera o valor de Bex_12_RGT_MAQ_B12New:
        # ContentFileCduNew[58-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[58-1], Bex_12_RGT_MAQ_B12New, 15, 32)   
            
        # #Altera o valor de Ta_31_RGT_MAQ_B14
        # ContentFileCduNew[283-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[283-1], Ta_31_RGT_MAQ_B14New, 15, 32) 
        
        #Altera o valor de 
        #ContentFileCduNew[21-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[21-1], Kp_1001_AVRG1_New, 15, 32) 
        
        #Altera o valor de Ka_1006_AVR_G6_New
        if Ka_1006_AVR_G6_New != 1:
            ContentFileCduNew[300-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[300-1], Ka_1006_AVR_G6_New, 15, 32) 
        
        #Altera o valor de Ka_1001_AVR_G1_New
        if Ka_1001_AVR_G1_New != 1:
            ContentFileCduNew[25-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[25-1], Ka_1001_AVR_G1_New, 15, 32)
        
        #Altera o valor de Ka_1004_AVR_G4_New
        if Ka_1004_AVR_G4_New != 1:
            ContentFileCduNew[190-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[190-1], Ka_1004_AVR_G4_New, 15, 32)
        
        #Altera o valor de Ka_1002_AVR_G2_New
        if Ka_1002_AVR_G2_New != 1:
            ContentFileCduNew[80-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[80-1], Ka_1002_AVR_G2_New, 15, 32)
        
        #Altera o valor de Ka_1003_AVR_G3_New
        if Ka_1003_AVR_G3_New != 1:
            ContentFileCduNew[135-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[135-1], Ka_1003_AVR_G3_New, 15, 32)
        
        #Altera o valor de Ka_1008_AVR_G8_New
        if Ka_1008_AVR_G8_New != 1:
            ContentFileCduNew[410-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[410-1], Ka_1008_AVR_G8_New, 15, 32)
        
        #Altera o valor de Ka_1012_AVR_G12_New
        if Ka_1012_AVR_G12_New != 1:
            ContentFileCduNew[597-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[597-1], Ka_1012_AVR_G12_New, 15, 32)
        
        #Altera o valor de Kp_1008_AVR_G8_New
        if Kp_1008_AVR_G8_New != 200:
            ContentFileCduNew[406-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[406-1], Kp_1008_AVR_G8_New, 15, 32)
            
        #Altera o valor de Tr_1009_AVR_G9_New
        if Tr_1009_AVR_G9_New != 0.01:
            ContentFileCduNew[458-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[458-1], Tr_1009_AVR_G9_New, 15, 32)
            
            
        
        #Altera o valor de Aex_1001_AVR_G1_New
        if Aex_1001_AVR_G1_New != 0.0000319:
            ContentFileCduNew[28-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[28-1], Aex_1001_AVR_G1_New, 15, 32)
        

        #Altera o valor de Ke_1006_AVR_G6_New
        if Ke_1006_AVR_G6_New != 1:
            ContentFileCduNew[304-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[304-1], Ke_1006_AVR_G6_New, 15, 32)
            
        #Altera o valor de Te_1007_AVR_G7_New
        if Te_1007_AVR_G7_New != 1:
            ContentFileCduNew[360-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[360-1], Te_1007_AVR_G7_New, 15, 32)
                
        #Altera o valor de K_1102_PSS_G2_New
        if K_1102_PSS_G2_New != 20:
            ContentFileCduNew[671-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[671-1], K_1102_PSS_G2_New, 15, 32)
            
        #Altera o valor de T1_1112_PSS_G12_New
        if T1_1112_PSS_G12_New != 0.15:
            ContentFileCduNew[930-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[930-1], T1_1112_PSS_G12_New, 15, 32)
            
        #Altera o valor de T2_1105_PSS_G5_New
        if T2_1105_PSS_G5_New != 0.04:
            ContentFileCduNew[752-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[752-1], T2_1105_PSS_G5_New, 15, 32)    
            
            
         #Altera o valor de TW_1102_PSS_G2_New
        if TW_1102_PSS_G2_New != 15:
            ContentFileCduNew[672-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[672-1], TW_1102_PSS_G2_New, 15, 32)
             
         #Altera o valor de T3_1109_PSS_G9_New
        if T3_1109_PSS_G9_New != 0.09:
             ContentFileCduNew[857-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[857-1], T3_1109_PSS_G9_New, 15, 32)    
             
        #Altera o valor de T4_1107_PSS_G7_New
        if T4_1107_PSS_G7_New != 0.04:
            ContentFileCduNew[806-1] = self.WriteValueInColumnANAT(self.ContentFileCduOrig[806-1], T4_1107_PSS_G7_New, 15, 32)     
        
        #Escreve o conteúdo em novo arquivo
        with open(NameFileCduNew, 'w') as FileCduNew:
            fileCduNew = open(NameFileCduNew, 'w')
            fileCduNew.writelines(ContentFileCduNew)
            print('Arquivo ' + str(NameFileCduNew) + ' criado.')                

        return 
    
    #altera o valor de um campo (coluna) 
    #posColIni e posColFim são índices de ínicio e fim de coluna de acordo com o manual do ANATEM
    #lineANAT é uma string de uma linha do arquivo .stb
    def WriteValueInColumnANAT(self, strlineANAT, valor, posColIni, posColFim):
        posColIni = posColIni - 1 #posColFim não tem alteração de índice
        
        #caso seja um número:
        if isinstance(valor, (int, float)):
            #converte em string com 20 números decimais (força ponto decimal)
            strValorDec = "{:.20f}".format(valor)
            #capturar somente os n caracteres para caber na coluna
            strValorComNCaracteres = strValorDec[:(posColFim - posColIni)]
        if isinstance(valor, str): 
            strValorComNCaracteres = valor
            
        #substitui a string na linha do arquivo .stb na posição da coluna
        return strlineANAT[:posColIni] + strValorComNCaracteres + strlineANAT[posColFim:] 
    
    
class BLT:
    def __init__(self,
                 NameFileBltOrig):
        
        self.NameFileBltOrig = NameFileBltOrig

        #Ler arquivo .blt -> self.ContentFileStbOrig tem o conteúdo do arquivo original (cada linha do arquivo é um array)
        self.ContentFileBltOrig = ''
        self._ReadFileBlt()
        
        
    def _ReadFileBlt(self):
        #with open(self.NameFileBltOrig, 'r') as file:
        #    self.ContentFileBltOrig = file.readlines()
        #    file.close()
        with open(self.NameFileBltOrig, 'rb') as file:  # Ler como bytes
            raw_data = file.read()

        detected_encoding = chardet.detect(raw_data)['encoding']  # Detectar a codificação
        if detected_encoding is None:
            detected_encoding = 'utf-8'  # Fallback para UTF-8 se não for detectado

        with open(self.NameFileBltOrig, 'r', encoding=detected_encoding, errors='replace') as file:
            self.ContentFileBltOrig = file.readlines()
            
            
            
    #Criar um novo arquivo blt com parâmetros diferentes do arquivo original
    def CreateNewBltNewParam(self, 
                             NameFileBltNew,
                             #H_Modelo202=2.474,
                             #H_Modelo201=3.588,
                             #Lq_Modelo201 = 59.9,
                             #T2d_Modelo202 = 0.048,
                             H_blt_0006=34.8,
                             H_blt_0010=31.0,
                             Ld_blt_0012=10.1,
                             Llq_blt_0004=5.86,
                             Llq_blt_0009=7.67,
                             Tld_blt_0011=4.1,
                             Tlld_blt_0008=0.05,
                             Ll_blt_0004=2.95,
                             Tllq_blt_0009=0.035):
        
       
        #Lê o arquivo Original direto do arquivo. Forçar a leitura do arquivo original
        self._ReadFileBlt()
        ContentFileBltNew = self.ContentFileBltOrig
        
        #Realiza alteração de Parâmetros:
            
        # #Altera o valor de H_Modelo201 
        # ContentFileBltNew[19-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[19-1], H_Modelo201, 13, 17)
        
        # #Altera o valor de H_Modelo202 
        # ContentFileBltNew[25-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[25-1], H_Modelo202, 13, 17)
        
        # #Altera o valor de Lq_Modelo201 
        # ContentFileBltNew[17-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[17-1], Lq_Modelo201, 18, 22)
        
        # #Altera o valor de T2d_Modelo202
        # ContentFileBltNew[23-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[23-1], T2d_Modelo202, 53, 57)
        
        # #Altera o valor de H
        # ContentFileBltNew[19-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[19-1], H_Modelo201, 13, 17)
        
        # #Altera o valor de H_blt_0006
        if H_blt_0006 != 34.8:
            ContentFileBltNew[50-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[50-1], H_blt_0006, 13, 17)
            
        # #Altera o valor de H_blt_0010
        if H_blt_0010 != 31.0:
            ContentFileBltNew[74-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[74-1], H_blt_0010, 13, 17)
            
        # #Altera o valor de Ld_blt_0012
        if Ld_blt_0012 != 10.1:
            ContentFileBltNew[83-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[83-1], Ld_blt_0012, 13, 17)
            
        # #Altera o valor de Llq_blt_0004
        #if Llq_blt_0004 != 5.86:
        #    ContentFileBltNew[35-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[35-1], Llq_blt_0004, 28, 33)
            
            
            
        # #Altera o valor de Tld_blt_0011
        if Tld_blt_0011 != 4.1:
            ContentFileBltNew[77-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[77-1], Tld_blt_0011, 43, 47)
            
        # #Altera o valor de Tlld_blt_0008
        if Tlld_blt_0008 != 0.05:
            ContentFileBltNew[59-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[59-1], Tlld_blt_0008, 53, 57)
            
        
        # #Altera o valor de Ll_blt_0004
        if Ll_blt_0004 != 2.95:
            ContentFileBltNew[35-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[35-1], Ll_blt_0004, 39, 42)
            
            
        # #Altera o valor de Tllq_blt_0009
        if Tllq_blt_0009 != 0.035:
            ContentFileBltNew[65-1] = self.WriteValueInColumnANAT(self.ContentFileBltOrig[65-1], Tllq_blt_0009, 58, 62)
                
        
        #Escreve o conteúdo em novo arquivo
        with open(NameFileBltNew, 'w') as FileBltNew:
            fileBltNew = open(NameFileBltNew, 'w')
            fileBltNew.writelines(ContentFileBltNew)
            print('Arquivo ' + str(NameFileBltNew) + ' criado.')                

        return 
    
    #altera o valor de um campo (coluna) 
    #posColIni e posColFim são índices de ínicio e fim de coluna de acordo com o manual do ANATEM
    #lineANAT é uma string de uma linha do arquivo .blt
    def WriteValueInColumnANAT(self, strlineANAT, valor, posColIni, posColFim):
        posColIni = posColIni - 1 #posColFim não tem alteração de índice
        
        #caso seja um número:
        if isinstance(valor, (int, float)):
            #converte em string com 20 números decimais (força ponto decimal)
            strValorDec = "{:.20f}".format(valor)
            #capturar somente os n caracteres para caber na coluna
            strValorComNCaracteres = strValorDec[:(posColFim - posColIni)]
        if isinstance(valor, str): 
            strValorComNCaracteres = valor
            
        #substitui a string na linha do arquivo .stb na posição da coluna
        return strlineANAT[:posColIni] + strValorComNCaracteres + strlineANAT[posColFim:] 
              

