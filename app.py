"""Project B — Simple data processing API."""


def process_data(items):
    """Process a list of items and return summary stats."""
    if not items:
        return {"count": 0, "total": 0, "average": 0}

    total = sum(items)
    return {
        "count": len(items),
        "total": total,
        "average": round(total / len(items), 2),
    }


def filter_items(items, min_value=None, max_value=None):
    """Filter items by min/max value range."""
    result = items
    if min_value is not None:
        result = [x for x in result if x >= min_value]
    if max_value is not None:
        result = [x for x in result if x <= max_value]
    return result
