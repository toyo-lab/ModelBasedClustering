import random

class HMM:
    def __init__(self, pi, a, b, desc = None):
        self.pi = pi
        self.a = a
        self.b = b

        self.q_n = len(pi)
        self.q = None
        self.desc = desc

    def sel_index(self, lst):
        v = random.random()
        sum = 0.0
        for i, e in enumerate(lst):
            sum += e
            if v < sum:
                return i
        assert False, '確率のリストがおかしい'
        

    def simulate(self, n):
        self.q = self.sel_index(self.pi)
        o_lst = []
        q_lst = []
        for i in range(n):
            o = self.sel_index(self.b[self.q])
            o_lst.append(o)
            q_lst.append(self.q)
            self.q = self.sel_index(self.a[self.q])

        return q_lst, o_lst
            

    def translate(self, o_lst):
        assert self.desc != None, "表現がない"
        lst = []
        for e in o_lst:
            lst.append(self.desc[e])

        return lst

if __name__ == '__main__':
    coin_hmm = HMM((0.5, 0.5), ((0.5, 0.5), (0.5, 0.5)), ((0.2, 0.8), (0.8, 0.2)), ('H', 'T'))
    q_lst , o_lst = coin_hmm.simulate(10)
    d_lst = coin_hmm.translate(o_lst)
    print(d_lst)
    
