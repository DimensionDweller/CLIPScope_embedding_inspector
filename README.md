# CLIPScope: Peering into the World of CLIP Embeddings.

This project provides an interactive visualization tool to explore the nearest neighbors in the embedding space produced by OpenAI's CLIP model. By inputting a set of terms, users can visualize the relationships and proximities of these terms in the embedding space, offering insights into the semantic associations made by the CLIP model.

### Example Visualization
https://github.com/DimensionDweller/CLIP_embedding_inspector/assets/75709283/c21e1f80-5b25-41f4-a060-b29ab2f88ebb
  
*Example using the terms: Women, Man, Boy, Girl, Puppy, Dog, Cat, Kitten.*

## Purpose

The primary aim of this tool is to:
1. **Understand Semantic Relationships**: By visualizing the nearest neighbors of terms in the embedding space, users can gain insights into how the CLIP model semantically groups different terms.
2. **Explore Potential Biases**: By examining the relationships between terms, it is possible to identify and understand potential biases in the model.
3. **Research and Education**: The tool can be used for educational purposes, allowing students and researchers to explore the intricacies of embedding spaces in deep learning models.

## Features

- **Interactive Input**: Users can input up to ten words to be visualized.
- **Dynamic Visualization**: The tool generates a directed graph showing the nearest neighbor relationships among the input terms.
- **Model Insights**: Leveraging the power of the CLIP model, the tool offers high-quality semantic embeddings for the terms.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone [(https://github.com/DimensionDweller/CLIP_embedding_inspector.git)]
   cd [DimensionDweller/CLIP_embedding_inspector/]
   ```

2. **(Optional) Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Main Script**:
   ```bash
   python main.py
   ```

2. **Interactive Usage**:
   - An interactive widget will appear.
   - Enter up to ten words separated by commas.
   - Click "Submit" to visualize the nearest neighbors in the embedding space.

## Contributing

Contributions are welcome! Please make sure to update tests as appropriate and follow the coding standards and conventions.

## License

[MIT](https://choosealicense.com/licenses/mit/)
