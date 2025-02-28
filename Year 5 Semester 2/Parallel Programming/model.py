import multiprocessing as mp
import random
import time

import utils.coloring as clr
import utils.progress_bar as bar
import utils.txt as txt

class Model:
    def __init__(self, crystal_len:int, atom_count:int, move_left_chance:float):
        self.crystal_len = crystal_len
        # atoms are represented by their position in crystal
        self.atoms = [0 for _ in range(atom_count)]
        self.move_left_chance = move_left_chance
        self.crystal_states = []
    
    
    def run(self,
            multiprocessed:bool,
            print_snapshots:bool,
            snapshot_count:int,
            iters_per_snapshot:int) -> None:
        """Simply a wrapper function for run_multiprocesse() and run_singleprocess()"""
        if multiprocessed:
            print(txt.multi)
        else:
            print(txt.single)
            
        print(f"> Довжина кристалу:           {self.crystal_len}\n"+
              f"> Кількість атомів:           {len(self.atoms)}\n"+
              f"> Ймовірність переходу вліво: {self.move_left_chance * 100}%\n"+
              f"> Кількість знімків:          {snapshot_count}\n"+
              f"> Ітерацій між знімками:      {iters_per_snapshot}\n")

        if multiprocessed:
            start = time.perf_counter()
            self.run_multiprocess(snapshot_count, iters_per_snapshot)
            end = time.perf_counter()
        else:
            start = time.perf_counter()
            self.run_singleprocess(snapshot_count, iters_per_snapshot)
            end = time.perf_counter()
        
        if print_snapshots:
            print("> Знімки:")
            for snapshot in self.crystal_states:
                print(snapshot)
            print()
        
        print(f"> Час виконання: "+
              clr.wrap(str(round(end - start, 1)) + ' сек.', clr.Color.FG.GREEN) +
              "\n")
    
    
    def run_multiprocess(self, snapshot_count:int, iters_per_snapshot:int) -> None:
        # init progressbar
        bar.display(0, snapshot_count)
        manager = mp.Manager()
        
        for snapshot in range(snapshot_count):
            moved_atoms = manager.list([])
            # prepare args for mapping
            args = [(self.atoms[i],
                     iters_per_snapshot,
                     self.move_left_chance,
                     self.crystal_len,
                     moved_atoms)
                    for i in range(len(self.atoms))]
            
            # literally all the multithreading
            with mp.Pool() as pool:
                pool.map(self.atom_mover, args)

            # retrieve atoms' positions
            self.atoms = list(moved_atoms)
            # snapshot the crystal state
            self.crystal_states.append(self.get_crystal_struct())
            # update progressbar
            bar.display(snapshot+1, snapshot_count)
            
        # print the crystal the pretty way
        self.print_crystal()
    
    
    def atom_mover(self, args):
        # unpack args
        atom, iters, move_left_chance, crystal_len, results = args
        local_random = random.Random()
        
        for _ in range(iters):
            move_chance = local_random.uniform(0, 1)
            # move left
            if move_chance > move_left_chance and not atom >= crystal_len-1:
                atom += 1
            # or move right
            elif atom != 0:
                atom -= 1
        # return results
        results.append(atom)
    
    
    def run_singleprocess(self, snapshot_count:int, iters_per_snapshot:int) -> list[list[int]]:
        # init progressbar
        bar_total = snapshot_count * len(self.atoms)
        iters_total = 0
        local_random = random.Random(0)
        bar.display(0, bar_total)
        
        # for each snapshot
        for _ in range(snapshot_count):
            # for each atom
            for i in range(len(self.atoms)):
                # do X iters
                for _ in range(iters_per_snapshot):
                    move_chance = local_random.uniform(0, 1)
                    # move left
                    if move_chance > self.move_left_chance and not self.atoms[i] >= self.crystal_len-1:
                        self.atoms[i] += 1
                    # or move right
                    elif self.atoms[i] != 0:
                        self.atoms[i] -= 1
                    
                # update progressbar
                iters_total += 1
                bar.display(iters_total, bar_total)

            # snapshot the crystal state
            self.crystal_states.append(self.get_crystal_struct())
            
        # just to add empty line after progressbar
        print()
        # print the crystal the pretty way
        self.print_crystal()
        return self.crystal_states
    
    
    def print_crystal(self):
        msg = [
            "╔",
            "║",
            "╚"]
        for val in self.get_crystal_struct():
            digits = len(str(val))
            msg[0] += "═" * digits + "╤"
            msg[1] += str(val) + "┊"
            msg[2] += "═" * digits + "╧"
        msg[0] = msg[0][:-1] + "╗\n"
        msg[1] = msg[1][:-1] + "║\n"
        msg[2] = msg[2][:-1] + "╝"
        
        print("> Кінцевий вигляд кристалу\n" +
              clr.wrap("".join(msg), clr.Color.FG.CYAN) + "\n"
            #   left it in case you would want to check if all atoms are in place
            #   + f"> Усього атомів: {sum(self.get_crystal_struct())}\n"
              )
    
    
    def get_crystal_struct(self) -> list[int]:
        # count atoms in each segment of crystal
        crystal = [0 for _ in range(self.crystal_len)]
        
        for atom in self.atoms:
            crystal[atom] += 1
        
        return crystal