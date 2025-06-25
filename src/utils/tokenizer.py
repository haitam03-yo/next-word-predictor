from torchtext.vocab import build_vocab_from_iterator
from torchtext.data.utils import get_tokenizer

class TorchTokenizer:
    def __init__(self):
        self.tokenizer = get_tokenizer("basic_english")  # Simple whitespace-based
        self.vocab = None

    def fit(self, texts: list[str]):
        def yield_tokens():
            for text in texts:
                yield self.tokenizer(text.lower())
        
        self.vocab = build_vocab_from_iterator(
            yield_tokens(),
            specials=["[PAD]", "[UNK]"],
            special_first=True
        )
        self.vocab.set_default_index(self.vocab["[UNK]"])

    def encode(self, text: str) -> list[int]:
        return self.vocab(self.tokenizer(text.lower()))

    def decode(self, ids: list[int]) -> str:
        return " ".join([self.vocab.lookup_token(idx) for idx in ids])