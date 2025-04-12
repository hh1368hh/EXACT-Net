from transformers import AutoTokenizer, AutoModel
import transformers
import torch


model = "meta-llama/Llama-2-13b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model)
# MM=AutoModel.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.bfloat16,
    device_map="cuda")
    
input_text="tell me a daddy joke"
# inputs=tokenizer.encode(input_text,return_tensors='pt')
# outputs=MM.generate(inputs, max_length=50)

# for output in outputs:
#     print(output)


import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

Report=getText('ANCaseReport1.docx')


ARTICLE=["where is the current determinate tumor or carcinoma or malignancy? " + Report]
sequences = pipeline(
    ARTICLE,
    # do_sample=True,
    # top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=700,
)




#sequences = pipeline(
#    input_text,
#    do_sample=True,
#    top_k=10,
#    num_return_sequences=1,
#    eos_token_id=tokenizer.eos_token_id,
#    max_length=700,
#)
print(sequences)