import difflib, time, json, random


# stores the file path of the json file
prompts_json = "/Users/zacharyyu/Desktop/other/CODING PROJECTS/AI-Projects/prompts.json"

try:
    # load the json file (the dict with prompts in it)
    with open(prompts_json, "r") as file:
        prompts = json.load(file)

# handle if the file doesn't exist yet    
except FileNotFoundError:
    prompts = {}
    

# helper function (for readability, smooth flow, ai-feel)
def typewriter(text, delay=0.07):
    time.sleep(1)
    
    for ch in text:
        # end="" gets rid of automatic new line, flush=True forcibly prints each character
        print(ch, end="", flush=True)
        time.sleep(delay)
        
    print()


def learn():
    print("Bot: ", end="", flush=True)
    
    # check if a response already exists 
    if user_input in prompts:
        typewriter("Can you teach me how to respond a different way? \n")
    else:
        typewriter("I do not know how to respond. Can you teach me? \n")
        
        
    new_response = input("Type the response or 'skip' to skip: ").lower()
    
    # if the user did not choose to skip, add the new response to the prompts
    if new_response != "skip":
        # if the prompt already exists, then add the new response to a list of responses
        if user_input in prompts:
            # check if the new response already exists for the prompt
            if new_response not in prompts[user_input]:
                prompts[user_input].append(new_response)
        
        # if the prompt doesn't exist, then make a new list with that response
        else:
            prompts[user_input] = [new_response]
        
        
        # update the new prompt into the json file
        with open(prompts_json, "w") as file:
            json.dump(prompts, file, indent=2)
            
        
        print("Bot: ", end="", flush=True)
        typewriter("Thank you! I now understand how to respond. \n")


def remove_punctuation(text):
    cleaned_input = ""
    # loop over each character to remove punctuation
    for ch in text:
        # if its not a punctuation, add to the cleaned string
        if ch not in ["?", "!", ".", ","]:
            cleaned_input += ch
    
    return cleaned_input


# main loop
while True:
    user_input = input("You: ").lower().strip()

    user_input = remove_punctuation(user_input)
    
    # find the closest response to the prompt (NOTE: it returns a list)
    closest_match = difflib.get_close_matches(user_input, list(prompts), n=1, cutoff=0.6)

    # if there is a close match, print the relevant response
    if closest_match:
        # print the response
        print("Bot: ", end="", flush=True)
        closest_prompt = closest_match[0]
        
        random_response = random.choice(prompts[closest_prompt])
        
        typewriter(random_response)
        print()
        
        # after responding, ask if it wants to add another response to that prompt
        choice = input("Add another response (y/n)? ").lower().strip()
        # if they do, learn the response
        if choice == "y":
            learn()
        
        

    # otherwise, learn the response
    else:   
        learn()