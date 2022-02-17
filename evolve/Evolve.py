
import random
random.seed


class Source:
    GENES = ('G','T','C','A')
    def __init__(self) -> None:
        self.genome = []

class Strain(Source):
    def spawn(self, base_length):
        self.genome = []
        for i in range(base_length+1):
            self.genome.append(random.choice(self.GENES))



class Mutation(Source):
    def expand(self, strain):
        strain.genome.append(random.choice(self.GENES))
        print('Sequence expanded')

    def remove(self, strain):
        if len(strain.genome)>=1:
            strain.genome.pop(random.randrange(len(strain.genome)))
            print('Sequence cut down')

    def change(self, strain):
        if len(strain.genome)>=1:
            strain.genome[(random.randrange(len(strain.genome)))] =(
                random.choice(self.GENES))
        print('Sequence link changed')



class Mutate(Source):
    def set_mutrate(self, mutation_rate = 1):
        self.mutrate = mutation_rate

    def evolve(self, strain):
        mutator = Mutation()
        MUT_DIC = {
                0: mutator.expand,
                1: mutator.remove,
                2: mutator.change
                }
        for i in range(self.mutrate):
            MUT_DIC[random.randrange(3)](strain)

class Selection(Source):
    def set_target(self, target_seq):
        self.target = []
        target_seq.upper()
        for sym in target_seq:
            if sym in self.GENES:
                self.target.append(sym)

    def survive(self, strain, mode):
        if mode == 1: breaker = len(self.target)
        elif mode == 0: breaker = self.threshold
        if len(strain.genome) < len(self.target):
            return False
        for i in range((len(strain.genome) - len(self.target)+1)):
            check = 0
            for k in range(len(self.target)):
                if strain.genome[i+k] == self.target[k] : check += 1
                else: check = 0
                if check == breaker:
                    return True
        return False

    def set_threshold(self, threshold):
        self.threshold = threshold

    def set_popcap(self, popcap):
        self.popcap = popcap

    def set_itercap(self, itercap):
        self.itercap = itercap

    def select_print(self, strain):
        mutator = Mutate()
        counter = 0
        mutator.set_mutrate(1)
        pops = []
        pops.append(strain)
        evolved = False
        while True:   
            counter += 1
            print('Iteration ', counter)
            for specimen in pops:
                print('Population is:', len(pops))
                if counter > self.itercap: 
                    print('Iterations limit reached')
                    break
                mutator.evolve(specimen)
                
                print ('Specimen sequence: ', specimen.genome)
                
                if self.survive(strain, 1) == True:
                    print('Evolved!')
                    evolved = True
                    print('With target', self.target)
                    break
                elif self.survive(specimen, 0) == True:
                    print('Survived, duplicating')
                    pops.append(specimen)                
                else:
                    print('Died')
                    pops.remove(specimen)

                if len(pops) == 0:
                    print('Population extinct, reseeding...')
                    strain.spawn((len(self.target)+1))
                    pops.append(strain)
                    break

                elif len(pops) > self.popcap:
                    print('Population overcrowd, culling...')
                    sli = int(self.popcap/2)+1
                    pops = pops[0:sli]
                    break

            if counter > self.itercap: break
            if evolved: break



def main():
    target = 'GATTACA'
    threshold = 3
    iter =  5000
    popcap = 50
    sample = Strain()
    sample.spawn(len(target)+1)
    enviro = Selection()
    enviro.set_threshold(int(threshold))
    enviro.set_target(target)
    enviro.set_popcap(int(popcap))
    enviro.set_itercap(int(iter))
    print('Target is:', enviro.target)
    print('Over ', enviro.itercap, ' iterations. With ', enviro.popcap, ' popcap')
    enviro.select_print(sample)

main()