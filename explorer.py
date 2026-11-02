"""graphql-contrib-explorer: map a GitHub user's contributions.

This module is the starter scaffold for the tool. It defines the shape
of an exploration result and a main() entry point that states what the
tool will do once it is built out. The query engine, the part that
talks to the GitHub GraphQL API, is the next build step.
"""

from dataclasses import dataclass, field


@dataclass
class ExplorationResult:
    """The outcome of one contribution graph exploration."""

    username: str = ""
    organizations: list = field(default_factory=list)
    repositories: list = field(default_factory=list)
    notes: list = field(default_factory=list)


def main() -> None:
    print("graphql-contrib-explorer")
    print("This tool will map a GitHub user's contribution graph and")
    print("organizations with the GraphQL API: where the work happens,")
    print("how it clusters over time, and which organizations it")
    print("passes through.")
    print("Status: scaffold. The query engine is the next build step.")


if __name__ == "__main__":
    main()
