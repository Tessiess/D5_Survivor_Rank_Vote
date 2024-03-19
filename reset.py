import pickle

with open('list/win_score.pickle', 'wb') as f:
    pickle.dump([1] * 43, f)
with open('list/lose_score.pickle', 'wb') as f:
    pickle.dump([1] * 43, f)

ip_dict = dict()
ip_ban = set()

with open('ip/ip_dict.pickle', 'wb') as f:
    pickle.dump(ip_dict, f)
with open('ip/ip_ban.pickle', 'wb') as f:
    pickle.dump(ip_ban, f)

with open('list/win_score.pickle', 'rb') as f:
    lst_win_score = pickle.load(f)
with open('list/lose_score.pickle', 'rb') as f:
    lst_lose_score = pickle.load(f)
lst_win_score