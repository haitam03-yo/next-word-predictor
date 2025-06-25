import os


class DataPipeline():
    def __init__(self, data_dir='data/raw/'):
        self.data_dir = data_dir
        self.corpus = None
        
    def load_data(self):
        if not os.path.exists(self.data_dir):
            raise ValueError("Data directory not found")
        
        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('.txt'):
                file_path = os.path.join(self.data_dir, file_name)
                with open(file_path) as file:
                    content = file.read()
                    if self.corpus is None:
                        self.corpus = content
                    else:
                        self.corpus += "\n" + content
                        
    def get_corpus(self):
        if self.corpus is None:
            raise ValueError("Corpus is not loaded. Call load_data() first.")
        return self.corpus
    
    def build_vocabulary(self, max_vocab_size=20000):
        if self.corpus is None:
            raise ValueError("Corpus is not loaded. Call load_data() first.")
        
        