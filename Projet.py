#Importation des bibliothèques
import turtle
import random

#Fonctions
def Get_start_point(chemin):
    '''Cette fonction permet de trouver les coordonnées du point de départ
    à partir de la liste chemin.
    '''
    start_point = ['']
    for ligne in range(len(chemin)):
        if start_point[0] != '':
            break
        for collone in range(len(chemin[ligne])):
            if chemin[ligne][collone] == '1':
                start_point = [ligne,collone]
                break
    return start_point

def Mouv_turtle(chemin, point, listPath, origine):
    '''Cette fonction permet de déplacer le curseur.
    Elle permet de vérifier si des cases alentours sont libres, et si c'est le cas d'y aller.
    Si aucune case proche n'est libre elle permet de faire demi-tour, et de tracer un trait rouge.
    Elle permet aussi de modifier la liste chemin et de remplir la liste listPath.
    '''
    points_proches = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(len(points_proches)):
        if chemin[point[0]+points_proches[i][0]][point[1]+points_proches[i][1]] == '1' \
        or chemin[point[0]+points_proches[i][0]][point[1]+points_proches[i][1]] == '2' \
        or chemin[point[0]+points_proches[i][0]][point[1]+points_proches[i][1]] == '3':
            listPath.append(point)
            chemin[point[0]][point[1]] = '-1'      
            point = [point[0]+points_proches[i][0],point[1]+points_proches[i][1]]
            turtle.pencolor('black')
            turtle.goto(origine[1]+20*point[1],origine[0]+20*point[0])
            return chemin, point, listPath
    for i in range(len(points_proches)):
        if chemin[point[0]+points_proches[i][0]][point[1]+points_proches[i][1]] == '-1': 
            del listPath[-1]
            chemin[point[0]][point[1]] = '-2'
            point = [point[0]+points_proches[i][0],point[1]+points_proches[i][1]]
            turtle.pencolor('red')
            turtle.goto(origine[1]+20*point[1],origine[0]+20*point[0])
            return chemin, point, listPath     

def creation_case(point, origine, color):
    turtle.pencolor(color)
    turtle.pensize(20)
    turtle.speed('fastest')
    turtle.up()
    turtle.goto(origine[1]+20*point[1], origine[0]+20*point[0])
    turtle.down()
    turtle.forward(1)
    turtle.left(90)
    turtle.backward(1)
    turtle.left(90)
    turtle.forward(1)
    turtle.left(90)
    turtle.backward(1)
    turtle.left(90)
    turtle.up()
    return

def creation_map(point, origine):
    if chemin[point[0]][point[1]] == '1':
        creation_case(point, origine, 'red')
    elif chemin[point[0]][point[1]] == '3':
        creation_case(point, origine, 'green')
    elif chemin[point[0]][point[1]] == '0':
        creation_case(point, origine, 'black')
    return

def generation_lab():
    # Création du labyrinthe
    lab = []
    ligne = [] 
    taille_lab = random.randint(3,15)
    ligne_externe = []
    
    for i in range(3*taille_lab):
        ligne.append('0')
    for j in range(3*taille_lab):
        lab.append(ligne)
        
    # Positionnement du point de départ et d'arrivé
    c_start = 3*random.randint(0,taille_lab-1)+1
    l_start = 3*random.randint(0,taille_lab-1)+1
    c_end = 3*random.randint(0,taille_lab-1)+1
    l_end = 3*random.randint(0,taille_lab-1)+1
    while c_end == c_start and l_end == l_start:
        c_start = 3*random.randint(0,taille_lab-1)+1
        l_start = 3*random.randint(0,taille_lab-1)+1
        c_end = 3*random.randint(0,taille_lab-1)+1
        l_end = 3*random.randint(0,taille_lab-1)+1
    
    
    lab[l_start]=lab[l_start][:c_start]+['1']+lab[l_start][c_start+1:]
    lab[l_end]=lab[l_end][:c_end]+['4']+lab[l_end][c_end+1:]
    
    
    # Positionnement de nouveaux points
    points_proches=[[[0,1],[0,2],[0,3]],[[1,0],[2,0],[3,0]],[[0,-1],[0,-2],[0,-3]],[[-1,0],[-2,0],[-3,0]]]
    pts_utilises = [[l_start,c_start]]
    
    rdm_pts_utilises = pts_utilises[random.randint(0,len(pts_utilises)-1)]
    rdm_points_proches = points_proches[random.randint(0,len(points_proches)-1)]
    
    while len(pts_utilises) < taille_lab**2:
        if rdm_points_proches[2][0]+rdm_pts_utilises[0] > len(lab)-1 or rdm_points_proches[2][1]+rdm_pts_utilises[1] > len(lab)-1 or rdm_points_proches[2][0]+rdm_pts_utilises[0] < 0 or rdm_points_proches[2][1]+rdm_pts_utilises[1] < 0:
            rdm_points_proches = points_proches[random.randint(0,len(points_proches)-1)]
            rdm_pts_utilises = pts_utilises[random.randint(0,len(pts_utilises)-1)]
        else:
            if lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][rdm_points_proches[2][1]+rdm_pts_utilises[1]] == '0':
                lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][:rdm_points_proches[2][1]+rdm_pts_utilises[1]]+['2']+lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][rdm_points_proches[2][1]+rdm_pts_utilises[1]+1:]
                lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]][:rdm_points_proches[1][1]+rdm_pts_utilises[1]]+['2']+lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]][rdm_points_proches[1][1]+rdm_pts_utilises[1]+1:]
                lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]][:rdm_points_proches[0][1]+rdm_pts_utilises[1]]+['2']+lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]][rdm_points_proches[0][1]+rdm_pts_utilises[1]+1:]
                pts_utilises.append([(rdm_points_proches[2][0]+rdm_pts_utilises[0]),(rdm_points_proches[2][1]+rdm_pts_utilises[1])])
                rdm_points_proches = points_proches[random.randint(0,len(points_proches)-1)]
                rdm_pts_utilises = pts_utilises[random.randint(0,len(pts_utilises)-1)]
            elif lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][rdm_points_proches[2][1]+rdm_pts_utilises[1]] == '4':
                lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][:rdm_points_proches[2][1]+rdm_pts_utilises[1]]+['3']+lab[rdm_points_proches[2][0]+rdm_pts_utilises[0]][rdm_points_proches[2][1]+rdm_pts_utilises[1]+1:]
                lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]][:rdm_points_proches[1][1]+rdm_pts_utilises[1]]+['2']+lab[rdm_points_proches[1][0]+rdm_pts_utilises[0]][rdm_points_proches[1][1]+rdm_pts_utilises[1]+1:]
                lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]] = lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]][:rdm_points_proches[0][1]+rdm_pts_utilises[1]]+['2']+lab[rdm_points_proches[0][0]+rdm_pts_utilises[0]][rdm_points_proches[0][1]+rdm_pts_utilises[1]+1:]
                pts_utilises.append([(rdm_points_proches[2][0]+rdm_pts_utilises[0]),(rdm_points_proches[2][1]+rdm_pts_utilises[1])])
                rdm_points_proches = points_proches[random.randint(0,len(points_proches)-1)]
                rdm_pts_utilises = pts_utilises[random.randint(0,len(pts_utilises)-1)]
            else:
                rdm_points_proches = points_proches[random.randint(0,len(points_proches)-1)]
                rdm_pts_utilises = pts_utilises[random.randint(0,len(pts_utilises)-1)]
    
    #Suppression des lignes et collones doubles
    l_supp = 2
    c_supp = 2
        
    while l_supp < 2*taille_lab:
        del lab[l_supp]
        l_supp +=2
        
    while c_supp < 2*taille_lab:
        for i in range(len(lab)-2):
            del lab[i+1][c_supp]
        c_supp += 2
    i=0   
    while i < len(lab):   
        ligne_externe.append('0')
        i += 1
        
    lab[0]=ligne_externe
    lab[len(lab)-1] = ligne_externe
    return lab

#Initialisation des variables
listPath = []

#Programme principale
chemin = generation_lab()
point = Get_start_point(chemin)


''' Création du graphique '''
origine = [-(20*len(chemin))/2 + 10, -(20*len(chemin[0]))/2 + 10]
turtle.setup(20*(len(chemin[0])+2), 20*(len(chemin)+2)) 

turtle.title(f'Réalisation du labyrinthe') 
for i in range(len(chemin)):
    for j in range(len(chemin)):
        creation_map([i,j], origine) 
turtle.up()
turtle.goto(origine[1]+20*point[1], origine[0]+20*point[0])
turtle.down()
turtle.pensize(1)
turtle.speed('slow')

while chemin[point[0]][point[1]] != '3':
    chemin, point, listPath = Mouv_turtle(chemin, point, listPath, origine)


turtle.exitonclick()