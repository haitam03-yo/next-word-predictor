import re
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_text(file_path: str) -> str:
    try:
        logger.info(f"Loading file: {file_path}")
        with Path(file_path).open('r', encoding='utf-8') as f:
            return f.read()
        
    except FileNotFoundError:
        logger.error(f"File {file_path} not found")
        raise ValueError(f"File {file_path} not found")
    
    except UnicodeDecodeError:
        logger.error(f"File {file_path} has encoding issues")
        raise ValueError(f"File {file_path} has encoding issues")
    
    except Exception as e:
        logger.error(f"Error loading {file_path}: {str(e)}")
        raise
    

def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Keep words + whitespace
    text = re.sub(r'\s+', ' ', text)     # Collapse multiple spaces
    return text
