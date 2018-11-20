% //////////////////////////Substitutes/////////////////////////////////
% Substitutes with M the elements of the list which value is equal to N.
% Base case triggered when the first list is empty.
substitute(_, _, [], []).

% In case M and the head are the same, it changes it with N.
substitute(M, N, [M|T], [N|NT]):- !,
  substitute(M, N, T, NT).

% In case the head and M are different it goes with the next value.
substitute(M, N, [H|T], [H|NT]):-
  substitute(M, N, T, NT).

% ///////////////////////////Is in////////////////////////////////////
% Proofs that an element is in a list.
is_in(N, [N|_]):- !.
is_in(N, [_|T]):-
  is_in(N, T).

% //////////////////////Add element to the end///////////////////////
% Append an element to the end of the list.
addend(X, [], [X]).
addend(X, [H|T], [H|NewList]):-
  addend(X, T, NewList).

% //////////////////////Append list to list/////////////////////////
% Append one list M next to list N.
append([], List, List).
append([NH|NT], M, [NH|NewList]):-
  append(NT, M, NewList).
