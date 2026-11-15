from patchwork_ai.repository.java_source_analyzer import JavaSourceAnalyzer

def test_extract_package_name():
    analyzer = JavaSourceAnalyzer()
    source_code = b"""
    package com.patchwork.payment;

    public class PaymentService {
    }
    """

    tree = analyzer.parser.parse(source_code)
    package_name = analyzer.extract_package_name(tree.root_node)

    assert package_name == "com.patchwork.payment"

def test_extrace_package_name_when_missing():
    analyzer = JavaSourceAnalyzer()
    source_code = b"""
    public class PaymentService {
        }
    """

    tree = analyzer.parser.parse(source_code)
    package_name = analyzer.extract_package_name(tree.root_node)

    assert package_name == None

def test_extract_class_names():
    analyser = JavaSourceAnalyzer()
    source_code = b"""package com.example;
    public class PaymentService {
        class PaymentValidator {
        }
    }

    class RefundService {
    }
    """
    tree = analyser.parser.parse(source_code)
    class_names = analyser.extract_class_names(tree.root_node)

    assert class_names == ["PaymentService", "PaymentValidator", "RefundService"]

def test_extrace_method_names():
    analyzer = JavaSourceAnalyzer()
    source_code = b"""
    public class PaymentService {
        public void processPayment() {
            validatePayment();
        }

        private boolean validatePayment() {
            return true;
        }

        class PaymentValidator {
            public void validate() {
            }
        }
    }

    class RefundService {
        public void processRefund() {
        }
    }
    """

    tree = analyzer.parser.parse(source_code)
    method_names = analyzer.extract_method_names(tree.root_node)

    assert method_names == [
    "processPayment",
    "validatePayment",
    "validate",
    "processRefund"
    ]

def test_extract_import_names():
    analyzer = JavaSourceAnalyzer()
    source_code = b"""
    import java.util.List;
    import java.util.Map;
    import java.io.File;

    public class PaymentService {
    }
    """
    tree = analyzer.parser.parse(source_code)
    import_names = analyzer.extract_import_names(tree.root_node)

    assert import_names == [
    "java.util.List",
    "java.util.Map",
    "java.io.File"
    ]

def test_extract_static_and_wildcard_imports():
    analyzer = JavaSourceAnalyzer()
    source_code = b"""
    import static java.util.Collections.sort;
    import java.util.*;
    """

    tree = analyzer.parser.parse(source_code)
    static_and_wildcard_imports = analyzer.extract_import_names(tree.root_node)

    assert static_and_wildcard_imports == ["static java.util.Collections.sort", "java.util.*"]