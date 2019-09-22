#!/usr/bin/env python3

import platform
from pathlib import Path
from subprocess import CalledProcessError, check_call  # noqa: S404
from typing import List, Union


class OSInteractionLayer():
    """Detects package manager used by system and attempts to install HomePage dependencies."""

    def __init__(self) -> None:
        self.IS_WINDOWS: bool = (platform.system().lower() == "windows")

    def __get_distro(self) -> bool:
        """Get the OS-release"""

        if not(self.IS_WINDOWS):
            with open(Path("/etc/os-release"), "r") as RELEASE_FILE:
                self.OS_RELEASE: Union[List[str], str] = RELEASE_FILE.read().split("\n")
            self.OS_RELEASE = sum([i.split("=") for i in self.OS_RELEASE], [])
            self.OS_RELEASE = self.OS_RELEASE[self.OS_RELEASE.index("ID") + 1].strip('"').lower()
            return True

        else:
            return False

    def __is_pkg_mgr_present(self, pkg_mgr_name) -> bool:
        checker_cmd: str = ('/usr/bin/env bash -c '
                            f'"hash {pkg_mgr_name} '
                            '>/dev/null 2>/dev/null '
                            f'|| command -v {pkg_mgr_name} '
                            '>/dev/null 2>/dev/null"'
                            )
        try:
            return not bool(
                check_call(checker_cmd, shell=True)  # noqa: S602
            )
        except(CalledProcessError):
            return False

    def __install_nix_pkg(self) -> bool:
        """Determine package manager and install packages required."""

        try:
            for name, actions in self.package_mapping.items():
                if self.__is_pkg_mgr_present(name):
                    for pkg_mgr_cmd in actions:
                        check_call(f"{pkg_mgr_cmd}", shell=True)  # noqa: S602
                    else:
                        return True
            else:
                return False

        except(CalledProcessError, KeyboardInterrupt):
            return False

    def __install_win_pkg(self) -> bool:
        """Install the windows packages. Not added yet."""

        return False

    def install_packages(self, **package_mapping) -> bool:
        self.package_mapping = package_mapping

        if not self.IS_WINDOWS:
            return self.__install_nix_pkg()

        else:
            return self.__install_win_pkg()
