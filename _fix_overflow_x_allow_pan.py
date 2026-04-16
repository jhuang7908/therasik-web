"""Allow horizontal pan/scroll when content exceeds viewport (replace overflow-x: hidden -> auto)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def patch(text: str) -> str:
    # Order matters: longest / most specific first
    text = text.replace("overflow-x: hidden !important", "overflow-x: auto !important")
    text = text.replace("overflow-x: hidden;", "overflow-x: auto;")
    text = text.replace("overflow-x:hidden;", "overflow-x:auto;")
    text = text.replace("overflow-x:hidden}", "overflow-x:auto}")
    text = text.replace("overflow-x: hidden}", "overflow-x: auto}")
    return text


def main():
    for name in sorted(os.listdir(HERE)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(HERE, name)
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        new = patch(raw)
        if new != raw:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(new)
            print("updated:", name)
        else:
            print("skip:", name)


if __name__ == "__main__":
    main()
