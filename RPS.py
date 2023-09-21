# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
  if prev_play == "":
    opponent_history = []
  opponent_history.append(prev_play)
  guess = "P"
  tours = len(opponent_history)
  if tours>=2:
    half = tours/2 if tours%2==0 else (tours-1)/2
    probable_moves = {"R":0, "P":0, "S":0}
    c = 1
    while c<=half:
      lastc = opponent_history[-c:]
      for i in range(len(opponent_history)-c):
        if opponent_history[i:i+c] == lastc:
          next_move = opponent_history[i+c]
          probable_moves[next_move] +=1
      c += 1
      forwin = {"R":"P", "P":"S", "S":"R"}
    return forwin[max(probable_moves, key=probable_moves.get)]
  else:
    return guess
    
  return guess
