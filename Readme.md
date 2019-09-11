# Préambule

ce petit projet fais pour le MDF2019, mon premier petit bout de code en python avec le support
de Romain Bru, Marion Tuvache et les petits bouts de code de Christophe Bornet  
Merci à eux ;-)

# Utilisation

1 - déposer les fichiers de téléchargement dans le dossier *filescoding*  
2 - coder votre algo dans le fichier coding puis executer / debugger la main  
3 - A l'execution vous pouvez voir dans la console votre résultat  
    A la fin de l'éxécution il compare la sortie pour chaque fichier input avec le résultat attendu de chaque output

#Lors du copier coller vers le site

1 - penser aux imports  
2 - ne pas oublier de virer les lignes pré-saisies de la pages ... 

````
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
Sinon 
	
EOFError: EOF when reading a line
````

#Trucs en plus qui servent ou pas...

1 - classe debug , pour permettre de faire des affichages dans la sortie facilement
2 - Possibilité de filtrer sur un fichier en particulier

````
#exemple
ligne 10 :  filtre = ""  #tous les fichiers sont lus
ou 
ligne 10 :  filtre = "input1" #seul le fichier input est lu :-)

````


Exemple de sortie


````
######################################################
######################################################
			RESULTAT
######################################################
######################################################
Result file : filescoding\input1.txt		votre sortie : ['udbo'] vs attendu ['udbo'] 	 ===========> True
Result file : filescoding\input2.txt		votre sortie : ['myre udbo'] vs attendu ['myre udbo'] 	 ===========> True
Result file : filescoding\input3.txt		votre sortie : ['udbo'] vs attendu ['udbo'] 	 ===========> True
Result file : filescoding\input4.txt		votre sortie : ['htzv'] vs attendu ['htzv'] 	 ===========> True
Result file : filescoding\input5.txt		votre sortie : ['rhia'] vs attendu ['rhia'] 	 ===========> True
````
