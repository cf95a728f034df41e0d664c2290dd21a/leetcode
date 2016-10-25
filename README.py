#! /usr/bin/python
# -*- coding: utf-8 -*-


import os
from datetime import datetime

import requests


def markdown():
    session = requests.Session()

    host = 'https://leetcode.com'
    url_algorithms = '{}/problemset/algorithms/'.format(host)
    url_problems = '{}/api/problems/algorithms/'.format(host)

    session.get(url=url_algorithms)

    problems = session.get(url=url_problems).json()

    yield '# LeetCode Online Judge of [{}]({})'.format(problems['category_slug'].capitalize(), url_algorithms)

    yield '\n'
    yield 'Solved with Python 3.x'
    yield '\n' * 2

    header = ['#', 'Title', 'Solution', 'Difficulty', 'Acceptance', 'Protected', 'Solved']

    yield '### Table of Contents'
    yield datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    yield '\n'
    yield '| {} |'.format(' | '.join(header))
    yield '| {} |'.format('|'.join(['-' * (len(item) + 2) for item in header]))

    for problem in sorted(problems['stat_status_pairs'], key=lambda x: x['stat']['question_id']):
        py = '{}.{}.py'.format(
            problem['stat']['question_id'], problem['stat']['question__title_slug'].replace('-', '_')
        )

        yield '| {} |'.format(
            ' | '.join([
                str(problem['stat']['question_id']),
                '[{}]({})'.format(
                    problem['stat']['question__title'],
                    '{}/problems/{}/'.format(host, problem['stat']['question__title_slug'])
                ),
                "[Python](/{})<span style='margin: 0 10px 0 10px;'></span>[Discuss]({})".format(
                    py, '{}/discuss/questions/oj/{}/'.format(host, problem['stat']['question__title_slug'])
                ),
                {1: 'Easy', 2: 'Medium', 3: 'Hard'}[problem['difficulty']['level']],
                '%.1f%% (%d of %d)' % (
                    100 * problem['stat']['total_acs'] / problem['stat']['total_submitted'],
                    problem['stat']['total_acs'], problem['stat']['total_submitted']
                ),
                str(problem['paid_only']),
                str(os.path.exists(py) and os.path.isfile(py))
            ])
        )


if __name__ == '__main__':
    with open(os.path.splitext(os.path.basename(__file__))[0] + '.md', mode='w', encoding='utf-8') as fp:
        for index, line in enumerate(markdown()):
            if index != 0:
                fp.write('\n')

            fp.write(line)
