from chain import MarkovChain

new_chain = MarkovChain.from_json('markov_chain_2nd_order.json')
print(new_chain.find_next_state('it was'))

new_chain3 = MarkovChain.from_json('markov_chain_3rd_order.json')
print(new_chain3.find_next_state('it was a'))
