def visualizador(node, prefix="", is_tail=True, role="Raiz"):
    if node is None:
        return
    connector = "└── " if is_tail else "├── "
    is_leaf = (node.getIzq() is None and node.getDer() is None)
    print(prefix + connector + f"{node.getValor()} ({role}{', Hoja' if is_leaf else ''})")
    children = []
    if node.getDer():
        children.append(("Derecha", node.getDer()))
    if node.getIzq():
        children.append(("Izquierda", node.getIzq()))
    new_prefix = prefix + ("    " if is_tail else "│   ")
    for i, (child_role, child) in enumerate(children):
        is_last = (i == len(children) - 1)
        visualizador(child, new_prefix, is_last, child_role)