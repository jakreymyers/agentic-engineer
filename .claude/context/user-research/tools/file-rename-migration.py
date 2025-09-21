#!/usr/bin/env python3
"""
File Rename Migration Tool for User Research System
Renames all files to comply with standardized naming conventions
"""

import os
import re
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class FileRenameMigration:
    """Handles migration of files to new naming standards"""

    def __init__(self, base_path: str, dry_run: bool = True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.rename_map: Dict[str, str] = {}
        self.errors: List[str] = []
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def analyze_current_files(self) -> Dict[str, List[Path]]:
        """Analyze and categorize current files"""
        categories = {
            'agents': [],
            'workflows': [],
            'tasks': [],
            'templates': [],
            'tools': [],
            'quality_gates': [],
            'tests': [],
            'other': []
        }

        for file_path in self.base_path.rglob('*'):
            if file_path.is_file():
                category = self._categorize_file(file_path)
                categories[category].append(file_path)

        return categories

    def _categorize_file(self, file_path: Path) -> str:
        """Categorize a file based on its current name and location"""
        name = file_path.name.lower()
        parent = file_path.parent.name.lower()

        if 'agent' in parent or 'agent' in name:
            return 'agents'
        elif 'workflow' in parent or 'workflow' in name:
            return 'workflows'
        elif 'task' in parent or parent == 'tasks':
            return 'tasks'
        elif 'template' in parent or 'tmpl' in name:
            return 'templates'
        elif 'tool' in parent or parent == 'tools':
            return 'tools'
        elif 'quality' in parent or 'gate' in name:
            return 'quality_gates'
        elif 'test' in parent or 'test' in name:
            return 'tests'
        else:
            return 'other'

    def generate_new_name(self, file_path: Path, category: str) -> Optional[str]:
        """Generate new name according to naming standards"""
        current_name = file_path.stem
        extension = file_path.suffix

        # Clean up the current name
        cleaned = self._clean_name(current_name)

        # Apply category-specific patterns
        if category == 'agents':
            if not cleaned.endswith('-agent'):
                cleaned = f"{cleaned}-agent"
            return f"{cleaned}.yaml"

        elif category == 'workflows':
            if not cleaned.endswith('-workflow'):
                cleaned = f"{cleaned}-workflow"
            return f"{cleaned}.yaml"

        elif category == 'tasks':
            # Ensure starts with verb
            if not self._starts_with_verb(cleaned):
                cleaned = self._add_verb_prefix(cleaned)
            return f"{cleaned}.md"

        elif category == 'templates':
            if not cleaned.endswith('-tmpl'):
                cleaned = f"{cleaned}-tmpl"
            return f"{cleaned}.yaml"

        elif category == 'tools':
            return f"{cleaned}.md"

        elif category == 'quality_gates':
            if not cleaned.startswith('quality-gates-'):
                cleaned = f"quality-gates-{cleaned}"
            return f"{cleaned}.yaml"

        elif category == 'tests':
            if 'test' not in cleaned:
                cleaned = f"{cleaned}-test"
            return f"{cleaned}{extension}"

        else:
            return f"{cleaned}{extension}"

    def _clean_name(self, name: str) -> str:
        """Clean filename to comply with standards"""
        # Convert to lowercase
        name = name.lower()

        # Replace underscores and spaces with hyphens
        name = re.sub(r'[_\s]+', '-', name)

        # Remove special characters
        name = re.sub(r'[^a-z0-9\-]', '', name)

        # Remove duplicate hyphens
        name = re.sub(r'-+', '-', name)

        # Trim hyphens from ends
        name = name.strip('-')

        return name

    def _starts_with_verb(self, name: str) -> bool:
        """Check if name starts with an action verb"""
        common_verbs = [
            'create', 'establish', 'design', 'analyze', 'synthesize',
            'generate', 'conduct', 'extract', 'map', 'identify',
            'formulate', 'prepare', 'develop', 'build', 'define',
            'plan', 'execute', 'validate', 'review', 'document'
        ]

        first_word = name.split('-')[0] if '-' in name else name
        return first_word in common_verbs

    def _add_verb_prefix(self, name: str) -> str:
        """Add appropriate verb prefix to task name"""
        # Analyze name to determine appropriate verb
        if 'guide' in name or 'template' in name:
            return f"create-{name}"
        elif 'analysis' in name:
            return f"conduct-{name}"
        elif 'report' in name:
            return f"generate-{name}"
        elif 'plan' in name:
            return f"develop-{name}"
        else:
            return f"execute-{name}"

    def create_rename_map(self, categories: Dict[str, List[Path]]) -> None:
        """Create mapping of old names to new names"""
        for category, files in categories.items():
            for file_path in files:
                new_name = self.generate_new_name(file_path, category)
                if new_name and new_name != file_path.name:
                    new_path = file_path.parent / new_name
                    self.rename_map[str(file_path)] = str(new_path)

    def update_references(self, file_path: Path, old_name: str, new_name: str) -> None:
        """Update references to renamed files in other files"""
        # Search for references in yaml, md, and json files
        for ref_file in self.base_path.rglob('*'):
            if ref_file.is_file() and ref_file.suffix in ['.yaml', '.md', '.json']:
                try:
                    content = ref_file.read_text()
                    if old_name in content:
                        updated_content = content.replace(old_name, new_name)
                        if not self.dry_run:
                            ref_file.write_text(updated_content)
                        print(f"  Updated reference in: {ref_file.relative_to(self.base_path)}")
                except Exception as e:
                    self.errors.append(f"Error updating {ref_file}: {e}")

    def execute_migration(self) -> None:
        """Execute the file rename migration"""
        print(f"{'DRY RUN: ' if self.dry_run else ''}Starting file rename migration...")
        print(f"Base path: {self.base_path}\n")

        # Analyze current files
        categories = self.analyze_current_files()

        # Report current state
        print("Current file distribution:")
        for category, files in categories.items():
            print(f"  {category}: {len(files)} files")
        print()

        # Create rename map
        self.create_rename_map(categories)

        if not self.rename_map:
            print("No files need renaming. All files comply with standards!")
            return

        # Create backup if not dry run
        if not self.dry_run:
            self.create_backup()

        # Execute renames
        print(f"Renaming {len(self.rename_map)} files:\n")
        for old_path, new_path in self.rename_map.items():
            old_name = Path(old_path).name
            new_name = Path(new_path).name

            print(f"  {old_name} -> {new_name}")

            if not self.dry_run:
                try:
                    # Rename file
                    os.rename(old_path, new_path)

                    # Update references
                    self.update_references(Path(new_path), old_name, new_name)

                except Exception as e:
                    self.errors.append(f"Error renaming {old_path}: {e}")

        # Generate report
        self.generate_report()

    def create_backup(self) -> None:
        """Create backup of current file structure"""
        backup_dir = self.base_path / f"backups/pre-migration-{self.timestamp}"
        backup_dir.mkdir(parents=True, exist_ok=True)

        print(f"Creating backup in: {backup_dir}")

        # Copy all files to backup
        for file_path in self.base_path.rglob('*'):
            if file_path.is_file() and 'backup' not in str(file_path):
                relative = file_path.relative_to(self.base_path)
                backup_path = backup_dir / relative
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, backup_path)

    def generate_report(self) -> None:
        """Generate migration report"""
        report_path = self.base_path / f"migration-report-{self.timestamp}.json"

        report = {
            "timestamp": self.timestamp,
            "dry_run": self.dry_run,
            "base_path": str(self.base_path),
            "files_renamed": len(self.rename_map),
            "rename_map": self.rename_map,
            "errors": self.errors
        }

        if not self.dry_run:
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"\nMigration report saved to: {report_path}")

        if self.errors:
            print(f"\nEncountered {len(self.errors)} errors:")
            for error in self.errors:
                print(f"  - {error}")
        else:
            print("\nMigration completed successfully!")

    def validate_migration(self) -> bool:
        """Validate that migration was successful"""
        print("\nValidating migration...")

        # Check all files follow naming standards
        violations = []
        for file_path in self.base_path.rglob('*'):
            if file_path.is_file():
                if not self._validate_filename(file_path):
                    violations.append(file_path)

        if violations:
            print(f"Found {len(violations)} files violating standards:")
            for v in violations[:10]:  # Show first 10
                print(f"  - {v.relative_to(self.base_path)}")
            return False

        print("All files comply with naming standards!")
        return True

    def _validate_filename(self, file_path: Path) -> bool:
        """Validate a filename against standards"""
        name = file_path.name

        # Check for spaces
        if ' ' in name:
            return False

        # Check for uppercase (except in extension)
        if name != name.lower():
            return False

        # Check for underscores (should be hyphens)
        if '_' in file_path.stem:
            return False

        # Check for special characters
        if re.search(r'[^a-z0-9\-\.]', name):
            return False

        return True


def main():
    """Main execution function"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Migrate files to standardized naming conventions'
    )
    parser.add_argument(
        'path',
        help='Base path for migration'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute migration (default is dry run)'
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate current naming'
    )

    args = parser.parse_args()

    migrator = FileRenameMigration(
        base_path=args.path,
        dry_run=not args.execute
    )

    if args.validate_only:
        migrator.validate_migration()
    else:
        migrator.execute_migration()
        if not migrator.dry_run:
            migrator.validate_migration()


if __name__ == "__main__":
    main()