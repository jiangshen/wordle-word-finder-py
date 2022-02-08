import re, csv, sys

class Wordle_Word_Finder:
  def __init__(self, word_bank_data_file) -> None:
    self.valid_word_bank = []
    self.read_word_bank(word_bank_data_file)
    self.yellow_location = {}
    self.yellow_positions = []
    self.num_yellows = 0

  def read_word_bank(self, file) -> None:
    with open(file, 'r') as f:
      reader = csv.reader(f)
      for line in reader: self.valid_word_bank += line

  def parse_input(self) -> str:
    args = sys.argv[1:]
    input = args[0]

    expr = ""
    for i, c in enumerate(input):
      if c == '_':
        self.yellow_positions += [i]
        if len(args) > 1:
          # Exclusions
          expr += '[^' + args[1] + ']'
        else:
          # Match any letter
          expr += "[a-z]"
      else:
        if c.isupper():
          # Match green letter
          expr += c.lower()
        else:
          if len(args) > 1:
            expr += '[^' + args[1] + ']'
          else:
            expr += "[a-z]"

          # Add info for yellow letters
          self.yellow_positions += [i]
          self.yellow_location[c] = i
          self.num_yellows += 1
    return expr

  def find_words(self):
    # Pass 1: Match green letters and filter out exclusions
    expr = self.parse_input()
    found1, found2 = [], []
    for w in self.valid_word_bank:
      match = re.match(expr, w)
      if match: found1 += [match.group()]

    # Pass 2: Match yellow letters
    if self.num_yellows > 0:
      for w in found1:
        count = self.yellow_location.fromkeys(self.yellow_location, 0)
        c_positions = {}
        for i in self.yellow_positions:
          c = w[i]
          for y_letter in self.yellow_location.keys():
            if c == y_letter:
              count[c] += 1
              c_positions[c] = i
        if all(v == 1 for v in count.values()):
          # Do not include words matching yellow letters location
          include = True
          for key in c_positions:
            if self.yellow_location[key] == c_positions[key]:
              include = False
              break
          if include:
            found2 += [w]
    else:
      found2 = found1

    # Output word suggestions (matches)
    print(str(len(found2)) + (' Matches' if len(found2) > 1 else ' Match'))
    print(' '.join(found2))

wordle = Wordle_Word_Finder('wordle-word-bank.txt')
wordle.find_words()