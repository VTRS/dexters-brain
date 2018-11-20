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
% -------------Primary Emotions-------------
primary_emotions(joy).
primary_emotions(love).
primary_emotions(fear).
primary_emotions(anger).
primary_emotions(sadness).
primary_emotions(surprise).

% ----------Secondary Emotions--------------
% Love related
secondary_emotions(love, lust).
secondary_emotions(love, longing).
secondary_emotions(love, affection).

% Joy related
secondary_emotions(joy, zest).
secondary_emotions(joy, pride).
secondary_emotions(joy, relief).
secondary_emotions(joy, optimism).
secondary_emotions(joy, contentment).
secondary_emotions(joy, enthrallment).
secondary_emotions(joy, cheerfulness).

% Surprise related
secondary_emotions(surprise, surprise).

% Anger related
secondary_emotions(anger, rage).
secondary_emotions(anger, envy).
secondary_emotions(anger, disgust).
secondary_emotions(anger, torment).
secondary_emotions(anger, irritation).
secondary_emotions(anger, exasperation).

% Sadness related
secondary_emotions(sadness, shame).
secondary_emotions(sadness, sadness).
secondary_emotions(sadness, neglect).
secondary_emotions(sadness, sympathy).
secondary_emotions(sadness, suffering).
secondary_emotions(sadness, disappointment).

% Fear related
secondary_emotions(fear, horror).
secondary_emotions(fear, nervousness).


% ----------Terniary Emotions---------------
% ||||||||||||||||||||||||||||||||||||||||||
% ------------------Love--------------------
% Affection related
tertiary_emotions(affection, liking).
tertiary_emotions(affection, caring).
tertiary_emotions(affection, fondness).
tertiary_emotions(affection, attraction).
tertiary_emotions(affection, tenderness).
tertiary_emotions(affection, compassion).
tertiary_emotions(affection, sentimentality).

% Lust related
tertiary_emotions(lust, desire).
tertiary_emotions(lust, passion).
tertiary_emotions(lust, infatuation).

% ------------------JOY---------------------
% Cheerfulness related
tertiary_emotions(cheerfulness, glee).
tertiary_emotions(cheerfulness, bliss).
tertiary_emotions(cheerfulness, gaiety).
tertiary_emotions(cheerfulness, delight).
tertiary_emotions(cheerfulness, elation).
tertiary_emotions(cheerfulness, ecstasy).
tertiary_emotions(cheerfulness, euphoria).
tertiary_emotions(cheerfulness, gladness).
tertiary_emotions(cheerfulness, jolliness).
tertiary_emotions(cheerfulness, amusement).
tertiary_emotions(cheerfulness, enjoyment).
tertiary_emotions(cheerfulness, joviality).
tertiary_emotions(cheerfulness, happiness).
tertiary_emotions(cheerfulness, jubilation).
tertiary_emotions(cheerfulness, satisfaction).
tertiary_emotions(cheerfulness, cheerfulness).

% Zest related
tertiary_emotions(zest, zeal).
tertiary_emotions(zest, thrill).
tertiary_emotions(zest, excitement).
tertiary_emotions(zest, enthusiasm).
tertiary_emotions(zest, exhilaration).

% Contentment related
tertiary_emotions(contentment, pleasure).

% Pride related
tertiary_emotions(pride, triumph).

% Optimism related
tertiary_emotions(optimism, hope).
tertiary_emotions(optimism, eagerness).

% Enthrallment related
tertiary_emotions(enthrallment, rapture).

% ------------------SURPRISE---------------------
% Surprise related
tertiary_emotions(surprise, amazement).
tertiary_emotions(surprise, astonishment).

% -------------------ANGER-----------------------
% Irritation related
tertiary_emotions(irritation, agitation).
tertiary_emotions(irritation, annoyance).
tertiary_emotions(irritation, grumpiness).
tertiary_emotions(irritation, aggravation).
tertiary_emotions(irritation, grouchiness).

% Exasperation related
tertiary_emotions(exasperation, frustration).

% Rage related
tertiary_emotions(rage, fury).
tertiary_emotions(rage, hate).
tertiary_emotions(rage, wrath).
tertiary_emotions(rage, scorn).
tertiary_emotions(rage, spite).
tertiary_emotions(rage, dislike).
tertiary_emotions(rage, outrage).
tertiary_emotions(rage, ferocity).
tertiary_emotions(rage, loathing).
tertiary_emotions(rage, hostility).
tertiary_emotions(rage, bitterness).
tertiary_emotions(rage, resentment).
tertiary_emotions(rage, vengefulness).

% Disgust related
tertiary_emotions(disgust, revulsion).
tertiary_emotions(disgust, contentment).

% Envy related
tertiary_emotions(envy, jealousy).

% ------------------SADNESS----------------------
% Suffering related
tertiary_emotions(suffering, hurt).
tertiary_emotions(suffering, agony).
tertiary_emotions(suffering, tired).
tertiary_emotions(suffering, anguish).
tertiary_emotions(suffering, exhaust).

% Sadness related
tertiary_emotions(sadness, woe).
tertiary_emotions(sadness, grief).
tertiary_emotions(sadness, gloom).
tertiary_emotions(sadness, misery).
tertiary_emotions(sadness, sorrow).
tertiary_emotions(sadness, sadness).
tertiary_emotions(sadness, despair).
tertiary_emotions(sadness, glumness).
tertiary_emotions(sadness, depression).
tertiary_emotions(sadness, melancholy).
tertiary_emotions(sadness, unhappiness).
tertiary_emotions(sadness, hopelessness).

% Disappointment related
tertiary_emotions(disappointment, dismay).
tertiary_emotions(disappointment, despleasure).

% Shame related
tertiary_emotions(shame, guilt).
tertiary_emotions(shame, regret).
tertiary_emotions(shame, remorse).

% Neglect related
tertiary_emotions(neglect, insult).
tertiary_emotions(neglect, defeat).
tertiary_emotions(neglect, dejection).
tertiary_emotions(neglect, isolation).
tertiary_emotions(neglect, rejection).
tertiary_emotions(neglect, insecurity).
tertiary_emotions(neglect, alienation).
tertiary_emotions(neglect, loneliness).
tertiary_emotions(neglect, humiliation).
tertiary_emotions(neglect, homesickness).
tertiary_emotions(neglect, embarrassment).

%Sympathy related
tertiary_emotions(sympathy, pity).

% --------------------FEAR-----------------------
% Horror related
tertiary_emotions(horror, fear).
tertiary_emotions(horror, alarm).
tertiary_emotions(horror, shock).
tertiary_emotions(horror, panic).
tertiary_emotions(horror, fright).
tertiary_emotions(horror, terror).
tertiary_emotions(horror, hysteria).
tertiary_emotions(horror, mortification).

% Nervousness related
tertiary_emotions(nervousness, worry).
tertiary_emotions(nervousness, dread).
tertiary_emotions(nervousness, anxiety).
tertiary_emotions(nervousness, distress).
tertiary_emotions(nervousness, tenseness).
tertiary_emotions(nervousness, uneasiness).
tertiary_emotions(nervousness, apprehension).

% ------------------OPPOSITES---------------------
opposites(sadness, surprise).
opposites(joy, sadness).
opposites(anger, fear).
opposites(love, anger).
