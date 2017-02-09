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


Usage from Python
-----------------

Import the codenamize function:

    >>> from codenamize import codenamize

Consecutive numbers yield differentiable codenames:

    >>> codenamize("1")
    'familiar-grand'
    >>> codenamize("2")
    'little-tip'

If you later want to add more adjectives, your existing codenames
are retained as suffixes:

    >>> codenamize("11:22:33:44:55:66")
    'craven-delivery'
    >>> codenamize("11:22:33:44:55:66", 2)
    'separate-craven-delivery'

Note that integers are internally converted to strings before hashing:

    >>> codenamize(1)
    'familiar-grand'

Other options (max characters, join character, capitalize):

    >>> codenamize(0x123456aa, 2, 3, '', True)
    'SadBigFat'
    >>> codenamize(0x123456aa, 2, 0, '', True)
    'BrawnyEminentBear'
    >>> codenamize(0x123456aa, 5, 0, ' ', True)
    'Spotty Disagreeable Modern Brawny Eminent Bear'
    >>> codenamize(0x123456aa, 4, 0, ' ', False)
    'disagreeable modern brawny eminent bear'


Usage as command line tool
--------------------------

After installing, run `codenamize --help` for help:

    usage: codenamize [-h] [-p PREFIX] [-m MAXCHARS] [-j JOIN] [-c] [--space]
                      [--tests] [--version]
                      [strings [strings ...]]

    Generate consistent easier-to-remember codenames from strings and numbers.

    positional arguments:
      strings               One or more strings to codenamize.

    optional arguments:
      -h, --help            show this help message and exit
      -p PREFIX, --prefix PREFIX
                            number of prefixes to use
      -m MAXCHARS, --maxchars MAXCHARS
                            max word characters (0 for no limit)
      -a HASH_ALGO, --hash_algorithm HASH_ALGO
                            the algorithm to use to hash the input value
      -j JOIN, --join JOIN  separator between words (default: -)
      -c, --capitalize      capitalize words
      --space               show codename space for the given arguments
      --tests               show information and samples
      --list_algorithms     List the hash algorithms available
      --version             show program's version number and exit


Examples
--------

For numbers 100000-100009, show codenames with 0-2 adjectives and different options:

    OBJ       ADJ0-MAX5    ADJ1-MAX5         ADJ2-MAX5  ADJ-0, ADJ-1, ADJ-2 (capitalized, empty join character)
    100001         boat   funny-boat   real-funny-boat  Community, RacialCommunity, PluckyRacialCommunity
    100002        award  first-award  tidy-first-award  Repeat, UptightRepeat, HelpfulUptightRepeat
    100003         rush   super-rush  equal-super-rush  Intention, ExpensiveIntention, JazzyExpensiveIntention
    100004        uncle   calm-uncle   icky-calm-uncle  March, SubduedMarch, AdamantSubduedMarch
    100005        salad   warm-salad   true-warm-salad  Plant, QuickestPlant, ReminiscentQuickestPlant
    100006         gift   witty-gift    odd-witty-gift  Estimate, CreepyEstimate, SpectacularCreepyEstimate
    100007          son     zany-son    gaudy-zany-son  Truck, MiniatureTruck, OptimalMiniatureTruck
    100008        angle   damp-angle  dusty-damp-angle  Steak, SpectacularSteak, RightfulSpectacularSteak
    100009         link   utter-link   null-utter-link  Bike, ImportantBike, SweetImportantBike


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

