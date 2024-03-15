

from poly_sbst.generators.abstract_generator import AbstractGenerator
import numpy as np
import string
import random
import typing
from poly_sbst.common.abstract_grammar import AbstractGrammar


class urlGenerator(AbstractGenerator):

    """urlGenerator is a generator that generates random url inputs."""

    def __init__(self) -> None:
        super().__init__()
        self._name = "urlGenerator"
        self.min_length = 2
        self.max_length = 40

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x:np.ndarray, y:np.ndarray) -> float:
        return 0.0


    def generate_random_test(self) -> str:
        return self.generate_random_string(
            random.randint(self.min_length, self.max_length)
        )
    
    def generate_random_string(self, length) -> str:
        cgi_grammar = {
            "<start>": ["<url>"],
            "<url>": ["<scheme>://<host>/<path>"],
            "<scheme>": ["http", "https"],
            "<host>": ["<domain>", "<ip>"],
            "<domain>": ["<subdomain>.<body>.<tld>"],
            "<body>": ["<word>", "<randomtext>"],
            "<randomtext>": ["<randomtext><letter>","<letter>"],
            "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
            "<subdomain>": ["www", "forum", "api"],
            "<tld>": ["com", "net", "org", "edu", "gov", "eg" ,"ca" , "jp"],
            "<ip>": ["<ipp>.<ipp>.<ipp>.<ipp>"],
            "<ipp>": ["<digit>", "<digit><digit>", "1<digit><digit>", "25<digit>"],
            "<path>": ["/", "/<segment>"],
            "<segment>": ["<segment>/<segment>", "<word>"],
            "<word>": ["index", "home", "folder", "file", "something"],
            "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}

        CGIgrammar = AbstractGrammar(cgi_grammar)
        cgi_input = ""
        
        while len(cgi_input) < length:
            new_part = CGIgrammar.generate_input()
            if len(cgi_input) + len(new_part) <= length:
                cgi_input += new_part
            else:
                break
            
        return cgi_input

