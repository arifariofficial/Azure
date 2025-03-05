from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

try:
    # Get project client
    project_connection_string = "swedencentral.api.azureml.ms;c5542233-b514-4b4f-8752-ca0868e17fb6;rg-arifulis-2330_ai;demo-project"
    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=project_connection_string,
    )
    # Get the properties of the default Azure AI Services connection with credentials
    connection = project_client.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SERVICES,
        include_credentials=True,
    )
    # Use the connection information to create a text analytics client
    ai_svc_credential = AzureKeyCredential(connection.key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=connection.endpoint_url, credential=ai_svc_credential
    )
    # Use the Language service to analyze some text (to infer sentiment)
    text = "I loved the movie. It was so quick!"
    sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
    print("Text: {}\nSentiment: {}".format(text, sentimentAnalysis.sentiment))

except Exception as ex:
    print(ex)
