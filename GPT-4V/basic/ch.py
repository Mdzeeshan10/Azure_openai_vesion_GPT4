from dotenv import dotenv_values
config_file_z = dotenv_values(".env")
print(config_file_z["GPT-4V_DEPLOYMENT_NAME"])


from dotenv import load_dotenv
import os
load_dotenv()
print("2")
print(os.getenv("OPENAI_API_KEY"))