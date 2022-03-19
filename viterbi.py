import HMM

class Viterbi:
    def __init__(self, hmm):
        self.hmm = hmm

    def eval(self, o_lst):
        o_len = len(o_lst)
        o0 = o_lst[0]
        delta0 = []
        psi0 = []
        for q, q_p in enumerate(self.hmm.pi):
            delta0.append(q_p * self.hmm.b[q][o0])
        psi0 = [0.0] * self.hmm.q_n

        delta = [delta0]
        psi = [psi0]

        delta_t_1 = delta0

        for o in o_lst[1:]:
            delta_t = []
            psi_t = []

            for q in range(self.hmm.q_n):
                max_delta_t_q = 0.0
                max_psi_t_q = None
                for o_q in range(self.hmm.q_n):
                    delta_t_q = delta_t_1[o_q] * self.hmm.a[o_q][q]
                    if max_delta_t_q < delta_t_q:
                        max_delta_t_q = delta_t_q
                        max_psi_t_q = o_q
                delta_t.append(max_delta_t_q * self.hmm.b[q][o])
                psi_t.append(max_psi_t_q)

            delta.append(delta_t)
            psi.append(psi_t)
            delta_t_1 = delta_t

        max_delta_last = 0
        for qi, e in enumerate(delta[-1]):
            if max_delta_last < e:
                max_delta_last = e
                q = qi
        p = max_delta_last
        r_q = [q]
        for p_t in psi[-1:0:-1]:
            prev_q = p_t[q]
            r_q.append(prev_q)
            q = prev_q
            
        r_q.reverse()
        return r_q, p

if __name__ == '__main__':
    coin_hmm = HMM.HMM((0.5, 0.5), ((0.5, 0.5), (0.5, 0.5)), ((0.2, 0.8), (0.8, 0.2)), ('H', 'T'))

    #coin_hmm = HMM.HMM((0.5, 0.5, 0.0, 0.0), ((0.5, 0.3, 0.1, 0.1), (0.1, 0.4, 0.1, 0.4), (0.2, 0.4, 0.2, 0.2), (0.1, 0.5, 0.2, 0.2)), ((0.2, 0.8), (0.4, 0.6), (0.7, 0.3), (0.6, 0.4)), ('H', 'T'))

    q_lst , o_lst = coin_hmm.simulate(10)
    q_lst = [1, 0, 0, 0, 0, 1, 0, 0, 1, 1] 
    o_lst = [0, 1, 0, 1, 1, 0, 1, 1, 0, 0]
    d_lst = coin_hmm.translate(o_lst)
    print(d_lst)
    #print(q_lst, o_lst)

    vit = Viterbi(coin_hmm)
    v_q_lst, p = vit.eval(o_lst)
    print(q_lst, p)
    print(v_q_lst)
    sum = 0
    for q, v_q in zip(q_lst, v_q_lst):
        if ( q == v_q ) :
            sum += 1
    print(sum / len(v_q_lst))
