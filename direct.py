import HMM

class DirectMethod:
    def __init__(self, hmm, o_lst):
        self.hmm = hmm
        self.o_lst = o_lst
        self.o_len = len(o_lst)

    def eval(self):
        max_n = self.hmm.q_n ** self.o_len
        sum_p = 0.0
        for qs_v in range(max_n):
            target_qs = qs_v
            p = 1.0
            p_set = self.hmm.pi
            for i, o in enumerate(self.o_lst):
                target_qs, q = divmod(target_qs, self.hmm.q_n)

                p *= p_set[q] * self.hmm.b[q][o]
                p_set = self.hmm.a[q]
            sum_p += p

        return sum_p

if __name__ == '__main__':
    coin_hmm = HMM.HMM((0.5, 0.5), ((0.5, 0.5), (0.5, 0.5)), ((0.2, 0.8), (0.8, 0.2)), ('H', 'T'))
    q_lst , o_lst = coin_hmm.simulate(10)
    d_lst = coin_hmm.translate(o_lst)
    print(d_lst)

    dm = DirectMethod(coin_hmm, o_lst)
    p = dm.eval()
    print(p, p * (2 ** 10))
    
