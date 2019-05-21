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
row(house_idx(I), house(H), pet(P), smoke(S), drink(D), person(Person)).
*/

row(house_idx(1), house(H), pet(P), smoke(S), drink(D), person(Person)).
row(house_idx(3), house(H), pet(P), smoke(S), drink(D), person(Person)).
row(house_idx(4), house(H), pet(P), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(ivory), pet(P), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(blue), pet(P), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(H), pet(zebra), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(H), pet(fox), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(H), pet(horse), smoke(S), drink(D), person(Person)).
row(house_idx(I), house(H), pet(P), smoke(chesterfields), drink(D), person(Person)).
row(house_idx(I), house(H), pet(P), smoke(S), drink(water), person(Person)).

row(house_idx(I), house(H), pet(dog), smoke(S), drink(D), person(spaniard)).
row(house_idx(I), house(red), pet(P), smoke(S), drink(D), person(englishman)).
row(house_idx(0), house(H), pet(P), smoke(S), drink(D), person(norwegian)).
row(house_idx(I), house(green), pet(P), smoke(S), drink(coffee), person(Person)).
row(house_idx(I), house(H), pet(P), smoke(S), drink(tea), person(ukranian)).
row(house_idx(2), house(H), pet(P), smoke(S), drink(milk), person(Person)).
row(house_idx(I), house(H), pet(snail), smoke(og), drink(D), person(Person)).
row(house_idx(I), house(yellow), pet(P), smoke(kools), drink(D), person(Person)).
row(house_idx(I), house(H), pet(P), smoke(luckystrike), drink(oj), person(Person)).
row(house_idx(I), house(H), pet(P), smoke(parliaments), drink(D), person(japanese)).

%# The man who smokes Chesterfields lives in the house next to the man with the fox.
%# Kools are smoked in the house next to the house where the horse is kept.
%# The Norwegian lives next to the blue house.
adj(smoke(chesterfields), pet(fox)).
adj(smoke(kools), pet(horse)).
adj(person(norwegian), house(blue)).
%# The green house is immediately to the right of the ivory house.
left(house(ivory), house(green)).

%row(house_idx(I), house(H), pet(P), smoke(S), drink(D), person(Person)).
left(row(house_idx(I), house(ivory), pet(P), smoke(S), drink(D), person(Person)),
row(house_idx(I), house(green), pet(P), smoke(S), drink(D), person(Person))).

left_of(L, R) :- left(L, R).

left_of(HouseLHS, HouseRHS) :- house(HouseLHS), house(HouseRHS), left(house(HouseLHS), house(HouseRHS)).
left_of(HouseLHS, HouseRHS) :- house_idx(HouseLHS), house_idx(HouseRHS), HouseLHS < HouseRHS.

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
row(1, H, P, S, D, N).
row(3, H, P, S, D, N).
row(4, H, P, S, D, N).
row(I, ivory, P, S, D, N).
row(I, blue, P, S, D, N).
row(I, H, zebra, S, D, N).
row(I, H, fox, S, D, N).
row(I, H, horse, S, D, N).
row(I, H, P, chesterfields, D, N).
row(I, H, P, S, water, N).

row(I, H, dog, S, D, spaniard).
row(I, red, P, S, D, englishman).
row(0, H, P, S, D, norwegian).
row(I, green, P, S, coffee, N).
row(I, H, P, S, tea, ukranian).
row(2, H, P, S, milk, N).
row(I, H, snail, og, D, N).
row(I, yellow, P, kools, D, N).
row(I, H, P, luckystrike, oj, N).
row(I, H, P, parliaments, D, japanese).

left(ivory, green).

left_of(C1, C2) :-
    row(I, C1, P, S, D, N),
    row(I, C2, P, S, D, N),
    left(C1, C2).

adj_to(I1, I2) :-
    row(I1, H, P, S, D, N),
    row(I2, H, P, S, D, N),
    I1 + 1 =:= I2 ; I1 - 1 =:= I2.

neighbor(I1, I2) :-
    row(I1, H, P, chesterfields, D, N),
    row(I2, H, fox, S, D, N).




%drinks(drink(water), Person).
%owns(pet(zebra), Person).
% row(I, H, P, S, water, N).
% row(I, H, zebra, S, D, N).
