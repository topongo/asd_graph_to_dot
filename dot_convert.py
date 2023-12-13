from argparse import ArgumentParser
from sys import stdin, stderr

if __name__ == "__main__":
    parser = ArgumentParser(description="Convert asd barbie project input file file to dot file")
    parser.add_argument("input_file", help="Input file")
    parser.add_argument("--layout", default="dot", help="Layout to use", choices=["neato", "dot", "twopi", "circo", "nop", "nop1", "nop2", "osage", "patchwork", "fdp", "sfdp"])

    args = parser.parse_args()

    if args.input_file == "-":
        f = stdin
    else:
        f = open(args.input_file)
    try:
        l = f.readline()
        cities_n, roads_n = l.split()
        cities_n = int(cities_n)
        roads_n = int(roads_n)
        print(f"cities: {cities_n}, roads: {roads_n}", file=stderr)
        print("strict graph {")
        # for i in range(cities_n):
            # print(f"    {i}")
        
        connections = []
        readlines = f.__iter__()
        for _, l in zip(range(roads_n), readlines):
            c_s, c_e, c_w = l.split()
            connections.append((int(c_s), int(c_e), int(c_w)))

        l = next(readlines).strip()
        occupied_n = int(l)

        occupied = []
        for _, l in zip(range(occupied_n), readlines):
            occupied.append(int(l))

        print(f"    layout={args.layout}")
        print("    node [style=filled]")
        print("    B [fillcolor=pink]")
        print("    A [fillcolor=yellow]")
        for i in occupied:
            print(f"    {i} [fontcolor=white fillcolor=black]")

        for c_s, c_e, c_w in connections:
            if c_s == 0:
                c_s = "B"
            elif c_s == cities_n - 1:
                c_s = "A" 
            if c_e == 0:
                c_e = "B"
            elif c_e == cities_n - 1:
                c_e = "A"
            print(f"    {c_s} -- {c_e} [label={c_w}]")
        print("\n}")
    finally:
        if args.input_file != "-":
            f.close()

