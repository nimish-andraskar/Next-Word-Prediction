from chain import MarkovChain


mc = MarkovChain(2)


mc.train("sampledata.txt")



mc.to_json("markov_chain_3rd_order.json")

print("3rd-order Markov Chain trained and saved.")
