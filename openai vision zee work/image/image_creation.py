# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
# import os
# from openai import AzureOpenAI
# import json

# client = AzureOpenAI(
#     api_version="2023-12-01-preview",
#     azure_endpoint="https://nain-dev-gpt4.openai.azure.com/",
#     api_key="50909f7eb1c246b0bb5db13078af95ec",
# )

# result = client.images.generate(
#     model="Dalle3", # the name of your DALL-E 3 deployment
#     prompt="This image captures a tranquil scene of a natural landscape at either sunrise or sunset. The sky is a dramatic display of clouds with hints of blue and streaks of orange and yellow light, indicating the sun is just below the horizon. The scene is mirrored almost perfectly on the still surface of a body of water, likely a lake, creating a symmetrical reflection that adds to the serene beauty of the image. The silhouettes of trees and vegetation can be seen along the water's edge, completing this picturesque view. The overall effect is peaceful and calming.",
#     n=1
# )

# image_url = json.loads(result.model_dump_json())['data'][0]['url']

# print(image_url)


def image_gen(query):
    from openai import AzureOpenAI
    import json

    client = AzureOpenAI(
        api_version="2023-12-01-preview",
        azure_endpoint="https://nain-dev-gpt4.openai.azure.com/",
        api_key="50909f7eb1c246b0bb5db13078af95ec",
    )

    result = client.images.generate(
        model="Dalle3", # the name of your DALL-E 3 deployment
        prompt=query,
        n=1
    )

    image_url = json.loads(result.model_dump_json())['data'][0]['url']

    return image_url


query = str(input("Enter your image generation query : "))

print(image_gen(query))
