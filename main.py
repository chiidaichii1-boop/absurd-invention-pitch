import os

SENTENCE = (
    "The Parachute Toast: a slice of bread with a tiny parachute that "
    "pops open mid-fall, so it always lands butter-side up, drifting "
    "down like a tiny edible skydiver."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
