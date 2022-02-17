
import random
random.seed


class Source:
    GENES = ('G','T','C','A')
    def __init__(self) -> None:
        self.genome = []

class Strain(Source):
    def spawn(self, base_length):
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
        check = 0
        breaker = 0
        if mode == 1: breaker = len(self.threshold) + 1
        else: breaker = len(self.target) + 1
        if len(strain.genome) < len(self.target):
            return False
        for i in range((len(strain.genome) - len(self.target))):
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
        while True:
            counter += 1
            print('Iteration ', counter)
            mutator.evolve(strain)
            if self.survive(strain, 0) == True:
                print('Finished sequence: ', strain.genome)
                print('With target', self.target)
                break
            else: print('Intermedeate sequence:', strain.genome)
            if counter > self.itercap: break

def main():
    target = input('Input target')
    print('Target is', target)
    sample = Strain()
    sample.spawn(5)
    enviro = Selection()
    enviro.set_threshold(3)
    enviro.set_target(target)
    enviro.set_itercap(1000)
    enviro.select_print(sample)

main()