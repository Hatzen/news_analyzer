
import datetime
import weaviate
from news_analyzer.config import weaviate_url

def saveAll(result):
    

    client = weaviate.Client(
        url=weaviate_url,  # oder z. B. "https://your-cluster.weaviate.network"
    )
    class_obj = {
        "class": "OllamaResponse",
        "properties": [
            {"name": "content", "dataType": ["text"]},
            {"name": "timestamp", "dataType": ["date"]},
            {"name": "metadata", "dataType": ["text"]},
        ]
    }

    if not client.schema.contains(class_obj):
        client.schema.create_class(class_obj)


    response_data = {
        "content": "The AI assistant responded with ...",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "metadata": '{"model": "llama3", "tokens": 289}'
    }

    client.data_object.create(data_object=response_data, class_name="OllamaResponse")

    """
    results = client.query.get("OllamaResponse", ["content", "timestamp"]).with_limit(5).do()
    print(results)
    """
    