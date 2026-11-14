import tree_sitter_java as tsjava
from tree_sitter import Language, Parser

class JavaSourceAnalyzer:
    def __init__(self):
        java_language = Language(tsjava.language())
        self.parser = Parser(java_language)

    def extract_package_name(self, root_node):
        for node in root_node.children:
            if(node.type == "package_declaration"):
                package_name = node.text.decode("utf-8").removeprefix("package ").removesuffix(";").strip()
                return package_name
        return None

    def extract_class_names(self, root_node):
        class_names = []
        if self.is_a_class_node(root_node):
            class_name_node = root_node.child_by_field_name("name")
            if class_name_node is not None:
                class_name = class_name_node.text.decode("utf-8")
                class_names.append(class_name)
        for child in root_node.children:
            class_names.extend(self.extract_class_names(child))
        return class_names

    def extract_method_names(self, root_node):
        method_names = []
        if root_node.type == "method_declaration":
            method_name_node = root_node.child_by_field_name("name")
            if method_name_node is not None:
                method_name = method_name_node.text.decode("utf-8")
                method_names.append(method_name)
        for child in root_node.children:
            method_names.extend(self.extract_method_names(child))    
        return method_names

    def extract_import_names(self, root_node):
        import_names = []
        for child in root_node.children:
            if child.type == "import_declaration":
                if child is not None:
                    import_name = child.text.decode("utf-8").removeprefix("import ").removesuffix(";").strip()
                    import_names.append(import_name)
        return import_names
                
    @staticmethod
    def is_a_class_node(curr_node):
       return curr_node.type in {
        "class_declaration",
        "enum_declaration",
        "interface_declaration",
        "record_declaration"
    }

    def analyze(self, source_code: bytes) -> dict:
        tree = self.parser.parse(source_code)
        root_node = tree.root_node
        return {
            "package_name": self.extract_package_name(root_node= root_node),
            "class_names": self.extract_class_names(root_node= root_node),
            "imports": self.extract_import_names(root_node=root_node),
            "method_names": self.extract_method_names(root_node=root_node)
        }