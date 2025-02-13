from model import Model

if __name__ == "__main__":
    m = Model(crystal_len=20,
              atom_count=200,
              move_left_chance=.5)
    
    states = m.run_multiprocess(snapshot_count=10, iters_per_snapshot=50000)
    states = m.run_singleprocess(snapshot_count=10, iters_per_snapshot=50000)