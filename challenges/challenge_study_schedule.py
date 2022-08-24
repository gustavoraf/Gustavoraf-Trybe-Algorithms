def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for schedule in permanence_period:
            if schedule[0] <= target_time <= schedule[1]:
                counter += 1
        return counter
    except TypeError:
        return None
