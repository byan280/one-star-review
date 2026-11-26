# one-star-review: round 3 entry.
# A one-star review of a force of nature.
# Gravity has no customer service desk.
# The complaint is specific: the phone, twice, no apology.
# Output is a single line, nothing else.
# Round 3: written fresh in this session, verified deterministic.


def build_review():
    # The product under review, and the verdict.
    product = "Gravity"
    # One star. The grievance follows, in one breath.
    grievance = "works 24/7 with no off switch, dropped my phone twice, and has never once apologized."
    return "One star. " + product + ": " + grievance


def main():
    print(build_review())


if __name__ == "__main__":
    main()
