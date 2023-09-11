def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    terms_dict = {}
    for term in terms:
        t, period = term.split()
        terms_dict[t] = int(period)
    for i, collect in enumerate(privacies):
        dates, t = collect.split()
        dates = list(map(int, dates.split(".")))

        term_period = terms_dict[t]
        dates[1] += term_period
        if dates[1] > 12:
            dates[0] += (dates[1] // 12)
            if dates[1] % 12 > 0:
                dates[1] %= 12
            else:
                dates[0] -= 1
                dates[1] = 12

        if today == dates:
            answer.append(i + 1)
            continue

        for j in range(len(today)):
            if today[j] > dates[j]:  # 폐기
                answer.append(i + 1)
                break
            elif today[j] == dates[j]:
                continue
            else:
                break
                
    return answer