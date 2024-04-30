edges = {         
  (1,'1') : 2,
  (1,'0') : 4,
  (2,'0') : 3,
  (2,'1') : 2,
  (3,'1') : 2,
  (3,'0') : 3,
  (4,'0') : 4,
  (4,'1') : 4,
}
accepting = [3,4]

def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print(dfa(string, 1, edges, accepting))



