import numpy as np
import matplotlib.pyplot as plt

# LE CONTENU DE CETTE CELLLULE EST A SOUMETTRE SUR INGINIOUS
def window(n,n0,n1,A):
    #fonction mauvaise
    """
    input:
    n = un numpy array contenant les indexes qu'on veut avoir en window
    n0 = le début de la fenêtre
    n1 = la fin de la fenêtre
    A = l'indice qui multiplie la formule
    result:
    le résultat de la fonction window
    """
    result = np.zeros(n.size)
    begin = n[0]
    end = n[-1]
    
    arrn0 = np.arange(begin-n0, end-n0)
    arrn1 = np.arange(begin-n1, end-n1)
    
    heavn0 = np.zeros(arrn0.shape) 
    heavn0[arrn0 >= 0] = 1.        # modifie "result" aux indices où "n>=0" vaut "True"
    
    heavn1 = np.zeros(arrn1.shape) 
    heavn1[arrn1 >= 0] = 1.        # modifie "result" aux indices où "n>=0" vaut "True"
    
    
    for index in range(begin, end+1):
        result[index] = A * (heavn0[index] - heavn1[index])
    
    # A COMPLETER

    return result

def plotWindow(n,w,name):
    """
    input:
    n = les absisces  --> ici les points où on effectue la fonction fenêtre
    w = les ordonnées --> ici notre le résultat de la fonction window
    """
    
    # Création de la figure, de taille fixe.
    fig = plt.figure(figsize=(6,3))
    ax = fig.add_subplot(111)
    
    # A MODIFIER : créez ici votre plot
    markerline, stemlines, baseline = plt.stem(n,w)
    plt.xlabel("$n$ [-]")
    plt.ylabel("$w[n]$ [-]")
    plt.title("Fenêtre discret w[n]")
    
    plt.xticks(n[::5]) #met les valeurs tous les 5 unités
    plt.yticks([0,np.max(w)]) #affiche 0 et la valeur max en ordonnée
    
    baseline.set_color('k')
    
    temp = w[::-1] #renverse le numpy array window pour trouver n1
    
    n0 = ax.plot(w[np.argmax(w>=np.max(w))] - 1,0, 'x', markersize=10, color="red", label="n0") #mets une croix au n0
    n1 = ax.plot(int(len(temp)-np.argmax(w>=np.max(temp)))+n[0],0, 'x', markersize=10, color="red", label="n1") #mets une croix au n1
    
    ax.legend()
    #plt.plot([w.get(np.max(w))])
    # Sauvegarde de la figure avec le bon nom.
    # Le second argument rétrécit les marges, par défaut relativement larges.
    plt.savefig(name + '.png', bbox_inches='tight', dpi=200)
    
    # De-commentez ceci pour tester "localement", ne pas inclure cette ligne sur Inginious !

    return

