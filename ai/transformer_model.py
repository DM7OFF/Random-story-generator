import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# =========================
# MINI TRANSFORMER
# =========================

class MiniTransformer:
    def __init__(self, model_name="distilgpt2"):
        self.device = torch.device("cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def rewrite(self, story: str, character: dict) -> str:
        context = (
            f"{character['name']} is a {character['role']}. "
            f"Personality: {character['traits']}. "
            f"Writing level: {character['level']}.\n\n"
        )

        full_input = context + story

        inputs = self.tokenizer(
            full_input,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=180,   # <-- fixé ici
                do_sample=True,
                temperature=0.85,
                top_p=0.92
            )

        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated[len(full_input):].strip()


# =========================
# INSTANCE GLOBALE
# =========================

_transformer = None

def init_transformer():
    global _transformer
    if _transformer is None:
        _transformer = MiniTransformer()

def rewrite_story(story, character):
    if _transformer is None:
        raise RuntimeError("Transformer not initialized")
    return _transformer.rewrite(story, character)
