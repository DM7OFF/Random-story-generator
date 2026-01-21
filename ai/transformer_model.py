from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# =========================
# MINI TRANSFORMER
# =========================
class MiniTransformer:
    def __init__(self, model_name="distilgpt2"):
        # Charge tokenizer et modèle
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32  # force float32
        )
        
        # Ajoute un token PAD si absent
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def rewrite(self, story: str, character: dict) -> str:
        # Prefixe structurel avec infos du personnage
        prefix = f"{character['name']} is a {character['role']}. {character['traits']}. "
        full_input = prefix + "\n" + story

        # Tokenize
        inputs = self.tokenizer(
            full_input,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        # Génération
        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=180,
                temperature=0.85,
                top_p=0.92,
                do_sample=True
            )

        # Décodage
        generated = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # On enlève le texte d’entrée pour garder uniquement la réécriture
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
