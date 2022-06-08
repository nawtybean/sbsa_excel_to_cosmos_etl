from typing import List
from azure.cosmos import database, exceptions, CosmosClient

def get_nnaa_filter_data(client: CosmosClient, database_id: str, container_id: str, column_names: List[str]) -> List:
    result = []
    try:
        database_proxy = client.get_database_client(database_id)
        container_proxy = database_proxy.get_container_client(container_id)
        for item in container_proxy.read_all_items(max_item_count=10):
            data = []
            for column_name in column_names:
                data.append(item.get(column_name))
            result.append(tuple(data))
    except:
        result = []
    return result
