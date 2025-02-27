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
    base_url_gh = "https://github.com/actions/runner/releases/download/v2.321.0/"
    # linux
    runners[("linux", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-x64-2.321.0.tar.gz",
        "ba46ba7ce3a4d7236b16fbe44419fb453bc08f866b24f04d549ec89f1722a29e",
    )
    runners[("linux", "arm", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-arm-2.321.0.tar.gz",
        "2b96a4991ebf2b2076908a527a1a13db590217f9375267b5dd95f0300dde432b",
    )
    runners[("linux", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-linux-arm64-2.321.0.tar.gz",
        "62cc5735d63057d8d07441507c3d6974e90c1854bdb33e9c8b26c0da086336e1",
    )
    # macos
    runners[("macos", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-osx-x64-2.321.0.tar.gz",
        "b2c91416b3e4d579ae69fc2c381fc50dbda13f1b3fcc283187e2c75d1b173072",
    )
    runners[("macos", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-osx-arm64-2.321.0.tar.gz",
        "fbee07e42a134645d4f04f8146b0a3d0b3c948f0d6b2b9fa61f4318c1192ff79",
    )
    # windows
    runners[("windows", "amd64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-win-x64-2.321.0.zip",
        "88d754da46f4053aec9007d172020c1b75ab2e2049c08aef759b643316580bbc",
    )
    runners[("windows", "arm64", "gh")] = Runner(
        base_url_gh,
        "actions-runner-win-arm64-2.321.0.zip",
        "22df5a32a65a55e43dab38a200d4f72be0f9f5ce1839f5ad34e689a0d3ff0fb7",
    )

    # https://github.com/ChristopherHX/github-act-runner
    base_url_chx = (
        "https://github.com/ChristopherHX/github-act-runner/releases/download/v0.9.0/"
    )
    # linux
    runners[("linux", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-amd64.tar.gz",
        "0d260236142e7f171182aab18703ab0c5b727ef141b00f7ad068b9ccf77d435d",
    )
    runners[("linux", "i386", "chx")] = Runner(
        base_url_chx,
        "binary-linux-386.tar.gz",
        "c307d3d89989dc10a355a81f73d917c86ace2fd7080db7f6ffbc59aad40efab6",
    )
    runners[("linux", "arm", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm.tar.gz",
        "3734e8aa3a2d4bf9e41ff0377f9cdaf80038386c4907ee87ad1e6ddba64d9a4e",
    )
    runners[("linux", "armv6", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm5.tar.gz",
        "7a06202f770482dbb1f9ea36c3a7a39ca4b2f58eb3b167e08a42de6330a23f11",
    )
    runners[("linux", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-arm64.tar.gz",
        "252e5c97ac8f51a2910c1184bd23c8a4d6dae13f04b37c9606a59e3dbba9eb23",
    )
    runners[("linux", "ppc64el", "chx")] = Runner(
        base_url_chx,
        "binary-linux-ppc64le.tar.gz",
        "79a7bee25e3201d3e76f006a1caa804ec3a371762c97d97a343d271078e0195e",
    )
    runners[("linux", "riscv64", "chx")] = Runner(
        base_url_chx,
        "binary-linux-riscv64.tar.gz",
        "2c7824df834ee093cbbdbfa38ef8254f8bf6afffc2d90687a342a762aff35daa",
    )
    # macos
    runners[("macos", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-darwin-amd64.tar.gz",
        "b9d7877190c4f332c72029daea990d1c5e9c48408c659806a5e6ac58236ec22c",
    )
    runners[("macos", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-darwin-arm64.tar.gz",
        "e38951f5653cdb146ce9682234c986cd4fab10b46e7367c1852a1ab13aedb78c",
    )
    # windows
    runners[("windows", "amd64", "chx")] = Runner(
        base_url_chx,
        "binary-windows-amd64.zip",
        "3eee8a2a621240f69d8c1353bfafad99af89a8f91e6389d877e3016fc55b9be5",
    )
    runners[("windows", "i386", "chx")] = Runner(
        base_url_chx,
        "binary-windows-386.zip",
        "89497496b1c5065617c3595a344effe58aa4067d5bf76e898a0caa7177c4cb34",
    )
    runners[("windows", "arm64", "chx")] = Runner(
        base_url_chx,
        "binary-windows-arm64.zip",
        "18283b3b6087587497535ca6f9c4bb15fffb2dedd3fcb545756f5c8a852690da",
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
