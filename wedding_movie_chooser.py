#wedding movies
#tree structure
#binary search
#traverse

class Wedding_Movie:
  def __init__(self, value, deets={}):
    self.value = value
    self.children = []
    self.deets = deets

  def add_child(self, child_node):
    #print("Adding " + child_node.value)
    self.children.append(child_node)

  def get_child(self):
    for child in self.children:
      print(child.value)
    return "There are " + str(len(self.children)) + " items in the list " + self.value
    

  def print_deets(self):
    return self.value.upper() + "\n" + self.deets["summary"] + "\nRated " + self.deets["rated"]

  def reveal_movie(self):
    print("\nI HAVE THE PERFECT MOVIE FOR YOU!\n")
    for each in choice_path:
      print(each + " --> ")
    print(self.print_deets())
    print("Enjoy your movie!\n")

  
female_lead = Wedding_Movie("Female Lead")
male_lead = Wedding_Movie("Male Lead")

dresses27 = Wedding_Movie("27 Dresses", {"summary": "A young woman who's been a bridesmaid 27 times is forced to serve as maid of honor as her capricious little sister marries the man she's in love with.", "rated": "PG-13"})

satc = Wedding_Movie("Sex and the City: The Movie", {"summary": "When Carrie suffers a devastating emotional setback, Charlotte, Miranda, and Samantha are there to help her write a book about it.", "rated": "R"})

bfgw = Wedding_Movie("My Big Fat Greek Wedding", {"summary": "A shy, frumpy woman gives her life a makeover in order to win the man of her dreams...but she's Greek!", "rated": "PG"})

mamma_mia = Wedding_Movie("Mamma Mia!", {"summary": "A young bride invites the three men who might be her father to her wedding...without telilng her mother.", "rated": "PG"})

bridesmaids = Wedding_Movie("Bridesmaids", {"summary": "A middle-aged, underemployed woman struggles to keep up with the lavish wedding her best friend is planning with her work bestie.", "rated": "R"})

wedding_planner = Wedding_Movie("The Wedding Planner", {"summary": "An unlucky-in-love wedding planner meets the man of her dreams when he saves her life...and then hires her to plan his wedding!", "rated": "PG-13"})

crazy_rich_a = Wedding_Movie("Crazy Rich Asians", {"summary": "A Chinese-American woman tries to fit in at a wedding when she learns that her suave boyfriend is a member of the richest family in Singapore.", "rated": "PG-13"})

freaky_friday = Wedding_Movie("Freaky Friday", {"summary": "A mother and daughter who never listen to each other magically swap bodies to learn about each other's lives.", "rated": "PG"})

muriels = Wedding_Movie("Muriel's Wedding", {"summary": "A woman who's never been on a date steals some cash, runs away, changes her name, and changes her life.", "rated": "R"})

royal_treat = Wedding_Movie("The Royal Treatment", {"summary": "An uptown stylist is hired to do hair and makeup for a prince's wedding...but he's handsome!", "rated": "PG"})

hangover = Wedding_Movie("The Hangover", {"summary": "A groom goes missing after his brother-in-law-to-be surreptitiously drugs his bachelor party, sending the men on a scavenger hunt to track down their friend and remember what happened that night.", "rated": "R"})

wedding_singer = Wedding_Movie("The Wedding Singer", {"summary": "A brokenhearted wedding singer finds the will to love again when he's befriended by an adorable bride-to-be.", "rated": "PG-13"})

one_night = Wedding_Movie("It Happened One Night", {"summary": "When an heiress disappears in order to marry her scandalous European lover, an American journalist agrees to help her in exchange for exclusive rights to her story.", "rated": "G"})

repeat = Wedding_Movie("Love Wedding Repeat", {"summary": "Alternate timelines abound when the best man is tasked with keeping a troublesome guest out of the wedding.", "rated": "R"})

proposal = Wedding_Movie("The Proposal", {"summary": "A Canadian book publisher proposes a green card marriage (and a promotion) to her ambitious subordinate, and they have to keep up the ruse when they fly to Alaska to meet his family.", "rated": "PG-13"})

tag = Wedding_Movie("Tag", {"summary": "Five lifelong best friends continue their decades-long game of tag at a lavish wedding with a tag-hating bride.", "rated": "R"})

love_you_man = Wedding_Movie("I Love You, Man", {"summary": "After getting engaged, a straight-laced fella realizes he doesn't have any close guy friends and recruits a chill acquaintance to be his best man.", "rated": "R"})

father_bride = Wedding_Movie("Father of the Bride", {"summary": "A successful but uptight father freaks out over every little decision made when his daughter brings home a man he's never met and says she's getting married.", "rated": "PG"})

crashers = Wedding_Movie("Wedding Crashers", {"summary": "Two bros have strict rules when they crash weddings and seduce bridesmaids all summer, but he's broken the biggest one: don't fall in love.", "rated": "R"})

parents = Wedding_Movie("Meet the Parents", {"summary": "He's about to propose to his girlfriend when he learns that he's expected to ask her father, an intense ex-CIA agent who looks and talks exactly like Robert De Niro, for her hand in marriage.", "rated": "PG-13"})

naked = Wedding_Movie("Naked", {"summary": "A cold-footed groom finds himself naked and stuck in a time loop as his bride waits for him to get it all right and show up at the altar.", "rated": "PG-13"})

week_of = Wedding_Movie("The Week Of", {"summary": "Two family patriarchs find themselves at odds in the seven days leading up to the marriage of their children.", "rated": "PG-13"})

seven_brides = Wedding_Movie("Seven Brides for Seven Brothers", {"summary": "Seven brothers from a rural family travel to town to kidnap one bride for each of them.", "rated": "PG"})


female_lead.add_child(dresses27)
female_lead.add_child(satc)
female_lead.add_child(bfgw)
female_lead.add_child(mamma_mia)
female_lead.add_child(bridesmaids)
female_lead.add_child(wedding_planner)
female_lead.add_child(crazy_rich_a)
female_lead.add_child(freaky_friday)
female_lead.add_child(muriels)
female_lead.add_child(royal_treat)


male_lead.add_child(one_night)
male_lead.add_child(father_bride)
male_lead.add_child(hangover)
male_lead.add_child(wedding_singer)
male_lead.add_child(repeat)
male_lead.add_child(proposal)
male_lead.add_child(tag)
male_lead.add_child(love_you_man)
male_lead.add_child(crashers)
male_lead.add_child(parents)
male_lead.add_child(naked)
male_lead.add_child(week_of)
male_lead.add_child(seven_brides)

#print(classic.get_child())

welcome = input("Are you ready for wedding movie season?!! ")
choices = ["A", "B"]

while welcome.upper() != "NO":
  choice_path = []
  male_female = input("\nLet's help you choose a movie.\nType A or B from the choices below.\nWould you prefer a movie with a...\nA) male lead\nB) female lead\n")
  #male protag
  while male_female.upper() not in choices:
    male_female = input("\nPlease enter A or B.\nA) male lead\nB) female lead\n")
  if male_female.upper() == "A":
    choice_path.append("Male lead")
    ff_adult = input("\nMale protags it is.\nDo you want a movie that is...\nA) family-friendly\nB) not for kids\n")
    while ff_adult.upper() not in choices:
      ff_adult = input("\nPlease enter A or B.\nA) family-friendly\nB) not for kids\n")
    if ff_adult.upper() == "A":
      choice_path.append("Family-friendly")
      classic_mod = input("\nAll right, a family-friendly movie with a male protagonist. Hmm...this might be tricky.\nDo you want...\nA) a black & white or technicolor classic\nB) a more modern film\n")
      while classic_mod.upper() not in choices:
        classic_mod = input("\nPlease enter A or B.\nA) a black & white classic\nB) a more modern film\n")
      if classic_mod.upper() == "A":
        choice_path.append("Classic")
        musical = input("\nDo you like musicals?\nA) Love musicals!\nB) Not for me\n")
        while musical.upper() not in choices:
          musical = input("\nPlease choose A or B.\nA) Love musicals!\nB) Not for me\n")
        if musical.upper() == "A":
          choice_path.append("Musical")
          seven_brides.reveal_movie()
        elif musical.upper() == "B":
          choice_path.append("Not musical")
          one_night.reveal_movie()
        #one_night.reveal_movie()
      elif classic_mod.upper() == "B":
        choice_path.append("Modern")
        father_bride.reveal_movie()
    elif ff_adult.upper() == "B":
      choice_path.append("Not suitable for kids")
      buddy = input("\nMaybe kids shouldn't be allowed to go to weddings. Anything can happen.\nDo you want...\nA) a buddy comedy\nB) something else\n")
      while buddy.upper() not in choices:
        buddy = input("\nPlease enter A or B.\nA) a buddy comedy\nB) something else\n")
      if buddy.upper() == "A":
        choice_path.append("Buddy comedy")
        ed_helms = input("\nBuddy comedies! Great. There's some good ones. Are you a fan of...\nA) Ed Helms! YES INDEED\nB) Not so much\n")
        while ed_helms.upper() not in choices:
          ed_helms = input("\nPlease enter A or B.\nA) Ed Helms! YES INDEED\nB) Meh. Got anyone more handsome?\n")
        if ed_helms.upper() == "A":
          choice_path.append("Ed Helms")
          raunch = input("\nThe kids aren't there. So. How raunchy do you want it?\nA) as raunchy as possible\nB) I would prefer my raunch on the side, thank you\n ")
          while raunch.upper() not in choices:
            raunch = input("\nPlease enter A or B.\nA) as raunchy as possible\nB) I would refer my raunch on the side, thank you\n")
          if raunch.upper() == "A":
            choice_path.append("Extra raunch")
            hangover.reveal_movie()
          elif raunch.upper() == "B":
            choice_path.append("Raunch on the side")
            tag.reveal_movie()
        elif ed_helms.upper() =="B":
          choice_path.append("Better-looking than Ed Helms")
          crash = input("\nHmm. I've only got two movies left. I guess...the real question is...do you want to watch something you've probably already seen, or something that you slept on?\nA) give me what I came here expecting\nB) give me something new\n")
          while crash.upper() not in choices:
            crash = input("\nPlease enter A or B.\nA) give me what I came here expecting\nB) give me something new\n")
          if crash.upper() == "A":
            choice_path.append("I'm specifically here to watch Wedding Crashers")
            crashers.reveal_movie()
          elif crash.upper() =="B":
            choice_path.append("Paul Rudd is People's Sexiest Man Alive 2021")
            love_you_man.reveal_movie()
      elif buddy.upper() == "B":
        sandler = input("\nNo problem, no problem. How about Adam Sandler?\nA) Love Adam Sandler\nB) Who?\n")
        while sandler.upper() not in choices:
          sandler = input("\nPlease enter A or B.\nA) Love Adam Sandler\nB) Who?\n")
        if sandler.upper() == "A":
          choice_path.append("Adam Sandler")
          nineties = input("\nWow, really? Huh. Okay. Then, uh...\nA) 1990s Adam Sandler\nB) 2010s Adam Sandler?\n")
          while nineties.upper() not in choices:
            nineties = input("\nPlease enter A or B.\nA) 1990s Adam Sandler\nB) 2010s Adam Sandler\n")
          if nineties.upper() == "A":
            choice_path.append("1990s Sandler")
            wedding_singer.reveal_movie()
          elif nineties.upper() == "B":
            choice_path.append("2010s Sandler")
            week_of.reveal_movie()
        elif sandler.upper() == "B":
          choice_path.append("Not A Damn Sandler")
          timeline = input("\nAre you a fan of time loops and alternate timelines?\nA) yes\nB) no\n")
          while timeline.upper() not in choices:
            timeline = input("\nPlease enter A or B.\nA) time loops rule\nB) time loops drool\n")
          if timeline.upper() == "A":
            choice_path.append("Timeline wackiness")
            time = input("\nTime stuff, excellent. Last question:\nA) a time loop a la Groundhog Day?\nB) alternate timelines a la Sliding Doors?\n")
            while time.upper() not in choices:
              time = input("\nPlease enter A or B.\nA) a time loop a la Groundhog Day?\nB) alternate timelines a la Sliding Doors?\n")
            if time.upper() == "A":
              choice_path.append("Groundhog Day-esque")
              naked.reveal_movie()
            elif time.upper() == "B":
              choice_path.append("Sliding Doors-esque")
              repeat.reveal_movie()
          elif timeline.upper() == "B":
            choice_path.append("Normal time stuff")
            stiller = input("\nWho do you prefer as a leading man?\nA) Ben Stiller\nB) Ryan Reynolds\n")
            while stiller.upper() not in choices:
              stiller = input("\nPlease enter A or B.\nA) Ben Stiller\nB) Ryan Reynolds\n")
            if stiller.upper() == "A":
              choice_path.append("Ben Stiller")
              parents.reveal_movie()
            elif stiller.upper() == "B":
              choice_path.append("Ryan Reynolds")
              proposal.reveal_movie()      
  #female protag     
  elif male_female.upper() == "B":
    choice_path.append("Female protagonist")
    ff_adult = input("\nFemale leads it is.\nDo you want...\nA) a family-friendly movie\nB) something naughty for me and the girls\n")
    while ff_adult.upper() not in choices:
      ff_adult = input("\nPlease enter A or B.\nA) a family-friendly movie\nB) something naughty for me and the girls\n")
    if ff_adult.upper() == "A":
      choice_path.append("Family-friendly")
      nostalgic = input("\nCool. You have some good options.\nAre you looking for...\nA) something nostalgic\nB) something fresh and new!\n")
      while nostalgic.upper() not in choices:
        nostalgic = input("\nPlease enter A or B.\nA) something nostalgic\nB) something fresh and new\n")
      if nostalgic.upper() == "A":
        choice_path.append("Nostalgic")
        music = input("\nDo you want a lot of singing and dancing?\nA) Yes! A musical!\nB) Not my thing\n")
        while music.upper() not in choices:
          music = input("\nPlease enter A or B.\nA) Yes! A musical!\nB) Not my thing\n")
        if music.upper() == "A":
          choice_path.append("Musical")
          mamma_mia.reveal_movie()
        if music.upper() == "B":
          choice_path.append("Not musical")
          body_swap = input("\nDo you enjoy the whimsical magic of a body swap?\nA) Body swap magic please\nB) No thanks, I just want a good wedding\n")
          while body_swap.upper() not in choices:
            body_swap = input("\nPlease enter A or B.\nA) Body swap magic please\nB) No thanks, I just want a good wedding\n")
          if body_swap.upper() == "A":
            choice_path.append("Body swap")
            freaky_friday.reveal_movie()
          elif body_swap.upper() == "B":
            choice_path.append("Good wedding")
            bfgw.reveal_movie()
      elif nostalgic.upper() == "B":
        royal_treat.reveal_movie()
    elif ff_adult.upper() == "B":
      choice_path.append("Something for me and the girls")
      wedding = input("\nGreat, that will make it easier. You've got some very different options, so let's narrow it down. Do you want...\nA) a movie that's all about the wedding, the bride, and the glamour\nB) a movie that's all about the DRAMA\n")
      while wedding.upper() not in choices:
        wedding = input("\nPlease enter A or B.\nA) a movie that's all about the wedding, the dress, and the glamour\nB) a movie that's all about the DRAMA\n")
      if wedding.upper() == "A":
        choices = ["A", "B", "C"]
        choice_path.append("Wedding, wedding, wedding")
        leading_man = input("\nPerfect! One question left. Choose your leading man.\nA) Matthew McConaghey\nB) James Marsden\nC) Neither\n")
        while leading_man.upper() not in choices:
          leading_man = input("\nPlease enter A, B, or C. \nA) Matthew McConaghey\nB) James Marsden\nC) Neither\n")
        if leading_man.upper() == "A":
          choice_path.append("McConaghey")
          wedding_planner.reveal_movie()
        elif leading_man.upper() =="B":
          choice_path.append("Marsden")
          dresses27.reveal_movie()
        elif leading_man.upper() == "C":
          choice_path.append("\nI don't care who the leading man is, I'm here for Toni Colette")
          muriels.reveal_movie()
      elif wedding.upper() == "B":
        choice_path.append("Here for the drama")
        glamour = input("\nDo you want to indulge in some really obscene opulance?\nA) Yes, smother me with capitalist fantasy\nB) No, I want to be reminded how poor I am\n")
        while glamour.upper() not in choices:
          glamour = input("\nPlease enter A or B.\nA) Yes, smother me with capitalist fantasy\nB) No, I want to be reminded how poor I am\n")
        if glamour.upper() == "A":
          choices = ["A", "B", "C", "D"]
          choice_path.append("Rich people problems")
          carrie = input("\nLast question. Are you...\nA) a Carrie\nB) a Samantha\nC) a Miranda\nD) a Charlotte\n")
          while carrie.upper() not in choices:
            carrie = input("\nPlease enter A, B, C, or D.\nA) a Carrie\nB) a Samantha\nC) a Miranda\nD) a Charlotte\n")
          if carrie.upper() == "A" or carrie.upper() == "B" or carrie.upper() =="C":
            choice_path.append("Spice")
            satc.reveal_movie()
          elif carrie.upper() == "D":
            choice_path.append("Sugar")
            crazy_rich_a.reveal_movie()
        elif glamour.upper() == "B":
          choice_path.append("Help me, I'm poor")
          bridesmaids.reveal_movie()
  
  ###
  welcome = input("\nDo you want to find another movie?\n")
  if welcome.lower() == 'no':
    print("\nK byyyyyyyyyye")
