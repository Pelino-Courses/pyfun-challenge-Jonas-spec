def format_text(
        text: str,
        prefix: str = "",
        suffix: str = "",
        capitalizer: bool = False,
        max_length: int = None
) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(prefix, str):
        raise TypeError("prefix must be a string")
    if not isinstance(suffix, str):
        raise TypeError("suffix must be a string")
    if not isinstance(capitalizer, bool):
        raise TypeError("capitalizer must be a boolean")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("max_length must be an integer or None")
        if max_length < 0:
            raise ValueError("max_length cannot be negative")

    if capitalizer:
        text = text.capitalize()

    formatted = f"{prefix}{text}{suffix}"

    if max_length is not None:
        formatted = formatted[:max_length]

    return formatted


if __name__ == "__main__":
    print(format_text("hello", prefix=">>", suffix="<<"))         # Output: >>hello<<
    print(format_text("hello", capitalizer=True))                 # Output: Hello
    print(format_text("hello world", max_length=5))              # Output: hello
