
from random import *
import time

def start_game(time) : 
  """paramètre : début du jeu -> str et int ; retour : valeur saisie -> str ou int"""
  global mode_jeu, manches
  #La fonction "global" permet de pouvoir utiliser les variables appartiennet au script et non à la fonction, ici "mode_jeu" et "manches" 
  print("/!\ Ce jeu a été réalisé dans le but d'un projet. \n") 

  time.sleep(2)  
  
  print("Bienvenue dans le jeu du Pierre, Feuille ou Ciseaux.")
  time.sleep(0.5)
 
  rules = str(input("Voulez-vous qu'on vous rappelle les règles du jeu?\n"))
  if rules == "oui" and "o" and "yes" and "Oui" : 
    print("Les règles du pierre feuille ciseaux sont simples : \n La pierre bat le ciseau, le ciseau bat la feuille et la feuille bat la pierre")
    #Si la réponse n'est pas "oui" ou "o" ou "yes" ou "Oui", les règles ne s'affichent pas
  else : 
    print("Veuillez sélectionner votre mode de jeu entre : le mode 'démo', le mode 'joueur vs joueur' et le mode 'joueur vs ordinateur'")
    time.sleep(1)
    
  mode_jeu = input("Choisissez votre mode : \n --> 1 pour joueur vs ordinateur \n --> 2 pour joueur vs joueur \n --> 3 pour ordinateur vs ordinateur\n")
  time.sleep(0.5)
  

start_game(time)

def manches() :
  """paramètre : nombres de manches -> int ; retour : valeur saisie -> int"""
  global manches
  manches = int(input("En combien de points voulez-vous faire ces parties?"))

def options() :  
  """paramètre : options -> str ; retour : pierre, feuille ou ciseaux -> str"""
  global pierre, feuille, ciseaux
  pierre = "pierre"
  feuille = "feuille"
  ciseaux = "ciseaux"
    




if mode_jeu == "2" :
    print("Vous entrez dans le mode joueur vs joueur!")
    options()   
    manches()
    
    print("\n")
    nomjoueur1 = input("joueur1, quel est votre nom d'utilisateur ? : ")
    pointsjoueur1 = 0

    nomjoueur2 = input("joueur2, quel est votre nom d'utilisateur ? : ")
    pointsjoueur2 = 0

    print("\n")


    while pointsjoueur1 != manches and pointsjoueur2 != manches :
      #tant que le nombre de points est différent du nombre de manches, la partie continue.
      print("--------------------------------------------------------------")

      print(nomjoueur1)
      joueur1 = str(input("choisissez entre 'pierre', 'feuille' ou 'ciseaux' : \n"))
      
      print("\n")
      print("--------------------------------------------------------------")
      print(nomjoueur2)
      joueur2 = str(input("choisissez entre 'pierre', 'feuille' ou 'ciseaux' : \n"))
      
      
      def choix_joueur1(joueur1) :     
        """paramètre : choix du joueur 1 -> str ; retour : valeur saisie -> str"""
        if joueur1 == pierre :
            joueur1 = "pierre"
        elif joueur1  == feuille :
            joueur1 = "feuille"
        else :
            joueur1 = "ciseaux"

      def choix_joueurs2(joueur2) :
        """paramètre : choix du joueur 2 -> str ; retour : valeur saisie -> str"""
        if joueur2 == pierre :
            joueur2 = "pierre"
        elif joueur2  == feuille :
            joueur2 = "feuille"    
        else :
            joueur2 = "ciseaux" 

      print(nomjoueur1, "a choisi : ", joueur1)
      print(nomjoueur2, "a choisi : ", joueur2)
        
      
      if joueur1 == joueur2:
        print("--> égalité, il n'y a aucun gagnant.\n")
        print("--------------------------------------------------------------")

      elif joueur1 == "pierre" and joueur2 == "feuille":
        pointsjoueur2 += 1 
        print("-->", nomjoueur2, "a gagné ! Tu as", pointsjoueur2, "points \n")
        print("--------------------------------------------------------------")
            
      elif joueur1 == "feuille" and joueur2 == "ciseaux":
        pointsjoueur2 += 1 
        print("-->", nomjoueur2,  "a gagné ! Tu as", pointsjoueur2, "points \n")
        print("--------------------------------------------------------------")

      elif joueur1 == "ciseaux" and joueur2 == "pierre":
        pointsjoueur2 += 1 
        print("-->", nomjoueur2, "a gagné ! Tu as", pointsjoueur2, "points \n")
        print("--------------------------------------------------------------")
            
      else:
        pointsjoueur1 += 1 
        print("-->", nomjoueur1, "a gagné! Tu as", pointsjoueur1, "points \n")
        print("--------------------------------------------------------------")

    if pointsjoueur2 > pointsjoueur1 :
      print("Bravo!", nomjoueur2, "a remporté la partie avec succès!")
    else :
      print("Bravo!", nomjoueur1, "a remporté la partie avec succès")




elif mode_jeu == "1" : 
    print("Vous entrez dans le mode joueur contre ordinateur!")
    options()
    manches()
     
    nomjoueur = input("Quel est votre nom  d'utilisateur ? : ")
    time.sleep(1)
    print("Bonjour", nomjoueur, "\n")
    pointsjoueur = 0
    pointsordi = 0

    while pointsjoueur != manches and pointsordi != manches :
      print("--------------------------------------------------------------")
      joueur = str(input("Choisissez entre choix entre 'pierre', 'feuille' ou 'ciseaux' : \n"))
      assert type(joueur) == str
      ordinateur = choice([pierre, feuille, ciseaux])
      
      time.sleep(1)

      if joueur == pierre :
        joueur = "pierre"
      elif joueur == feuille :
        joueur = "feuille"
      else :
        joueur = "ciseaux"
        
      print(nomjoueur, "a choisi : ", joueur) 
      print("L'ordinateur a choisi : " , ordinateur)
        
      if ordinateur == joueur:
        print("égalité, il n'y a aucun gagnant. \n")
        print("--------------------------------------------------------------")

      elif ordinateur == "pierre" and joueur == "feuille":
        pointsjoueur += 1 
        print("-->", nomjoueur, "a gagné ! Tu as", pointsjoueur, "points \n")
        print("--------------------------------------------------------------")
        
      elif ordinateur == "feuille" and joueur == "ciseaux":
        pointsjoueur += 1 
        print("-->", nomjoueur,  "a gagné ! Tu as", pointsjoueur, "points \n")
        print("--------------------------------------------------------------")

      elif ordinateur == "ciseaux" and joueur == "pierre":
        pointsjoueur += 1 
        print("-->", nomjoueur, "a gagné ! Tu as", pointsjoueur, "points  \n")
        print("--------------------------------------------------------------")
        
      else:
        pointsordi += 1 
        print("--> L'ordinateur a gagné ! Il a", pointsordi, "points \n")
        print("--------------------------------------------------------------")

    if pointsjoueur > pointsordi :
      print("Bravo!", nomjoueur, "a remporté la partie avec succès!")

    else :
      print("Pas de chance, l'ordinateur a  remporté la partie...")

else :
    print("Vous entrez dans le mode démo!")

    options()
    manches()
    
    pointsordi1 = 0
    pointsordi2 = 0

    while pointsordi1 != manches and pointsordi2 != manches :
      ordinateur1 = choice([pierre, feuille, ciseaux])
      ordinateur2 = choice([pierre, feuille, ciseaux])
      time.sleep(1)
      print("--------------------------------------------------------------")

      print(ordinateur1, "vs" , ordinateur2)
      time.sleep(1)
        
      if ordinateur1 == ordinateur2:
        print("--> égalité, il n'y a aucun gagnant.")
        print("--------------------------------------------------------------")

      elif ordinateur1 == "pierre" and ordinateur2 == "feuille":
        pointsordi2 += 1 
        time.sleep(1)
        print("--> L'ordinateur 2 a gagné ! Il a", pointsordi2, "points")
        print("--------------------------------------------------------------")
        
      elif ordinateur1 == "feuille" and ordinateur2 == "ciseaux":
        pointsordi2 += 1 
        time.sleep(1)
        print("--> L'ordinateur 2 a gagné ! Il a", pointsordi2, "points")
        print("--------------------------------------------------------------")

      elif ordinateur1 == "ciseaux" and ordinateur2 == "pierre":
        pointsordi2 += 1 
        time.sleep(1)
        print("--> L'ordinateur 2 a gagné ! Il a", pointsordi2, "points")
        print("--------------------------------------------------------------")
        
      else:
        pointsordi1 += 1 
        time.sleep(1)
        print("--> L'ordinateur 1 a gagné. Il  a", pointsordi1, "points")
        print("--------------------------------------------------------------")

    if pointsordi1 > pointsordi2 :
      print("Bravo! L'ordinateur 1 a gagné!")

    else :
      print("Bravo! L'ordinateur 2 a gagné!")
