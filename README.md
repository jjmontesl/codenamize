Codenamize
==========

**Generate consistent easier-to-remember codenames from strings and numbers.**


Overview
========

**Codenamize** is a command line tool and Python library that
returns consistent codenames for objects, by joining
adjectives and words together. These are easier to remember and
write down than pure numbers, and can be used instead or along UUIDs,
GUIDs, hashes (MD5, SHA...), network addresses and other difficult
to remember strings.

This can be used to replace identifiers or codes when presenting those to users.
As words are easier to identify and remember for humans, this module maps
Python objects to easy to remember words.


How to install
==============

    1. easy_install codenamize
    2. pip install codenamize
    3. git clone http://github.com/jjmontesl/codenamize
        a. cd codenamize
        b. run python setup.py
    4. wget https://github.com/jjmontesl/codenamize/zipball/master
        a. unzip the downloaded file
        b. cd into codenamize-* directory
        c. run python setup.py


Usage
-----

Import the codenamize function:

    >>> from codenamize import codenamize

Consecutive numbers yield differentiable codenames:

    >>> codenamize(1)
    'toothsome-sick'
    >>> codenamize(2)
    'periodic-white'

Note that strings are different from integers:

    >>> codenamize("1")
    'smoggy-nobody'

If you later want to add more adjectives, your existing codenames
are retained as suffixes:

    >>> codenamize(0x123456aa)
    'precious-ratio'
    >>> codenamize(0x123456aa, 2)
    'tan-precious-ratio'

Other options (max characters, join character, capitalize):

    >>> codenamize(0x123456aa, 2, 3, '', True)
    'DryShyRip'
    >>> codenamize(0x123456aa, 2, 0, '', True)
    'Tan Precious Ratio'
    >>> codenamize(0x123456aa, 5, 0, ' ', True)
    'Homeless Helpful Clean Tan Precious Ratio'

Examples
--------

For numbers 100000-100009, show codenames with 0-2 adjectives and different options:

    OBJ       ADJ0-MAX5    ADJ1-MAX5         ADJ2-MAX5  ADJ-0, ADJ-1, ADJ-2 (capitalized, empty join character)
    100001         mall   messy-mall   four-messy-mall  Location, ZestyLocation, RudeZestyLocation
    100002         chip   white-chip   bent-white-chip  Put, DaffyPut, AmusingDaffyPut
    100003          can     many-can      fat-many-can  Bench, BadBench, ImperfectBadBench
    100004        royal  dizzy-royal tough-dizzy-royal  Estate, ToothsomeEstate, GoofyToothsomeEstate
    100005        doubt  rabid-doubt spicy-rabid-doubt  Audience, PeriodicAudience, NaughtyPeriodicAudience
    100006         song     sad-song    ritzy-sad-song  Car, SmilingCar, HistoricalSmilingCar
    100007         joke    shut-joke   nifty-shut-joke  Task, StrongTask, SwiftStrongTask
    100008         bank   gaudy-bank  legal-gaudy-bank  Beyond, ToughBeyond, ChemicalToughBeyond
    100009        whole  slimy-whole giant-slimy-whole  Resolve, BoredResolve, IncandescentBoredResolve

Codename space sizes
--------------------

In selecting the number of adjectives and max chars to use, consider how
many codenames you need to fit the number of objects you'll handle, since
the probability of collision increases with the number of different objects
used.

    0 adj (max 3 chars) = 115 combinations
    0 adj (max 4 chars) = 438 combinations
    0 adj (max 5 chars) = 742 combinations
    0 adj (max 6 chars) = 987 combinations
    0 adj (max 7 chars) = 1176 combinations
    0 adj (max 0 chars) = 1525 combinations
    1 adj (max 3 chars) = 2760 combinations
    1 adj (max 4 chars) = 56940 combinations
    1 adj (max 5 chars) = 241150 combinations
    1 adj (max 6 chars) = 492513 combinations
    1 adj (max 7 chars) = 789096 combinations
    1 adj (max 0 chars) = 1701900 combinations
    2 adj (max 3 chars) = 66240 combinations
    2 adj (max 4 chars) = 7402200 combinations
    2 adj (max 5 chars) = 78373750 combinations
    2 adj (max 6 chars) = 245763987 combinations
    2 adj (max 7 chars) = 529483416 combinations
    2 adj (max 0 chars) = 1899320400 combinations

An example is shown by running  codenamize --tests .


License
====================

Codenamize is released under MIT license.

For full license see the LICENSE file.

