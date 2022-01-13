# /usr/bin/python3
#createurs Peter Stopschinski 2021-05-20, pstopschinski@free.fr
#d'après les sources de uncledens , http://uncledens.chez-alice.fr/

from time import localtime, mktime

#variables à l'entrée :
fuser=input("vous avez un fichier USER.BIN dans votre répertoire ? - o=oui, n=non :\n")
#fichier=input("Nom du fichier à charger sans .Extension :\n")
fichier='ACT_0003'
out=input("Nom du fichier .tcx à créer sans .Extension :\n")

#données de base par défaut
date_naissance='1952-01-29'
sex='homme'
age=69
taille=167
poids=62
bpm_min=68
bpm_max=159

user=["sex","age","taille","poids","bpm-min","bpm-max","nr","nr","nr","nr",
      "nr","nr","nr","nr","nr","nr","nr","nr","nr","nr"]  #nr=nonrenseigné ou inconnu

champomh=["distancem0","distancem1","distancem2","distancem3","times0","times1","inconnu","inconnu","inconnu","inconnu",
          "kcal0","kcal1","heartbpm","inconnu","year","month","day","hour","minute","inconnu",
          "inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu",
          "inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu",
          "inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu",
          "inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu","inconnu"]

champ=["lat0","lat1","lat2","lat3","lon0","lon1","lon2","lon3","dist0","dist1",
       "dist2","dist3","tps0","tps1","inconnu","alt0","alt1","inconnu","inconnu","F1",
       "lat0","lat1","lat2","lat3","lon0","lon1","lon2","lon3","dist0","dist1",
       "dist2","dist3","tps0","tps1","inconnu","alt0","alt1","inconnu","inconnu","F1",
       "tps0","tps1","vit0","vit1","KCal0","KCal1","coeur","inconnu","inconnu","moitieF2",
       "tps0","tps1","vit0","vit1","KCal0","KCal1","coeur","inconnu","inconnu","F2"]
#-----------------------------------------------------
#section fonctions
def get_age(naissance,fix):
    naissance=naissance.split('-')
    fix=fix.split('-')
    nupnaiss=(int(naissance[0]),int(naissance[1]),int(naissance[2]),0,0,0,0,0,0,)
    nupfix=(int(fix[0]),int(fix[1]),int(fix[2]),0,0,0,0,0,0,)
    agesec=mktime(nupfix)-mktime(nupnaiss)
    agenup=localtime(agesec)
    mage = agenup[0]-1970
    return mage

#-------------------------------------------------------------
#section main

#début de production des arguments de base

# définition du jour et du début de l'exercice
cpt=0
with open(fichier+'.OMH', 'rb') as file: #OMD et OMH 1, 2, 5, 40
    for c in file: #boucle ligne
        for i in c:
            octet=str(i)
            col=cpt%60

            champomh[col]=int(octet)
            cpt+=1
            
#calcul de date et heure du début
dateheure=str(int(champomh[14])+2000)+"-"

if champomh[15]<10:
    dateheure+="0"+str(champomh[15])
else:
    dateheure+=str(champomh[15])        
dateheure+="-"
if champomh[16]<10:
    dateheure+="0"+str(champomh[16])
else:
    dateheure+=str(champomh[16])

datefix=dateheure
dateheure+="T"

if champomh[17]<10:
    dateheure+="0"+str(champomh[17]) 
else:
    dateheure+=str(champomh[17]) 
dateheure+=":"
if champomh[18]<10:
    dateheure+="0"+str(champomh[18])
else:
    dateheure+=str(champomh[18]) 
dateheure+=":00+02:00"
champomhsec=0

#-------------------------------------------------------------
#Arguments de l'utilisateur
#au cas où fuser=='n' :
if fuser=='n':
    sexi=input("Votre sexe : La valeur par défaut est "+str(sex)+". Si vous êtes une femme tapez 'femme' :\n")
    if sexi=='femme':
        sex='femme'
    agi=input("Votre âge : la valeur par défaut est "+str(age)+". Si ce n'est pas exact tapez votre date de naissance en 'aaaa-mm-jj' :\n")
    age=agi
    if len(agi)>0:
        date_naissance=agi
        age=get_age(date_naissance, datefix)
    tailli=input("if votre taille n'est pas "+str(taille)+"cm tapez votre taille en cm :\n")
    if int(tailli)>0:
        taille=int(tailli)
    poidsi=input("if votre poids n'est pas "+str(poids)+"kg tapez votre poids en kg :\n")
    if int(poidsi)>0:
        poids=int(poidsi)
    bpm_mini=input("if votre bpm minimal (de repos) n'est pas "+str(bpm_min)+" par minute tapez votre bpm minimal par minute :\n")
    if int(bpm_mini)>0:
        bpm_min=int(bpm_mini)
    if sex=='femme':
        bpm_max=int(226-0.7*age)
    else:
        bpm_max=int(220-0.7*age)
                 
#chercher données utilisateur à partir de USER.BIN
else:
    cpt=0
    with open('USER.BIN', 'rb') as file: #OMD et OMH 1, 2, 5, 40
        for c in file: #boucle ligne
            for i in c:
                octet=str(i)
                col=cpt%20

                user[col]=int(octet)
                cpt+=1
    if int(user[0])==0:
        sex='homme'
    else:
        sex='femme'
    age=int(user[1])
    taille=int(user[2])
    poids=int(user[3])
    bpm_min=int(user[4])
    bpm_max=int(user[5])

#fin des arguments de base
#----------------------------------------------------------
#traitement du fichier .OMD
champ=["lat0","lat1","lat2","lat3","lon0","lon1","lon2","lon3","dist0","dist1","dist2","dist3","tps0","tps1","inconnu","alt0","alt1","inconnu","inconnu","F1",
       "lat0","lat1","lat2","lat3","lon0","lon1","lon2","lon3","dist0","dist1","dist2","dist3","tps0","tps1","inconnu","alt0","alt1","inconnu","inconnu","F1",
       "tps0","tps1","vit0","vit1","KCal0","KCal1","coeur","inconnu","inconnu","moitieF2","tps0","tps1","vit0","vit1","KCal0","KCal1","coeur","inconnu","inconnu","F2"]

nombremesures=0
sommebpm=0
maxheartrate=0
maxspeed=0
distavant=0
tpsavant=0
tcx1=""
cpt=0
premiereligne=1
with open(fichier+'.OMD', 'rb') as file: #OMD et OMH 1, 2, 5, 40
    for c in file:
        for i in c:
            octet=str(i)
            col=cpt%60

            
            if col==0:
                
                if premiereligne==1:
                    tcx1='<Trackpoint><Time>'+dateheure+'</Time><DistanceMeters>0</DistanceMeters><Extensions><TPX xmlns="http://www.garmin.com/xmlschemas/ActivityExtension/v2"><Speed>0</Speed></TPX></Extensions></Trackpoint>'
                    tcx1+='\n\n'
                    premiereligne=0
                else:# calcule toutes les variables et intégre dans txtresult
                    #calcul du temps
                    tps1=(champ[13]*256+champ[12])
                    sec1=tps1%60
                    min1=champomh[18]+int(tps1/60)
                    hour1=champomh[17]+int(min1/60)
                    min1=min1%60
                    if hour1<10:
                        hour1='0'+str(hour1)
                    else:
                        hour1=str(hour1)
                    if min1<10:
                        min1='0'+str(min1)
                    else:
                        min1=str(min1)
                    if sec1<10:
                        sec1='0'+str(sec1)
                    else:
                        sec1=str(sec1)
                    time1=datefix+'T'+hour1+':'+min1+':'+sec1+'+02:00'
                    tps2=(champ[33]*256+champ[32])
                    sec2=tps2%60
                    min2=champomh[18]+int(tps2/60)
                    hour2=champomh[17]+int(min2/60)
                    min2=min2%60
                    if hour2<10:
                        hour2='0'+str(hour2)
                    else:
                        hour2=str(hour2)
                    if min2<10:
                        min2='0'+str(min2)
                    else:
                        min2=str(min2)
                    if sec2<10:
                        sec2='0'+str(sec2)
                    else:
                        sec2=str(sec2)
                    time2=datefix+'T'+hour2+':'+min2+':'+sec2+'+02:00'
                    #Cardio
                    card1=champ[46]
                    sommebpm+=card1
                    if card1>maxheartrate:
                        maxheartrate=card1
                    card2=champ[56]
                    sommebpm+=card2
                    if card2>maxheartrate:
                        maxheartrate=card2
                    #distance(m)
                    dist1=(champ[11]*256**3+champ[10]*256**2+champ[9]*256+champ[8])
                    dist2=(champ[31]*256**3+champ[30]*256**2+champ[29]*256+champ[28])
                    #vitesse en km/h
                    #vit1=(champ[42]+champ[43]*256)/100
                    vit1=(dist1-distavant)/(tps1-tpsavant)
                    distavant=dist1
                    tpsavant=tps1
                    if vit1>maxspeed:
                        maxspeed=vit1
                    #vit2=(champ[52]+champ[53]*256)/100
                    vit2=(dist2-distavant)/(tps2-tpsavant)
                    distavant=dist2
                    tpsavant=tps2
                    if vit2>maxspeed:
                        maxspeed=vit2
                    #longitude
                    if champ[7]>127:
                        cha=champ[7]-256
                    else:
                        cha=champ[7]
                    if champ[27]>127:
                        chb=champ[27]-256
                    else:
                        chb=champ[27]
                    lon1=str((cha*256**3+champ[6]*256**2+champ[5]*256+champ[4])/1000000)
                    lon2=str((chb*256**3+champ[26]*256**2+champ[25]*256+champ[24])/1000000)
                    #latitude
                    if champ[3]>127:
                        cha=champ[3]-256
                    else:
                        cha=champ[3]
                    if champ[23]>127:
                        chb=champ[23]-256
                    else:
                        chb=champ[23]
                    lat1=str((cha*256**3+champ[2]*256**2+champ[1]*256+champ[0])/1000000)
                    lat2=str((chb*256**3+champ[22]*256**2+champ[21]*256+champ[20])/1000000)
                    #altitude
                    if champ[16]>127:
                        cha=champ[16]-256
                    else:
                        cha=champ[16]
                    if champ[36]>127:
                        chb=champ[36]-256
                    else:
                        chb=champ[36]
                    alt1=str(cha*256+champ[15])
                    alt2=str(chb*256+champ[35])
                    #kilocalories
                    kcal1=str(champ[44]+256*champ[45])
                    kcal2=str(champ[54]+256*champ[55])
                    #compteur nombre mesures
                    nombremesures+=2

                    tcx1+='<Trackpoint><Time>'+time1+'</Time><Position><LatitudeDegrees>'+str(lat1)+'</LatitudeDegrees>'
                    tcx1+='<LongitudeDegrees>'+str(lon1)+'</LongitudeDegrees></Position><AltitudeMeters>'+str(alt1)+'</AltitudeMeters>'
                    tcx1+='<DistanceMeters>'+str(dist1)+'</DistanceMeters><HeartRateBpm><Value>'+str(card1)+'</Value></HeartRateBpm>'
                    tcx1+='<Extensions><TPX xmlns="http://www.garmin.com/xmlschemas/ActivityExtension/v2"><Speed>'+str(vit1)+'</Speed></TPX></Extensions></Trackpoint>'
                    tcx1+='\n'
                    
                    tcx1+='<Trackpoint><Time>'+time2+'</Time><Position><LatitudeDegrees>'+str(lat2)+'</LatitudeDegrees>'
                    tcx1+='<LongitudeDegrees>'+str(lon2)+'</LongitudeDegrees></Position><AltitudeMeters>'+str(alt2)+'</AltitudeMeters>'
                    tcx1+='<DistanceMeters>'+str(dist2)+'</DistanceMeters><HeartRateBpm><Value>'+str(card2)+'</Value></HeartRateBpm>'
                    tcx1+='<Extensions><TPX xmlns="http://www.garmin.com/xmlschemas/ActivityExtension/v2"><Speed>'+str(vit2)+'</Speed></TPX></Extensions></Trackpoint>'
                    tcx1+='\n'

            champ[col]=int(octet)
            cpt+=1

#----------------------------------------------------------
#production des valeurs / et ecriture : pour le/du : .tcx
tcx='<?xml version="1.0" encoding="utf-8"?>\n<TrainingCenterDatabase xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" '
tcx+='xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd" '
tcx+='xmlns:ns5="http://www.garmin.com/xmlschemas/ActivityGoals/v1" xmlns:ns3="http://www.garmin.com/xmlschemas/ActivityExtension/v2" '
tcx+='xmlns:ns2="http://www.garmin.com/xmlschemas/UserProfile/v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
tcx+='xmlns:ns4="http://www.garmin.com/xmlschemas/ProfileExtension/v1">'
tcx+='\n\n'
tcx+='<Activities><Activity Sport="Other"><Id>'+dateheure+'</Id><Lap StartTime="'+dateheure+'"><TotalTimeSeconds>'+str(tps2)+'</TotalTimeSeconds>'
tcx+='<DistanceMeters>'+str(dist2)+'</DistanceMeters><MaximumSpeed>'+str(maxspeed)+'</MaximumSpeed><Calories>'+kcal2+'</Calories>'
tcx+='<AverageHeartRateBpm><Value>'+str(int(sommebpm/nombremesures))+'</Value></AverageHeartRateBpm><MaximumHeartRateBpm><Value>'+str(maxheartrate)+'</Value></MaximumHeartRateBpm>'
tcx+='<Intensity>Active</Intensity><TriggerMethod>Manual</TriggerMethod>'
tcx+='\n\n'
tcx+='<Track>'
tcx+='\n'
tcx+=tcx1
tcx+='</Track>'
tcx+='\n\n'
tcx+='<Extensions><LX xmlns="http://www.garmin.com/xmlschemas/ActivityExtension/v2"><AvgSpeed>'+str(int(dist2)/tps2)+'</AvgSpeed></LX></Extensions>'
tcx+='</Lap></Activity></Activities>'
tcx+='<Author xsi:type="Application_t"><Name>DECATHLON - SPORTDATA</Name>'
tcx+='<Build><Version><VersionMajor>2</VersionMajor><VersionMinor>2</VersionMinor></Version></Build>'
tcx+='<LangID>en</LangID><PartNumber>000-00000-00</PartNumber></Author>'
tcx+='</TrainingCenterDatabase>'

destinationsave = open(out+'.tcx', "w")# export des données calculées depuis les valeurs brutes du précédent tableau
destinationsave.write(tcx)
destinationsave.close()
