"""
Module: Working with JSON in Python
Description: Comprehensive guide to JSON data handling in Python

This module covers:
- JSON basics and structure
- Reading and writing JSON files
- Converting between JSON and Python objects
- Working with nested JSON
- JSON validation
- Pretty printing
- Common use cases
"""

import json
from datetime import datetime
from pathlib import Path


def demonstrate_json_basics():
    """
    Demonstrates JSON data structure basics.
    
    JSON (JavaScript Object Notation) is a lightweight data format.
    """
    print("=== JSON Basics ===")
    
    # Python dictionary that can be converted to JSON
    person = {
        "name": "Alice Johnson",
        "age": 30,
        "email": "alice@example.com",
        "is_active": True,
        "balance": 1250.50,
        "hobbies": ["reading", "coding", "hiking"],
        "address": {
            "street": "123 Main St",
            "city": "Boston",
            "zip": "02101"
        }
    }
    
    print("Python dictionary:")
    print(f"  {person}")
    
    # Convert to JSON string
    json_string = json.dumps(person)
    print(f"\nJSON string:")
    print(f"  {json_string[:100]}...")
    
    # Pretty print JSON
    print("\nPretty printed JSON:")
    pretty_json = json.dumps(person, indent=2)
    print(pretty_json)
    
    print()


def demonstrate_json_serialization():
    """
    Demonstrates converting Python objects to JSON (serialization).
    """
    print("=== JSON Serialization (Python to JSON) ===")
    
    # Dictionary to JSON
    data = {
        "name": "Product A",
        "price": 99.99,
        "in_stock": True,
        "tags": ["electronics", "gadget"],
        "specs": {"color": "black", "weight": "200g"}
    }
    
    # dumps - to string
    json_str = json.dumps(data)
    print(f"json.dumps() - String:")
    print(f"  {json_str[:80]}...")
    print(f"  Type: {type(json_str)}")
    
    # dumps with formatting options
    formatted = json.dumps(data, indent=4, sort_keys=True)
    print(f"\nFormatted with indent=4, sort_keys=True:")
    print(formatted)
    
    # Different separators
    compact = json.dumps(data, separators=(',', ':'))
    print(f"\nCompact (no spaces):")
    print(f"  {compact}")
    
    print()


def demonstrate_json_deserialization():
    """
    Demonstrates converting JSON to Python objects (deserialization).
    """
    print("=== JSON Deserialization (JSON to Python) ===")
    
    # JSON string
    json_string = '''
    {
        "user_id": 12345,
        "username": "john_doe",
        "email": "john@example.com",
        "is_verified": true,
        "score": 98.5,
        "badges": ["beginner", "contributor"],
        "profile": {
            "bio": "Python developer",
            "location": "San Francisco"
        }
    }
    '''
    
    # loads - from string
    data = json.loads(json_string)
    print("json.loads() - Parsed data:")
    print(f"  Type: {type(data)}")
    print(f"  Username: {data['username']}")
    print(f"  Email: {data['email']}")
    print(f"  Badges: {data['badges']}")
    print(f"  Location: {data['profile']['location']}")
    
    # Type conversions
    print("\nType conversions:")
    print(f"  JSON true -> Python {data['is_verified']} ({type(data['is_verified']).__name__})")
    print(f"  JSON array -> Python {data['badges']} ({type(data['badges']).__name__})")
    print(f"  JSON object -> Python {type(data['profile']).__name__}")
    
    print()


def demonstrate_json_files():
    """
    Demonstrates reading from and writing to JSON files.
    """
    print("=== JSON Files ===")
    
    # Ensure data directory exists
    Path("../data").mkdir(exist_ok=True)
    
    # Writing to JSON file
    print("Writing to JSON file:")
    users = [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "role": "admin"
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "role": "user"
        },
        {
            "id": 3,
            "name": "Charlie",
            "email": "charlie@example.com",
            "role": "user"
        }
    ]
    
    with open("../data/users.json", "w") as file:
        json.dump(users, file, indent=2)
    print("  users.json created")
    
    # Reading from JSON file
    print("\nReading from JSON file:")
    with open("../data/users.json", "r") as file:
        loaded_users = json.load(file)
    
    print(f"  Loaded {len(loaded_users)} users:")
    for user in loaded_users:
        print(f"    {user['id']}. {user['name']} ({user['role']})")
    
    print()


def demonstrate_nested_json():
    """
    Demonstrates working with nested JSON structures.
    """
    print("=== Nested JSON ===")
    
    # Complex nested structure
    company = {
        "name": "TechCorp",
        "founded": 2015,
        "departments": [
            {
                "name": "Engineering",
                "employees": [
                    {"name": "Alice", "position": "Senior Dev", "salary": 120000},
                    {"name": "Bob", "position": "Junior Dev", "salary": 70000}
                ]
            },
            {
                "name": "Sales",
                "employees": [
                    {"name": "Charlie", "position": "Sales Manager", "salary": 90000},
                    {"name": "Diana", "position": "Sales Rep", "salary": 60000}
                ]
            }
        ]
    }
    
    # Save to file
    with open("../data/company.json", "w") as file:
        json.dump(company, file, indent=2)
    
    print("Navigating nested structure:")
    print(f"  Company: {company['name']}")
    print(f"  Departments: {len(company['departments'])}")
    
    for dept in company['departments']:
        print(f"\n  {dept['name']} Department:")
        for emp in dept['employees']:
            print(f"    - {emp['name']}: {emp['position']} (${emp['salary']:,})")
    
    print()


def demonstrate_json_data_types():
    """
    Demonstrates JSON data type conversions.
    """
    print("=== JSON Data Types ===")
    
    # All JSON types
    json_types = {
        "string": "Hello",
        "number_int": 42,
        "number_float": 3.14,
        "boolean_true": True,
        "boolean_false": False,
        "null_value": None,
        "array": [1, 2, 3],
        "object": {"key": "value"}
    }
    
    print("JSON type mapping:")
    json_str = json.dumps(json_types, indent=2)
    print(json_str)
    
    print("\nPython to JSON conversions:")
    print(f"  dict -> object")
    print(f"  list, tuple -> array")
    print(f"  str -> string")
    print(f"  int, float -> number")
    print(f"  True -> true")
    print(f"  False -> false")
    print(f"  None -> null")
    
    print()


def demonstrate_json_errors():
    """
    Demonstrates handling JSON errors.
    """
    print("=== JSON Error Handling ===")
    
    # Invalid JSON
    print("Handling invalid JSON:")
    invalid_json = '{"name": "Alice", "age": 30'  # Missing closing brace
    
    try:
        data = json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"  Error: {e}")
        print(f"  Line: {e.lineno}, Column: {e.colno}")
    
    # Non-serializable object
    print("\nHandling non-serializable object:")
    class CustomObject:
        def __init__(self, value):
            self.value = value
    
    try:
        obj = CustomObject(42)
        json_str = json.dumps({"obj": obj})
    except TypeError as e:
        print(f"  Error: {e}")
    
    # File not found
    print("\nHandling missing file:")
    try:
        with open("../data/nonexistent.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("  Error: File not found")
    
    print()


def demonstrate_custom_encoding():
    """
    Demonstrates custom JSON encoding for special types.
    """
    print("=== Custom JSON Encoding ===")
    
    # Custom encoder for datetime
    class DateTimeEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    
    # Data with datetime
    event = {
        "name": "Conference",
        "date": datetime(2025, 6, 15, 10, 0),
        "location": "Boston"
    }
    
    print("Encoding datetime:")
    json_str = json.dumps(event, cls=DateTimeEncoder, indent=2)
    print(json_str)
    
    # Custom encoder function
    def custom_encoder(obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        raise TypeError(f"Type {type(obj)} not serializable")
    
    print("\nUsing custom encoder function:")
    json_str = json.dumps(event, default=custom_encoder, indent=2)
    print(json_str)
    
    print()


def demonstrate_json_validation():
    """
    Demonstrates simple JSON validation techniques.
    """
    print("=== JSON Validation ===")
    
    def validate_user(data):
        """Validates user data structure."""
        required_fields = ["name", "email", "age"]
        
        # Check required fields
        for field in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
        
        # Check types
        if not isinstance(data["name"], str):
            return False, "name must be a string"
        if not isinstance(data["email"], str):
            return False, "email must be a string"
        if not isinstance(data["age"], int):
            return False, "age must be an integer"
        
        # Check values
        if data["age"] < 0 or data["age"] > 150:
            return False, "age must be between 0 and 150"
        
        return True, "Valid"
    
    # Test cases
    test_users = [
        {"name": "Alice", "email": "alice@example.com", "age": 25},
        {"name": "Bob", "age": 30},  # Missing email
        {"name": "Charlie", "email": "charlie@example.com", "age": "25"},  # Wrong type
        {"name": "Diana", "email": "diana@example.com", "age": -5},  # Invalid value
    ]
    
    for i, user in enumerate(test_users, 1):
        valid, message = validate_user(user)
        status = "✓" if valid else "✗"
        print(f"  {status} User {i}: {message}")
    
    print()


# EXERCISES
def exercise_1():
    """
    Exercise 1: JSON Config Manager
    
    TODO: Create a configuration manager that:
    - Loads config from JSON
    - Updates specific settings
    - Saves back to JSON
    - Validates configuration
    """
    print("=== Exercise 1: Config Manager ===")
    
    class ConfigManager:
        """Manages application configuration."""
        
        def __init__(self, config_file):
            self.config_file = config_file
            self.config = self.load()
        
        def load(self):
            """Loads configuration from file."""
            try:
                with open(self.config_file, "r") as file:
                    return json.load(file)
            except FileNotFoundError:
                return {}
        
        def save(self):
            """Saves configuration to file."""
            with open(self.config_file, "w") as file:
                json.dump(self.config, file, indent=2)
        
        def get(self, key, default=None):
            """Gets a configuration value."""
            return self.config.get(key, default)
        
        def set(self, key, value):
            """Sets a configuration value."""
            self.config[key] = value
            self.save()
    
    # Test the manager
    config = ConfigManager("../data/app_config.json")
    config.set("app_name", "MyApp")
    config.set("version", "1.0.0")
    config.set("debug", True)
    
    print(f"  App name: {config.get('app_name')}")
    print(f"  Version: {config.get('version')}")
    print(f"  Debug: {config.get('debug')}")
    print()


def exercise_2():
    """
    Exercise 2: JSON Data Transformer
    
    TODO: Transform JSON data:
    - Read JSON from file
    - Filter data based on criteria
    - Transform/map values
    - Write to new JSON file
    """
    print("=== Exercise 2: Data Transformer ===")
    
    # Create sample data
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics", "in_stock": True},
        {"id": 2, "name": "Mouse", "price": 29.99, "category": "Electronics", "in_stock": True},
        {"id": 3, "name": "Desk", "price": 299.99, "category": "Furniture", "in_stock": False},
        {"id": 4, "name": "Chair", "price": 199.99, "category": "Furniture", "in_stock": True},
        {"id": 5, "name": "Monitor", "price": 349.99, "category": "Electronics", "in_stock": True}
    ]
    
    with open("../data/products.json", "w") as file:
        json.dump(products, file, indent=2)
    
    # Transform: Get electronics in stock with 10% discount
    with open("../data/products.json", "r") as file:
        all_products = json.load(file)
    
    electronics_sale = [
        {
            "name": p["name"],
            "original_price": p["price"],
            "sale_price": round(p["price"] * 0.9, 2)
        }
        for p in all_products
        if p["category"] == "Electronics" and p["in_stock"]
    ]
    
    with open("../data/electronics_sale.json", "w") as file:
        json.dump(electronics_sale, file, indent=2)
    
    print("  Transformed electronics on sale:")
    for item in electronics_sale:
        print(f"    {item['name']}: ${item['original_price']} -> ${item['sale_price']}")
    
    print()


def exercise_3():
    """
    Exercise 3: JSON Merger
    
    TODO: Merge multiple JSON files:
    - Read from multiple sources
    - Combine data intelligently
    - Handle duplicates
    - Save merged result
    """
    print("=== Exercise 3: JSON Merger ===")
    
    # Create sample files
    file1_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 87}
    ]
    
    file2_data = [
        {"id": 3, "name": "Charlie", "score": 92},
        {"id": 2, "name": "Bob", "score": 90}  # Duplicate ID, updated score
    ]
    
    with open("../data/scores1.json", "w") as f:
        json.dump(file1_data, f, indent=2)
    
    with open("../data/scores2.json", "w") as f:
        json.dump(file2_data, f, indent=2)
    
    # Merge function
    def merge_json_files(files):
        """Merges multiple JSON files, keeping latest entry for duplicates."""
        merged = {}
        
        for file in files:
            with open(file, "r") as f:
                data = json.load(f)
                for item in data:
                    merged[item["id"]] = item
        
        return list(merged.values())
    
    # Merge and save
    merged_data = merge_json_files(["../data/scores1.json", "../data/scores2.json"])
    
    with open("../data/scores_merged.json", "w") as f:
        json.dump(merged_data, f, indent=2)
    
    print("  Merged data:")
    for item in sorted(merged_data, key=lambda x: x["id"]):
        print(f"    {item['id']}. {item['name']}: {item['score']}")
    
    print()


def exercise_4():
    """
    Exercise 4: JSON Query Tool
    
    TODO: Create a simple query tool for JSON data:
    - Filter by field values
    - Sort results
    - Select specific fields
    - Return formatted results
    """
    print("=== Exercise 4: JSON Query Tool ===")
    
    def query_json(data, filter_fn=None, sort_by=None, fields=None):
        """Queries JSON data with filtering, sorting, and field selection."""
        result = data
        
        # Filter
        if filter_fn:
            result = [item for item in result if filter_fn(item)]
        
        # Sort
        if sort_by:
            result = sorted(result, key=lambda x: x.get(sort_by, ''))
        
        # Select fields
        if fields:
            result = [{k: item[k] for k in fields if k in item} for item in result]
        
        return result
    
    # Test with users data
    with open("../data/users.json", "r") as file:
        users = json.load(file)
    
    # Query 1: Admins only
    admins = query_json(users, filter_fn=lambda u: u['role'] == 'admin')
    print(f"  Admins: {[u['name'] for u in admins]}")
    
    # Query 2: All users, sorted by name, only name and email
    sorted_users = query_json(users, sort_by='name', fields=['name', 'email'])
    print(f"  Sorted users:")
    for user in sorted_users:
        print(f"    {user['name']}: {user['email']}")
    
    print()


def exercise_5():
    """
    Exercise 5: JSON Schema Validator (Simple)
    
    TODO: Create a simple schema validator:
    - Define expected schema
    - Validate JSON against schema
    - Report validation errors
    - Support nested objects
    """
    print("=== Exercise 5: Schema Validator ===")
    
    def validate_schema(data, schema):
        """Simple schema validator."""
        errors = []
        
        # Check required fields
        for field, rules in schema.items():
            if rules.get('required', False) and field not in data:
                errors.append(f"Missing required field: {field}")
                continue
            
            if field in data:
                value = data[field]
                expected_type = rules.get('type')
                
                # Type checking
                if expected_type == 'string' and not isinstance(value, str):
                    errors.append(f"{field} must be a string")
                elif expected_type == 'number' and not isinstance(value, (int, float)):
                    errors.append(f"{field} must be a number")
                elif expected_type == 'array' and not isinstance(value, list):
                    errors.append(f"{field} must be an array")
                elif expected_type == 'object' and not isinstance(value, dict):
                    errors.append(f"{field} must be an object")
        
        return len(errors) == 0, errors
    
    # Define schema
    user_schema = {
        'name': {'type': 'string', 'required': True},
        'age': {'type': 'number', 'required': True},
        'email': {'type': 'string', 'required': True},
        'hobbies': {'type': 'array', 'required': False}
    }
    
    # Test cases
    test_cases = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": "30", "email": "bob@example.com"},  # Wrong type
        {"name": "Charlie", "email": "charlie@example.com"},  # Missing age
    ]
    
    for i, user in enumerate(test_cases, 1):
        valid, errors = validate_schema(user, user_schema)
        if valid:
            print(f"  ✓ User {i}: Valid")
        else:
            print(f"  ✗ User {i}: Invalid")
            for error in errors:
                print(f"      - {error}")
    
    print()


if __name__ == "__main__":
    """
    Main execution block - runs all demonstrations and exercises.
    """
    # Ensure data directory exists
    Path("../data").mkdir(exist_ok=True)
    
    print("=" * 60)
    print("WORKING WITH JSON IN PYTHON - COMPLETE GUIDE")
    print("=" * 60)
    print()
    
    # Run all demonstrations
    demonstrate_json_basics()
    demonstrate_json_serialization()
    demonstrate_json_deserialization()
    demonstrate_json_files()
    demonstrate_nested_json()
    demonstrate_json_data_types()
    demonstrate_json_errors()
    demonstrate_custom_encoding()
    demonstrate_json_validation()
    
    # Run all exercises
    print("=" * 60)
    print("EXERCISES")
    print("=" * 60)
    print()
    
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    
    print("=" * 60)
    print("END OF WORKING WITH JSON MODULE")
    print("=" * 60)
