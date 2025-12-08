"""
Module: Building Simple Apps
Description: Collection of simple but complete Python applications

This module includes:
1. To-Do List Manager (CLI)
2. Contact Manager
3. Expense Tracker
4. Simple Calculator
5. Password Generator
6. File Organizer

Each app demonstrates real-world programming concepts and best practices.
"""

import json
import os
import random
import string
import shutil
from datetime import datetime
from pathlib import Path


class TodoApp:
    """
    Simple To-Do List Manager.
    
    Features:
    - Add tasks
    - View tasks
    - Mark tasks as complete
    - Delete tasks
    - Save/load from file
    """
    
    def __init__(self, filename="../data/todos.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Loads tasks from file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_tasks(self):
        """Saves tasks to file."""
        Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def add_task(self, description):
        """Adds a new task."""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task['id']
    
    def view_tasks(self):
        """Returns all tasks."""
        return self.tasks
    
    def complete_task(self, task_id):
        """Marks a task as complete."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id):
        """Deletes a task."""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        return True
    
    def get_stats(self):
        """Returns task statistics."""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        pending = total - completed
        return {'total': total, 'completed': completed, 'pending': pending}


class ContactManager:
    """
    Simple Contact Manager.
    
    Features:
    - Add contacts
    - Search contacts
    - Update contacts
    - Delete contacts
    - Export contacts
    """
    
    def __init__(self, filename="../data/contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Loads contacts from file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_contacts(self):
        """Saves contacts to file."""
        Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=2)
    
    def add_contact(self, name, phone, email, address=""):
        """Adds a new contact."""
        contact = {
            'id': len(self.contacts) + 1,
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'created_at': datetime.now().isoformat()
        }
        self.contacts.append(contact)
        self.save_contacts()
        return contact['id']
    
    def search_contacts(self, query):
        """Searches contacts by name, phone, or email."""
        query = query.lower()
        return [
            contact for contact in self.contacts
            if query in contact['name'].lower() or
               query in contact['phone'] or
               query in contact['email'].lower()
        ]
    
    def update_contact(self, contact_id, **kwargs):
        """Updates a contact."""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                for key, value in kwargs.items():
                    if key in contact:
                        contact[key] = value
                contact['updated_at'] = datetime.now().isoformat()
                self.save_contacts()
                return True
        return False
    
    def delete_contact(self, contact_id):
        """Deletes a contact."""
        self.contacts = [c for c in self.contacts if c['id'] != contact_id]
        self.save_contacts()
        return True


class ExpenseTracker:
    """
    Simple Expense Tracker.
    
    Features:
    - Add expenses
    - View expenses by category
    - Calculate totals
    - Generate reports
    """
    
    def __init__(self, filename="../data/expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Loads expenses from file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def save_expenses(self):
        """Saves expenses to file."""
        Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=2)
    
    def add_expense(self, amount, category, description=""):
        """Adds a new expense."""
        expense = {
            'id': len(self.expenses) + 1,
            'amount': float(amount),
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat()
        }
        self.expenses.append(expense)
        self.save_expenses()
        return expense['id']
    
    def get_expenses_by_category(self, category):
        """Gets all expenses for a category."""
        return [e for e in self.expenses if e['category'] == category]
    
    def get_total(self):
        """Calculates total expenses."""
        return sum(e['amount'] for e in self.expenses)
    
    def get_category_totals(self):
        """Calculates totals by category."""
        totals = {}
        for expense in self.expenses:
            category = expense['category']
            totals[category] = totals.get(category, 0) + expense['amount']
        return totals
    
    def get_monthly_summary(self, year, month):
        """Gets expenses for a specific month."""
        month_str = f"{year}-{month:02d}"
        monthly = [e for e in self.expenses if e['date'].startswith(month_str)]
        return {
            'expenses': monthly,
            'total': sum(e['amount'] for e in monthly),
            'count': len(monthly)
        }


class Calculator:
    """
    Simple Calculator with history.
    
    Features:
    - Basic operations (+, -, *, /)
    - Advanced operations (power, sqrt, etc.)
    - Calculation history
    """
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Addition."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtraction."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiplication."""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Division."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base, exponent):
        """Power operation."""
        result = base ** exponent
        self.history.append(f"{base}^{exponent} = {result}")
        return result
    
    def sqrt(self, n):
        """Square root."""
        if n < 0:
            raise ValueError("Cannot take square root of negative number")
        result = n ** 0.5
        self.history.append(f"√{n} = {result}")
        return result
    
    def get_history(self):
        """Returns calculation history."""
        return self.history
    
    def clear_history(self):
        """Clears calculation history."""
        self.history = []


class PasswordGenerator:
    """
    Secure Password Generator.
    
    Features:
    - Customizable length
    - Include/exclude character types
    - Strength assessment
    - Multiple password generation
    """
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    
    def generate(self, length=12, use_uppercase=True, use_digits=True, use_symbols=True):
        """Generates a random password."""
        if length < 4:
            raise ValueError("Password length must be at least 4")
        
        # Build character pool
        chars = self.lowercase
        required = [random.choice(self.lowercase)]
        
        if use_uppercase:
            chars += self.uppercase
            required.append(random.choice(self.uppercase))
        
        if use_digits:
            chars += self.digits
            required.append(random.choice(self.digits))
        
        if use_symbols:
            chars += self.symbols
            required.append(random.choice(self.symbols))
        
        # Generate remaining characters
        remaining_length = length - len(required)
        password_chars = required + [random.choice(chars) for _ in range(remaining_length)]
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def assess_strength(self, password):
        """Assesses password strength."""
        score = 0
        feedback = []
        
        # Length
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password is too short (min 8 chars)")
        
        # Character variety
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add digits")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        # Determine strength
        if score >= 6:
            strength = "Strong"
        elif score >= 4:
            strength = "Moderate"
        else:
            strength = "Weak"
        
        return {
            'strength': strength,
            'score': score,
            'max_score': 6,
            'feedback': feedback
        }


class FileOrganizer:
    """
    File Organizer - Organizes files by extension.
    
    Features:
    - Scan directory
    - Group files by extension
    - Move files to categorized folders
    - Undo organization
    """
    
    def __init__(self):
        self.file_categories = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.java', '.cpp', '.c', '.html', '.css']
        }
    
    def get_category(self, file_extension):
        """Gets the category for a file extension."""
        for category, extensions in self.file_categories.items():
            if file_extension.lower() in extensions:
                return category
        return 'Others'
    
    def scan_directory(self, directory):
        """Scans a directory and categorizes files."""
        path = Path(directory)
        if not path.exists():
            return {}
        
        categorized = {}
        for file in path.iterdir():
            if file.is_file():
                category = self.get_category(file.suffix)
                if category not in categorized:
                    categorized[category] = []
                categorized[category].append(str(file.name))
        
        return categorized
    
    def organize(self, source_dir, dry_run=True):
        """Organizes files in a directory."""
        source = Path(source_dir)
        if not source.exists():
            return {"error": "Directory does not exist"}
        
        results = {
            'moved': [],
            'errors': [],
            'dry_run': dry_run
        }
        
        for file in source.iterdir():
            if file.is_file():
                category = self.get_category(file.suffix)
                target_dir = source / category
                target_file = target_dir / file.name
                
                if not dry_run:
                    target_dir.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(file), str(target_file))
                        results['moved'].append(f"{file.name} -> {category}/")
                    except Exception as e:
                        results['errors'].append(f"Error moving {file.name}: {e}")
                else:
                    results['moved'].append(f"{file.name} -> {category}/ (dry run)")
        
        return results


# DEMONSTRATIONS
def demonstrate_todo_app():
    """Demonstrates the To-Do List app."""
    print("=== To-Do List App ===")
    
    app = TodoApp()
    
    # Add tasks
    app.add_task("Complete Python tutorial")
    app.add_task("Write documentation")
    app.add_task("Review code")
    
    # View tasks
    print("\nAll tasks:")
    for task in app.view_tasks():
        status = "✓" if task['completed'] else "○"
        print(f"  {status} {task['id']}. {task['description']}")
    
    # Complete a task
    app.complete_task(1)
    
    # Stats
    stats = app.get_stats()
    print(f"\nStats: {stats['completed']} completed, {stats['pending']} pending")
    
    print()


def demonstrate_contact_manager():
    """Demonstrates the Contact Manager."""
    print("=== Contact Manager ===")
    
    manager = ContactManager()
    
    # Add contacts
    manager.add_contact("Alice Johnson", "555-0101", "alice@example.com")
    manager.add_contact("Bob Smith", "555-0102", "bob@example.com")
    
    # Search
    print("\nSearch results for 'alice':")
    results = manager.search_contacts("alice")
    for contact in results:
        print(f"  {contact['name']}: {contact['phone']} ({contact['email']})")
    
    # Update
    manager.update_contact(1, phone="555-9999")
    print("\nContact updated")
    
    print()


def demonstrate_expense_tracker():
    """Demonstrates the Expense Tracker."""
    print("=== Expense Tracker ===")
    
    tracker = ExpenseTracker()
    
    # Add expenses
    tracker.add_expense(50.00, "Food", "Groceries")
    tracker.add_expense(100.00, "Transport", "Gas")
    tracker.add_expense(30.00, "Food", "Restaurant")
    tracker.add_expense(75.00, "Entertainment", "Movie and dinner")
    
    # Category totals
    print("\nExpenses by category:")
    for category, total in tracker.get_category_totals().items():
        print(f"  {category}: ${total:.2f}")
    
    # Total
    print(f"\nTotal expenses: ${tracker.get_total():.2f}")
    
    print()


def demonstrate_calculator():
    """Demonstrates the Calculator."""
    print("=== Calculator ===")
    
    calc = Calculator()
    
    # Perform calculations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"√16 = {calc.sqrt(16)}")
    
    # History
    print("\nCalculation history:")
    for calc_str in calc.get_history():
        print(f"  {calc_str}")
    
    print()


def demonstrate_password_generator():
    """Demonstrates the Password Generator."""
    print("=== Password Generator ===")
    
    gen = PasswordGenerator()
    
    # Generate passwords
    print("Generated passwords:")
    for i in range(5):
        password = gen.generate(length=16)
        assessment = gen.assess_strength(password)
        print(f"  {i+1}. {password} [{assessment['strength']}]")
    
    # Assess custom password
    print("\nPassword strength assessment:")
    test_passwords = ["weak", "Better123", "Strong!Pass123"]
    for pwd in test_passwords:
        result = gen.assess_strength(pwd)
        print(f"  '{pwd}': {result['strength']} ({result['score']}/{result['max_score']})")
    
    print()


def demonstrate_file_organizer():
    """Demonstrates the File Organizer."""
    print("=== File Organizer ===")
    
    organizer = FileOrganizer()
    
    # Create test directory
    test_dir = Path("../data/test_organize")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create test files
    test_files = [
        "document.pdf", "image.jpg", "video.mp4", 
        "data.csv", "script.py", "archive.zip"
    ]
    
    for filename in test_files:
        (test_dir / filename).touch()
    
    # Scan directory
    print(f"\nScanning directory: {test_dir}")
    categorized = organizer.scan_directory(test_dir)
    for category, files in categorized.items():
        print(f"  {category}: {', '.join(files)}")
    
    # Organize (dry run)
    print("\nOrganizing files (dry run):")
    results = organizer.organize(test_dir, dry_run=True)
    for item in results['moved']:
        print(f"  {item}")
    
    # Cleanup
    shutil.rmtree(test_dir)
    
    print()


if __name__ == "__main__":
    """
    Main execution block - demonstrates all apps.
    """
    print("=" * 60)
    print("SIMPLE PYTHON APPS - DEMONSTRATIONS")
    print("=" * 60)
    print()
    
    # Ensure data directory exists
    Path("../data").mkdir(exist_ok=True)
    
    # Run all demonstrations
    demonstrate_todo_app()
    demonstrate_contact_manager()
    demonstrate_expense_tracker()
    demonstrate_calculator()
    demonstrate_password_generator()
    demonstrate_file_organizer()
    
    print("=" * 60)
    print("END OF SIMPLE APPS MODULE")
    print("=" * 60)
    print("\nThese apps demonstrate real-world Python applications.")
    print("Feel free to extend and customize them for your needs!")
