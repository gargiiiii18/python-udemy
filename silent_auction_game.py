import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("The Silent Auction Game")

auctioners={}
winner=''
next_person=True
while next_person:
  key=input("Enter your name: ")
  bid=int(input("Enter your bid: "))
  auctioners[key]=bid
  next_person=input("Are there any more persons? ")
  if next_person=="no":
    next_person=False
  clear()
print(auctioners)

max=0
for key in auctioners:
  if auctioners[key]>=max:
    max=auctioners[key]
    winner=key
print(f"{winner} made the highest bid of {auctioners[winner]} usd")

# for item in auctioners:
#   if auctioners[key]