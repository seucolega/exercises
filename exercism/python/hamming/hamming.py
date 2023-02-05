def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return len([1 for base_a, base_b in zip(strand_a, strand_b) if base_a != base_b])
