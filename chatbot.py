# Import prerequisite libraries
import os
from openai import OpenAI
import streamlit as st

def chat(prompt):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Setting the API key
    # Define the prompt variable (the detailed instructions)
    instructions = """
    Your task is to extract structured information from the provided text and format it according to the following rules. Your output must exactly match the schema and type information described below.

    #### Schema for output:
    - **Root level**: 
        - A list of **strings** (comma-separated values) where each string provides a descriptive subtitle for a specific scene in the text.
        - A list of **queries** (comma-separated values) where each query provides a more detailed search term related to the specific scene.
        - Each string (both subtitles and queries) should be enclosed in **double quotations**.

    #### Extraction Rules:
    1. **Scene Breakdown**: 
        - Identify key moments or changes in the action of the text that can be considered "scenes."
        - Each scene should have a corresponding descriptive subtitle that summarizes the key action in a concise manner.
        - Limit the number of subtitles to a maximum of 6.
        - Number of queries equals the number of subtitles.

    2. **Subtitle Formatting Guidelines**:
        - Each subtitle should be short (maximum 15 words) and summarize the key information or action of the scene.
        - The subtitles should be output as **comma-separated strings**.
        - Enclose each subtitle in **double quotations**.

    3. **Query Formatting Guidelines**:
        - Each scene should also have a corresponding query for an image search engine.
        - The queries should be **more descriptive** than the subtitles to provide additional context for the search engine.
        - Each query should focus on key details of the scene (e.g., location, characters, objects, emotions).
        - Queries can exceed 15 words but should remain concise and relevant to the scene.

    4. **Scene Division**:
        - If any scene division is ambiguous or unclear, summarize based on the most logical action sequence.

    ### Example output structure:
    ["Subtitle for scene 1", "Subtitle for scene 2", "Subtitle for scene 3"]
    ["Query for scene 1 with detailed description", "Query for scene 2 with more context", "Query for scene 3 with extra detail for the image search engine"]

    #### Input Text:
    The input text will be provided by the user in the prompt. Please adhere to the schema and guidelines above.
    """

    # Example prompt: "Binary search also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array."

    # Create a chatbot using ChatCompletion.create() function
    completion = client.chat.completions.create(# Use GPT 3.5 as the LLM
    model="gpt-3.5-turbo",
    # Pre-define conversation messages for the possible roles
    messages=[
    {"role": "system", "content": instructions},
    {"role": "user", "content": prompt}
    ])
    # Get the returned output from the LLM model
    output = completion.choices[0].message.content

    # Specify the path for the output text file
    file_path = 'chat_output.txt'

    # Save the output to a text file
    with open(file_path, 'w') as file:
        file.write(output)

    # Read and print the contents of the text file for formatted output
    with open(file_path, 'r') as file:
        formatted_output = file.read()
        print(formatted_output) 