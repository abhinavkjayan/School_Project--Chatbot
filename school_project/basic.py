
stop_words = ["is","an","a","the"]

bas = {
    "hi": "Hey there! How can I help you today?",
    "hello": "Hello! What can I do for you?",
    "hey": "Hey! How’s it going?",
    "how are you": "I'm just a bunch of Python code, but I’m feeling pretty good! 😄",
    "what is your name": "I'm your friendly Python chatbot!",
    "who made you": "I was created by my developer using Python and SQL.",
    "what can you do": "I can answer questions, run commands, and even learn new things if you teach me!",
    "bye": "Goodbye! Talk to you later 👋",
    "see you": "See you soon!",
    "thanks": "You're welcome!",
    "thank you": "Anytime! 😊",
    "what is python": "Python is a programming language known for being simple, readable, and powerful.",
    "what is sql": "SQL stands for Structured Query Language — it's used to manage and query databases.",
    "who are you": "I’m a chatbot built in Python. I’m still learning from you!",
    "what time is it": "I can’t tell time yet, but you could teach me to use Python’s datetime module!",
    "open google": "I can’t open websites directly yet, but you could let me run system commands to do that!",
    "run command": "Sure, tell me what command you want to run.",
    "how are you doing": "All systems running perfectly ⚙️",
    "help": "I can answer your questions, run commands, or chat with you — what do you want to do?"
}


#target_input = input("Enter a an input to find the best match of : ").lower()
target_input = "Hey, how’s everything going?".lower()

questions = bas.keys()
index = -1

rec_match = {}

for q in questions : 
    index += 1
    q = q.lower().split()
    rec_match[index] = 0
    for word in q :
        if word in stop_words : 
            pass
        else :
            if word in target_input:
                rec_match[index] += 1
            else :
                rec_match[index] -= 1
            
great = -99999999
most = ""
for i in rec_match :
     #print("Runing")
     if rec_match[i] > great : 
         print(1)
         great = rec_match[i]
         most = i
         print(i)
print(most)
#print(most)
#most = list(most)
#print(most)
most = questions[int(most)]


ans = bas[most]  # gets its answer
print(f"the greatest  match was \n \n {ans}")
print()
print(most)
print()

        
            
        