from datetime import timedelta
from deltaman import delta_parser


def test_parser():
    parse = delta_parser.parse

    assert parse('3sec') == parse('3.0sec') == timedelta(seconds=3)

    assert parse('3.1sec') == timedelta(seconds=3, milliseconds=100)

    assert parse('8s') == parse('8 s') \
        == parse('8sec') == parse('8 sec') \
        == parse('8second') == parse('8 second') \
        == parse('8seconds') == parse('8 seconds') \
        == timedelta(seconds=8)

    assert parse('1m12s') \
        == parse('1m 12s') \
        == parse("1 min 12 sec") \
        == parse("1 minute 12 seconds") \
        == timedelta(minutes=1, seconds=12)

    assert parse('1h-15m') \
        == parse("1h -15m") \
        == parse("1 hour -15 minutes") \
        == parse('45m') \
        == timedelta(minutes=45)
