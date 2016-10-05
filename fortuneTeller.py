import random

# Create a program that accepts a question from the user and responds
#  with a random answer from a list of 15-20 answers.
# variable answers

fortunes = ["It really does not matter", "Ask again when you are not busy", "You can't handle the truth",
            "I wish I had more time to tell you the whole story, but for now---", "You will be wildly successful",
            "I know the answer you seek, PLEASE ENTER $19.95 TO CONTINUE", "Really, just give up",
            "You are an amazing person", "You can accomplish anything you put your mind too",
            "A galaxy rotation curvature is a plot of the orbital velocities of discernible stars or vapor in that congregation \n as opposed to their centrifugal aloofness from that galaxy's epicenter",
            "Copy and paste is your best friend", "Don't forget to save your work", "Use a pencil so you can erase your mistakes",
            "Don't ask me, how should I know, you are the expert", "I know all, but I can't help right now, make an appointment",
            "Forget about that, go play the lottery, I have a good feeling about you", "The secret to the life is peace and acceptance", "Time travel is now available, life is now trial and error",
            "Be a gentleman, be kind, be courteous, and good things will fall in your lap", "Uh, umm, like..., huh; sorry, I have to take this call, maybe later",
            "Sure, just be at 555 Winchester Ln at 5:30pm and you'll see", "Inadvertent actions do not excuse the action's consequences"]

# statement to user
print("I am the all knowing foreseer. I will tell you about your life in the future. Ask me anything.")
print ("When you are finished asking me questions, type finished. \n")
# for words in fortunes:
#    print words
# input from user
question = raw_input("What is it you wish to know? \n")
question = question.lower()
# response to user, using random statements from 'fortunes' variable
response = random.choice(list(fortunes))

print ("\nSILENCE!!! I know you wish to ask " + question + "; the answer to your question is:\n\n" + response + ".\n")

# teller will keep asking questions until user types finished
while question != "finished":
    question = raw_input("Next question, what else do you wish to know? \n")
    question = question.lower()
    response = random.choice(list(fortunes))
    if question == "finished":  # print this when finished
        print ("\nI hope you have enjoyed learning about your future, tell your friends, and have a worry-free day, \n and remember: GENUINE GREEN GRASS GENERALLY GROWS GRADUALLY!!!")
    else:
        print ("\nSILENCE!!! I know you wish to ask " + question + "; the answer to your question is: \n \n" + response + ".\n")
# response to user, using random statements from 'fortunes' variable
