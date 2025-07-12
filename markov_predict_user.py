from chain import MarkovChain
import sys

def load_markov_chain(order):
    """
    Loads the trained markov chain
    """
    if order == "1":
        try:
            new_chain = MarkovChain.from_json('markov_chain_1st_order.json')
            print("Loaded 1st-order Markov Chain")
            return new_chain
        except FileNotFoundError:
            print("File not found. Please train 1st-order model first.")
            sys.exit(0)
    elif order == "2":
        try:
            new_chain = MarkovChain.from_json('markov_chain_2nd_order.json')
            print("Loaded 2nd-order Markov Chain")
            return new_chain
        except FileNotFoundError:
            print("File not found. Please train 2nd-order model first.")
            sys.exit(0)
    elif order == "3":
        try:
            new_chain = MarkovChain.from_json('markov_chain_3rd_order.json')
            print("Loaded 3rd-order Markov Chain")
            return new_chain
        except FileNotFoundError:
            print("File not found. Please train 3rd-order model first.")
            sys.exit(0)
    else:
        print("Invalid input. Choose 1, 2, or 3.")
        sys.exit(0)

def predict_next_word(state, chain, order):
    """
    Predicts the next word based on the current state
    """
    if order == "1":
        print("State: " + state[-1])
        prediction = chain.find_next_state(state[-1])
        return prediction
    elif order == "2":
        print("State: " + " ".join(state[-2:]))
        prediction = chain.find_next_state(" ".join(state[-2:]))
        return prediction
    elif order == "3":
        print("State: " + " ".join(state[-3:]))
        prediction = chain.find_next_state(" ".join(state[-3:]))
        return prediction
    else:
        return "Error: Invalid order"



typed = []
quit = False

order = input("Choose Markov chain order (1, 2, 3): ")
while order not in ["1", "2", "3"]:
    print("Invalid input. Enter 1, 2, or 3.")
    order = input("Choose Markov chain order (1, 2, 3): ")

chain = load_markov_chain(order)

print("\nType your input below.")
print(f"(Enter at least {order} word(s). Press ENTER to predict next word. Type 'q' to quit.)")

while not quit:
    print("\n(To exit, type 'q')")
    word = input("Type here --> ").split()
    typed.extend(word[:])

    if typed and typed[-1] == 'q':
        quit = True
        break
    elif len(typed) < int(order):
        print(f"Enter at least {order} word(s) total.")
    else:
        next_word = predict_next_word(typed, chain, order)
        print("Prediction:", next_word)

# --- Optional Save ---
save = input("\nDo you want to save your input to a file? (y/n): ").strip().lower()
if save in ['y', 'yes']:
    with open("user_input.txt", "w") as f:
        f.write(" ".join(typed[:-1]))  # Exclude 'q'
    print("Input saved to user_input.txt")

# --- Optional Retrain ---
retrain = input("Do you want to retrain the model with your input? (y/n): ").strip().lower()
if retrain in ['y', 'yes']:
    try:
        chain.train("user_input.txt")
        print("Retraining complete.")
    except UnicodeDecodeError:
        print("Error reading input file.")
