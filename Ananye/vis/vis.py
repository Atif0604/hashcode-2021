from graphviz import Digraph
from tqdm import tqdm

filename = "b.txt"

dot = Digraph(comment=filename)

streets = []
street_dict = {}

with open(filename) as fh:
    d, i, s, v, f = [int(x) for x in fh.readline()[:-1].split()]

    for j in range(i):
        dot.node(str(j))

    for _ in tqdm(range(s), desc="Reading graph"):
        line = fh.readline().split()
        a, b, street, dur = line
        street_dict[street] = (a, b, dur)
        dot.edge(a, b)

with open("{}.dot".format(filename), 'w') as f:
    f.write(dot.source)

# dot.render("{}.png".format(filename), view=True)






