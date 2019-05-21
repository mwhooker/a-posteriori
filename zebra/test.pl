/* vi: ft=prolog
*

    Foo     Bar
X   red     1
Y   blue    


foo(red).
foo(blue).

bar(1).

x(red).
x(1).

y(blue).
y(2).


*/

lecturer(Lecturer, Course) :-
    course(Course, Time, Lecturer, Location).
duration(Course, Length) :-
    course(Course, time(Day, Start, Finish), Lecturer, Location),
    plus(Start, Length, Finish).
teaches(Lecturer, Day) :-
    course(Course, time(Day, Start, Finish), Lecturer, Location).
occupied(Room, Day, Time) :-
    course(Course, time(Day, Start, Finish), Lecturer, Room),
    Start =< Time, Time =< Finish.
    

course(complexity, time(monday,9,11), lecturer(david,hare), location(feinberg,a)).
