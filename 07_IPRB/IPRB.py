with open('rosalind_iprb.txt') as sets:
    for population in sets.readlines():
        k, m, n = map(float, population.split())
        t = k + m + n
        pk = k/t
        pm = m/t
        pn = n/t
        # Total probability
        prob = 1
        # Minus the probability of both parents being homozygous recessive
        prob -= pn * ((n-1)/(t-1))
        # Minus twice the probability of one being homozygous recessive and the other
        #one heterozygous with the recessive allele (this is the 0.5)
        prob -= 2 * pn * (m/(t-1)) * 0.5
        # Minus the probability of both being heterozygous with the recessive allele
        # (this is the 0.25)
        prob -= pm * ((m-1)/(t-1)) * 0.25
        print(prob)
