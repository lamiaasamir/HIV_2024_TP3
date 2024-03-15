import random


def generate_random_html_page():
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
    attributes = ['class="some-class"', 'id="some-id"', 'style="color:red"', 'href="https://example.com"', 'src="image.jpg"']

    # Randomly select tags and attributes
    num_tags = random.randint(1, 5)
    html_content = ''
    open_tags = []

    for _ in range(num_tags):
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

print(generate_random_html_page())