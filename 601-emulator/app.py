# <imports>
from gremlin_python.driver import client

# </imports>

# <client>
client = client.Client(
    url="ws://localhost:8901/",
    traversal_source="g",
    username="/dbs/db1/colls/coll1",
    password=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnq"
        "yMsEcaGQy67XIw/Jw=="
    ),
)
# </client>

# <graph>
client.submit(message="g.V().drop()")
# </graph>

# <insert>
client.submit(
    message=(
        "g.addV('product').property('id', prop_id).property('name', prop_name)"
    ),
    bindings={
        "prop_id": "68719518371",
        "prop_name": "Kiama classic surfboard",
    },
)
# </insert>
