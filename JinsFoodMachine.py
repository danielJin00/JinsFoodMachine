import random, time
import PySimpleGui as sg


# Dictionary for each meal : time, ingredients , time of the day ,
# {"Zutaten": ["","", "" ],"Bearbeitungszeit in min": , "Typ": "" } 
MaboTofu = {"Zutaten": ["Tofu","Hackfleisch", "" ],"Bearbeitungszeit in min": 30, "Typ": "Dinner" }
CurryReis = {"Zutaten": ["","", "" ],"Bearbeitungszeit in min": , "Typ": "Dinner" }  
PestoNudeln = {"Zutaten": ["Nudeln","Pesto", "Tomaten", "Pinienkerne"],"Bearbeitungszeit in min": 15 , "Typ": "Dinner" } 
Fischstäbchen_mit_Kartoffelbrei = {"Zutaten": ["","", "" ],"Bearbeitungszeit in min": , "Typ": "Dinner" } 
KäseSpätzel = {"Zutaten": ["","", "" ],"Bearbeitungszeit in min": , "Typ": "Dinner" } 
Chilli_Con_Carne = {"Zutaten": ["","", "" ],"Bearbeitungszeit in min": , "Typ": "Dinner" } 
Burrito = {"Zutaten": ["Tortilla","Salat", "", ],"Bearbeitungszeit in min": , "Typ": "Dinner" }
Carbonara = {"Zutaten": ["Nudeln","Eier", "Guanciale","Pecorino", "Parmesan"],"Bearbeitungszeit in min": 30 , "Typ": "Dinner"  }



# Main meal list
Gerichte_Liste = [MaboTofu,CurryReis,PestoNudeln,Fischstäbchen_mit_Kartoffelbrei,KäseSpätzel,Chilli_Con_Carne,Wraps]


#Anforderungen :

#1. Gericht Random ausgeben, 2. Abhängig von Lebensmitteln (oder Tageszeit,Bearbeitungszeit,...) passende Gerichte ausgeben, 3. Möglichkeit Gericht hinzuzufügen

#1.
randomGericht = random.randint(0,len(Gerichte_Liste))


