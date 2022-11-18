import random

class Female_Lead:
  def __init__(self):
    fl_name = random.randint(1, 6)
    if fl_name == 1:
      self.name = 'Noelle'
    if fl_name == 2:
      self.name = 'Chrissy'
    if fl_name == 3:
      self.name = 'Holly'
    if fl_name == 4:
      self.name = 'Ebbie'
    if fl_name == 5:
      self.name = 'Ivy'
    if fl_name == 6:
      self.name = 'Belle'

    fl_job = random.randint(1, 4)
    if fl_job == 1:
      self.job = 'Lawyer'
    if fl_job == 2:
      self.job = 'Interior Designer'
    if fl_job == 3:
      self.job = 'Baker'
    if fl_job == 4:
      self.job = 'Marketing Executive'
    
    fl_amb = random.randint(1, 5)
    if fl_amb == 1:
      self.ambition = ' building her own app about how much she loves Christmas.'
    if fl_amb == 2:
      self.ambition = ' taking over her family\'s company when her father retires.'
    if fl_amb == 3:
      self.ambition = ' being taken seriously by her boss.'
    if fl_amb == 4:
      self.ambition = ' giving her family the perfect Christmas.'
    if fl_amb == 5:
      self.ambition = ' opening a movie theater with her sister but also finding love with an exciting new man.'
    
  def __repr__(self):
    rep = f'{self.name} is a successful {self.job} whose real ambition is{self.ambition}'
    return rep

  def be_betrayed(self):
    return f'{self.name} discovers his terrible secret, and decides to go to that humungous public event after all, though her heart is broken.'

  def forgive(self):
    return f'{self.name} forgives him and they share a PG kiss.'

class Male_Lead:
  def __init__(self):
    ml_name = random.randint(1, 6)
    if ml_name == 1:
      self.name = 'Noel'
    if ml_name == 2:
      self.name = 'Chris'
    if ml_name == 3:
      self.name = 'Luke'
    if ml_name == 4:
      self.name = 'Jack'
    if ml_name == 5:
      self.name = 'Raheem'
    if ml_name == 6:
      self.name = 'Mohammed'
    
    ml_job = random.randint(1, 4)
    if ml_job == 1:
      self.job = 'Carpenter'
    if ml_job == 2:
      self.job = 'Small-town lawyer'
    if ml_job == 3:
      self.job = 'Well-adjusted heir to a family fortune who spends his time helping others'
    if ml_job == 4:
      self.job = 'Coffee roaster'
    
    ml_sec = random.randint(1, 5)
    if ml_sec == 1:
      self.secret = ' he lost the girl of his dreams because he was selfish.'
    if ml_sec == 2:
      self.secret = f' he is only pretending to be a {self.job} to gain her trust.'
    if ml_sec == 3:
      self.secret = ' he hates Christmas.'
    if ml_sec == 4:
      self.secret = ' he was engaged before but she left him and he hasn\'t has a serious relatioship since.'
    if ml_sec == 5:
      self.secret = ' his extremely fancy and snobby ex is plotting to get him back and might mess everything up.'

  def __repr__(self):
    rep = f'{self.name} is a charming {self.job} in her hometown.'
    return rep
  
  def be_angry(self):
    return f'{self.name} is angry that she doesn\'t believe him, but most of all, he\'s angry at himself.'

  def make_up(self):
    return f'{self.name} catches her right before she\'s going to do that big thing. He looks so handsome because he\'s wearing a slightly nicer version of his regular clothes. He explains everything and for some reason, she listens this time.'

lead_1 = Female_Lead()
lead_2 = Male_Lead()

welcome = input('Happy Holidays! Are you ready to tolerate a medicore story literally written by an algorithm? Type sure or hell no: ')

print(welcome)

if welcome == 'sure':
  print('Great! Let\'s begin.') 
  print('Meet ' + lead_1.name + '. ' + lead_1.__repr__())
  keep_going = input('Keep watching? Type sure or hell no: ')
  if keep_going == 'sure':
    print('She meets ' + lead_2.name + '. ' + lead_2.__repr__())
    whats_next = input('What could possibly happen next??? Want to find out? Type of course or absolutely not: ')
    if whats_next == 'of course':
      event_num = random.randint(1, 6)
      if event_num == 1:
        event = 'movie theater reopening, because her sister has finally finished the remodel.'
      if event_num == 2:
        event = f'snowperson building contest where the organizer is a member of the LGBTQ community who went to high school with {lead_1.name}.'
      if event_num == 3:
        event = 'food drive for people experiencing food insecurity, where they will see that little girl that {lead_1.name} has made such a connection with.'
      if event_num == 4:
        event = 'Santa Claus parade where her wheelchair-bound father is playing Santa for the first time.'
      if event_num == 5:
        event = 'gingerbread house pageant, where her homely nephew is determined to win.'
      if event_num == 6:
        event = 'gospel cantata, where her shy best friend is singing a solo of "O Holy Night."'
      print(f'They hit it off right away, but there\'s a problem. You see,{lead_1.name} doesn\'t know that {lead_2.name} is hiding a shameful past: {lead_2.secret}, and if she finds out, he might lose her forever. Despite this, they decide to go to a festive and extremely public {event}. They are both nervous but excited as it will test the waters of their relationship.')
      finale = input('Uh oh. Well, you have to find out what happens now. Type what happens: ')
      if finale == 'what happens':
        print(f'On Christmas eve, {lead_1.be_betrayed()} {lead_2.be_angry()}')
        but_then = input(f'Oh no! But {lead_2.name} has actually changed so much! {lead_1.name} will never find love now! Type ending to get the ending you know you need: ')
        if but_then == 'ending':
          print(lead_2.make_up())
          print(lead_1.forgive())
          print('That\'s the end of the story. Feel free to "keep watching" though, these stories are endless. Happy holidays!')
      else:
        print('You did something wrong. Refresh. Sorry. My programming isn\'t quite good enough yet')
    else:
      print('Snob!')
  else:
    print('What, you have better things to do?')
elif welcome == 'hell no':
  print('All right. Fuck off then!')
else:
  input('Are you sure you got that right?')


