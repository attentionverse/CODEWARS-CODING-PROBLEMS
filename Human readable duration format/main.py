def pluralize(word, num):
    return '{} {}{}'.format(num, word, 's' if num != 1 else '')


def format_duration(seconds):
    duration_parts = []

    secs = seconds % 60
    if secs:
        duration_parts = [pluralize('second', secs)]
    minutes_total = (seconds - secs) // 60

    if minutes_total:
        minutes = minutes_total % 60
        if minutes:
            duration_parts.insert(0, pluralize('minute', minutes))
        hours_total = (minutes_total - minutes) // 60

        if hours_total:
            hours = hours_total % 24
            if hours:
                duration_parts.insert(0, pluralize('hour', hours))
            days_total = (hours_total - hours) // 24

            if days_total:
                days = days_total % 365
                if days:
                    duration_parts.insert(0, pluralize('day', days))
                years = (days_total - days) // 365
                if years:
                    duration_parts.insert(0, pluralize('year', years))

    if len(duration_parts) > 2:
        duration = ', '.join(duration_parts[0:-1]) + ' and ' + duration_parts[-1]
    elif len(duration_parts) == 2:
        duration = ' and '.join(duration_parts)
    elif len(duration_parts) == 1:
        duration = duration_parts[0]
    else:
        duration = 'now'

    return duration


if __name__ == "__main__":
    for assert_input in [
        [0, 'now'],
        [1, '1 second'],
        [62, "1 minute and 2 seconds"],
        [120, "2 minutes"],
        [3600, "1 hour"],
        [2460, "41 minute"],
        [3662, "1 hour, 1 minute and 2 seconds"],
    ]:
        print('assert_input: {}'.format(assert_input))
        assert (format_duration(assert_input[0]) == assert_input[1])
