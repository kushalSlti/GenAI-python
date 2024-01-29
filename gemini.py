import google.generativeai as genai
from PyPDF2 import PdfReader 
  
# creating a pdf reader object 
reader = PdfReader('lease.pdf') 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 
extracted_text = ""
# getting a specific page from the pdf file 
for i in range(0,len(reader.pages)):
    page = reader.pages[i]  
    extracted_text += page.extract_text() 
 

GOOGLE_API_KEY="AIzaSyCQrTwz_0-Zk0QJIYWXz1FE4CmDoUq9CgM"
genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel('gemini-pro')



response = model.generate_content(f"Extract landlord name , tenant name , property name , rent , starting date , ending date from the following text :{extracted_text}" )

print(response.text)