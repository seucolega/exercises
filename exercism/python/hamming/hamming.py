def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("A very specific bad thing happened.")
    return len([1 for compare_a, compare_b in zip(strand_a, strand_b) if compare_a != compare_b])
