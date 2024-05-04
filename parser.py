def parse_newick(tree_file):
    newick_tree = open(tree_file, 'r').readline().strip('();\n') + ','

    Graph_tree = {'Node_0': {}}
    clade_stack = ['Node_0']

    n_node = 1
    length = []
    name = []

    # leaf_name = ''
    # leaf_length = -1
    node_close = False

    for i, symbol in enumerate(newick_tree):

        if symbol == '(':
            last_node = clade_stack[-1]
            clade_stack.append(f'Node_{n_node}')
            Graph_tree[last_node][f'Node_{n_node}'] = None
            Graph_tree[f'Node_{n_node}'] = {last_node: None}
            n_node += 1

        elif symbol.isalpha():
            name.append(symbol)

        elif symbol == ':':
            if newick_tree[i - 1] == ')':
                continue
            else:
                leaf_name = ''.join(name)
                name = []

        elif symbol.isnumeric() or symbol == '.':
            if newick_tree[i - 2] == ')':
                node_close = True
                length.append(symbol)
            else:
                length.append(symbol)

        elif symbol == ' ':
            continue

        elif symbol in {',', ')'}:

            leaf_length = float(''.join(length))
            length = []

            if node_close:
                curr_node = clade_stack.pop()
                Graph_tree[clade_stack[-1]][curr_node] = leaf_length
                Graph_tree[curr_node][clade_stack[-1]] = leaf_length
                node_close = False
            else:
                Graph_tree[clade_stack[-1]][leaf_name] = leaf_length

    return Graph_tree


if __name__ == '__main__':
    print(
        parse_newick('animals.tree')
    )
