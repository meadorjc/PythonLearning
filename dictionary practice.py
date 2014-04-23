import functools

# sort_options = dict(sh = shuffle(cards), in = cards.sort(key=lambda x: x[3], reverse=True))

def puffle(cards):
  for x in cards:
    print('howdy', x)
cards = ['count me in', 'praise be', 'hallelujah', 'all hail']
print(cards)

so = {  'sh': lambda :puffle(cards),
        'in': lambda :list.sort(cards, key=lambda x: x[2], reverse=True),
        'co': lambda :cards.sort(key=lambda x: x[3], reverse=True),
        'ind' : lambda :cards.sort(key=lambda x: x[4], reverse=True)}
x = 'in'  
if x in so:
  so[x]()

print(cards)

#print(so[x][0], so[x][1], so[x][2], so[x][3])
#exe=functools.partial(so[x][0], so[x][1], so[x][2], so[x][3])
#exe = functools.partial(list.sort, cards, key=lambda cards:cards[len(cards)-1])
#list.sort( cards, key=lambda cards:cards[len(cards)-1])


# , co = cards.sort(key=lambda x: x[4], reverse=True), ind =cards.sort(key=lambda x: x[5]))

# sort_cards( in=False, co=False, ind=False):
    


# def shuffle():
  # answer= input("Would you like to (sh)uffle, sort by (in)correct, by (ind)ex or sort by (co)rrect?")
  # if answer=="sh":
    # shuffle(cards)
  # if answer=="in":
  # if answer=="co":
    
  # if answer=="ind":
    # cards.sort(key=lambda x: x[5])