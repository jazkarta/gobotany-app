'''Deployment script to automate the steps of a production deployment'''
import argparse
import subprocess


def run(branch):
    print 'Deploy branch: ', branch

def _parse_args():
    parser = argparse.ArgumentParser(description='Deploy a branch to a Heroku instance')
    parser.add_argument('branch', metavar='branch_name', help='Name of a git branch to push to Heroku')
    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = _parse_args()
    run(args.branch)
