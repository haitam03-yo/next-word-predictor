from utils import NLTKTokenizer  
tokenizer = NLTKTokenizer()  # or TorchTokenizer/TensorFlowTokenizer
tokenizer.fit(["Hello world!", "This is a test."])
print(tokenizer.encode("Hello unknown"))  # Should handle OOV
print(tokenizer.decode([2, 1]))          # Should map IDs back to text