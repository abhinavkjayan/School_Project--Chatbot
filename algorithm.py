inp = input("Enter a text : ")

s = 1

#a = ["Hey how are you doing young man !?"]
#print(a[0],"is to match with")

questions = [
    # --- Greetings & Small Talk ---
    "Hey how are you doing young man !?",
    "Hello there!",
    "Hi, how’s your day going?",
    "Good morning!",
    "Good evening!",
    "What’s up?",
    "How have you been?",
    "Nice to meet you!",
    "How’s life?",
    "What are you doing right now?",

    # --- Personal & Casual ---
    "What’s your name?",
    "Who are you?",
    "Where are you from?",
    "How old are you?",
    "Do you like music?",
    "What kind of movies do you enjoy?",
    "Do you have any hobbies?",
    "What’s your favorite food?",
    "Do you like animals?",
    "Do you play video games?",

    # --- Weather & Time ---
    "What’s the weather like today?",
    "Is it raining?",
    "Is it hot outside?",
    "What’s the temperature right now?",
    "Is it going to rain tomorrow?",
    "What time is it?",
    "What day is it today?",
    "Is it the weekend?",
    "When does school start?",
    "When does the sun set?",

    # --- School & Study ---
    "Did you finish your homework?",
    "What subjects do you study?",
    "Who’s your favorite teacher?",
    "Do you like math?",
    "Can you solve math problems?",
    "What is 2 plus 2?",
    "What is the square root of 9?",
    "Can you help me study?",
    "What’s your favorite subject?",
    "Do you like science?",

    # --- Knowledge & Trivia ---
    "Who invented the light bulb?",
    "What is the capital of France?",
    "Who is the president of India?",
    "What planet is closest to the Sun?",
    "What is photosynthesis?",
    "How many continents are there?",
    "Who wrote the Harry Potter books?",
    "What is the largest animal in the world?",
    "How far is the Moon?",
    "What is gravity?",

    # --- Emotions & Responses ---
    "I am sad.",
    "I am happy!",
    "I feel bored.",
    "I’m tired.",
    "I’m angry.",
    "I feel stressed.",
    "I love programming!",
    "I hate homework.",
    "I am excited for the holidays!",
    "You are funny!",

    # --- Random / Fun ---
    "Tell me a joke.",
    "Do you know any riddles?",
    "What’s your favorite color?",
    "Can you sing?",
    "Can you dance?",
    "Do you believe in aliens?",
    "Do robots dream?",
    "Who’s your best friend?",
    "What’s your favorite animal?",
    "Can you tell me something cool?",

    # --- System / Meta ---
    "What can you do?",
    "Are you a real person?",
    "Are you a robot?",
    "Who made you?",
    "Do you have feelings?",
    "Can you learn new things?",
    "Are you connected to the internet?",
    "How do you work?",
    "Do you remember me?",
    "What programming language are you written in?"
]
               # some quetions from chatgpt for testing the algorithm


def find_best_match (inp , available , sens=1) :
    #inp -->  user input
    #sens --> the accuracy of the answer
    #available --> the database

    
    sens = len(inp) // sens # atleast this much match count

    inv_inp = inp.lower().split()  #optimized input string

    ign_words = ["is","the","an","a"]

    index = -1
    word_match = 0
    order_match = {}
    overall_match = { }  # "question" : average of word match and word count

    has_the_req = [] # all the questions from available that is matches {for next matching}
    for question in available :
        word_match = 0

        index += 1 # index of the taken question in the database

        q = question.lower().split() # list of all individual words in the selected question(optimized question string)

        for word in inv_inp :

            if word.lower() in ign_words :
                pass
            
            elif word in q :
                word_match += 1


        word_match = int(( word_match/len(inv_inp)) * 100 ) # percentage of words matched
        
        if word_match >= 50 :
            has_the_req.append(question)

        #ind = 0 # for checkiung the order of the words
        #try : 
        #    if inv_inp[in1] == q[in2] :   ingnore these.......

    #print(has_the_req)

    split_inp = inp.split()

    if has_the_req == [] :  # returns an error code if it didnt find any match from words match
        return 204
    
    elif len(has_the_req) == 1 :  # if it only got one output from word matching , it returns that {dosent go for order matching}
        return has_the_req[0]


    for each in has_the_req :      # order matching each sentences that met the requirement for word match
        
        common1 = []       # common words in db question from input
        common2 = []       #  common words in input from db question

        for i in split_inp :
            if i.strip() in each.split() :
                common1.append(i)      # adding stuff to the list
            
        for i in each.split() :
            if i.strip() in split_inp:
                common2.append(i)      # same thing but with respect to the other string
            
        tmp_length = len(common1)  # both of the would have the same length

        ind = 0 


        while ind < tmp_length :             # checking if the order matches
            if common1[ind] == common2[ind] :
                if each not in order_match :             
                    order_match[each] = 0
                else :
                    order_match[each] += 1
            ind += 1
                
    for i in order_match :
        val = order_match[i]
        val = int((val / len(split_inp)) * 100)  # the percentage of similarity
        order_match[i] = val                 # making an actual value for comparing 

    
    
    
    best = max(order_match , key=order_match.get)  # find the best of it
 

    
    return best  
    

        
            
              

a = find_best_match(inp,questions,s)

print(a)
