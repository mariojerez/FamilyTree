import datetime

class Member:
  def __init__(self, name):
    self.name = name
    self.pronouns = Pronouns()
    self.dateOfBirth = None
    self.description = ""
    self.children = []
    self.siblings = []
    self.parents = []
    self.partners = []
    self.xpartners = []

  def __str__(self):
    return self.name
  
  def changeName(self, newName):
    self.name = newName
    print("Changed name to ", self.name)

  def changePronouns(self, sub, obj, pos):
    self.pronouns = Pronouns(sub, obj, pos)

  def setDateOfBirth(self, day, month, year, hours=0, minutes=0):
    self.dateOfBirth = datetime.datetime(year, month, day, hours, minutes)
    print("Updated {:s}'s birthdate to {:s}.".format(self.name, str(self.dateOfBirth)))

  def addChild(self, child):
    if child not in self.children:
      self.children.append(child)
      self.children = orderMembersByAge(self.children)
      print("Added {:s} as a child".format(child.name))
    else:
      print("{:s} is already a child of {:s}".format(child.name, self.name))

  def addPartner(self, partner):
    if partner not in self.partners:
      self.partners.append(partner)
      print("Added {:s} as a partner".format(partner.name))
    else:
      print("{:s} is already a partner of {:s}".format(partner.name, self.name))

  def breakUpWith(self, ex):
    if ex in self.partners:
      self.partners.remove(ex)

      if ex not in self.xpartners:
        self.xpartners.append(ex)
        print(ex, "is now an ex-partner")
  
    else:
      if ex in self.xpartners:
        print(ex, " is already an ex-partner")
      else:
        print(ex, "was never even a partner...")
      
  def addSibling(self, sibling):
    if sibling not in self.siblings:
      self.siblings.append(sibling)
      self.siblings = orderMembersByAge(self.siblings)
      print(sibling, " added as a sibling")
    else:
      print(sibling, " is already a sibling")

def orderMembersByAge(members):
  listOfTuples = [(member.dateOfBirth, member) for member in members]
  listOfTuples.sort()
  listOfTuples.reverse()
  orderedMembers = [t[1] for t in listOfTuples]
  return orderedMembers


class Pronouns:
  def __init__(self, subject="they", objct="their", possessive="them"):
    self.subject = subject
    self.object = objct
    self.possessive = possessive


