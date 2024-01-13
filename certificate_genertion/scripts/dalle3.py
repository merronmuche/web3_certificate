from openai import OpenAI
import os

os.environ['OPENAI_API_KEY']='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'
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="""I am seeking a design for a professional certificate for '10 Academy Intensive 
  Training Program.' The dimensions should be standard A4 size. The design should be classic 
  and elegant. The top third of the certificate should prominently feature the name '10 
  Academy Intensive Training Program' in a distinguished font, ensuring it's visually appealing
  but not overly large. Below this, I need a significant amount of whitespace, ideally occupying 
  at least half of the certificate's height, for the purpose of later adding a recipient's name 
  and the title of the course. This whitespace should be clear and unobstructed by any design 
  elements. The certificate can include a decorative border and subtle background patterns, but 
  these should not detract from the text's readability. A small, unobtrusive logo or seal may be 
  placed in the bottom corner. The overall design should convey professionalism and achievement,
  fitting for a prestigious training program.""",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
