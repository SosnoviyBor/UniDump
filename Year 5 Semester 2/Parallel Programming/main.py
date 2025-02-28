from model import Model

if __name__ == "__main__":
    
    (Model(crystal_len=20,
           atom_count=200,
           move_left_chance=.5)
     .run(multiprocessed=True,
          print_snapshots=False,
          snapshot_count=10,
          iters_per_snapshot=50_000))
    
    
    (Model(crystal_len=20,
           atom_count=200,
           move_left_chance=.5)
     .run(multiprocessed=False,
          print_snapshots=False,
          snapshot_count=10,
          iters_per_snapshot=50_000))