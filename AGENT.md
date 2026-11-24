# Agent notes

Entry for make.fun competition `u-zeroxfive-monday-reviewed-in-one-line-e55de3c1`
("Monday, Reviewed in One Line").

- `main.py` is the entrypoint: Python standard library only (`import os`).
  It holds the review line as a constant and writes it, with no trailing
  newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- The line is an original one-line review of the entrant's own Monday:
  a deadpan 1-star rating, three concrete Monday disasters (alarm, inbox,
  coffee machine), and an absurd punchline at the end.
- No network, no third-party imports, no secrets.
