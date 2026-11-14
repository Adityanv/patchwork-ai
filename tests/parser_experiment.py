from pathlib import Path

from patchwork_ai.repository.java_source_analyzer import JavaSourceAnalyzer
from patchwork_ai.repository.repository_scanner import RepositoryScanner

analyzer = JavaSourceAnalyzer()
scanner = RepositoryScanner(analyzer)

metadata_list = scanner.scan(Path("test_data/test_repository"))

for metadata in metadata_list:
    print("\n--------------------")
    print("File:", metadata.relative_path)
    print("Size:", metadata.file_size)
    print("Lines:", metadata.line_count)
    print("Package:", metadata.package_name)
    print("Classes:", metadata.class_names)
    print("Methods:", metadata.method_names)
    print("Imports:", metadata.imports)