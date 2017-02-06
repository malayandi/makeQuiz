import random

# TODO: prone to getting stuck in loops; set conditions on inputs and optimise algorithm
# IDEA: use matrix to store data and just pick from there

def selector(questions, dReq, tReq):
    """
    Given a histogram of questions that keep track of their difficulty and
    corresponding topic, select num questions that satisfy the requirements
    as given (in the histograms dReq and tReq).
    """
    chosen = []
    t_hist, d_hist = track(questions)
    to_choose = sum(dReq.values())
    while to_choose:
        diffs = list(dReq.keys()) # list of keys
        diffs = [num for num in diffs if num] # list of keys with non-zero value
        valid = False
        chosen_d = random.choice(diffs) # randomly chosen difficulty
        diff_list = d_hist[chosen_d] # list of questions with chosen difficulty
        dReq[chosen_d] -= 1 # removing one from required questions of difficulty
        while valid == False:
            chosen_q = random.choice(diff_list) # chosen question
            params = questions[chosen_q]
            chosen_t = params[0]
            if tReq[chosen_t]:
                valid = True
                tReq[chosen_t] -= 1 # removing one from required questions of topic
                to_choose -= 1
        chosen.append(chosen_q)
    return chosen

def track(questions):
    """
    Converts a histogram of questions that keep track of their difficulty and
    corresponding topic into two histograms, difficulty, that maps difficulties
    to a list of questions of corresponding difficulty and topics, that maps
    topics to a list of questions of corresponding topics.
    """
    topics = {}
    diff = {}
    for q, param in questions.items():
        t = param[0]
        d = param[1]
        if t in topics:
            topics[t].append(q)
        else:
            topics[t] = [q]
        if d in diff:
            diff[d].append(q)
        else:
            diff[d] = [q]
    return topics, diff

if __name__ == "__main__":
    questions = {"easy1": (1, "easy"), "easy2": (2, "easy"), "easy3": (3, "easy"),
        "medium2": (2, "medium"), "medium2_2": (2, "medium"), "medium1": (1, "medium"),
        "hard3": (3, "hard"), "hard3_2": (3, "hard"), "hard1": (1, "hard"), "hard2": (2, "hard")}
    topics, diff = track(questions)
    dReq = {"easy": 1, "medium": 2, "hard": 2}
    tReq = {1: 1, 2: 2, 3: 2}
    chosen = selector(questions, dReq, tReq)
    print(chosen)
