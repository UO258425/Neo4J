from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "newneo4j"))



def printPageRankMarriages(tx):
    print("PageRank applied to gods and marriages:")
    for record in tx.run("CALL algo.pageRank.stream('God', 'MARRIED', {iterations:100, dampingFactor:0.85}) YIELD nodeId, score RETURN algo.asNode(nodeId).name AS page,score ORDER BY score DESC "):
        print(record["page"]+ " " + str(record["score"]) )




with driver.session() as session:
    session.read_transaction(printPageRankMarriages)

driver.close()
