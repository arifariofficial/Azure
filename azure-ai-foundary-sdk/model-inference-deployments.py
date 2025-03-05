from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

try:
    # Initialize the project client
    project_connection_string = "swedencentral.api.azureml.ms;c5542233-b514-4b4f-8752-ca0868e17fb6;rg-arifulis-2330_ai;demo-project"

    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(),
        conn_str=project_connection_string,
    )

    ## Get a chat client
    chat = project_client.inference.get_chat_completions_client()

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question: ")

    response = chat.complete(
        model="gpt-35-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant that answers questions.",
            },
            {"role": "user", "content": user_prompt},
        ],
    )
    print(response.choices[0].message.content)
except Exception as ex:
    print(ex)
