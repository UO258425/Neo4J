from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://polectron.xyz:7687", auth=("neo4j", "newneo4j"))


def print_gods_daughters(tx):
    print("These are all of the gods who have one or more daughters:")
    for record in tx.run("MATCH (p:God )-[:PARENT]->(o) where o.gender=$a RETURN DISTINCT p.name",a="Female"):
        print(record["p.name"])


def print_gods_not_married_to_gods(tx):
    print("These are all of the gods who are married to non gods:")
    for record in tx.run("MATCH p=(:God)-[:MARRIED]->(o) where not o:God RETURN p,labels(o)"):

        print(record["p"].nodes[0]["name"]+ " is married to "+record["p"].nodes[1]["name"]+" who is a "+record["labels(o)"][0])



with driver.session() as session:
    session.read_transaction(print_gods_daughters)
    session.read_transaction(print_gods_not_married_to_gods)

driver.close()