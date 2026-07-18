from pathlib import Path
import argparse
import hashlib
import json
import shutil

from androguard.core.apk import APK


class APKAnalyzer:

    def __init__(
        self,
        apk_path: str,
        output_dir: str = "apk_analysis"
    ):
        self.apk_path = Path(apk_path)
        self.output_dir = Path(output_dir)

        if not self.apk_path.exists():
            raise FileNotFoundError(
                f"APK file not found: {self.apk_path}"
            )

        self.apk = APK(
            str(self.apk_path)
        )

    def extract_resources(self):
        """Extract APK resources temporarily."""

        resource_path = (
            self.output_dir / "resources"
        )

        resource_path.mkdir(
            parents=True,
            exist_ok=True
        )

        for file_name in self.apk.get_files():

            destination = (
                resource_path / file_name
            )

            destination.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            try:
                data = (
                    self.apk.get_file(file_name)
                )

                with open(
                    destination,
                    "wb"
                ) as file:

                    file.write(
                        data
                    )

            except Exception as error:

                print(
                    f"[!] Failed extracting {file_name}: {error}"
                )

    def remove_resources(self):
        """Remove temporary extracted resources."""

        resource_path = (
            self.output_dir / "resources"
        )

        if resource_path.exists():

            shutil.rmtree(
                resource_path
            )

    def extract_icon(self):
        """Extract application icon."""

        try:
            icon_name = (
                self.apk.get_app_icon()
            )

            if not icon_name:
                return None

            icon_data = (
                self.apk.get_file(icon_name)
            )

            icon_file = (
                self.output_dir / "icon.png"
            )

            with open(
                icon_file,
                "wb"
            ) as file:

                file.write(
                    icon_data
                )

            return str(
                icon_file
            )

        except Exception as error:

            print(
                f"[!] Icon extraction failed: {error}"
            )

            return None

    def get_certificate_hash(self):

        try:
            certificates = (
                self.apk.get_certificates()
            )

            if not certificates:
                return None

            return hashlib.sha256(
                certificates[0].dump()
            ).hexdigest()

        except Exception:
            return None

    def save_certificate(self, value):

        if not value:
            return

        file_path = (
            self.output_dir / "certificate.sha256"
        )

        with open(
            file_path,
            "w"
        ) as file:

            file.write(
                value
            )

    def get_architecture(self):

        result = []

        files = (
            self.apk.get_files()
        )

        architectures = [
            "arm64-v8a",
            "armeabi-v7a",
            "x86",
            "x86_64"
        ]

        for arch in architectures:

            prefix = f"lib/{arch}/"

            if any(
                item.startswith(prefix)
                for item in files
            ):
                result.append(
                    arch
                )

        return result

    def get_framework(self):

        files = (
            self.apk.get_files()
        )

        frameworks = {
            "Flutter": "flutter",
            "Unity": "unity",
            "Xamarin": "xamarin",
            "React Native": "reactnative"
        }

        for name, keyword in frameworks.items():

            if any(
                keyword in file.lower()
                for file in files
            ):
                return name

        return "Native Android"

    def get_launcher_activity(self):

        try:
            return (
                self.apk.get_main_activity()
            )

        except Exception:
            return None

    def get_version_name(self):

        try:
            return (
                self.apk.get_androidversion_name()
            )

        except Exception:
            return None

    def get_version_code(self):

        try:
            return (
                self.apk.get_androidversion_code()
            )

        except Exception:
            return None

    def analyze(self):

        certificate = (
            self.get_certificate_hash()
        )

        return {

            "name": (
                self.apk.get_app_name()
            ),

            "package": (
                self.apk.get_package()
            ),

            "version": (
                self.get_version_name()
            ),

            "version_code": (
                self.get_version_code()
            ),

            "icon": (
                self.extract_icon()
            ),

            "size": (
                f"{self.apk_path.stat().st_size / 1024 / 1024:.2f} MB"
            ),

            "permissions": [
                item.replace(
                    "android.permission.",
                    ""
                )
                for item in self.apk.get_permissions()
            ],

            "architecture": (
                self.get_architecture()
            ),

            "min_android": (
                self.apk.get_min_sdk_version()
            ),

            "target_android": (
                self.apk.get_target_sdk_version()
            ),

            "framework": (
                self.get_framework()
            ),

            "launcher_activity": (
                self.get_launcher_activity()
            ),

            "certificate_sha256": certificate,

            "files_count": (
                len(
                    self.apk.get_files()
                )
            )
        }

    def save_json(self, data):

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.output_dir / "metadata.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def save_report(self, data):

        with open(
            self.output_dir / "info.txt",
            "w",
            encoding="utf-8"
        ) as file:

            for key, value in data.items():

                file.write(
                    f"{key}: {value}\n"
                )


def main():

    parser = argparse.ArgumentParser(
        description="Android APK Analyzer"
    )

    parser.add_argument(
        "apk",
        help="APK file path"
    )

    args = parser.parse_args()

    apk_path = Path(
        args.apk
    )

    output_dir = (
        apk_path.stem + "_analysis"
    )

    analyzer = APKAnalyzer(
        apk_path,
        output_dir
    )

    analyzer.output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        "[+] Extracting resources..."
    )

    analyzer.extract_resources()

    print(
        "[+] Analyzing APK..."
    )

    metadata = (
        analyzer.analyze()
    )

    analyzer.save_json(
        metadata
    )

    analyzer.save_report(
        metadata
    )

    analyzer.save_certificate(
        metadata["certificate_sha256"]
    )

    print(
        "[+] Cleaning temporary files..."
    )

    analyzer.remove_resources()

    print(
        "\n[+] Completed"
    )

    print(
        json.dumps(
            metadata,
            indent=4,
            ensure_ascii=False
        )
    )

    print(
        f"\n[+] Output: {output_dir}"
    )


if __name__ == "__main__":
    main()