import re
from pathlib import Path
import aiofiles
import asyncio



async def load_text(file_path: str) -> str:
    """Load raw text from file."""
    # Your code here (handle file reading + errors)
    async with aiofiles.open('filename', mode='r', encoding='utf-8') as f:
        contents = await f.read()
    return contents

def clean_text(text: str) -> str:
    """Remove noise from text."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Keep alphanumeric + whitespace
    return text