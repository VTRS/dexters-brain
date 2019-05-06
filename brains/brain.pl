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
:-consult(tools).
:-consult(phrases_knowledge_base).
:-consult(language_knowledge_base).
:-consult(feelings_knowledge_base).
:-consult(understandable_knowledge_base).

% talk(Message, Response):-
%   understand(Message, Feeling),
%   build_response(Message, Feeling, Response).

% Find if the word is understandable and if it is
% then find the primary emotion that relates to it.
get_root_feeling(Word, Word):-
  primary_emotions(Word), !.

get_root_feeling(Word, Feeling):-
  understandable(Word),
  secondary_emotions(Feeling, Word), !.

get_root_feeling(Word, Feeling):-
  understandable(Word),
  tertiary_emotions(Secondary, Word), !,
  secondary_emotions(Feeling, Secondary).

get_root_feeling(Word, Feeling):-
  possibleways(Understand, Word),
  get_root_feeling(Understand, Feeling).


feeling_in_phrase([MHead|MTail], Feeling):-
  get_root_feeling(MHead, Feeling);
  feeling_in_phrase(MTail, Feeling).

answer(Message, Feeling):-
  feeling_in_phrase(Message, Feeling).

build_response(Message, Feeling, Response):-
  substitute_person(Message, SubstitutedMessage),
  responsive(Feeling, FeelResponse),
  recommend(Recommend),
  atomic_list_concat(SubstitutedMessage, ' ', AtomSubstituted),
  atom_string(AtomSubstituted, StringSubstituted),
  append([FeelResponse], [StringSubstituted], AuxResponse),
  append(AuxResponse, [Recommend], Response).

% /////////////////////// Substitute Persons //////////////////////////////////
substitute_person([], []).

substitute_person([MH|MT], [Substituted|NewT]):-
  swapable_person(MH, Substituted), !,
  substitute_person(MT, NewT).

substitute_person([MH|MT], [MH|NewT]):-
  substitute_person(MT, NewT).
