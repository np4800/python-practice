

bids = {}
biding_finished = False

def find_highest_bidder(bidder_record):
  highest_bid = 0
  winner = ""
  
  for bidder in bidder_record:
    if bidder_record[bidder] > highest_bid:
      highest_bid = bidder_record[bidder]
      winner = bidder

  print(f"The highest bid has been given by {winner} with ${highest_bid}")

while not biding_finished:
  name = input("Enter your name?: ")
  bid = int(input("What is your bid?: $"))
  bids[name] = bid
  
  should_continue = input("Are there any bidders? type 'yes' or 'no' : ")
  if should_continue == "yes":
    biding_finished = False
  else:
    biding_finished = True
    find_highest_bidder(bids)


