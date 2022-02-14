import os
import random


class Layer:
    def __init__(self, path: str):
        self.path = path
        self.rarity: float = 1.0

    def get_random_image_path(self):
        image_file_names = os.listdir(self.path)
        random_image_file_name = random.choice(image_file_names)
        return os.path.join(self.path, random_image_file_name)

    def should_generate(self) -> bool:
        return random.random() < self.rarity
