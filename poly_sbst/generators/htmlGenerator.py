

from poly_sbst.generators.abstract_generator import AbstractGenerator
import numpy as np
import random


def generate_random_html_page(output_length):
    # List of possible HTML tags with their corresponding closing tags
    html_tags = {
        '<h1>': '</h1>',
        '<h2>': '</h2>',
        '<h3>': '</h3>',
        '<p>': '</p>',
        '<div>': '</div>',
        '<span>': '</span>',
        '<a>': '</a>',
        '<img>': ''
    }

    # List of possible attributes
    attributes = ['class="some-class"', 'id="some-id"', 'style="color:red"', 'href="https://helloworld.com"', 'src="image.jpg"']

    # Randomly select tags and attributes
    html_content = ''
    open_tags = []

    while len(html_content) < output_length:
        tag = random.choice(list(html_tags.keys()))
        attr = ' '.join(random.sample(attributes, random.randint(0, len(attributes))))
        closing_tag = html_tags[tag]

        html_content += f"{tag} {attr}>Content here"

        if closing_tag:
            html_content += f" {closing_tag}"
            open_tags.append(tag)

    # Close any remaining open tags
    for tag in reversed(open_tags):
        closing_tag = html_tags[tag]
        if closing_tag:
            html_content += closing_tag

    # Trim excess content if generated length exceeds the desired length
    html_content = html_content[:output_length]

    return html_content

# Example usage with output length of 1000 characters
print(generate_random_html_page(1000))




def generate_random_html_page(length):
    # List of possible HTML tags with their corresponding closing tags
    html_tags = {
        '<h1>': '</h1>',
        '<h2>': '</h2>',
        '<h3>': '</h3>',
        '<p>': '</p>',
        '<div>': '</div>',
        '<span>': '</span>',
        '<a>': '</a>',
        '<img>': ''
    }

    # List of possible attributes
    attributes = ['class="some-class"', 'id="some-id"', 'style="color:red"', 'href="https://helloworld.com"', 'src="image.jpg"']

    # Randomly select tags and attributes
    num_tags = random.randint(1, 5)
    html_content = ''
    open_tags = []

    while len(html_content) < length:
        tag = random.choice(list(html_tags.keys()))
        attr = ' '.join(random.sample(attributes, random.randint(0, len(attributes))))
        closing_tag = html_tags[tag]

        html_content += f"{tag} {attr}>Content here"

        if closing_tag:
            html_content += f" {closing_tag}"
            open_tags.append(tag)

    # Close any remaining open tags
    for tag in reversed(open_tags):
        closing_tag = html_tags[tag]
        if closing_tag:
            html_content += closing_tag

    return html_content

class htmlGenerator(AbstractGenerator):

    """htmlGenerator is a generator that generates random html inputs."""

    def __init__(self) -> None:
        super().__init__()
        self._name = "htmlGenerator"
        self.min_length = 2
        self.max_length = 40

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x:np.ndarray, y:np.ndarray) -> float:
        pass

    def generate_random_test(self) -> str:
        return self.generate_random_string(
            random.randint(self.min_length, self.max_length)
        )
    
    def generate_random_string(self, length) -> str:
        
        return generate_random_html_page(length)

