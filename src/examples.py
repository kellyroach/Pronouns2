################################################################
#
#     examples.py
#
################################################################

"""Demo sentence examples."""

################################################################
#(1.1) is from Huddleston~\cite{Huddleston78}.
#(1.3) is from Chomsky~\cite{Chomsky57}.
#(1.4) and (1.5) are from Bresnan~\cite{Bresnan71}.
#(1.6) is from Bresnan~\cite{Bresnan71}.
#(1.7) and (1.8) are from Roberts~\cite{Roberts67}.
#(1.9) is from Bloom and Hayes~\cite{BloomHayes78}.
#(1.10) is from Hockett~\cite{Hockett58}.
#(1.11)-(1.14) are from Ross~\cite{Ross67}.
#(1.24)-(1.25) from Kuno~\cite{Kuno74}.
#(1.27) is from Fauconnier~\cite{Fauconnier75}.
#(1.51) is from Huddleston~\cite{Huddleston78}.
#(1.52) is from Grosu~\cite{Grosu73}.
#(1.66) is from Ross\cite{Ross67}.
#(1.70) and (1.74) are from Huddleston~\cite{Huddleston78}.
#(1.86)-(1.89) are from Langacker~\cite{Langacker69}.
#(1.91)-(1.110) are from Ross~\cite{Ross67}.
#(1.111) and (1.112) from Langacker~\cite{Langacker69}.
#(1.113) and (1.114) are adapted from Chiba~\cite{Chiba71}.
#(5.2) ???
#(8.1) == (10.1) ???
#(10.2)-(10.4) ??? or ours
#(10.5)-(10.11) are from Lees and Klima~\cite{LeesKlima63}.
#(11.12) ???
#(11.16)-(11.25) are from Bresnan~\cite{Bresnan71}.
#(11.26) and (11.27) are from Evans~\cite{Evans77}.
#(11.28)-(11.36) more Evans?
#(12.2)-(12.13) ??? or ours
#(13.2) is from Grinder~\cite{Grinder71}.
#(13.5)-(13.11) are from Grinder~\cite{Grinder71}.
#(13.12)-(13.22) more Grinder or ???
################################################################

example_dict = {
"1.1":
 ["The boy who was fooling her kissed the girl who loved him.",
  ["S",
   "boy",
   ["S", "boy", "her"],
   "girl",
   ["S", "girl", "him"]]],
"1.2":
 ["*John killed herself.",
  ["S", "John", "herself"]],
"1.4":
 ["Some students think they are smarter than they are.",
  ["S", "students", "they", "they"]],
"1.6":
 ["My uncle has never ridden a camel but his brother has, although it was lame.",
  ["C",
   ["S", "my", "uncle", "camel"],
   ["S", "his", "brother", "camel"],
   ["S", "it"]]],
"1.10":
 ["I like the fresh candy better than the stale PHI.",
  ["S", "I", "candy", "PHI"]],
"1.11":
 ["If John can, he will do it.",
  ["C",
   ["S", "John"],
   ["S", "he"]]],
"1.12":
 ["If he can, John will do it.",
  ["C",
   ["S", "he"],
   ["S", "John"]]],
"1.13":
 ["John will do it if he can.",
  ["C",
   ["S", "John"],
   ["S", "he"]]],
"1.14":
 ["He will do it if John can.",
  ["C",
   ["S", "he"],
   ["S", "John"]]],
"1.24":
 ["I have a cat at home, but hate it.",
  ["C",
   ["S", "I", "cat", "home"],
   ["S", "PHI", "it"]]],
"1.25":
 ["I want to get a cat for myself.",
  ["S", "I", ["S", "PHI", "cat", "myself"]]],
"1.27":
 ["The men took off their hats.",
  ["S", "men", "their", "hats"]],
"1.51":
 ["The man who lives next door said that he would mow my lawn.",
  ["S",
   "man",
   ["S", "man"],
   ["S", "he", "my", "lawn"]]],
"1.52":
 ["Somebody seduced Bill's sister, but no one will ever seduce Jack’s and she knows it.",
  ["C",
   ["S", "somebody", "Bill's", "sister"],
   ["S", "somebody", "Jack's", "PHI"],
   ["S", "she"]]],
"1.66":
 ["Realizing that he was unpopular didn't disturb Oscar.",
  ["S",
   ["S", "PHI", ["S", "he"]],
   "Oscar"]],
"1.70":
 ["My neighbor who is pregnant said that she was very happy.",
  ["S",
   "my",
   "neighbor",
   ["S", "neighbor"],
   ["S", "she"]]],
"1.74":
 ["The pilot who shot at it hit the Mig that chased him.",
  ["S",
   "pilot",
   ["S", "pilot", "it"],
   "Mig",
   ["S", "Mig", "him"]]],
"1.86":
 ["The mosquito which bit Algernon was killed by him.",
  ["S",
   "mosquito",
   ["S", "mosquito", "Algernon"],
   "him"]],
"1.87":
 ["The mosquito which bit him was killed by Algernon.",
  ["S",
   "mosquito",
   ["S", "mosquito", "him"],
   "Algernon"]],
"1.88":
 ["Algernon killed the mosquito which bit him.",
  ["S",
   "Algernon",
   "mosquito",
   ["S", "mosquito", "him"]]],
"1.89":
 ["He killed the mosquito which bit Algernon.",
  ["S",
   "he",
   "mosquito",
   ["S", "mosquito", "Algernon"]]],
"1.91":
 ["After John Adams woke up, he was hungry.",
  ["C",
   ["S", "John"],
   ["S", "he"]]],
"1.92":
 ["That Oscar was unpopular didn't disturb him.",
  ["S",
   ["S", "Oscar"],
   "him"]],
"1.93":
 ["For your brother to refuse to pay taxes would get him into trouble.",
  ["C",
   ["S", "your", "brother", ["S", "PHI"]],
   ["S", "him", "trouble"]]],
"1.94":
 ["Anna's complaining about Peter infuriated him.",
  ["S",
   ["S", "Anna's", "complaining", "Peter"],
   "him"]],
"1.95":
 ["The possibility that Fred will be unpopular doesn’t bother him.",
  ["S",
   "possibility",
   ["S", "Fred"],
   "him"]],
"1.96":
 ["After he woke up, John Adams was hungry.",
  ["C",
   ["S", "he"],
   ["S", "John"]]],
"1.97":
 ["That he was unpopular didn't disturb Oscar.",
  ["S",
   ["S", "he"],
   "Oscar"]],
"1.98":
 ["For him to refuse to pay taxes would get your brother into trouble.",
  ["C",
   ["S", "him", ["S", "PHI", "taxes"]],
   ["S", "your", "brother", "trouble"]]],
"1.99":
 ["Anna's complaining about him infuriated Peter.",
  ["S",
   ["S", "Anna's", "complaining", "him"],
   "Peter"]],
"1.100":
 ["The possibility that he will be unpopular doesn’t bother Fred.",
  ["S",
   "possibility",
   ["S", "he"],
   "Fred"]],
"1.101":
 ["John Adams was hungry after he woke up.",
  ["C",
   ["S", "John"],
   ["S", "he"]]],
"1.102":
 ["Oscar wasn't disturbed that he was unpopular.",
  ["S",
   "Oscar",
   ["S", "he"]]],
"1.103":
 ["It would get your brother into trouble for him to refuse to pay taxes.",
  ["S",
   ["S", "your", "brother", "trouble"],
   ["S", "him", ["S", "PHI", "taxes"]]]],
"1.104":
 ["Peter was infuriated at Anna's complaining about him.",
  ["S",
   "Peter",
   ["S", "Anna's", "complaining", "him"]]],
"1.105":
 ["Fred isn't bothered by the possibility that he will be unpopular.",
  ["S",
   "Fred",
   "possibility",
   ["S", "he"]]],
"1.106":
 ["*He was hungry after John Adams woke up.",
  ["S",
   "he",
   ["S", "John"]]],
"1.107":
 ["*He wasn't disturbed that Oscar was unpopular.",
  ["S",
   "he",
   ["S", "Oscar"]]],
"1.108":
 ["*It would get him into trouble for your brother to refuse to pay taxes.",
  ["C",
   ["S", "him", "trouble"],
   ["S", "your", "brother", ["S", "PHI", "taxes"]]]],
"1.109":
 ["*He was infuriated at Anna's complaining about Peter.",
  ["S",
   "he",
   ["S", "Anna's", "complaining", "Peter"]]],
"1.110":
 ["*He isn't bothered by the possibility that Fred will be unpopular.",
  ["S",
   "he",
   "possibility",
   ["S", "Fred"]]],
"1.111":
 ["Penelope cursed Peter and slandered him.",
  ["C",
   ["S", "Penelope", "Peter"],
   ["S", "PHI", "him"]]],
"1.112":
 ["*Penelope cursed him and slandered Peter.",
  ["C",
   ["S", "Penelope", "him"],
   ["S", "PHI", "Peter"]]],
"1.113":
 ["The interest in visiting Las Vegas that Mary displayed is typical of gamblers.",
  ["S",
   "interest",
   ["S", "PHI1", "Las Vegas"],
   ["S", "Mary", "PHI2"],
   "gamblers"]],
"5.2":
 ["June hates flowers, but she waters them anyway.",
  ["C",
   ["S", "June", "flowers"],
   ["S", "she", "them"]]],
"8.1":
 ["John wants to give June a present, but he isn't sure she’ll like it.",
  ["C",
   ["S", "John", ["S", "PHI", "June", "present"]],
   ["S", "he", ["S", "she", "it"]]]],
"10.1":
 ["John wants to give June a present, but he isn't sure she’ll like it.",
  ["C",
   ["S", "John", ["S", "PHI", "June", "present"]],
   ["S", "he", ["S", "she", "it"]]]],
"10.2":
 ["Janet saw herself.",
  ["S", "Janet", "herself"]],
"10.3":
 ["Janet saw her.",
  ["S", "Janet", "her"]],
"10.4":
 ["*Janet saw himself.",
  ["S", "Janet", "himself"]],
"10.5":
 ["The men threw a smokescreen around themselves.",
  ["S", "men", "smokescreen", "themselves"]],
"10.6":
 ["The men found a smokescreen around them.",
  ["S", "men", "smokescreen", "them"]],
"10.7":
 ["The men found a smokescreen to be around them.",
  ["S",
   "men",
   ["S", "smokescreen", "them"]]],
"10.8":
 ["The men found a smokescreen and it was around them.",
  ["C",
   ["S", "men", "smokescreen"],
   ["S", "it", "them"]]],
"10.9":
 ["I told John to protect himself.",
  ["S",
   "I",
   "John",
   ["S", "PHI", "himself"]]],
"10.10":
 ["I told John to protect me.",
  ["S",
   "I",
   "John",
   ["S", "PHI", "me"]]],
"10.11":
 ["I told John to protect myself.",
  ["S",
   "I",
   "John",
   ["S", "PHI", "myself"]]],
"11.12":
 ["Jack's house burned down, but he rebuilt it.",
  ["C",
   ["S", "Jack's", "house"],
   ["S", "he", "it"]]],
"11.26":
 ["John owns some sheep and Harry vaccinates them.",
  ["C",
   ["S", "John", "sheep"],
   ["S", "Harry", "them"]]],
"11.27":
 ["Mary danced with many boys and they found her interesting.",
  ["C",
   ["S", "Mary", "boys"],
   ["S", "they", "her"]]],
"11.28":
 ["John lost a pen yesterday and Bill found one today.",
  ["C",
   ["S", "John", "pen"],
   ["S", "Bill", "one"]]],
"11.29":
 ["John claimed to have found the solution to the problem, but Bill was sure he had found it.",
  ["C",
   ["S", "John", ["S", "PHI", "solution", "problem"]],
   ["S", "Bill", ["S", "he", "it"]]]],
"11.30":
 ["John wants to catch a fish and eat it for supper.",
  ["S",
   "John",
   ["C",
    ["S", "PHI1", "fish"],
    ["S", "PHI2", "it", "supper"]]]],
"11.31":
 ["No one would put the blame on himself.",
  ["S",
   "one",
   ["S", "PHI", "blame", "himself"]]],
"11.32":
 ["Sue told Sandy about herself.",
  ["S",
   "Sue",
   "Sandy",
   "herself"]],
"11.33":
 ["*Jill kept talking about himself.",
  ["S",
   "Jill",
   "himself"]],
"11.34":
 ["Does Jack's making a pig of himself bother Bill?",
  ["S",
   ["S", "Jack's", "pig", "himself"],
   "Bill"]],
"11.35":
 ["John wants to give June a present, but he is afraid she won’t like it.",
  ["C",
   ["S", "John", ["S", "PHI", "June", "present"]],
   ["S", "he", ["S", "she", "it"]]]],
"11.36":
 ["Ernie doesn't like Bernie, because he is such an asshole.",
  ["C",
   ["S", "Ernie", "Bernie"],
   ["S", "he", "asshole"]]],
"12.2":
 ["Mary's father killed himself.",
  ["S", "Mary's", "father", "himself"]],
"12.3":
 ["*Mary's father killed him.",
  ["S", "Mary's", "father", "him"]],
"12.4":
 ["*Mary's father killed herself.",
  ["S", "Mary's", "father", "herself"]],
"12.5":
 ["Mary's father killed her.",
  ["S", "Mary's", "father", "her"]],
"12.6":
 ["The father of Mary killed himself.",
  ["S", "father", "Mary", "himself"]],
"12.7":
 ["*The father of Mary killed him.",
  ["S", "father", "Mary", "him"]],
"12.8":
 ["*The father of Mary killed herself.",
  ["S", "father", "Mary", "herself"]],
"12.9":
 ["The father of Mary killed her.",
  ["S", "father", "Mary", "her"]],
"12.11":
 ["Mary's mother cooks only for herself.",
  ["S", "Mary's", "mother", "herself"]],
"12.12":
 ["Mary's mother cooks only for her.",
  ["S", "Mary's", "mother", "her"]],
"12.13":
 ["Mary's mother cooks only for her mother.",
  ["S", "Mary's", "mother1", "her", "mother2"]],
"13.2":
 ["It was difficult to sketch myself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "myself"]]]],
"13.5a":
 ["It was difficult for me to sketch myself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "me", "myself"]]]],
"13.6a":
 ["It was difficult for you to sketch yourself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "you", "yourself"]]]],
"13.7a":
 ["It was difficult for him to sketch himself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "him", "himself"]]]],
"13.8a":
 ["It was difficult for her to sketch herself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "her", "herself"]]]],
"13.9a":
 ["It was difficult for us to sketch ourselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "us", "ourselves"]]]],
"13.10a":
 ["It was difficult for you to sketch yourselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "you", "yourselves"]]]],
"13.11a":
 ["It was difficult for them to sketch themselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "them", "themselves"]]]],
"13.5b":
 ["It was difficult to sketch myself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "myself"]]]],
"13.6b":
 ["It was difficult to sketch yourself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "yourself"]]]],
"13.7b":
 ["*It was difficult to sketch himself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "himself"]]]],
"13.8b":
 ["*It was difficult to sketch herself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "herself"]]]],
"13.9b":
 ["It was difficult to sketch ourselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "ourselves"]]]],
"13.10b":
 ["It was difficult to sketch yourselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "yourselves"]]]],
"13.11b":
 ["*It was difficult to sketch themselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "themselves"]]]],
"13.12a":
 ["Nurse Bob Breezy gave up drawing.",
  ["C", ["S", "I0", "you0"], ["S", "Bob"]]],
"13.12b":
 ["[Bob] It was difficult to sketch himself.",
  ["C", ["S", "I0", "you0", "Bob"], ["S", ["S", "PHI", "himself"]]]],
"13.13a":
 ["Astronaut Linda Smith gave up drawing.",
  ["C", ["S", "I0", "you0"], ["S", "Linda"]]],
"13.13b":
 ["[Linda] It was difficult to sketch herself.",
  ["C", ["S", "I0", "you0", "Linda"], ["S", ["S", "PHI", "herself"]]]],
"13.14a":
 ["The bank embezzlers gave up drawing.",
  ["C", ["S", "I0", "you0"], ["S", "embezzlers"]]],
"13.14b":
 ["[the bank embezzlers] It was difficult to sketch themselves.",
  ["C", ["S", "I0", "you0", "embezzlers"], ["S", ["S", "PHI", "themselves"]]]],
"13.15":
 ["*It was difficult to sketch himself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "himself"]]]],
"13.16":
 ["*It was difficult to sketch herself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "herself"]]]],
"13.17":
 ["*It was difficult to sketch themselves.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "themselves"]]]],
"13.18":
 ["[Bob] It was difficult to sketch himself.",
  ["C", ["S", "I0", "you0", "Bob"], ["S", ["S", "PHI", "himself"]]]],
"13.19":
 ["[Linda] It was difficult to sketch herself.",
  ["C", ["S", "I0", "you0", "Linda"], ["S", ["S", "PHI", "herself"]]]],
"13.20":
 ["[the bank embezzlers] It was difficult to sketch themselves.",
  ["C", ["S", "I0", "you0", "embezzlers"], ["S", ["S", "PHI", "themselves"]]]],
"13.21":
 ["It was difficult to sketch myself.",
  ["C", ["S", "I0", "you0"], ["S", ["S", "PHI", "myself"]]]],
"13.22":
 ["[toy] Give me that!",
  ["C", ["S", "I0", "you0", "toy"], ["S", "PHI", "me", "that"]]]
}
"""Dictionary mapping example identifiers to pairs of [sentence,
parse_tree], where sentences test various pronoun binding
scenarios."""

def example(number: str) -> list:
    """Retrieves a specific example sentence and its parse tree
    from example_dict.
    
    Args:
        number (str): Example identifier (e.g. "1.1", "10.2")
    Returns:
        list: [sentence, parse_tree]
    """
    return example_dict[number]
