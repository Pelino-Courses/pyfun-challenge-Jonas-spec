def format_text(
        text: str,
        prefix: str = "",
        suffix: str = "",
        capitalizer: bool = False,
        max_length: int = None
) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(prefix,str):
        raise TypeError("prefix must be a string")
    if not isinstance(suffix, str):
      raise TypeError("suffix must be a string.")
   if not isinstance(capitalize, bool):
   raise TypeError("capitalize must be a boolean.")
   if max_length is not None:
   if not isinstance(max_length, int):
   raise TypeError("max_length must be an integer or None.")
      if max_length < 0:
    raise ValueError("max_length cannot be negative.")

if capitalize:
   text = text.capitalize()
   formatted = [:max_length]
return formatted
 
 if __name__== " __main__":
   print(format_text("hello", prefix=">>", siffix="<<"))
   print(format_text("hello", capitalize=True))
   print(format_text("hello world", max_length=5))
