# <imports>
import os
from gremlin_python.driver import client, serializer

# </imports>

# <import_async_bug_fix>
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# </import_async_bug_fix>

# <environment_variables>
ACCOUNT_NAME = os.environ["COSMOS_GREMLIN_ENDPOINT"]
ACCOUNT_KEY = os.environ["COSMOS_GREMLIN_KEY"]
# </environment_variables>

print(ACCOUNT_NAME)
print(ACCOUNT_KEY)

# <authenticate_connect_client>
client = client.Client(
    url=f"wss://{ACCOUNT_NAME}.gremlin.cosmos.azure.com:443/",
    traversal_source="g",
    username="/dbs/cosmicworks/colls/products",
    password=f"{ACCOUNT_KEY}",
    message_serializer=serializer.GraphSONSerializersV2d0(),
)
# </authenticate_connect_client>

# <drop_graph>
client.submit(message="g.V().drop()")
# </drop_graph>

# <create_vertices_1>
client.submit(
    message=(
        "g.addV('product')"
        ".property('id', prop_id)"
        ".property('name', prop_name)"
        ".property('price', prop_price)"
        ".property('category', prop_partition_key)"
    ),
    bindings={
        "prop_id": "68719518371",
        "prop_name": "Kiama classic surfboard",
        "prop_price": 285.55,
        "prop_partition_key": "surfboards",
    },
)
# </create_vertices_1>

# <create_vertices_2>
client.submit(
    message=(
        "g.addV('product')"
        ".property('id', prop_id)"
        ".property('name', prop_name)"
        ".property('price', prop_price)"
        ".property('category', prop_partition_key)"
    ),
    bindings={
        "prop_id": "68719518403",
        "prop_name": "Montau Turtle Surfboard",
        "prop_price": 600.00,
        "prop_partition_key": "surfboards",
    },
)
# </create_vertices_2>

# <create_vertices_3>
client.submit(
    message=(
        "g.addV('product')"
        ".property('id', prop_id)"
        ".property('name', prop_name)"
        ".property('price', prop_price)"
        ".property('category', prop_partition_key)"
    ),
    bindings={
        "prop_id": "68719518409",
        "prop_name": "Bondi Twin Surfboard",
        "prop_price": 585.50,
        "prop_partition_key": "surfboards",
    },
)
# </create_vertices_3>

# <create_edges_1>
client.submit(
    message=(
        "g.V([prop_partition_key, prop_source_id])"
        ".addE('replaces')"
        ".to(g.V([prop_partition_key, prop_target_id]))"
    ),
    bindings={
        "prop_partition_key": "surfboards",
        "prop_source_id": "68719518403",
        "prop_target_id": "68719518371",
    },
)
# </create_edges_1>

# <create_edges_2>
client.submit(
    message=(
        "g.V([prop_partition_key, prop_source_id])"
        ".addE('replaces')"
        ".to(g.V([prop_partition_key, prop_target_id]))"
    ),
    bindings={
        "prop_partition_key": "surfboards",
        "prop_source_id": "68719518403",
        "prop_target_id": "68719518409",
    },
)
# </create_edges_2>

# <query_vertices_edges>
result = client.submit(
    message=(
        "g.V().hasLabel('product')"
        ".has('category', prop_partition_key)"
        ".has('name', prop_name)"
        ".outE('replaces').inV()"
    ),
    bindings={
        "prop_partition_key": "surfboards",
        "prop_name": "Montau Turtle Surfboard",
    },
)
# </query_vertices_edges>

# <output_vertices_edges>
print(result)
# </output_vertices_edges>
