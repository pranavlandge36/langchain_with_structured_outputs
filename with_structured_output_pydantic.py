from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
from typing import Literal , Optional

import os
load_dotenv()
from pydantic import BaseModel , Field

model = ChatOpenAI(
    model="openai/gpt-4o-mini",  # or any model from OpenRouter
    api_key=os.getenv("openai"),
    base_url="https://openrouter.ai/api/v1",
)
class Review(BaseModel):
    summary: str = Field(description='discuss entire review in short ')
    keythemes: list[str] = Field(description='list all key themes discussed in review')
    rating:float=Field(ge=0.0,le=10.0,description='rate the product based on review')
    sentiment: Literal['positive','negative','neutral']=Field(description='give sentiment of review as neagtive, positive or neutral')
    pros:Optional[list[str]]=Field(description='list down pros if present in review')
    cons:Optional[list[str]]=Field(description='list down cons if present in review')
    reviewer:Optional[str]=Field(description='give name of reviewer if present')
    


msg='''I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Pranav Sanjay Landge'''

structured_model=model.with_structured_output(Review)

print("Calling model...")
result = structured_model.invoke(msg)
print(result)
print(result.reviewer)
print("Got response!")

