import ipywidgets as widgets

def create_input_widget():
    """
    Create and return an input widget for user words.
    """
    input_widget = widgets.Textarea(
        value='',
        placeholder='Enter up to ten words, separated by commas',
        description='Words:',
        disabled=False
    )
    return input_widget

def create_submit_button():
    """
    Create and return a submit button.
    """
    submit_button = widgets.Button(description="Submit")
    return submit_button
