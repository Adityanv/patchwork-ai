from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class JavaFileMetadata:
    relative_path: Path
    file_size: int
    line_count: int
    package_name: str | None = None
    class_names: list[str] = field(default_factory = list)
    method_names: list[str] = field(default_factory = list)
    imports: list[str] = field(default_factory = list)

