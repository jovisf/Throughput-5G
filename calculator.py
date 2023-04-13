import math
symboylspdata = [0.2344, 0.377, 0.6016, 0.877, 1.1758, 1.4766, 1.6953, 1.9141, 2.1602, 2.4063, 2.5703, 2.7305, 3.0293, 3.223, 3.6094, 3.9023, 4.2129, 4.5234, 4.8164, 5.1152, 5.332, 5.5547, 5.8906, 6.2266, 6.5703, 6.9141, 7.1602, 7.4063 ]
symbolsfordata = 12
bandalarga = [20, 50, 100, 400]
camadasMIMO = [1, 2, 4]
totaldataresourceelements = 132 #subcarries * symbolsfordata
datacarriedover1slot = []
slotsavaible = 2000
downlink3 = 1500
downlink4 = 1600
throughput5g = 0
resourceBlocks = []

# digamos que a banda seja de 100Mhz, entao 100000 Khz / 360 Khz = 277 - 4 Rb usados como guarda
def convertebanda(banda):
    return (((banda*1000)//360) - 4)

def revertebanda(resourceBlock):
    return math.ceil(((resourceBlock + 4) * 360) / 1000)


for i in range(len(bandalarga)):
    resourceBlocks.append(convertebanda(bandalarga[i]))


for i in symboylspdata:
    datacarriedover1slot.append(math.floor(totaldataresourceelements * i))


#para razão da divisão dos slots entre DL e UL =  3.1
for MiMo in camadasMIMO:
    for data in range(len(datacarriedover1slot)):
        for i in resourceBlocks:
            throughput5g = ((i*datacarriedover1slot[data]*downlink3*MiMo)//1024)//1024
            print(f"Ordem de modulação:{data}, largura de banda:{revertebanda(i)}, Número de camadas Mimo: {MiMo} e razão da divisão dos slots entre DL e UL: 3:1 a vazão foi de {throughput5g} Mbps")



#para razão da divisão dos slots entre DL e UL =  4.1
for MiMo in camadasMIMO:
    for data in range(len(datacarriedover1slot)):
        for i in resourceBlocks:
            throughput5g = ((i*datacarriedover1slot[data]*downlink4*MiMo)//1024)//1024
            print(f"Ordem de modulação:{data}, largura de banda:{revertebanda(i)}, Número de camadas Mimo: {MiMo} e razão da divisão dos slots entre DL e UL: 4:1 a vazão foi de {throughput5g} Mbps")

