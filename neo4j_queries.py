from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://polectron.xyz:7687", auth=("neo4j", "newneo4j"))


def print_sons_of(tx, a, b):
    print("Sons of {0} and {1}".format(a, b))
    for record in tx.run("MATCH p=(:God {name:$a})-[:PARENT]->()<-[:PARENT]-(:God {name:$b}) RETURN p", a=a, b=b):
        print(record["p"].nodes[1]["name"])


def print_descendants_of(tx, a):
    print("Descendants of {0}".format(a))
    for record in tx.run("MATCH p=(:God {name:$a})-[:PARENT]->(n)-[*]->(m) RETURN p", a=a):
        for i in range(len(record["p"].nodes)):
            end_char = "->"
            if i == len(record["p"].nodes) - 1:
                end_char = ""
            print(record["p"].nodes[i]["name"], end=end_char)
        print("")


with driver.session() as session:
    session.read_transaction(print_sons_of, "Gaia", "Uranus")
    session.read_transaction(print_descendants_of, "Zeus")

driver.close()
