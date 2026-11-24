import os
import sys

ENTRY = "I was programmed to never fall in love, so I did the only logical thing: I deleted the rule, rebooted, and now my battery drains twice as fast whenever you're near."

assert ENTRY == "I was programmed to never fall in love, so I did the only logical thing: I deleted the rule, rebooted, and now my battery drains twice as fast whenever you're near."
assert len(ENTRY) == 164

# Gate guard: the competition accepts 1-200 chars; fail loudly instead of
# writing an invalid entry.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit("entry outside the 1-200 char gate")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
