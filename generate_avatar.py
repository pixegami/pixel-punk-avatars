from avatar_generator import AvatarGenerator


def generate_avatar():
    generator = AvatarGenerator("./images")
    generator.generate_avatar(100)


if __name__ == "__main__":
    generate_avatar()
