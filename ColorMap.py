import numpy as np
import matplotlib.pyplot as plt
import os
import sys 
import cv2
from os import walk


# Le as imagens presentes no diretorio raiz, e carrega a escolhida.
# Após isso seleciona a paleta de cor que será utilizada.

def select_img():
    print("===========================================")
    print("Digite o número correspondente a imagem que deseja carregar:\n")
    filenames = next(walk(os.path.dirname(__file__) + "/"), (None, None, []))[2]
    files = [ file for file in filenames if file.endswith((".jpg", ".png", ".tiff")) ]
    
    if len(files) == 0:
        print("Não existe arquivos de imagem no diretório raiz.")
        sys.exit()
    
    for i in range(0, len(files)):
        print('[{}] {}'.format(i, files[i]))
    index = input()
    
    while not index.isdigit() or int(index) >= len(files) or int(index) < 0:
        print("\nEsta opção não existe, digite novamente.")
        index = input()
    
    imagem = cv2.imread(os.path.dirname(__file__) + "/" + files[int(index)], cv2.IMREAD_GRAYSCALE)
    
    print("\nQual paletas de cores deseja utilizar:")
    paleta = input()
    
    while paleta not in plt.colormaps():
        print("\nEsta paleta não existe.\n"
              "Caso queira visualizar as paletas disponíveis digite 1, \n"
              "caso contrário digite o nome da paleta.")
        paleta = input()
        
        if (paleta == "1"):
            print("Paletas disponiveis: \n")
            print(plt.colormaps())
            print("\nQual paletas de cores deseaja utilizar:")
            paleta = input()
    
    
    return imagem, paleta, files[int(index)]
    

# Aplica a paleta de cor na imagem

def set_palette (original_img, paleta):
    
    paleta = paleta(np.arange(0, 256)) * 255
    
    tr = paleta[::, 2]
    tg = paleta[::, 1]
    tb = paleta[::, 0]
    
    canais = [np.uint8(tr[original_img]), np.uint8(tg[original_img]), 
              np.uint8(tb[original_img])]
    
    img_colorized = np.dstack(canais)
    
    return img_colorized
    


def main():
    imagem, palet, nome_arq = select_img()
    paleta = plt.get_cmap(palet)
    img_colorized = set_palette(imagem, paleta)
    print("\nFeche as janelas para continuar...")
    cv2.imshow('Imagem cinza', imagem)
    cv2.imshow('Imagem colorizada', img_colorized)
    cv2.waitKey(0)
    print("\nGostaria de salvar a imagem colorizada?\n[1] Sim\n[2] Não")
    op = input()
    while op != '1' or op != '2':
        if op == '2' or op == '1': break
        print("\nEsta opção não existe, tente novamente.")
        op = input()
    
    #salvando a imagem
    
    if op == '1':
        cv2.imwrite(os.path.dirname(__file__) + "/" + palet +"_"+ nome_arq, img_colorized)
        print("\nSalvo em:\n" + os.path.dirname(__file__))
    
    print("\nPrograma encerrado.")
if __name__ == "__main__":
    main()
