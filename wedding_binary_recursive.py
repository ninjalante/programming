#put movies in a different file and import them here
import wedding_movies as wm

root_q = wm.Question("\nAre you looking for a movie with a male or female protagonist?\nA) male\nB) female\nC) both!\n", 'Let\'s find a movie')
ensemble = wm.Question("\nAre you looking for\nA) A single pair of protagonists\nB) An ensemble cast\n", 'No gender preference')
male_protag = wm.Question("\nGot it. Do you want something that's family-friendly, or not at all family-friendly?\nA) family-friendly please!\nB) as unfamily-unfriendly as you've got, thank you\n", 'Male protagonist')
m_f_f = wm.Question("\nWould you prefer a classic movie that might be in black & white, or something more modern?\nA) classic\nB) modern\n", 'Family-friendly')
classic = wm.Question("\nHow do you feel about musicals?\nA) love them\nB) not feeling one right now\n", 'Classic')
m_not_f_f = wm.Question("\nKids shouldn't be allowed to go to weddings anyway.\nDo you want...\nA) a buddy comedy\nB) something else\n", 'Adults only')
buddy = wm.Question("\nThere's some good buddy comedies. We can narrow this down pretty quickly. Do you want...\nA) a movie filled with actors who are easily recognized from their many roles on TV\nB) a story with actors who are a bit older but your mom knows who they are, and they're still funny\n", "A buddy comedy")
young_folks = wm.Question("\nGot it. Are you a fan of Ed Helms?\nA) YES INDEED\nB) Not so much\n", 'TV-friendly faces')
ed_helms = wm.Question("\nThe kids aren't there. So. How raunchy do you want it?\nA) as raunchy as possible\nB) I would prefer my raunch on the side, thank you\n ", 'Ed Helms')
crash = wm.Question("\nHmm. I've only got two movies left. I guess...the real question is...do you want to watch something you've probably already seen, or something that you slept on?\nA) give me what I came here expecting\nB) give me something new\n", 'A Buddy Comedy That Doesn\'t Have Ed Helms')
sandler = wm.Question("\nDo you like Adam Sandler?\nA) Love Adam Sandler\nB) Who?\n", 'Not a buddy comedy')
nineties = wm.Question("\nWow, really? Huh. Okay. Then, uh...\nA) 1990s Adam Sandler\nB) 2010s Adam Sandler?\n", 'I Stan-dler Adam Sandler')
mature_sandler = wm.Question("\nAmazingly, you've got two options. Do you want to see Adam Sandler...\nA) At like a mature and concerned father\nB) Act like an immature and unconcerned father\n", "2010s Adam Sandler")
timeline = wm.Question("\nAre you a fan of time loops and alternate timelines?\nA) yes\nB) no\n", 'Not  A-damn Sandler')
time = wm.Question("\nTime stuff, excellent.\nA) a time loop a la Groundhog Day?\nB) alternate timelines a la Sliding Doors?\n", 'Timeline wackiness')
stiller = wm.Question("\nWho do you prefer as a leading man?\nA) Ben Stiller\nB) Ryan Reynolds\n", 'Normal time stuff please')
female_protag = wm.Question("\nFemale leads it is.\nDo you want...\nA) a family-friendly movie\nB) something naughty for me and the girls\n", 'Female protagonist')
f_f_f = wm.Question("\nCool. You have some good options.\nAre you looking for...\nA) something nostalgic\nB) something fresh and new!\n", 'Family-friendly')
nostalgic = wm.Question("\nDo you want a lot of singing and dancing?\nA) Yes! A musical!\nB) Not my thing\n", 'Something nostalgic')
body_swap = wm.Question("\nDo you enjoy the whimsical magic of a body swap?\nA) Body swap magic please\nB) No thanks, I just want a good wedding\n", 'No singing')
f_not_f_f = wm.Question("\nGreat, that will make it easier. You've got some very different options, so let's narrow it down. Do you want...\nA) a story with interesting characters and conflicts\nB) a story with unnecessary amounts of GLAMOUR and DRAMA\n", 'Something just for me and the girls')
substance = wm.Question("\nI don't mean to assume, but most wedding movies aren't exactly...thought-provoking. Do you want a movie that...\nA) is easy-breezy and full of shenanigans\nB) introduces complicated characters and difficult situations\n", "Character and conflict")
wedding = wm.Question("\nPerfect! One question left. Choose your leading man.\nA) Matthew McConaghey\nB) James Marsden\nC) Neither\n", "Easy breezy shenanigans")
drama = wm.Question("\nDo you want to indulge in some really obscene opulance?\nA) Yes, smother me with capitalist fantasy\nB) No, I want to be reminded how poor I am\n", "Here for the drama")
obscene = wm.Question("\nLast question. Are you...\nA) a Carrie\nB) a Samantha\nC) a Miranda\nD) a Charlotte\n", "Obscene capitalist fantasy please")
nostalgic_or_modern = wm.Question("\nI've got some ideas. Do you want...\nA) a nostalgic classic\nB) something more modern\n", "Two protagonists")
cynical = wm.Question("\nAlmost done! Are you feeling...\nA) a somewhat cynical, but ultimately sweet, and certainly more realistic, look at new relationships\nB) 100% bonkers fairy tale\n", "Something new")
cringe = wm.Question("\nI think I've got something for you, but tell me, do you like extremely relevant cringe comedy?\nA) no thank you\nB) BRING ON THE CRINGE!\n", "More realistic")
how_realistic = wm.Question("\nLow cringe, ok. But like, HOW realistic?\nA) Mostly real\nB) I wouldn't mind some timeline wackiness\n", "No cringe please")
hidden_gem = wm.Question("\nI think I've got it. Tell me one more thing...\nA) I want an instantly recognizable classic\nB) I want a hidden gem that I can impress my snootier friends with\n", "Ensemble cast")
italian_or_indian = wm.Question("\nThis last question should be easy. You're about to watch a wedding movie with your friends or family. What take-out do you get?\nA) Italian\nB) Indian\n", "Something new")

#here's all the babies

root_q.a = male_protag
root_q.b = female_protag
root_q.c = ensemble
ensemble.a = nostalgic_or_modern
ensemble.b = hidden_gem
hidden_gem.a = wm.four_ws_1f
hidden_gem.a.name = "Something classic"
hidden_gem.b = wm.monsoon
hidden_gem.b.name = "Something lesser-known"
nostalgic_or_modern.a = wm.princess
nostalgic_or_modern.b = cynical
cynical.a = cringe
cringe.a = how_realistic
how_realistic.a = wm.destination
how_realistic.a.name = "Mostly realistic"
how_realistic.b = wm.palm_springs
how_realistic.b.name = "I'm okay with some wackiness"
cringe.b = wm.you_people
cringe.b.name = "I want to curl into a ball from cringing so hard"
cynical.b = wm.marry_me
cynical.b.name = "A love story so unbelievable that I can't help but enjoy it"
female_protag.a = f_f_f
f_f_f.a = nostalgic
f_f_f.b = italian_or_indian
italian_or_indian.a = wm.royal_treat
italian_or_indian.a.name = 'Italian food'
italian_or_indian.b = wm.wedding_season
italian_or_indian.b.name = 'Indian food'
female_protag.b = f_not_f_f
f_not_f_f.a = substance
f_not_f_f.b = drama
substance.a = wedding
substance.b = wm.rachel
substance.b.name = 'Something with substance'
drama.a = obscene
drama.b = wm.bridesmaids
drama.b.name = "Help me, I'm poor"
obscene.a = wm.satc
obscene.a.name = "such a Carrie"
obscene.b = wm.satc
obscene.b.name = "100% Samantha"
obscene.c = wm.satc
obscene.c.name = "totally Miranda"
obscene.d = wm.crazy_rich_a
obscene.d.name = "a real Charlotte"
wedding.a = wm.wedding_planner
wedding.a.name = 'McConaghey'
wedding.b = wm.dresses27
wedding.b.name = "Marsden"
wedding.c = wm.muriels
wedding.c.name = "I don't care about a leading man, I'm here for Toni Collette"
nostalgic.a = wm.mamma_mia
nostalgic.a.name = 'A musical extravaganza'
nostalgic.b = body_swap
body_swap.a = wm.freaky_friday
body_swap.a.name = 'Body swap hijinks'
body_swap.b = wm.bfgw
body_swap.b.name = 'I want a wedding that\'s a good time'
male_protag.a = m_f_f
male_protag.b = m_not_f_f
m_f_f.a = classic
classic.a = wm.seven_brides
classic.a.name = 'Musical'
classic.b = wm.one_night
classic.b.name = 'Not a musical'
m_f_f.b = wm.father_bride
m_f_f.b.name = 'Modern'
m_not_f_f.a = buddy
buddy.a = young_folks
young_folks.a = ed_helms
young_folks.b = crash
buddy.b = wm.in_laws
buddy.b.name = 'Older actors can still be buddies'
ed_helms.a = wm.hangover
ed_helms.a.name = 'Extra raunchy'
ed_helms.b = wm.tag
ed_helms.b.name = 'Raunch on the side'
crash.a = wm.crashers
crash.a.name = "I'm specifically here so someone will tell me that it's okay to watch Wedding Crashers again"
crash.b = wm.love_you_man
crash.b.name = 'Paul Rudd is People\'s Sexiest Man Alive 2021'
m_not_f_f.b = sandler
sandler.a = nineties
nineties.a = wm.wedding_singer
nineties.a.name = '90s Adam Sandler'
nineties.b = mature_sandler
mature_sandler.a = wm.week_of
mature_sandler.a.name = "A mature Adam Sandler"
mature_sandler.b = wm.my_boy
mature_sandler.b.name = "An immature Adam Sandler"
sandler.b = timeline
timeline.a = time
time.a = wm.naked
time.a.name = 'Groundhog Day-esque'
time.b = wm.repeat
time.b.name = 'Sliding Doors-esque'
timeline.b = stiller
stiller.a = wm.parents
stiller.a.name = 'Ben Stiller'
stiller.b = wm.proposal
stiller.b.name = 'Ryan Reynolds'


#helper functions
def print_deets(movie):
  return movie.value.upper() + "\n" + movie.deets["summary"] + "\nRated " + movie.deets["rated"]

def reveal_movie(movie, choice_path):
  print("\nI HAVE THE PERFECT MOVIE FOR YOU!\n")
  for each in choice_path:
    print(each + " --> ")
  print(print_deets(movie))
  return "Enjoy your movie!\n"
#make a function that asks the questions

def find_a_movie(movie_tree, path=[]):
  #base case
  #if movie_tree is a Wedding_Movie
  if isinstance(movie_tree, wm.Wedding_Movie):
    return reveal_movie(movie_tree, path)
  #recursive case
  answer = movie_tree.get_input()
  if not hasattr(movie_tree, answer):
    print("\nPlease enter a valid choice!\n")
    answer = movie_tree.get_input()
  if answer.upper() == 'A':
    path += [movie_tree.a.name]
    movie_tree = movie_tree.a
    return find_a_movie(movie_tree, path)
  if answer.upper() == 'B':
    path += [movie_tree.b.name]
    movie_tree = movie_tree.b
    return find_a_movie(movie_tree, path)
  if answer.upper() == 'C':
    path += [movie_tree.c.name]
    movie_tree = movie_tree.c
    return find_a_movie(movie_tree, path)
  if answer.upper() == 'D':
    path += [movie_tree.d.name]
    movie_tree = movie_tree.d
    return find_a_movie(movie_tree, path)
  

start = input('Are you ready for wedding season?\n')
while start.upper() == 'YES': 
  test = find_a_movie(root_q, path=[])
  print(test)
  start = input('Do you want to find another movie?\n')
print("Bye bye!")

  
