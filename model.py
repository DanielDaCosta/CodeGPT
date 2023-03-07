from transformers import GPT2Tokenizer, GPT2Model, GPT2LMHeadModel
from transformers import pipeline, set_seed

# generate text feature
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
text = "I like to sleep"
encoded_input = tokenizer(text, return_tensors = 'pt')
output = model(**encoded_input)
# print(output)

# generate text
input_ids = encoded_input.input_ids
gen_tokens = model.generate(
  input_ids,
  do_sample=True,
  temperature=0.9,
  max_length=20
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)