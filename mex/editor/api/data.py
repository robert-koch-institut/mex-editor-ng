from typing import Any

from fastapi import APIRouter

router = APIRouter()

_sample_data = [
    {
        "title": "Überschrift 1",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Überschrift 2",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Überschrift 3",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Überschrift 4",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
]


@router.get("/sample-data")
def sample_data() -> list[dict[str, Any]]:
    """Return the list of sample data items."""
    return _sample_data
