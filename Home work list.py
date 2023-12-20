class List:
    def __init__(self):
        self.nodes = []

    def insert(self, coef, power):
        new_node = {"coef": coef, "power": power}
        index = 0
        while index < len(self.nodes) and self.nodes[index]["power"] > power:
            index += 1
        self.nodes.insert(index, new_node)

    def get(self, ind):
        if ind < 0 or ind >= len(self.nodes):
            raise Exception("Index out of bounds")
        node = self.nodes[ind]
        return f"coef: {node['coef']}, power: {node['power']}"

    def delete(self, ind):
        if ind < 0 or ind >= len(self.nodes):
            raise Exception("Index out of bounds")
        return self.nodes.pop(ind)

    def size(self):
        return len(self.nodes)

    def add(self, ind1, ind2):
        node1 = self.node_at(ind1)
        node2 = self.node_at(ind2)
        node1["coef"] += node2["coef"]
        self.delete(ind2)

    def multiply(self, ind1, ind2):
        node1 = self.node_at(ind1)
        node2 = self.node_at(ind2)

        if node1["power"] == node2["power"]:
            result_coef = node1["coef"] * node2["coef"]
            result_power = node1["power"]
            self.delete(ind1)
            self.delete(ind2)
            self.insert(result_coef, result_power)
        elif node1["coef"] == node2["coef"]:
            result_coef = node1["coef"]
            result_power = node1["power"] + node2["power"]
            self.delete(ind1)
            self.delete(ind2)
            self.insert(result_coef, result_power)
        else:
            raise Exception("Multiply operation cannot be done!")

    def node_at(self, ind):
        if ind < 0 or ind >= len(self.nodes):
            raise Exception("Index out of bounds")
        return self.nodes[ind]