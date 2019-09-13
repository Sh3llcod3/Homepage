#!/usr/bin/env python3

import platform
from pathlib import Path
from subprocess import call, check_output  # noqa: S404


class OSInteractionLayer():
    """Detects package manager used by system and attempts to install HomePage dependencies."""

    def __init__(self, **install_mapping) -> None:
        self.IS_WINDOWS = (platform.system().lower() == "windows")

        if not(self.IS_WINDOWS):
            with open(Path("/etc/os-release"), "r") as RELEASE_FILE:
                self.OS_RELEASE: str = RELEASE_FILE.read().split("\n")
                self.OS_RELEASE = sum([i.split("=") for i in OS_RELEASE], [])
                self.OS_RELEASE = OS_RELEASE[OS_RELEASE.index("ID") + 1].strip('"').lower()

    def install_packages(self) -> None:
        pass




OS_RELEASE = "cat /etc/os-release | grep \"^ID=\" | cut -d\= -f2 | sed -e 's/\"//g'"
OS_RELEASE = check_output(OS_RELEASE, shell=True).decode('utf-8').rstrip()
