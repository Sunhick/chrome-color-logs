#!/usr/bin/env python3

import sys
import time

def main(args):
    logi = "[0318/214434.970195:INFO:content_main_runner_impl.cc(974)] Chrome is running in full browser mode."
    logw = "[0318/214434.970195:WARNING:content_main_runner_impl.cc(974)] Chrome is running in full browser mode."
    logf = "[0318/214434.970195:FATAL:content_main_runner_impl.cc(974)] Chrome is running in full browser mode."
    loge = "[0318/214434.970195:ERROR:content_main_runner_impl.cc(974)] Chrome is running in full browser mode."
    logu = "[0318/214434.970195:NOPE:content_main_runner_impl.cc(974)] Chrome is running in full browser mode."
    while True:
        print(logi)
        print(logw)
        print(loge)
        print(logf)
        print(logu)
        # linux buffer's output when it's being piped. so make sure to install expect package which comes
        # with "unbuffer" comamnd which will make pipe(|) command not buffer it' s output before it's being
        # passed to command following the pipe.
        # on mac: brew install expect
        time.sleep(1)

if __name__ == "__main__":
    main(sys.argv[1:])