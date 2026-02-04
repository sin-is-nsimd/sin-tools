#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to add a github action runner."""

# Copyright © 2023-2026 Lénaïc Bagnères, lenaicb@singularity.fr

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import os
import sys

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "..", "..", "sin-python", "src"
    )
)
import sin.fs
import sin.sh
import sin.term


class Runner:
    def __init__(self, url: str, archive_file: str, sha256: str):
        self.url = url
        self.archive_file = archive_file
        self.sha256 = sha256


if __name__ == "__main__":

    runners = {}

    # https://github.com/actions/runner
    base_url_gh = "https://github.com/actions/runner/releases/download/v2.322.0/"
    # linux
    runners[("linux", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-x64-2.322.0.tar.gz",
        "b13b784808359f31bc79b08a191f5f83757852957dd8fe3dbfcc38202ccf5768",
    )
    runners[("linux", "arm", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-arm-2.322.0.tar.gz",
        "583fc5f933eb2f0f9f388ef304085629181cef54e63fe3445eed92dba4a87c46",
    )
    runners[("linux", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-arm64-2.322.0.tar.gz",
        "a96b0cec7b0237ca5e4210982368c6f7d8c2ab1e5f6b2604c1ccede9cedcb143",
    )
    # macos
    runners[("macos", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-osx-x64-2.322.0.tar.gz",
        "aa0fc262363912167dcdbc746ffcdf7b8996bc587f51cf1bab38ad86cf70b6ea",
    )
    runners[("macos", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-osx-arm64-2.322.0.tar.gz",
        "67d3b4dd6f1eec8ec43dda12c189cff68ec3ba1dfa054791cb446ddcfb39d2aa",
    )
    # windows
    runners[("windows", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-win-x64-2.322.0.zip",
        "ace5de018c88492ca80a2323af53ff3f43d2c82741853efb302928f250516015",
    )
    runners[("windows", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-win-arm64-2.322.0.zip",
        "74b67df4e94e3cd7d79b9320d421b0a62c66b77a019cf2471aba793dac0139fb",
    )

    # https://github.com/ChristopherHX/github-act-runner
    base_url_chx = (
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.13.0/"
    )
    # linux
    runners[("linux", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-amd64.tar.gz",
        "6c5b7776e0c93be08e65ceec0d0eca138b09c3d44255cddaecf5112623300376",
    )
    runners[("linux", "i386", "chx")] = Runner(
        base_url_chx,
        "binary-linux-386.tar.gz",
        "cb67eb1d26fee23079aac38daff4d3d2d202f22e69e82dfc37f5cb5f0edf2f40",
    )
    runners[("linux", "arm", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm.tar.gz",
        "b0fc2aad98bf461be59b41cffd629534af97f9b2a9f57a8cee69cbfde78dac1d",
    )
    runners[("linux", "armv6", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm5.tar.gz",
        "1721c7a5e10f9a1a34a26e2008c51dc14478f7465fb5bf4b35a06cbad729c62a",
    )
    runners[("linux", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm64.tar.gz",
        "5550d7c40f0888cec8ef5d79c39f977409f7b4e9185bf7f2ae74793eb42d3e9e",
    )
    runners[("linux", "ppc64el", "chx")] = Runner(
        base_url_chx,
        "binary-linux-ppc64le.tar.gz",
        "98741431fb56754db8d5bc33d4c71834b77431f2a69075a1cea075c305506fc0",
    )
    runners[("linux", "riscv64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-riscv64.tar.gz",
        "be84104d5f8fcf12afe9fcc3541900f5ccd033687cfb9b32105208efa5a8234d",
    )
    # macos
    runners[("macos", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-darwin-amd64.tar.gz",
        "15d50311e29130dfd06a30930212f900f01a68996e7b909e46392821b1fb41c0",
    )
    runners[("macos", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-darwin-arm64.tar.gz",
        "5f527e07a18c65e33f47ceb855003029af16a15eef27d7458ee49fa77d6e56de",
    )
    # windows
    runners[("windows", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-windows-amd64.zip",
        "ec125dc766c4d51e069de29160c6497cecba63af618e0a0db1735475421725fc",
    )
    runners[("windows", "i386", "chx")] = Runner(
        base_url_chx,
        "binary-windows-386.zip",
        "618fb48b0e44681e48153615c1d6962769239f2ec1d481343fab0d04a7d9f5ab",
    )
    runners[("windows", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-windows-arm64.zip",
        "721e99c2012e53249e565ca3e8d0c1d164a56ff86463ba63bbe94387ca1923d6",
    )

    parser = argparse.ArgumentParser(description="Add a new github action runner")
    parser.add_argument(
        "--test",
        help="Download archives, check sha256 and quit. All other options are ignored.",
        required=False,
        action="store_true",
    )
    required = "--test" not in sys.argv
    parser.add_argument(
        "--os",
        help="Operating system",
        required=required,
        choices=["macos", "linux", "windows"],
    )
    parser.add_argument(
        "--arch",
        help="Architecture",
        required=required,
        choices=["amd64", "arm", "arm64", "armv6", "i386", "ppc64el", "riscv64"],
    )
    parser.add_argument(
        "--runner",
        help="Github or ChristopherHX runner",
        required=required,
        choices=["gh", "chx"],
    )
    parser.add_argument("--user", help="User for the service", required=required)
    parser.add_argument("--url", help="Github project url", required=required)
    parser.add_argument("--token", help="Github token", required=required)
    parser.add_argument(
        "--directory", help="Output directory", default="HOME/actions-runner"
    )
    args = parser.parse_args()

    # Test

    if args.test:

        if sys.platform != "linux":
            print(sin.term.tag_error(), 'OS "' + sys.platform + '" is not implemented')
            sys.exit(0)

        r = 0
        for os_arch_runner, runner in runners.items():
            sin.sh.run_cmd(
                "curl -o "
                + runner.archive_file
                + " -L "
                + runner.url
                + runner.archive_file
            )
            sha256 = sin.fs.sha256(runner.archive_file)
            if sha256 == runner.sha256:
                print(
                    sin.term.tag_ok(),
                    'sha256 of "' + runner.archive_file + '" is ' + runner.sha256,
                )
            else:
                print(
                    sin.term.tag_error(),
                    'sha256 of "'
                    + runner.archive_file
                    + '" is '
                    + sha256
                    + " but expected one is "
                    + runner.sha256,
                )
                r = 1
            os.remove(runner.archive_file)
        sys.exit(r)

    # Directory

    if args.directory == "HOME/actions-runner":
        home = "/home" if args.os == "linux" else "/Users"
        args.directory = f"{home}/{args.user}/actions-runner"

    if os.path.exists(args.directory):
        print(sin.term.tag_error(), 'Directory "' + args.directory + '" already exist')
        sys.exit(1)
    os.makedirs(args.directory)

    # Runner

    runner = runners[(args.os, args.arch, args.runner)]

    if args.os in ["macos", "linux"]:

        cwd = os.getcwd()
        os.chdir(args.directory)

        sin.sh.run_cmd(
            "curl -o " + runner.archive_file + " -L " + runner.url + runner.archive_file
        )

        sin.sh.run_cmd(
            'echo "'
            + runner.sha256
            + "  "
            + runner.archive_file
            + '" | shasum -a 256 -c'
        )

        sin.sh.run_cmd("tar xzf ./" + runner.archive_file)

        sin.sh.run_cmd("./config.sh --url " + args.url + " --token " + args.token)

        os.chdir(cwd)

    elif args.os == "windows":

        print(sin.term.tag_error(), 'OS "' + args.os + '" is not implemented')
        sys.exit(1)

    else:

        print(sin.term.tag_error(), 'OS "' + args.os + '" is not implemented')
        sys.exit(1)

    # Service

    if args.os == "macos":

        service_path = os.path.join(args.directory, "github-action-runner.plist")
        with open(service_path, "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(
                '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
            )
            f.write('<plist version="1.0">\n')
            f.write("    <dict>\n")
            f.write("        <key>Label</key>\n")
            f.write("        <string>github.action.runner</string>\n")
            f.write("        <key>UserName</key>\n")
            f.write("        <string>" + args.user + "</string>\n")
            f.write("        <key>EnvironmentVariables</key>\n")
            f.write("        <dict>\n")
            f.write("            <key>PATH</key>\n")
            f.write(
                "            <string>/opt/homebrew/bin:/bin:/usr/bin:/usr/local/bin</string>\n"
            )
            f.write("        </dict>\n")
            f.write("        <key>WorkingDirectory</key>\n")
            f.write("        <string>" + args.directory + "</string>\n")
            f.write("        <key>Program</key>\n")
            f.write("        <string>" + args.directory + "/run.sh</string>\n")
            f.write("        <key>StandardOutPath</key>\n")
            f.write(
                "        <string>"
                + args.directory
                + "/log/github_action_runner_out.log</string>\n"
            )
            f.write("        <key>StandardErrorPath</key>\n")
            f.write(
                "        <string>"
                + args.directory
                + "/log/github_action_runner_err.log</string>\n"
            )
            f.write("        <key>RunAtLoad</key>\n")
            f.write("        <true/>\n")
            f.write("        <key>KeepAlive</key>\n")
            f.write("        <true/>\n")
            f.write("    </dict>\n")
            f.write("</plist>")

        print("You can activate the service (with root access):")
        print("```sh")
        print("cp " + service_path + " /Library/LaunchAgents/")
        print("launchctl load /Library/LaunchAgents/github-action-runner.plist")
        print("launchctl start /Library/LaunchAgents/github-action-runner.plist")
        print("launchctl print gui/$UID/github.action.runner")
        print("```")

    elif args.os == "linux":

        service_path = os.path.join(args.directory, "github-action-runner.service")
        with open(service_path, "w") as f:
            f.write("[Unit]\n")
            f.write('Description="Github CI service"\n')
            f.write("\n")
            f.write("[Service]\n")
            f.write("User=" + args.user + "\n")
            f.write("WorkingDirectory=" + args.directory + "\n")
            f.write("ExecStart=bash ./run.sh\n")
            f.write("Restart=always\n")
            f.write("RestartSec=3\n")
            f.write("\n")
            f.write("[Install]\n")
            f.write("WantedBy=multi-user.target\n")

        print("You can activate the service (with root access):")
        print("```sh")
        print("cp " + service_path + " /etc/systemd/system/")
        print("systemctl enable github-action-runner.service")
        print("service github-action-runner start")
        print("service github-action-runner status")
        print("```")

    # End

    sys.exit(0)
