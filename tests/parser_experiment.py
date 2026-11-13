
from patchwork_ai.repository.java_source_analyzer import JavaSourceAnalyzer

source_code = b"""
package com.patchwork.payment;

import java.util.List;
import java.util.ArrayList;
import java.util.*;
import static java.util.Collections.sort;

import com.patchwork.repository.PaymentRepository;

public class PaymentService {

    public void processPayment() {}

    class PaymentValidator {
        public boolean validate() {}
    }

    public void refundPayment() {
        class LocalHelper {
            public void help() {}
        }
    }
}

class PaymentRepository {}

// class FakeClass {}
// public void fakeMethod() {}
"""

analyzer = JavaSourceAnalyzer()
tree = analyzer.parser.parse(source_code)
root_node = tree.root_node

analyzer = JavaSourceAnalyzer()

metadata = analyzer.analyze(source_code)

for key, value in metadata.items():
    print(f"{key}: {value}")
