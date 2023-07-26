import os
import random
import clearLines
import sys
import time
def start(word, dash):
	indexes=random.sample(range(len(word)),dash)
	letter=list(set(word[index] for index in indexes)) #We don't need dupicate lettters
	
	#Creating the word
	counter=0
	finalWord=""
	record=dict()
	while True:
		if counter in indexes:
			finalWord=finalWord+"_"
			if word[counter] in record:
				record[word[counter]].append(counter)
			else:
				record[word[counter]]=[counter]
		else:
			finalWord=finalWord+word[counter]
		counter+=1
		if counter==len(word):
			break


	#Actual game
	hangMan=list("HANGMAN")
	tempList=list(finalWord)
	deathCounter=7
	while True:
		print("".join(hangMan))
		print(finalWord,"\t\tDeath in", deathCounter)
		guess=input("Enter the letter: ")
		if guess in letter:
			for index in record[guess]:
				tempList[index]=guess
				finalWord="".join(tempList)
				del record[guess]
				del letter[letter.index(guess)]
				if len(letter)==0:
					print("You won!!!\nThe word was ",word)
					sys.exit()
		else:
			deathCounter-=1
			hangMan.pop()
		if deathCounter==0:
			print("You lost.\nThe word was",word)
			sys.exit()
		clearLines.clear(3)





answer=input("Enter the word: ")
start(answer,len(answer)//2)