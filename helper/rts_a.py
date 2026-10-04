# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    thwikicc = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD"
    main_page = "https://reitaisai.com/"

    i = 1  # ==== rts_a1 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")

        thwikicc_arts1 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC1%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "01_arts1.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            Medium(
                "01_copy-web_arts1.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20141024075716/http://reitaisai.com/arts1/circlelist/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東ホール",
                sources=[
                    Source(
                        thwikicc_arts1,
                        (ReliabilityTypes.Likely, OriginTypes.External),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                "秋季例大祭1",
                "博麗神社秋季例大祭1",
                "Hakurei Jinja Shuuki Reitaisai 1",
                "Autumn Reitaisai 1",
                "ARTS1",
                "第一回 博麗神社秋季例大祭",
            ],
            dates="2014.11.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20141024075725/http://reitaisai.com/arts1/circlelist/block/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20141024075716/http://reitaisai.com/arts1/circlelist/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts1} (well sourced)",
                    (ReliabilityTypes.Likely, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.09.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== rts_a2 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts2 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC2%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "02_a7ebdb67e824fa07619173061887136a.png",
                [
                    Source(
                        "https://web.archive.org/web/20151020131043/http://reitaisai.com/arts2/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第二回 博麗神社秋季例大祭",
            ],
            dates="2015.10.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20151017083305/http://reitaisai.com/arts2/circlelist-haichi",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts2} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.09.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== rts_a3 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts3 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC3%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "03_arts3.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            Medium(
                "03_46259336d607ed2221ac25c4a129300f.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20161111135729/http://reitaisai.com/arts3/685",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東1・2・3ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20151020062424/http://reitaisai.com/arts2",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第三回 博麗神社秋季例大祭",
            ],
            dates="2016.10.16",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20161111135729/http://reitaisai.com/arts3/685",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20230801072415/http://s.reitaisai.com/arts3/block123/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts3} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.09.30",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== rts_a4 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts4 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC4%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "04_arts4.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20170910145450/http://reitaisai.com/arts4/reitaisai_kaisaijouhou/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第四回 博麗神社秋季例大祭",
            ],
            dates="2017.10.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20170910145450/http://reitaisai.com/arts4/reitaisai_kaisaijouhou/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20230801040646/http://s.reitaisai.com/arts4/block/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts4} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== rts_a5 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts5 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC5%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "05_arts5.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            Medium(
                "05_arts5_top.png",
                [
                    Source(
                        "https://web.archive.org/web/20180602071006/http://reitaisai.com/arts5",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20180602071006/http://reitaisai.com/arts5",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第五回 博麗神社秋季例大祭",
            ],
            dates="2018.10.14",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20180602071006/http://reitaisai.com/arts5",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20190918092605/https://reitaisai.com/arts5/?page_id=307",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts5} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== rts_a6 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts6 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC6%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "06_arts6.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "06_6b580cbb5c3fc11d24545d595f8e595f-1.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190930144340/https://reitaisai.com/arts6/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト 西ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190930144340/https://reitaisai.com/arts6/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第六回 博麗神社秋季例大祭",
            ],
            dates="2019.10.06",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20190930144340/https://reitaisai.com/arts6/",
                    (ReliabilityTypes.Likely, OriginTypes.External),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20251016125327/http://s.reitaisai.com/arts6/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts6} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== rts_a7 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts7 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC7%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "07_arts7.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "07_fb8f87a90080e46dedb9c588ee75142e.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20200629123900/https://reitaisai.com/arts7/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "07_fdc236847103a636ee8c144024c094c7.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20201101131725/https://reitaisai.com/arts7/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト 西ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20201101131725/https://reitaisai.com/arts7/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第七回 博麗神社秋季例大祭",
            ],
            dates="2020.10.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260921220654/https://reitaisai.com/arts7/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20251114105029/https://reitaisai.com/arts7/%E3%80%90%E9%85%8D%E7%BD%AE%E7%95%AA%E5%8F%B7%E9%A0%86%E3%80%91%E3%82%B5%E3%83%BC%E3%82%AF%E3%83%AB%E9%85%8D%E7%BD%AE/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts7} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== rts_a8 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts8 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC8%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "08_arts8.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "08_e4d67c444a24c5db518c592a05660c6a.png",
                [
                    Source(
                        "https://web.archive.org/web/20211026074828/https://reitaisai.com/arts8/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト青海展示棟",
                sources=[
                    Source(
                        "https://web.archive.org/web/20211026074828/https://reitaisai.com/arts8/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第八回 博麗神社秋季例大祭",
            ],
            dates="2021.10.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20211026074828/https://reitaisai.com/arts8/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20251020190006/https://reitaisai.com/arts8/circlelist_1/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts8} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.01",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 9  # ==== rts_a9 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts9 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC9%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "09_arts9.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "09_73df15bb7b794341eef9c8f3acf2ffae-1.png",
                [
                    Source(
                        "https://web.archive.org/web/20260921220653/https://reitaisai.com/arts9/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://web.archive.org/web/20240529124425/https://reitaisai.com/arts9/wp-content/uploads/sites/30/2022/09/ARTS9_map-for-circle.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20240529124425/https://reitaisai.com/arts9/wp-content/uploads/sites/30/2022/09/ARTS9_map-for-circle.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "https://reitaisai.com/arts9/wp-content/uploads/sites/30/2022/09/ARTS9_DigiAnaAlmighty_1.1.1-1.pdf",
                [
                    Source(
                        "https://reitaisai.com/arts9/wp-content/uploads/sites/30/2022/09/ARTS9_DigiAnaAlmighty_1.1.1-1.pdf",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト西ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260921220653/https://reitaisai.com/arts9/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第九回 博麗神社秋季例大祭",
            ],
            dates="2022.10.23",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260921220653/https://reitaisai.com/arts9/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20260618044656/https://reitaisai.com/arts9/place-assign/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts9} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.04",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 10  # ==== rts_a10 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts10 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC10%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "10_arts10.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "10_8089e50294910c6cb163e5cb54ad137b.png",
                [
                    Source(
                        "https://web.archive.org/web/20260921220653/https://reitaisai.com/arts10/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト西ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260921220653/https://reitaisai.com/arts10/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第十回 博麗神社秋季例大祭",
            ],
            dates="2023.11.12",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260921220653/https://reitaisai.com/arts10/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20251018162134/https://reitaisai.com/arts10/place-assign-announce/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts10} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.04",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 11  # ==== rts_a11 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts11 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC11%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "11_arts11.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "11_ARTS11_WebTopImg_Catalog_Pc.png",
                [
                    Source(
                        "https://web.archive.org/web/20260512005259/https://reitaisai.com/arts11/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト南1~4ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260512005259/https://reitaisai.com/arts11/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第十一回 博麗神社秋季例大祭",
            ],
            dates="2024.10.20",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260512005259/https://reitaisai.com/arts11/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20260512005316/https://reitaisai.com/arts11/circle-place-assign/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts11} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.04",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 12  # ==== rts_a12 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts12 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC12%E5%B1%8A%E6%91%8A%E4%BD%8D/%E3%83%87%EF%BD%9E%E3%81%93%E9%83%A8%E5%88%86"

        media_ = [
            Medium(
                "12_arts12.jpg",
                [Source(main_page, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
            Medium(
                "12_ARTS12_top_catalog_pc.png",
                [
                    Source(
                        "https://web.archive.org/web/20260921220655/https://reitaisai.com/arts12/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト西ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260921220655/https://reitaisai.com/arts12/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第十二回 博麗神社秋季例大祭",
            ],
            dates="2025.10.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260921220655/https://reitaisai.com/arts12/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20251213135528/https://reitaisai.com/arts12/circle-place-assign/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts12} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.04",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 13  # ==== rts_a13 ====
    if i not in disabled_events:
        event_name = f"rts_a{i}"
        print(f"Processing {event_name} ...")
        thwikicc_arts13 = "https://thwiki.cc/%E5%8D%9A%E4%B8%BD%E7%A5%9E%E7%A4%BE%E7%A7%8B%E5%AD%A3%E4%BE%8B%E5%A4%A7%E7%A5%AD/%E7%AC%AC13%E5%B1%8A%E6%91%8A%E4%BD%8D"

        media_ = [
            Medium(
                "13_sp.png",
                [
                    Source(
                        "https://web.archive.org/web/20260921220629/https://reitaisai.com/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "13_PC-1.png",
                [
                    Source(
                        "https://web.archive.org/web/20261004143659/https://reitaisai.com/arts13/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.6284445, 139.7926734),
                address="3 Chome-11-1 Ariake, Koto City, Tokyo 135-0063, Japan",
                description="東京ビッグサイト東ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20261004143659/https://reitaisai.com/arts13/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmniRNV84lzB1SNXuy60c0lznxgbqmNtYyJ8rkHQXk9u4qwSBeDafMEeWY7SaHOPcgw9m9BObYv4SvxJATFOtwEErABiE-oZjeBkl96ni8hTFClnpIJNnLLpRCBg6Ue9K__BWAAVQ=s0?imgmax=0",
                url="https://maps.app.goo.gl/6EYu64eY7PRhWRxu7",
            ),
        ]
        event = Event(
            aliases=[
                f"秋季例大祭{i}",
                f"博麗神社秋季例大祭{i}",
                f"Hakurei Jinja Shuuki Reitaisai {i}",
                f"Autumn Reitaisai {i}",
                f"ARTS{i}",
                "第十三回 博麗神社秋季例大祭",
            ],
            dates="2026.10.04",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20261004143659/https://reitaisai.com/arts13/", (RT.Reliable, OT.Official)),
                Source(
                    "Participating circles (1): https://web.archive.org/web/20260921221051/https://reitaisai.com/arts13/circle-place-assign/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    f"Participating circles (2): {thwikicc_arts13} (well sourced)",
                    (ReliabilityTypes.Reliable, OriginTypes.External),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.04",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =  # ==== rts_a ====
    # if i not in disabled_events:
    #     event_name = f"rts_a{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"秋季例大祭{i}",
    #             f"博麗神社秋季例大祭{i}",
    #             f"Hakurei Jinja Shuuki Reitaisai {i}",
    #             f"Autumn Reitaisai {i}",
    #             f"ARTS{i}",
    #             @@
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.10.04",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_20161007055000_logo.png",
            [
                Source(
                    "https://web.archive.org/web/20161007055000/http://reitaisai.com/arts3/setsuei",
                    (RT.Reliable, OT.Official),
                )
            ],
        ),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["https://reitaisai.com/", "https://x.com/HakureijinjyaS", "https://www.youtube.com/channel/UCWgWAk02r-HKSYX2h6wnJVA"]


    event_group = EventGroup(
        aliases=["博麗神社秋季例大祭", "Hakurei Jinja Shuuki Reitaisai", "秋季例大祭", "Autumn Reitaisai", "ARTS"],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.01",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
