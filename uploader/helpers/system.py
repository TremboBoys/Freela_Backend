from django.core.management.base import BaseCommand
import os
import platform

class SystemOps(BaseCommand):
    def handle(self, *args: any, **options: any) -> dict | None:
        os_name = os.name
        platform_system = platform.system()
        platform_details = platform.platform()
        return {
            "os_name": os_name,
            "plataform_system": platform_system,
            "plataform_details": platform_details
        }
