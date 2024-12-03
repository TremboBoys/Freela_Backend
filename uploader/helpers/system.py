from django.core.management.base import BaseCommand
import os
import platform
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        os_name = os.name
        platform_system = platform.system()
        platform_details = platform.platform()
        print(os_name, platform_system, platform_details)
        self.stdout.write(self.style.SUCCESS(f"{os_name} - {platform_details} - {platform_system}"))
    