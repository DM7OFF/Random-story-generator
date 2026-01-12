from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    trust_remote_code=True
)

def generate_text(prompt, max_tokens=600):
    output = generator(
        prompt,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        do_sample=True
    )

    return output[0]["generated_text"][len(prompt):].strip()
