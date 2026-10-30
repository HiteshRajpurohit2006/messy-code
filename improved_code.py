"""AFTER: the same script, cleaned up with AI assistance."""

def analyze_bounties(bounties: list[int]) -> dict:
    """Return total, average, highest and lowest bounty."""
    if not bounties:
        raise ValueError("Bounty list cannot be empty")
    total = sum(bounties)
    return {
        "total": total,
        "average": total / len(bounties),
        "highest": max(bounties),
        "lowest": min(bounties),
    }

if __name__ == "__main__":
    stats = analyze_bounties([300, 500, 1500, 3000])
    for label, value in stats.items():
        print(f"{label.capitalize()}: {value}")
