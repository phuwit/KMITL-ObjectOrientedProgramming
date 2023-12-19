def finding_wrong_series_member(series_string):
    # series = [int(n) for n in input().split()]
    series = [int(n) for n in series_string.split()]
    print(series)

    series_difference_recurring = [(series[i] - series[0]) for i in range(1, len(series))]
    print(series_difference_recurring)
    # series_difference_recurring_then_relative = [(series_difference_recurring[i] - series_difference_recurring[i - 1]) for i in range(1, len(series_difference_recurring))]
    # print(series_difference_recurring_then_relative)
    # series_difference_relative = [(series[i] - series[i-1]) for i in range(1, len(series))]
    # print(series_difference_relative)
    # series_difference_relative_then_relative = [(series_difference_relative[i] - series_difference_relative[i-1]) for i in range(1, len(series_difference_relative))]
    # print(series_difference_relative_then_relative)
    series_difference_recurring_normalized = [(series_difference_recurring[i] / (i + 1)) for i in range(len(series_difference_recurring))]
    print(series_difference_recurring_normalized)
    # series_difference_relative_normalized = [(series_difference_relative[i] / (i + 1)) for i in range(len(series_difference_relative))]
    # print(series_difference_relative_normalized)

    mode = max(set(series_difference_recurring_normalized), key=series_difference_recurring_normalized.count)
    if (series_difference_recurring_normalized.count(mode) == 1):
        # first one is wrong
        print(1)
    else:
        for i in range(len(series_difference_recurring_normalized)):
            if (mode != series_difference_recurring_normalized[i]):
                print(i + 2)
    print('======')


finding_wrong_series_member('8 20 30 40 50')
finding_wrong_series_member('10 18 30 40 50')
finding_wrong_series_member('10 20 28 40 50')
finding_wrong_series_member('10 20 30 38 50')
finding_wrong_series_member('10 20 30 40 48')
