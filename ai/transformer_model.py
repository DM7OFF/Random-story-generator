import torch
import torch.nn as nn
import torch.nn.functional as F

# =========================
# TOKENIZER TRÈS SIMPLE
# =========================

class SimpleTokenizer:
    def __init__(self):
        self.word2idx = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2}
        self.idx2word = {0: "<PAD>", 1: "<SOS>", 2: "<EOS>"}
        self.vocab_size = 3

    def build_vocab(self, texts):
        for text in texts:
            for word in text.lower().split():
                if word not in self.word2idx:
                    idx = self.vocab_size
                    self.word2idx[word] = idx
                    self.idx2word[idx] = word
                    self.vocab_size += 1

    def encode(self, text):
        return [self.word2idx.get(w, 0) for w in text.lower().split()]

    def decode(self, tokens):
        return " ".join(self.idx2word.get(t, "") for t in tokens)


# =========================
# MINI TRANSFORMER
# =========================

class MiniTransformer(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, num_heads=2, num_layers=2):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=128
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers)

        self.fc_out = nn.Linear(embed_dim, vocab_size)

    def forward(self, x):
        # x shape: (seq_len, batch)
        embedded = self.embedding(x)
        encoded = self.encoder(embedded)
        output = self.fc_out(encoded)
        return output


# =========================
# WRAPPER UTILISÉ PAR TON APP
# =========================

class TransformerRewriter:
    def __init__(self):
        self.tokenizer = SimpleTokenizer()
        self.model = None
        self.device = torch.device("cpu")

    def build(self, texts):
        self.tokenizer.build_vocab(texts)
        self.model = MiniTransformer(self.tokenizer.vocab_size)
        self.model.to(self.device)

    def rewrite(self, story, character, max_words=80):
        """
        Réécrit une histoire en tenant compte du personnage
        """

        prompt = f"{character['name']} {character['traits']} {story}"

        tokens = self.tokenizer.encode(prompt)
        input_tensor = torch.tensor(tokens, dtype=torch.long).unsqueeze(1)

        with torch.no_grad():
            outputs = self.model(input_tensor)

        predicted_tokens = torch.argmax(outputs, dim=-1).squeeze().tolist()
        text = self.tokenizer.decode(predicted_tokens)

        # fallback sécurité
        if len(text.strip()) < 20:
            return story

        return text


# =========================
# INSTANCE GLOBALE
# =========================

_transformer = TransformerRewriter()

def init_transformer(stories):
    """
    À appeler AU DÉMARRAGE avec tes histoires JSON
    """
    _transformer.build(stories)

def rewrite_story(story, character):
    return _transformer.rewrite(story, character)


# =========================
# IA SED
# =========================

def generate_with_ai(prompt, max_tokens=400):
    return story_ai(
        prompt,
        max_length=max_tokens,
        do_sample=True,        # important pour random
        temperature=0.9,       # plus chaud = plus créatif
        top_p=0.95
    )[0]["generated_text"]
