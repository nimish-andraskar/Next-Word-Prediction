import random
import json
from collections import defaultdict

class MarkovChain:
    def __init__(self, order):
        self.order = order  
        self.chain = defaultdict(list)

    def train(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().lower().split()

        for i in range(len(text) - (self.order + 1)):
            key = ' '.join(text[i:i + self.order + 1])
            next_word = text[i + self.order + 1]
            self.chain[key].append(next_word)

    def find_next_state(self, state):
        state = state.lower()
        if state in self.chain:
            return random.choice(self.chain[state])
        else:
            return "No prediction available"

    def to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chain, f)

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as f:
            chain_data = json.load(f)

        if not chain_data:
            raise ValueError("The Markov Chain JSON is empty. Please retrain with a valid dataset.")

        sample_key = next(iter(chain_data))
        order = len(sample_key.split()) - 1

        mc = cls(order)
        mc.chain = defaultdict(list, {k: v for k, v in chain_data.items()})
        return mc
