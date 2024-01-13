
import os


os.environ['OPENAI_API_KEY']='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'


from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
  image=open("/home/meron/Documents/work/tenacademy/week5/myweb3/outpu_image/final_certificate.png", "rb"),
  n=2,
  size="1024x1024"
)

image_url = response.data[0].url

print(image_url)