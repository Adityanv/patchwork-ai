from patchwork_ai.repository.java_source_analyzer import JavaSourceAnalyzer
import os
from pathlib import Path
from patchwork_ai.models.java_file_metadata import JavaFileMetadata


EXCLUDED_DIRECTORIES = {".git", 
                        "target", 
                        "build", 
                        "__pycache__", 
                        ".idea", 
                        ".venv"}

class RepositoryScanner:

    def __init__(self, java_source_analyzer):
        self.java_source_analyzer = java_source_analyzer

    def discover_java_files(self, repository_root: Path) -> list[Path]:
        java_files = []

        for current_path, directories, files in os.walk(repository_root):
            directories[:] = [
                directory
                for directory in directories
                if directory not in EXCLUDED_DIRECTORIES
            ]

            for file_name in files:
                if file_name.endswith(".java"):
                    java_files.append(Path(current_path)/file_name)

        return java_files
    
    def scan(self, repository_root: Path) -> list[JavaFileMetadata]:
        java_files = self.discover_java_files(repository_root=repository_root)
        list_java_file_metadata = []
        for java_file in java_files:
           source_code = java_file.read_bytes()
           file_size = len(source_code)
           relative_path = java_file.relative_to(repository_root)
           line_count = len(source_code.splitlines())
           java_file_metadata = JavaFileMetadata(relative_path=relative_path, 
                                                 file_size=file_size, 
                                                 line_count=line_count, 
                                                 **self.java_source_analyzer.analyze(source_code=source_code))
           list_java_file_metadata.append(java_file_metadata)
        return list_java_file_metadata

    