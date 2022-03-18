import random

class Coin:
    def __init__(self, heads):
        self.heads = heads

    def get_state(self):
        return 'H' if ( random.random() < self.heads) else 'T'

class CoinBag:
    def __init__(self, coins):
        self.coins = coins

    def get_state(self):
        clen = len(self.coins)
        index = int(random.random() * clen)
        coin = self.coins[index]
        return index, coin.get_state()

if __name__ == '__main__':
    coin0 = Coin(0.8)
    coin1 = Coin(0.2)
    cb = CoinBag((coin0, coin1))
    for i in range(10):
        o = (cb.get_state())[1]
        print(o)
        
    
