"""Small application used by the Jenkins CI/CD lab."""


def greet(name):
    """Return the personalized greeting required by the lab."""
    return f"Hello, {name} from Nathalio Hassoun!"


if __name__ == "__main__":
    print(greet("World"))
