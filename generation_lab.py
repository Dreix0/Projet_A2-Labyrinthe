import random

# Création du labyrinthe
lab = []
ligne = [] 
taille_lab = random.randint(3,10)
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