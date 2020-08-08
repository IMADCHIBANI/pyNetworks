from iteration_utilities import duplicates
from iteration_utilities import unique_everseen


class readAdresse:
    def __init__(self,fulllist):
        self.fulllist=fulllist
    """Fonction qui permet de combiner plusieurs numéros d'adresse dans une seule """
    def readFullListe(self):
        stringlist=[]
        FirstListNumberforAdresse=[]
        SecondListNumberfoAdresse=[]
        ThirdListNumberfoAdresse=[]
        FordListNumberfoAdresse=[]
        FifthListNumberForAdresse=[]

        for adresse in self.fulllist:
            if len(adresse)==3:
                stringlist.append(adresse[2])
            else:
                stringlist.append(adresse[1])
        Uniqueadresse=list(unique_everseen(stringlist))

        for adresse in self.fulllist:
            for i in range(0,len(Uniqueadresse)):
                if len(adresse)==2:
                    if Uniqueadresse[i]==adresse[1]:
                        if i==0:
                            FirstListNumberforAdresse.append(adresse[0])
                        elif i==1:
                            SecondListNumberfoAdresse.append(adresse[0])
                        elif i==2:
                            ThirdListNumberfoAdresse.append(adresse[0])
                        elif i==3:
                            FordListNumberfoAdresse.append(adresse[0])
                        elif i==4:
                            FifthListNumberForAdresse.append(adresse[0])
                else:
                    if Uniqueadresse[i]==adresse[2]:
                        if i==0:
                            FirstListNumberforAdresse.append(adresse[0]+adresse[1])
                        elif i==1:
                            SecondListNumberfoAdresse.append(adresse[0]+adresse[1])
                        elif i==2:
                            ThirdListNumberfoAdresse.append(adresse[0]+adresse[1])
                        elif i==3:
                            FordListNumberfoAdresse.append(adresse[0]+adresse[1])
                        elif i==4:
                            FifthListNumberForAdresse.append(adresse[0]+adresse[1])



        CombinedFirstAdresseNumbers="-".join(map(str, FirstListNumberforAdresse))
        CombinedSecondAdresseNumbers="-".join(map(str, SecondListNumberfoAdresse))
        CombinedThirdAdresseNumbers="-".join(map(str, ThirdListNumberfoAdresse))
        CombinedFordAdresseNumbers="-".join(map(str, FordListNumberfoAdresse))
        CombinedFifthAdresseNumbers="-".join(map(str, FifthListNumberForAdresse))


        if len(Uniqueadresse)==1:
            FullString=CombinedFirstAdresseNumbers+" "+Uniqueadresse[0]
            return FullString
        elif len(Uniqueadresse)==2:
            FullString=CombinedFirstAdresseNumbers+" "+Uniqueadresse[0]+"-"+CombinedSecondAdresseNumbers+" "+Uniqueadresse[1]
            return FullString
        elif len(Uniqueadresse)==3:
            FullString=CombinedFirstAdresseNumbers+" "+Uniqueadresse[0]+"-"+CombinedSecondAdresseNumbers+" "+Uniqueadresse[1]+"-"+CombinedThirdAdresseNumbers+" "+Uniqueadresse[2]
            return FullString
        elif len(Uniqueadresse)==4:
            FullString=CombinedFirstAdresseNumbers+" "+Uniqueadresse[0]+"-"+CombinedSecondAdresseNumbers+" "+Uniqueadresse[1]+"-"+CombinedThirdAdresseNumbers+" "+Uniqueadresse[2]+"-"+CombinedFordAdresseNumbers+" "+Uniqueadresse[2]
            return FullString
        elif len(Uniqueadresse)==5:
            FullString=CombinedFirstAdresseNumbers+" "+Uniqueadresse[0]+"-"+CombinedSecondAdresseNumbers+" "+Uniqueadresse[1]+"-"+CombinedThirdAdresseNumbers+" "+Uniqueadresse[2]+"-"+CombinedFordAdresseNumbers+" "+Uniqueadresse[2]+"-"+CombinedFifthAdresseNumbers+" "+Uniqueadresse[2]

#fulllist=[['1', ' ALLEE DES ACACIAS'], ['1','B', 'RUE DE LA COOPERATIVE'], ['5', 'RUE DE LA COOPERATIVE'], ['5','B', 'RUE DE LA COOPERATIVE'], ['5', 'ESPLANADE DU PIC SAINT LOUP'], ['1', 'RUE DES VIGNERONS'], ['5','B','ESPLANADE DU PIC SAINT LOUP']]
#v1=readAdresse(fulllist).readFullListe()
