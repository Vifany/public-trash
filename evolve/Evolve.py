
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

    def remove(self, strain):
        if len(strain.genome)>=1:
            strain.genome.pop(random.randrange(len(strain.genome)))
    
    def change(self, strain):
        strain.genome[(random.randrange(len(strain.genome)))] =(
            random.choice(self.GENES))



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
        for i in range(self.mutrate+1):
            MUT_DIC[random.randrange(2)](strain)

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
        survived = 0
        while True:
            counter += 1
            print('Iteration ', counter)
            mutator.evolve(strain)
            if self.survive(strain, 1) == True:
                print('Finished sequence: ', strain.genome)
                print('Survived for ', survived, ' generations')
                print('With target', self.target)
                break
            elif self.survive(strain, 0) == True:
                survived += 1
                print('Sequence: ', strain.genome)
                print('Survived for ', survived, ' generations, evolving...')
            else:
                survived = 0
                print('Sequence extinct: ', strain.genome)
                print('Reseeding...')
                strain.spawn(len(self.target)+1)
            if counter > self.itercap: break

def main():
    target = input('Input target')
    threshold = input('Input threshold')
    iter =  input('Input iteration cap')
    sample = Strain()
    sample.spawn(len(target)+1)
    enviro = Selection()
    enviro.set_threshold(int(threshold))
    enviro.set_target(target)
    print('Target is:', enviro.target)
    enviro.set_itercap(int(iter))
    enviro.select_print(sample)

main()