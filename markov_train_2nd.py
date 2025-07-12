from chain import MarkovChain

mc = MarkovChain(1)  


mc.train("sampledata.txt")


mc.to_json("markov_chain_2nd_order.json")

print("Training complete. Model saved.")
