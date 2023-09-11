def solution(players, callings):
    player_id = {}
    answer = players[:]
    for i in range(len(players)):
        player_id[players[i]] = i

    for name in callings:
        idx = player_id[name]
        player_id[name] = idx - 1
        player_id[answer[idx - 1]] = idx

        answer[idx], answer[idx - 1] = answer[idx - 1], answer[idx]
    return answer