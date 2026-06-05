"""Helpers Module"""
from typing import Any, Dict, List


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict:
    """Flatten nested dictionary

    Args:
        d: Dictionary to flatten
        parent_key: Parent key prefix
        sep: Separator for nested keys

    Returns:
        Flattened dictionary
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def paginate(
    items: List[Any], skip: int = 0, limit: int = 10
) -> Dict[str, Any]:
    """Paginate items

    Args:
        items: Items to paginate
        skip: Number of items to skip
        limit: Maximum number of items to return

    Returns:
        Paginated response with metadata
    """
    total = len(items)
    data = items[skip : skip + limit]
    return {
        "data": data,
        "total": total,
        "skip": skip,
        "limit": limit,
        "page": (skip // limit) + 1 if limit > 0 else 1,
        "pages": (total + limit - 1) // limit if limit > 0 else 1,
    }
