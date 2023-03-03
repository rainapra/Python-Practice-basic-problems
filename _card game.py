#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Spade', 'Heart', 'Diamond', 'Club')


# In[32]:


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[33]:


Ace_of_spade = Card("Spade","Ace")


# In[34]:


print(Ace_of_spade)


# In[35]:


Ace_of_spade.value


# In[36]:


Five_of_Diamond = Card("Diamond", "Five")


# In[37]:


Five_of_Diamond.value


# In[38]:


Five_of_Diamond.value < Ace_of_spade.value


# In[64]:


class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                create_card=Card(suit, rank)
                self.all_cards.append(create_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal(self):
        return self.all_cards.pop()


# In[65]:


new_deck = Deck()


# In[62]:


top_card=new_deck.all_cards[0]


# In[63]:


print(top_card)


# In[66]:


new_deck.shuffle()


# In[54]:


last_card=new_deck.all_cards[-1]


# In[55]:


print(last_card)


# In[67]:


mycard = new_deck.deal()


# In[74]:


print(mycard)


# In[69]:


len(new_deck.all_cards)


# In[48]:


for card_obj in new_deck.all_cards:
    print(card_obj)


# In[70]:


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    


# In[71]:


player1=Player("Prashant")


# In[72]:


print(player1)


# In[81]:


player1.add_cards([mycard])


# In[84]:


print(player1)


# In[78]:


print(player1.all_cards[0])


# In[83]:


player1.remove()


# In[97]:


# Game play
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal())
    player_two.add_cards(new_deck.deal())
    


# In[98]:


game_on = True


# In[99]:


round_count = 0
while game_on:
    round_count = round_count + 1
    print(f"Round: {round_count}")
    
    if len(player_one.all_cards) == 0:
        print('Player One Lost!!! Player Two Wins!!!')
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print('Player Two Lost!!! Player One Wins!!!')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove())
    
    war = True
    
    while war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False
            
        else:
            print("WAR!!!")
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to war")
                print("Player Two wins!!! Player One Loses!")
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to war")
                print("Player One wins!!! Player Two Loses!")
                game_on = False
                break
                
            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove())
                    player_two_cards.append(player_two.remove())
                    


# In[ ]:





# In[ ]:




