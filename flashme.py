#welcome to pythong
import os, re
import random
cards = []

def shuffle():
  answer= input("Would you like to (sh)uffle, sort by (in)correct, by (ind)ex or sort by (co)rrect?")
  
  sort_options = {  
        'sh': lambda : random.shuffle(cards),
        'in': lambda :list.sort(cards, key=lambda x: x[2], reverse=True),
        'co': lambda :cards.sort(key=lambda x: x[3], reverse=True),
        'ind': lambda :cards.sort(key=lambda x: x[4], reverse=True)
        }

  if answer in sort_options:
    sort_options[answer]()

  # if answer=="sh":
    # shuffle(cards)
  # if answer=="in":
    # cards.sort(key=lambda x: x[3], reverse=True)
  # if answer=="co":
    # cards.sort(key=lambda x: x[4], reverse=True)
  # if answer=="ind":
    # cards.sort(key=lambda x: x[5])

def quiz():
  while True:
    shuffle()
    #iterList  = iter(cards)
    for q, a, correct, wrong, index in cards:
      myAnswer= input(q+"\n> ")
      if (myAnswer=="die"):
        return
      elif myAnswer=="quizwrong":
        quizwrong()
      elif (myAnswer == a):
        cards[index][2]+=1
        print("correct")
      elif myAnswer=="stats":
        print (sum(map(lambda x: x[2], cards)))
        #print (lambda x: [x+=y for y[2] in cards])
        #print (lambda x+y: y for y[2] in cards)
        
      else:
        cards[index][3]+=1
        print("wrong")

def quizwrong():
  while True:
    list.sort(cards, key=lambda x: x[2], reverse=True)
    iterList = iter(cards)
    for q, a, correct, wrong, index in iterList:
      if wrong == 0: 
        continue
      myAnswer= input(q+"\n> ")
      if (myAnswer=="die"):
        return
      elif (myAnswer == a):
        cards[index][2]+=1
        print("correct")
      else:
        cards[index][3]+=1
        print("wrong")
  
def main():  
  index = 0
  while True:
    flashcard = input("Enter a flashcard: ")
    if flashcard == "q" or flashcard == "quit":
      break
    if flashcard == "quiz":
      quiz()
    question,  _ , answer = flashcard.partition("-")
  
    print(question, answer)
  
    cards.append([question,answer,0,0,index])
    index+=1

if __name__ == "__main__":
  main()