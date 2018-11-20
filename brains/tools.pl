% #     A bot that recomend music according to a given emotion
% #     Copyright (C) 2018 Victor Hugo Torres Rivera
% #
% #     This program is free software: you can redistribute it and/or modify
% #     it under the terms of the GNU General Public License as published by
% #     the Free Software Foundation, either version 3 of the License, or
% #     (at your option) any later version.
% #
% #     This program is distributed in the hope that it will be useful,
% #     but WITHOUT ANY WARRANTY; without even the implied warranty of
% #     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% #     GNU General Public License for more details.
% #
% #     You should have received a copy of the GNU General Public License
% #     along with this program.  If not, see <https://www.gnu.org/licenses/>
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
