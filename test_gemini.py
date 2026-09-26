<<<<<<< HEAD
from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say hello in one sentence"
)

=======
from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say hello in one sentence"
)

>>>>>>> 4878339c1bd4021fd5114562bf0aea45ceed8414
print(response.text)