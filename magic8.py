name = "Uchenna"
question = ""
answer = ""

import random
random_number = random.randint(1,11)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "it is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Maybe, maybe not."
elif random_number == 11:
  answer = "If you pray hard enough."
else:
  answer = "Error"

if name == "":
  print ("Question: " + question)
elif question == "":
  print("Magic 8-ball cannot provide a fortune, otherwise, the fabric of reality is at risk.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: "+answer)

