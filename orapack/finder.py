from returns.maybe import maybe
from sqlfluff.core.parser import BaseSegment


@maybe
def find_segment(
    start_segment: BaseSegment,
    segment_type: str,
) -> BaseSegment | None:
    """Find first segment by type in segment tree."""
    to_check = [start_segment]
    while to_check:
        segment = to_check.pop()
        if segment.type == segment_type:
            return segment
        to_check.extend(segment.segments)
    return None


def find_all_segments(
    start_segment: BaseSegment,
    segment_type: str,
) -> list[BaseSegment]:
    """Find all segments by type in segment tree."""
    to_check = [start_segment]
    found = []
    while to_check:
        segment = to_check.pop()
        if segment.type == segment_type:
            found.append(segment)
        to_check.extend(segment.segments)
    return found
