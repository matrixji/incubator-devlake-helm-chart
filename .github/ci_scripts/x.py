"""
if things are changed under the charts folder, the version field in charts/devlake/Chart.yaml should be promoted, e.g: v0.14.5 -> v0.14.6, v0.14.5 -> v0.15.0
the chart and the devlake version alignment: using the same major and minor version numbers, and could have different patch numbers. e.g chart version v0.14.5 for DevLake version v0.14.2
each merge to master should be fast-forwardable and all commits need to squash to one before it merged
"""

import os


def check_main():
    for k in os.environ:
        print(f'{k}={os.environ[k]}')


if __name__ == '__main__':
    check_main()
