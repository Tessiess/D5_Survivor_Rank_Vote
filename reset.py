import pickle

with open('list/win_score.pickle', 'rb') as f:
    l=pickle.load(f)
    l.append(10)
with open('list/win_score.pickle', 'wb') as f:
    pickle.dump([0.2*int(i) for i in l], f)

with open('list/lose_score.pickle', 'rb') as f:
    l=pickle.load(f)
    l.append(10)
with open('list/lose_score.pickle', 'wb') as f:
    pickle.dump([0.2*int(i) for i in l], f)

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
