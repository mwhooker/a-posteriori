/* vi: ft=prolog
*
There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
*/

owns(pet(dog), person(spaniard)).

lives(house(red), person(englishman)).
lives(house_idx(0), person(norweigian)).

drinks(drink(coffee), house(green)).
drinks(drink(tea), person(ukranian)).
drinks(drink(milk), house_idx(2)).

smokes(smoke(og), pet(snails)).
smokes(smoke(kools), house(yellow)).
smokes(smoke(luckystrike), drink(oj)).
smokes(smoke(parliaments), person(japanese)).

%# The man who smokes Chesterfields lives in the house next to the man with the fox.
%# Kools are smoked in the house next to the house where the horse is kept.
%# The Norwegian lives next to the blue house.
adj(smoke(chesterfields), pet(fox)).
adj(smoke(kools), pet(horse)).
adj(person(norwegian), house(blue)).
%# The green house is immediately to the right of the ivory house.
left(house(ivory), house(green)).


pet(dog).
pet(snails).
pet(zebra).
pet(fox).
pet(horse).

house(red).
house(green).
house(ivory).
house(yellow).
house(blue).

house_idx(0).
house_idx(1).
house_idx(2).
house_idx(3).
house_idx(4).

person(englishman).
person(spaniard).
person(ukranian).
person(norwegian).
person(japanese).

drink(coffee).
drink(tea).
drink(milk).
drink(oj).
drink(water).

smoke(kools).
smoke(og).
smoke(chesterfields).
smoke(luckystrike).
smoke(parliaments).

%    #Now, who drinks water? Who owns the zebra?
%drinks(drink(water), Person).
%owns(pet(zebra), Person).
