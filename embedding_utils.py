import torch
torch_device = "cuda" if torch.cuda.is_available() else "cpu"

def get_embeddings(terms, tokenizer, text_encoder):
    """
    Get embeddings for a list of terms.
    
    Args:
    - terms (list of str): Terms to get embeddings for.
    - tokenizer: Tokenizer for the text model.
    - text_encoder: Text encoder model.
    
    Returns:
    - dict: Dictionary of terms and their embeddings.
    """
    embeddings = {}
    for term in terms:
        input_text = tokenizer(term, return_tensors="pt").input_ids.to(torch_device)
        with torch.no_grad():
            embeddings[term] = text_encoder(input_text).pooler_output.squeeze().cpu().numpy()
    return embeddings
