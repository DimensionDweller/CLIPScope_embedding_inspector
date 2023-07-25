from transformers import CLIPTokenizer, CLIPTextModel
from embedding_utils import get_embeddings
from visual_utils import visualize_nearest_neighbors
from interactive_widgets import create_input_widget, create_submit_button
from IPython.display import display
import torch

torch_device = "cuda" if torch.cuda.is_available() else "cpu"


# Load the tokenizer and text encoder
tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")

input_widget = create_input_widget()
submit_button = create_submit_button()

def on_submit(button):
    terms = [word.strip() for word in input_widget.value.split(",")]
    terms = terms[:10]
    embeddings = get_embeddings(terms, tokenizer, text_encoder)
    visualize_nearest_neighbors(terms, embeddings)

submit_button.on_click(on_submit)
display(input_widget, submit_button)
from IPython.display import display

