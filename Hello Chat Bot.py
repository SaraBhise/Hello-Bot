#Greet the user
print("Hello! I am AI Bot. What's your name? : ")

#Got user input
name = input()

#Respond to the users name
print(f"Nice to meet you, {name}!")

#ask a question
print("How is the weather today? (good/bad) : ")
weather = input().lower()

#ues conditional statements to respond based on inputs
if weather == "good":
    print("Enjoy it with some delicious food!!")
elif weather == "bad":
    print("Enjow with your favourite thing!!")
else:
    print("I see. Sometimes it's hard to put weather into words.")

#end of the conversation
print(f"It was nice chatting with you {name}. Goodbye!!!")