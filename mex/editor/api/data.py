from typing import Any

from fastapi import APIRouter

router = APIRouter()

_sample_data = [
    {
        "title": "Heading 1",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Heading 2",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Heading 3",
        "text": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
        "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed"
        "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet"
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    },
    {
        "title": "Heading 4",
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
