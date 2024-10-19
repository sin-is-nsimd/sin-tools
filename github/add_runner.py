#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to add a github action runner."""

# Copyright © 2023-2024 Lénaïc Bagnères, lenaicb@singularity.fr

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
import sin.sh
import sin.term


class Runner:
    def __init__(self, url: str, archive_file: str, sha256: str):
        self.url = url
        self.archive_file = archive_file
        self.sha256 = sha256


if __name__ == "__main__":

    base_url = (
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.8.0/"
    )

    runners: dict[tuple[str, str], Runner] = {}
    # macos
    runners[("macos", "amd64")] = Runner(
        base_url,
        "binary-darwin-amd64.tar.gz",
        "ab5fb1996a6c1b87543d15d1973916d9d7a672931667dc5793e4efc076609741",
    )
    runners[("macos", "arm64")] = Runner(
        base_url,
        "binary-darwin-arm64.tar.gz",
        "daaa2f3d3672eaec6921c23153551d2984d720a6bfa51916568ee2e379156203",
    )
    # linux
    runners[("linux", "amd64")] = Runner(
        base_url,
        "binary-linux-amd64.tar.gz",
        "90faed7a8a39970b0281911ae57ad55607189c5894bd45cc09b3f81cef038311",
    )
    runners[("linux", "i386")] = Runner(
        base_url,
        "binary-linux-386.tar.gz",
        "463d169fbb11f109cc8cf948e072151344da5386d92e21f8f32d05c3df268c75",
    )
    runners[("linux", "arm")] = Runner(
        base_url,
        "binary-linux-arm.tar.gz",
        "f53618b413349a064944189afb4ede0b33570a75b0e070da94461e0c6f9c32a6",
    )
    runners[("linux", "armv6")] = Runner(
        base_url,
        "binary-linux-arm5.tar.gz",
        "1ff0de471c1b92f51f42c955372c810fcb62e1484138e1ee40f416c7f6b0c292",
    )
    runners[("linux", "arm64")] = Runner(
        base_url,
        "binary-linux-arm64.tar.gz",
        "7854554f85272e145a2a749f6992911b6efb39b4de39b35261830648cb0f5e13",
    )
    runners[("linux", "ppc64el")] = Runner(
        base_url,
        "binary-linux-ppc64le.tar.gz",
        "381aa79e4a834574da6923fd9c2c1f8a5cca237d359f7e42344387625edfa3b4",
    )
    runners[("linux", "riscv64")] = Runner(
        base_url,
        "binary-linux-riscv64.tar.gz",
        "0ade6a82bf4d5a1368a67255a6bafd7d8a070e9e2958463c98fd35479e69ddf1",
    )
    # windows
    runners[("windows", "amd64")] = Runner(
        base_url,
        "binary-windows-amd64.zip",
        "f1a93b75bd77058fc5fe10e3f4875f26488d5518b9ea94e8be028a4ef0d51ae3",
    )
    runners[("windows", "i386")] = Runner(
        base_url,
        "binary-windows-386.zip",
        "9f3af30e8c5ee3f2bc7422b8dc2581e5045a254632920672c2e41930eac8e63f",
    )
    runners[("windows", "arm64")] = Runner(
        base_url,
        "binary-windows-arm64.zip",
        "5d6a5b9e9d0fec4453411c3fd3f978acf608974205f269ce3a3053a47f2a179f",
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
