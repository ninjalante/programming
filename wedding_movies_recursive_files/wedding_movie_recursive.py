#put movies in a different file and import them here
import wedding_movies as wm

root_q = wm.Question("\nAre you looking for a movie with a male or female protagonist?\nA) male\nB) female\nC) both!\n", 'Let\'s find a movie')
ensemble = wm.Question("\nAre you looking for\nA) A single pair of protagonists\nB) An ensemble cast\n", 'No gender preference')
male_protag = wm.Question("\nGot it. Do you want something that's family-friendly, or not at all family-friendly?\nA) family-friendly please!\nB) as unfamily-unfriendly as you've got, thank you\n", 'Male protagonist')
m_f_f = wm.Question("\nWould you prefer a classic movie that might be in black & white, or something more modern?\nA) classic\nB) modern\n", 'Family-friendly')
classic = wm.Question("\nHow do you feel about musicals?\nA) love them\nB) not feeling one right now\n", 'Classic')
m_not_f_f = wm.Question("\nKids shouldn't be allowed to go to weddings anyway.\nDo you want...\nA) a buddy comedy\nB) something else\n", 'Adults only')
buddy = wm.Question("\nThere's some good buddy comedies. We can narrow this down pretty quickly. Do you want...\nA) a movie headlined by recognizable actors\nB) a story with actors who are a bit older but your mom knows who they are, and they're still funny\n", "A buddy comedy")
young_folks = wm.Question("\nGot it. Are you a fan of Ed Helms?\nA) YES INDEED\nB) Not so much\n", 'TV-friendly faces')
ed_helms = wm.Question("\nThe kids aren't there. So. How raunchy do you want it?\nA) as raunchy as possible\nB) I would prefer my raunch on the side, thank you\n ", 'Ed Helms')
crash = wm.Question("\nHmm. I've only got two movies left. I guess...the real question is...do you want to watch something you've probably already seen, or something that you slept on?\nA) give me what I came here expecting\nB) give me something new\nC) give me something amazing\n", 'A Buddy Comedy That Doesn\'t Have Ed Helms')
sandler = wm.Question("\nDo you like Adam Sandler?\nA) Love Adam Sandler\nB) Who?\n", 'Not a buddy comedy')
nineties = wm.Question("\nWow, really? Huh. Okay. Then, uh...\nA) 1990s Adam Sandler\nB) 2010s Adam Sandler?\n", 'I Stan-dler Adam Sandler')
mature_sandler = wm.Question("\nAmazingly, you've got two options. Do you want to see Adam Sandler...\nA) Act like a mature and concerned father\nB) Act like an immature and unconcerned father\n", "2010s Adam Sandler")
timeline = wm.Question("\nAre you a fan of time loops and alternate timelines?\nA) yes\nB) no\n", 'Not  A-damn Sandler')
time = wm.Question("\nTime stuff, excellent.\nA) a time loop a la Groundhog Day?\nB) alternate timelines a la Sliding Doors?\n", 'Timeline wackiness')
stiller = wm.Question("\nWho do you prefer as a leading man?\nA) Ben Stiller\nB) Ryan Reynolds\nC) Patrick Dempsey\n", 'Normal time stuff please')
female_protag = wm.Question("\nFemale leads it is.\nDo you want...\nA) a family-friendly movie\nB) something naughty for me and the girls\n", 'Female protagonist')
f_f_f = wm.Question("\nCool. You have some good options.\nAre you looking for...\nA) something nostalgic\nB) something fresh and new!\n", 'Family-friendly')
nostalgic = wm.Question("\nDo you want a lot of singing and dancing?\nA) Yes! A musical!\nB) Not my thing\n", 'Something nostalgic')
body_swap = wm.Question("\nDo you enjoy the whimsical magic of a body swap?\nA) Body swap magic please\nB) No thanks, I just want a good wedding\n", 'No singing')
f_not_f_f = wm.Question("\nGreat, that will make it easier. You've got some very different options, so let's narrow it down. Do you want...\nA) complicated characters and difficult situations\nB) easy-to-consume motivations I won't have to think about much\n", 'Not family-friendly')
substance = wm.Question("\nBut, like, how complicated and how difficult?\nA) Really dramatic. I want it to hurt\nB) Eh. It can have a side of fun\n", "Something with substance")
drama = wm.Question("\nWhich of these storylines appeals to you more?\nA) A recovering addict seeing her family for the first time in years\n B) Former high school classmates seeing each other for the first time in years\n", "Drama-rama")
##
more_fun = wm.Question("\nDo you want to hate the protagonist?\nA) Yes. I want to yell at the TV\nB) Of course not\n", "More fun")
##

romp = wm.Question("\nThis one is tricky: do you want a rom com or a *romp* com?\nA) A rom com. Straight up\nB) What's a romp com\n", "A likable, relatable protagonist")
easy_to_consume = wm.Question("\nI don't blame you. Do you want...\nA) Something you probably watched on a plane 15 years ago\nB) Something that's probably new to you\n", "Easy to consume")
##
plane15 = wm.Question("\nLast thing! Pick your preferred leading man.\n A) Matthew McConaghey\nB) James Marsden\nC) Dermot Mulroney. Wait, how'd he get in here?\n", "Watched on a plane 15 years ago")
##
new2you = wm.Question("How do you feel about meddling moms?\nA) Oooh, yass! I can totally identify with that\nB) No, thanks. Don't remind me", "New to me") 
laugh_sweet = wm.Question("One more question. Do you want a movie that's...\nA) Laugh-out-loud outrageous\nB) Sweet and comforting\n", "No meddling moms")
meddling_moms = wm.Question("Pick an Oscar-winner/feminist icon, and you're done\nA) Jane Fonda\n B) Diane Keaton\n", "Moms meddle")
hate = wm.Question("\nLast question. Are you...\nA) a Carrie\nB) a Samantha\nC) a Miranda\nD) a Charlotte\n", "An unlikable and irredeemable protagonist")
rom_com = wm.Question("\nLast question. How much do you want to indulge in obscene displays of capitalist consumerism?\nA) Yes! All the THINGS please\nB) No. Eat the rich", "A romp com isn't a thing",)
stop_motion = wm.Question("\nFirst question! Do you want...\nA) a whimsical stop-motion piece that's fun for the whole family\nB) literally anything else\n", "One couple")
nostalgic_or_modern = wm.Question("\nI've got some ideas. Do you want...\nA) a nostalgic classic\nB) something more modern\n", "Live-action")
cynical = wm.Question("\nAlmost done! Are you feeling...\nA) a somewhat cynical, but ultimately sweet, and certainly more realistic, look at new relationships\nB) 100% bonkers fairy tale\n", "Something new")
fairy_tale = wm.Question("\nEvery fairy tale has a princess. Who's the perfect princess?\nA) J. Lo, obviously\nB) Someone else\n", "A 100% bonkers fairy tale")
not_j_lo = wm.Question("\nAll right, no J. Lo. How about...\nA) Julia Roberts\nB) Anne Hathaway\nC) Ginnifer Goodwin\n", "I would have gone with J. Lo")
j_lo = wm.Question("\nOne more question! What kind of J.Lo do you need today?\nA) An adventurous and kick-ass one\nB) An emotionally complex and kick-ass one\n", "100% bonkers fairy tale")
cringe = wm.Question("\nI think I've got something for you, but tell me, do you like extremely relevant cringe comedy?\nA) nothankyou\nB) BRING ON THE CRINGE!\n", "More realistic")

how_realistic = wm.Question("\nLow cringe, ok. But like, HOW realistic?\nA) Mostly real\nB) I wouldn't mind some timeline wackiness\n", "No cringe please")
baggage = wm.Question("\nWhat kind of couple appeals to you most?\nA) Exes with baggage\nB) Strangers with baggage\nC) Siblings with baggage\nD) Friends with no baggage, really!\n", "Mostly realistic")

hidden_gem = wm.Question("\nI think I've got it. Tell me one more thing...\nA) I want an instantly recognizable classic\nB) I want a hidden gem that I can impress my snootier friends with\nC) I want something I'm not expecting\n", "Ensemble cast")
italian_or_indian = wm.Question("\nThis last question should be easy. You're about to watch a wedding movie with your friends or family. What take-out do you get?\nA) Italian\nB) Indian\n", "Something new")

#here's all the babies

root_q.a = male_protag
root_q.b = female_protag
root_q.c = ensemble

ensemble.a = stop_motion
stop_motion.a = wm.corpse_bride
stop_motion.a.name = "A whimsical stop-motion film"
stop_motion.b = nostalgic_or_modern

ensemble.b = hidden_gem
hidden_gem.a = wm.four_ws_1f
hidden_gem.a.name = "Something classic"
hidden_gem.b = wm.monsoon
hidden_gem.b.name = "Something lesser-known"
hidden_gem.c = wm.best_man
hidden_gem.c.name = "Something I'm not expecting"

nostalgic_or_modern.a = wm.princess
wm.princess.name = "A nostalgic classic"
nostalgic_or_modern.b = cynical
cynical.a = cringe
cringe.a = how_realistic

how_realistic.a = baggage
how_realistic.b = wm.palm_springs
how_realistic.b.name = "I'm okay with some wackiness"
baggage.a = wm.ticket2paradise
baggage.a.name = "Exes with baggage"
baggage.b = wm.destination
baggage.b.name = "Strangers with baggage"
baggage.c = wm.people_we_hate
baggage.c.name = "Siblings with baggage"
baggage.d = wm.plus_one
baggage.d.name = "Friends with no baggage...really"
cringe.b = wm.you_people
cringe.b.name = "I want to curl into a ball from cringing so hard"
cynical.b = fairy_tale
fairy_tale.a = j_lo
fairy_tale.b = not_j_lo
not_j_lo.a = wm.runaway
not_j_lo.a.name = "Julia Roberts"
not_j_lo.b = wm.bride_wars
not_j_lo.b.name = "Anne Hathaway"
not_j_lo.c = wm.something_borrowed
not_j_lo.c.name = "Ginnifer Goodwin"
j_lo.a = wm.shotgun
j_lo.a.name = "Kick-ass J.Lo"
j_lo.b = wm.marry_me
j_lo.b.name = "Kick-ass J.Lo"
female_protag.a = f_f_f
f_f_f.a = nostalgic
f_f_f.b = italian_or_indian
italian_or_indian.a = wm.royal_treat
italian_or_indian.a.name = 'Italian food'
italian_or_indian.b = wm.wedding_season
italian_or_indian.b.name = 'Indian food'
female_protag.b = f_not_f_f
f_not_f_f.a = substance
f_not_f_f.b = easy_to_consume
easy_to_consume.a = plane15
easy_to_consume.b = new2you
new2you.a = meddling_moms
meddling_moms.a = wm.monster
meddling_moms.a.name = "Jane Fonda was right"
meddling_moms.b = wm.because
meddling_moms.b.name = "Diane Keaton still rules"
new2you.b = laugh_sweet
laugh_sweet.a = wm.rough_night
laugh_sweet.a.name = "Laugh-out-loud outrageous"
laugh_sweet.b = wm.muriels
laugh_sweet.b.name = "Sweet and comforting"
###
substance.a = drama
drama.a = wm.rachel
drama.a.name = "Recovering alcoholic"
drama.b = wm.bachelorette
drama.b.name = "Recovering high schoolers"
substance.b = more_fun
more_fun.a = hate
more_fun.b = romp
hate.a = wm.best_friends
hate.a.name = "such a Carrie"
hate.b = wm.satc
hate.b.name = "100% Samantha"
hate.c = wm.satc
hate.c.name = "totally Miranda"
hate.d = wm.satc
hate.d.name = "a real Charlotte"
romp.a = rom_com
rom_com.a = wm.crazy_rich_a
rom_com.a.name = "I want to be rich and fancy and not worry about anything or anyone"
rom_com.b = wm.bridesmaids
rom_com.b.name = "Help me I'm poor"
romp.b = wm.polite_society
romp.b.name = "Let's romp it up!"
plane15.a = wm.wedding_planner
plane15.a.name = 'McConaghey'
plane15.b = wm.dresses27
plane15.b.name = "Marsden"
plane15.c = wm.wedding_date
plane15.c.name = "Mulroney"
##########
nostalgic.a = wm.mamma_mia
nostalgic.a.name = 'A musical extravaganza'
nostalgic.b = body_swap
body_swap.a = wm.freaky_friday
body_swap.a.name = 'Body swap hijinks'
body_swap.b = wm.bfgw
body_swap.b.name = 'I want a wedding that\'s a good time'
#########
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
crash.c = wm.sideways
crash.c.name = "It's better than Wedding Crashers"
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
stiller.c = wm.made_honor
stiller.c.name = 'Patrick Dempsey'

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

  
