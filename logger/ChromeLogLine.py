#!/usr/bin/env python3

"""
main.py:

Starter file for chrome colored logging

"""

__author__  = "Sunil"

from typing import List
from typing_extensions import Final
from .ChromeConstants import ChromeConstants

kExpectedLogLineChunks: Final = 3
kParsedLogDelimiterLimit: Final = 2

kDateTime: Final = 0
kLogLevel: Final = 1

class ChromeLogLine(object):
    def __init__(self, uncoloredLine: str) -> None:
        expectedLogLevels: List[str] = ["INFO", "ERROR", "WARNING", "FATAL"]
        parsedLine: List[str] = uncoloredLine.split(ChromeConstants.kLogDelimiter,
                                                    kParsedLogDelimiterLimit)

        # [28474:775:0318/214434.970195:INFO:content_main_runner_impl.cc(974)] Chrome is running in full browser mode.
        # chrome log line doesn't follow
        if (len(parsedLine) != kExpectedLogLineChunks):
            raise Exception(uncoloredLine)

        rawDateTime, level, rest = parsedLine

        print(level)
        if (level not in expectedLogLevels):
            raise Exception(uncoloredLine)

        # Colorize the chrome log line
        self.logLevel: str = level
        self.dateTime: str = rawDateTime[1:]

        if (len(rest.split(']')) != 2):
            raise Exception(uncoloredLine)

        # extract filename and message
        fileName, msg = rest.split(']', maxsplit=2)

        self.fileName: str = fileName
        self.message: str = msg

    def __str__(self) -> str:
        return f"{self.dateTime} {self.logLevel} {self.fileName} {self.message}"
