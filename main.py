"""make.fun entry: Ridiculous at First Glance, Real by the Second.

Writes one sentence pitching a bizarre startup that turns out to be a
real business to entry.txt in the output directory.
"""

import os

TEXT = (
    "We bottle genuine new-car smell and sell it to used-car dealers "
    "by the litre: one $30 spray per car lifts the average sale price "
    "by $400, so every dealership reorders monthly."
)


MAX_CHARS = 200


def validated_text() -> str:
    """Return the pitch, refusing anything the gate would reject."""
    text = TEXT.strip()
    if not text:
        raise SystemExit("entry text is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry text is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry text must be exactly one sentence")
    return text


def main() -> None:
    text = validated_text()
    payload = text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise SystemExit("written entry does not match the pitch bytes")


if __name__ == "__main__":
    main()
