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

lat_user = 45, 30, 31.9968
long_user = 73, 33, 42.0048
info_user = lat_user, long_user
#print(pole_user(info_user))

def dms_to_dd(dms):
    degres, minutes, secondes = dms
    return degres + minutes/60 + secondes/3600

def distance_2_point(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    #math.sqrt()

def distance_pole_nord(position):
    POLENORD_LAT = 86.494
    POLENORD_LONG = 162.867
    POLE_NORD = POLENORD_LAT, POLENORD_LONG

    lat, long = position
    lat_dd = dms_to_dd(lat)
    long_dd = dms_to_dd(long)
    position_dd = lat_dd, long_dd

    return distance_2_point(position_dd, POLE_NORD)

longitude = 45, 30, 31.9968
latitude = 73, 33, 42.0048
position = longitude, latitude

dist = distance_pole_nord(position)
print(dist)