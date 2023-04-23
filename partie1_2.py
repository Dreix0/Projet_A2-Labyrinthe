#Importation des bibliothèques
import turtle

#Fonctions
def Get_chemin():
    '''Cette fonction permet de demander à l'utilisateur quel labyrinthe il veut lancer,
    puis d'ouvrir et prendre les données du fichier texte correspondant.
    Les informations sont placés dans une liste de liste appelée chemin.
    '''
    chemin = []
    num_lab =input("Quel est le numero du labyrinthes que vous souhaitez executer ?")
    f = open(f'Data/Maze{num_lab}.txt', 'r')
    while True:
        ligne = f.readline()
        lst_ligne = list(ligne.strip())
        if(ligne == ''):
            break
        chemin.append(lst_ligne[:])
    return chemin, num_lab

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


#Initialisation des variables
listPath = []

#Programme principale
chemin, num_lab = Get_chemin()
point = Get_start_point(chemin)


''' Creéation du graphique '''
origine = [-(20*len(chemin))/2 + 10, -(20*len(chemin[0]))/2 + 10]
turtle.setup(20*(len(chemin[0])+2), 20*(len(chemin)+2)) 
turtle.title(f'Réalisation du labyrinthe {num_lab}') 

for i in range(len(chemin)):
    for j in range(len(chemin)):
        creation_map([i,j], origine) 
turtle.up()
turtle.goto(origine[1]+20*point[1], origine[0]+20*point[0])
turtle.down()
turtle.pensize(1)
turtle.speed('normal')


while chemin[point[0]][point[1]] != '3':
    chemin, point, listPath = Mouv_turtle(chemin, point, listPath, origine)

turtle.exitonclick()