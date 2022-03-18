import copy
import direct
import HMM

class IterativeMethod:
    def __init__(self, hmm, o_lst):
        self.hmm = hmm
        self.o_lst = o_lst
        self.o_len = len(o_lst)

    def eval(self):
        o0 = self.o_lst[0]
        p_lst = []
        for q, q_p in enumerate(self.hmm.pi):
            print(q_p, self.hmm.b[q][o0])
            p_lst.append(q_p * self.hmm.b[q][o0])

        pset = self.hmm.a[o0]
        print('start', o0, p_lst)
        for o in self.o_lst[1:]:
            new_p_lst = [0.0] * self.hmm.q_n
            for o_q in range(self.hmm.q_n):
                pset = self.hmm.a[o_q]
                for q in range(self.hmm.q_n):
                    #print(new_p_lst[q])
                    new_p_lst[q] += (p_lst[q] * pset[q] * self.hmm.b[q][o])
                    #print(o_q, '->', q, ':', pset[q], '   o:', o, '  :', self.hmm.b[q][o], '  total:', p_lst[q], pset[q], self.hmm.b[q][o], '=>', new_p_lst[q])
            p_lst = new_p_lst
            #print(o, p_lst)
        p = 0.0
        for q_p in p_lst:
            p += q_p
        return p

if __name__ == '__main__':
    coin_hmm = HMM.HMM((0.5, 0.5), ((0.5, 0.5), (0.5, 0.5)), ((0.2, 0.8), (0.8, 0.2)), ('H', 'T'))

    coin_hmm = HMM.HMM((0.5, 0.5, 0.0, 0.0), ((0.5, 0.3, 0.1, 0.1), (0.1, 0.4, 0.1, 0.4), (0.2, 0.4, 0.2, 0.2), (0.1, 0.5, 0.2, 0.2)), ((0.2, 0.8), (0.4, 0.6), (0.7, 0.3), (0.6, 0.4)), ('H', 'T'))

    q_lst , o_lst = coin_hmm.simulate(100)
    d_lst = coin_hmm.translate(o_lst)
    print(d_lst)

    iter = IterativeMethod(coin_hmm, o_lst)
    p = iter.eval()
    print(p)

    dm = direct.DirectMethod(coin_hmm, o_lst)
    print(p)
    
