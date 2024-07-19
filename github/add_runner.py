#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to add a github action runner."""

# Copyright © 2023 Lénaïc Bagnères, lenaicb@singularity.fr

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
import sin.sh  # nopep8
import sin.term  # nopep8


class Runner:
    def __init__(self, url, archive_file, sha256):
        self.url = url
        self.archive_file = archive_file
        self.sha256 = sha256


if __name__ == "__main__":

    runners = {}
    # macos
    runners[("macos", "amd64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-osx-x64-2.317.0.tar.gz",
        "0b23ee79731522d9e1229d14d62c200e06ac9d7dddf5641966209a7700a43c14",
    )
    runners[("macos", "arm64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-osx-arm64-2.317.0.tar.gz",
        "70b765f32062de395a35676579e25ab433270d7367feb8da85dcfe42560feaba",
    )
    # linux
    runners[("linux", "amd64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.316.1/",
        "actions-runner-linux-x64-2.316.1.tar.gz",
        "9e883d210df8c6028aff475475a457d380353f9d01877d51cc01a17b2a91161d",
    )
    runners[("linux", "arm")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-linux-arm-2.317.0.tar.gz",
        "8a767b09300472bbac8e1c27c9b2a1460640206d03ca469efd4ce1d49333a5a3",
    )
    runners[("linux", "arm64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-linux-arm64-2.317.0.tar.gz",
        "7e8e2095d2c30bbaa3d2ef03505622b883d9cb985add6596dbe2f234ece308f3",
    )
    runners[("linux", "armv6")] = Runner(
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.7.1/",
        "binary-linux-arm5.tar.gz",
        "2df04c14e94cc36dbfe039929f5fb9fa6584f5f80f5f247733b2d7c1d44ab346",
    )
    runners[("linux", "i386")] = Runner(
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.7.1/",
        "binary-linux-386.tar.gz",
        "ca5817541088a44bf70922f6033e868b2b8904a3fd36b753c1aa55b374429477",
    )
    runners[("linux", "ppc64el")] = Runner(
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.7.1/",
        "binary-linux-ppc64le.tar.gz",
        "79a92ab4c26243f19e499d41d9b13dd25915931f15f2ebb565a30025cf16a467",
    )
    runners[("linux", "riscv64")] = Runner(
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.7.1/",
        "binary-linux-riscv64.tar.gz",
        "d47d9cf4f533acb616c7483703095a376febd5ae0a2927d114e8293ad1ee891f",
    )
    # windows
    runners[("windows", "amd64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-win-x64-2.317.0.zip",
        "a74dcd1612476eaf4b11c15b3db5a43a4f459c1d3c1807f8148aeb9530d69826",
    )
    runners[("windows", "arm64")] = Runner(
        "https://github.com/actions/runner/releases/download/v2.317.0/",
        "actions-runner-win-arm64-2.317.0.zip",
        "450da62bdcbab0a34ebd5a14b466d630f9cdfb1985720785499f589fd3e3724c",
    )

    parser = argparse.ArgumentParser(description="Add a new github action runner")
    parser.add_argument(
        "--os",
        help="Operating system",
        required=True,
        choices=["macos", "linux", "windows"],
    )
    parser.add_argument(
        "--arch",
        help="Architecture",
        required=True,
        choices=["amd64", "arm", "arm64", "armv6", "i386", "ppc64el", "riscv64"],
    )
    parser.add_argument("--user", help="User for the service", required=True)
    parser.add_argument("--url", help="Github project url", required=True)
    parser.add_argument("--token", help="Github token", required=True)
    parser.add_argument(
        "--directory", help="Output directory", default="HOME/actions-runner"
    )
    args = parser.parse_args()

    if args.directory == "HOME/actions-runner":
        home = "/home" if args.os == "linux" else "/Users"
        args.directory = f"{home}/{args.user}/actions-runner"

    if os.path.exists(args.directory):
        print(sin.term.tag_error(), 'Directory "' + args.directory + '" already exist')
        sys.exit(1)
    os.makedirs(args.directory)

    # Runner

    runner = runners[(args.os, args.arch)]

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
