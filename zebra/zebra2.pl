/* vi: ft=prolog
*
*/


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

left_of(I1, I2) :-
    row(I1, H, P, S, D, N),
    row(I2, H, P, S, D, N),
    I1 < I2.

adj_to(I1, I2) :-
    row(I1, H, P, S, D, N),
    row(I2, H, P, S, D, N),
    I1 + 1 =:= I2 ; I1 - 1 =:= I2.

adj(I1, I2) :-
    row(I1, H, P, chesterfields, D, N),
    row(I2, H, fox, S, D, N).

adj(I1, I2) :-
    row(I1, H, P, kools, D, N),
    row(I2, H, horse, S, D, N).

adj(I1, I2) :-
    row(I1, H, P, S, D, norwegian),
    row(I2, blue, P, S, D, N).

right_of(I, [], []).

right_of(I, [H|T], [H|Result]) :-
    H > I,
    right_of(I, T, Result).

right_of(I, [_|T], Result) :-
    right_of(I, T, Result).

right_of(2, [0, 1, 2, 3, 4], Result).


/*
solve(I1) :-
    row(I1, H, P, S, D, N),
    left_of(I1, I1 + 1),
*/




%drinks(drink(water), Person).
%owns(pet(zebra), Person).
row(I, H, P, S, water, N).
row(I, H, zebra, S, D, N).
