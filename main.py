import os

# One-line review of the entrant's own Monday: deadpan star rating,
# three concrete Monday disasters, absurd punchline last.
ENTRY = "Monday, 1 star: my alarm gave up, my inbox hit 214 unread by 8am, and the coffee machine filed for divorce before 9am."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
