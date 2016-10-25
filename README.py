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

    yield '# LeetCode Online Judge, [{}]({})'.format(problems['category_slug'].capitalize(), url_algorithms)

    yield '\n'
    yield 'Solved with Python 3.x'
    yield '\n' * 2

    header = [
        '#', 'Title', 'Problem', 'Discuss', 'Solution', 'Difficulty',
        'Accepted', 'Submitted', 'Acceptance', 'Protected', 'Solved'
    ]

    yield '## Table of Contents ({})'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    yield '| {} |'.format(' | '.join(header))
    yield '| {} |'.format(' | '.join(['-' * len(item) for item in header]))

    for problem in sorted(problems['stat_status_pairs'], key=lambda x: x['stat']['question_id']):
        py = '{}.{}.py'.format(
            problem['stat']['question_id'], problem['stat']['question__title_slug'].replace('-', '_')
        )

        yield '| {} |'.format(
            ' | '.join([
                str(problem['stat']['question_id']),
                problem['stat']['question__title'],
                '[LeetCode]({}/problems/{}/)'.format(host, problem['stat']['question__title_slug']),
                '[LeetCode]({}/discuss/questions/oj/{}/)'.format(host, problem['stat']['question__title_slug']),
                '[Python](/{})'.format(py),
                {1: 'Easy', 2: 'Medium', 3: 'Hard'}[problem['difficulty']['level']],
                str(problem['stat']['total_acs']),
                str(problem['stat']['total_submitted']),
                '%.1f%%' % (100 * problem['stat']['total_acs'] / problem['stat']['total_submitted']),
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
