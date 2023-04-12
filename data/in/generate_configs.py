# Generate your experiment configuration files here.

setup = {
    "pop_size": 30,
    "sol_lb": -5,
    "sol_ub": 5,
    "sel_perc": 50,
    "mut_perc": 10,
    "mut_n": 1,
    "indiv_l": 33,
    "max_iter": 150,
    "out_file": "sys.stdout",
    "runs": 3,
    "random_seed": 123_123_123,
}

i = 0
for pop_size in [10, 50, 90]:
    for selection in [50, 40]:
        for boundary in [10, 5, 3, 2]:
            with open(f'test-{i}.ini', 'w') as f:
                f.write('[algo]\n')
                setup["pop_size"] = pop_size
                setup["sel_perc"] = selection
                setup["sol_lb"] = -boundary
                setup["sol_ub"] = boundary
                setup["out_file"] = f"/mnt/data/out/test-{i}"
                for k, v in setup.items():
                    f.write(f'{k} = {v}\n')
                i += 1
