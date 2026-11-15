from patchwork_ai.repository.repository_scanner import RepositoryScanner
from patchwork_ai.repository.java_source_analyzer import JavaSourceAnalyzer
from pathlib import Path

def test_discover_java_files(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)

    (tmp_path / "src").mkdir()
    (tmp_path / "target").mkdir()
    (tmp_path / ".git").mkdir()
    (tmp_path / "build").mkdir()

    (tmp_path / "src" / "PaymentService.java").write_text(
        "public class PaymentService {}"
    )
    (tmp_path / "target" / "Generated.java").write_text(
        "public class Generated {}"
    )
    (tmp_path / ".git" / "Internal.java").write_text(
        "public class Internal {}"
    )
    (tmp_path / "build" / "BuildFile.java").write_text(
        "public class BuildFile {}"
    )

    discovered_files = scanner.discover_java_files(tmp_path)

    assert len(discovered_files) == 1
    assert discovered_files[0].name == "PaymentService.java"

def test_scan_extracts_java_file_metadata(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)

    source_dir = tmp_path / "src" / "main" / "java"
    source_dir.mkdir(parents = True)
    java_file = source_dir / "PaymentService.java"
    java_file.write_text("""
    package com.example.payment;

    import java.util.List;

    public class PaymentService {
        public void processPayment() {
        }

        public boolean validatePayment() {
            return true;
        }
    }
    """)
    result = scanner.scan(tmp_path)
    assert len(result) == 1

    metadata = result[0]

    assert metadata.relative_path == (
        Path("src") / "main" / "java" / "PaymentService.java"
    )
    assert metadata.file_size == java_file.stat().st_size
    assert metadata.line_count == len(java_file.read_bytes().splitlines())
    assert metadata.package_name == "com.example.payment"
    assert metadata.class_names == ["PaymentService"]
    assert metadata.method_names == [
        "processPayment",
        "validatePayment"
    ]
    assert metadata.imports == ["java.util.List"]

def test_scan_returns_empty_list_for_empty_repository(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)
    source_dir = tmp_path / "src" / "main" / "java"
    source_dir.mkdir(parents = True)
    result = scanner.scan(tmp_path)
    assert result == []

def test_scan_extracts_multiple_java_file_accross_all_directories(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)

    source_dir = tmp_path / "src" / "main" / "java"
    module_dir = tmp_path / "modules" / "payment"
    source_dir.mkdir(parents = True)
    module_dir.mkdir(parents=True)
    java_files = ["PaymentService.java", "RefundService.java", "PaymentRepository.java"]
    java_file_1 = source_dir / "PaymentService.java"
    java_file_2 = source_dir / "RefundService.java"
    java_file_3 = module_dir / "PaymentRepository.java"
    java_file_1.write_text("public class PaymentService{}")
    java_file_2.write_text("public class RefundService{}")
    java_file_3.write_text("public class PaymentRepository{}")
    result = scanner.scan(tmp_path)
    discovered_java_files = {metadata.relative_path.name for metadata in result}
    assert discovered_java_files == {
        "PaymentService.java",
        "RefundService.java",
        "PaymentRepository.java"
    }

def test_scanner_excludes_nested_directories(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)

    source_dir = tmp_path / "repository" / "src"
    module_a_dir = tmp_path / "repository" / "module-a" / "src" / "target"
    module_b_dir = tmp_path / "repository" / "module-b" / ".git" 

    source_dir.mkdir(parents = True)
    module_a_dir.mkdir(parents = True)
    module_b_dir.mkdir(parents = True)
    java_file_1 = source_dir / "PaymentService.java"
    java_file_2 = module_a_dir / "Generated.java"
    java_file_3 = module_b_dir / "Internal.java"
    java_file_1.write_text("public class PaymentService{}")
    java_file_2.write_text("public class Generated{}")
    java_file_3.write_text("public class Internal{}")
    repository_root = tmp_path / "repository"
    result = scanner.scan(repository_root)
    discovered_files = {metadata.relative_path.name for metadata in result}
    assert discovered_files == {"PaymentService.java"}

def test_scanner_ignores_non_java_files(tmp_path):
    analyzer = JavaSourceAnalyzer()
    scanner = RepositoryScanner(analyzer)

    source_dir = tmp_path / "repository" / "src"

    source_dir.mkdir(parents = True)
    java_file = source_dir / "PaymentService.java"
    prop_file = source_dir / "application.properties"
    xml_file = source_dir / "pom.xml"
    readme_file = source_dir / "readme.md"
    config_file = source_dir / "config.xml"
    java_file.write_text("public class PaymentService{}")
    prop_file.write_text("public class PaymentService{}")
    xml_file.write_text("public class PaymentService{}")
    readme_file.write_text("public class PaymentService{}")
    config_file.write_text("public class PaymentService{}")
    repository_root = tmp_path / "repository"
    result = scanner.scan(repository_root)
    discovered_files = {metadata.relative_path.name for metadata in result}
    assert discovered_files == {"PaymentService.java"}
    