#Partie 1:

#Vous travaillez sur un système de géolocation 
# s'intitulant à la recherche du pôle Nord 
# utilisant des coordonnées sous la forme degrés minutes secondes (DMS).

#Pour faciliter l'utilisation du système, 
# on vous demande de créer un court programme permettant de convertir ces données sous la forme de degrés décimaux (DD).

#De plus, considérant que le but de l'application est d'indiquer la distance des usagers du pôle Nord magnétique
#  en plus d'indiquer leur position, on vous demande d'ajouter à votre programme une fonction permettant de calculer cette distance.

#Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois terminé.

#decimal degrees = degrees + (minutes / 60) + (seconds/3600)

def dms_to_dd(dms):
    degrees, minutes, secondes = dms
    dd = degrees + (minutes / 60) + (secondes / 3600)
    return dd

def distance_2_points(x1, y1, x2, y2):
    b = x2 - x1
    c = y2 - y1
    distance = (b ** 2 + c**2) ** 0.5
    return distance

def pole_user(position):
    LAT_POLE_N = 86.494
    LONG_POLE_N = 162.867

    lat_user, long_user = position
    lat_user = dms_to_dd(lat_user)
    long_user = dms_to_dd(long_user)

    return distance_2_points(LAT_POLE_N, LONG_POLE_N, lat_user, long_user)

lat_user = 11, 14, 22.3
long_user = 87, 46, 25.6
info_user = lat_user, long_user
print(pole_user(info_user))

#En partant de l'exercice du système de géolocation, 
# modifiez votre code pour que les positions en DMS incluent la direction cardinale(N, S, E, W ou O) 
# et retourne une position en DD pouvant être négative. 
# Modifiez ensuite votre code pour permettre à un utilisateur de manuellement rentrer sa position.

def dms_to_dd(dms):
    degrees, minutes, secondes, position = dms
    dd = degrees + (minutes / 60) + (secondes / 3600)
    if position == 'S' or position == 'W':
        dd = dd * -1
    return dd

def distance_2_points(x1, y1, x2, y2):
    b = x2 - x1
    c = y2 - y1
    distance = (b ** 2 + c**2) ** 0.5
    return distance

def pole_user():
    LAT_POLE_N = 86.494
    LONG_POLE_N = -162.867

    lat_degrees = float(input('Entrer vos degrees de latitude (11): '))
    lat_minutes = float(input('Entrer vos minutes de latitude (14): '))
    lat_secondes = float(input('Entrer vos secondes de latitude (22.3): '))
    lat_ns = str(input('Entrer votre indication nord/sud (N/S): '))
    lat_user = lat_degrees, lat_minutes, lat_secondes, lat_ns
    
    long_degrees = float(input('Entrer vos degrees de longitude (87): '))
    long_minutes = float(input('Entrer vos minutes de longitude (46): '))
    long_secondes = float(input('Entrer vos secondes de longitude (25.6): '))
    long_ew = str(input('Entrer votre indication est/west (E/W): '))
    long_user = long_degrees, long_minutes, long_secondes, long_ew
    
    lat_user = dms_to_dd(lat_user)
    long_user = dms_to_dd(long_user)

    return distance_2_points(LAT_POLE_N, LONG_POLE_N, lat_user, long_user), lat_user, long_user


lat = 11, 14, 22.3, 'S' 
long = 87, 46, 25.6, 'W'
print(pole_user())
#lat_dd = -11.239518
#long_dd = -87.773767